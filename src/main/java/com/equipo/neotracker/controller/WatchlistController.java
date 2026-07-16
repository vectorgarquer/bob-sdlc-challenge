package com.equipo.neotracker.controller;

import com.equipo.neotracker.model.Asteroid;
import com.equipo.neotracker.service.NeoService;
import com.equipo.neotracker.service.WatchlistService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/watchlist")
public class WatchlistController {

    private final WatchlistService watchlistService;
    private final NeoService neoService;

    public WatchlistController(WatchlistService watchlistService, NeoService neoService) {
        this.watchlistService = watchlistService;
        this.neoService = neoService;
    }

    /**
     * GET /api/watchlist
     */
    @GetMapping
    public ResponseEntity<List<Asteroid>> getWatchlist() {
        return ResponseEntity.ok(watchlistService.getAll());
    }

    /**
     * POST /api/watchlist/{asteroidId}?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
     * Looks up the asteroid in the NASA feed for the given date range and adds it to the watchlist.
     */
    @PostMapping("/{asteroidId}")
    public ResponseEntity<?> addToWatchlist(
            @PathVariable String asteroidId,
            @RequestParam String start_date,
            @RequestParam String end_date) {
        try {
            List<Asteroid> asteroids = neoService.getAsteroids(start_date, end_date, null, "desc");
            Asteroid asteroid = asteroids.stream()
                    .filter(a -> a.getId().equals(asteroidId))
                    .findFirst()
                    .orElseThrow(() -> new IllegalArgumentException(
                            "Asteroide con id '" + asteroidId + "' no encontrado en el rango de fechas."));
            watchlistService.add(asteroid);
            return ResponseEntity.status(HttpStatus.CREATED).body(asteroid);
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        } catch (IllegalStateException e) {
            return ResponseEntity.status(HttpStatus.CONFLICT).body(Map.of("error", e.getMessage()));
        }
    }

    /**
     * DELETE /api/watchlist/{asteroidId}
     */
    @DeleteMapping("/{asteroidId}")
    public ResponseEntity<?> removeFromWatchlist(@PathVariable String asteroidId) {
        try {
            watchlistService.remove(asteroidId);
            return ResponseEntity.noContent().build();
        } catch (IllegalStateException e) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(Map.of("error", e.getMessage()));
        }
    }
}

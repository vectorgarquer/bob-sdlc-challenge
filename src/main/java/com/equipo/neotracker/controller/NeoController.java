package com.equipo.neotracker.controller;

import com.equipo.neotracker.model.Asteroid;
import com.equipo.neotracker.service.NeoService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/neo")
public class NeoController {

    private final NeoService neoService;

    public NeoController(NeoService neoService) {
        this.neoService = neoService;
    }

    /**
     * GET /api/neo/feed?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&sort_by=size|velocity&order=asc|desc
     */
    @GetMapping("/feed")
    public ResponseEntity<?> getFeed(
            @RequestParam String start_date,
            @RequestParam String end_date,
            @RequestParam(required = false) String sort_by,
            @RequestParam(defaultValue = "desc") String order) {
        try {
            List<Asteroid> asteroids = neoService.getAsteroids(start_date, end_date, sort_by, order);
            return ResponseEntity.ok(asteroids);
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    /**
     * GET /api/neo/most-dangerous?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
     */
    @GetMapping("/most-dangerous")
    public ResponseEntity<?> getMostDangerous(
            @RequestParam String start_date,
            @RequestParam String end_date) {
        try {
            Asteroid asteroid = neoService.getMostDangerous(start_date, end_date);
            return ResponseEntity.ok(asteroid);
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        } catch (IllegalStateException e) {
            return ResponseEntity.status(404).body(Map.of("error", e.getMessage()));
        }
    }
}

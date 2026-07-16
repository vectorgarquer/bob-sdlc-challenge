package com.equipo.neotracker.service;

import com.equipo.neotracker.model.Asteroid;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class WatchlistServiceTest {

    private WatchlistService watchlistService;

    private Asteroid asteroidAlpha;
    private Asteroid asteroidBeta;

    @BeforeEach
    void setUp() {
        watchlistService = new WatchlistService();
        asteroidAlpha = new Asteroid("1", "Alpha", 0.1, 0.5, 30000.0, 500000.0, false, "2025-01-15");
        asteroidBeta  = new Asteroid("2", "Beta",  0.3, 1.2, 80000.0, 120000.0, true,  "2025-01-15");
    }

    // ── Test 7: Add asteroid to watchlist ────────────────────────────────────

    @Test
    void add_newAsteroid_addsSuccessfully() {
        watchlistService.add(asteroidAlpha);

        List<Asteroid> all = watchlistService.getAll();
        assertEquals(1, all.size());
        assertEquals("Alpha", all.get(0).getName());
    }

    // ── Test 8: Prevent duplicate in watchlist ───────────────────────────────

    @Test
    void add_duplicateAsteroid_throwsIllegalStateException() {
        watchlistService.add(asteroidAlpha);

        assertThrows(IllegalStateException.class,
                () -> watchlistService.add(asteroidAlpha));
    }

    // ── Test 9: Remove asteroid from watchlist ───────────────────────────────

    @Test
    void remove_existingAsteroid_removesSuccessfully() {
        watchlistService.add(asteroidAlpha);
        watchlistService.add(asteroidBeta);

        watchlistService.remove("1");

        List<Asteroid> all = watchlistService.getAll();
        assertEquals(1, all.size());
        assertEquals("Beta", all.get(0).getName());
    }

    // ── Test 10: Remove non-existent asteroid throws ─────────────────────────

    @Test
    void remove_nonExistentAsteroid_throwsIllegalStateException() {
        assertThrows(IllegalStateException.class,
                () -> watchlistService.remove("999"));
    }

    // ── Test 11: Get all returns empty list when watchlist is empty ──────────

    @Test
    void getAll_emptyWatchlist_returnsEmptyList() {
        List<Asteroid> all = watchlistService.getAll();
        assertNotNull(all);
        assertTrue(all.isEmpty());
    }
}

package com.equipo.neotracker.service;

import com.equipo.neotracker.client.NasaApiClient;
import com.equipo.neotracker.model.Asteroid;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
class NeoServiceTest {

    @Mock
    private NasaApiClient nasaApiClient;

    @InjectMocks
    private NeoService neoService;

    private List<Asteroid> mockAsteroids;

    @BeforeEach
    void setUp() {
        mockAsteroids = List.of(
                new Asteroid("1", "Alpha",   0.1, 0.5,  30000.0, 500000.0, false, "2025-01-15"),
                new Asteroid("2", "Beta",    0.3, 1.2,  80000.0, 120000.0, true,  "2025-01-15"),
                new Asteroid("3", "Gamma",   0.05, 0.2, 50000.0, 900000.0, false, "2025-01-16"),
                new Asteroid("4", "Delta",   0.8, 2.0,  15000.0,  80000.0, true,  "2025-01-16")
        );
    }

    // ── Test 1: Sort by velocity ascending ──────────────────────────────────

    @Test
    void getAsteroids_sortByVelocityAscending_returnsSortedList() {
        when(nasaApiClient.fetchAsteroids("2025-01-15", "2025-01-16")).thenReturn(mockAsteroids);

        List<Asteroid> result = neoService.getAsteroids("2025-01-15", "2025-01-16", "velocity", "asc");

        assertEquals(4, result.size());
        assertEquals("Delta",  result.get(0).getName()); // 15000 km/h
        assertEquals("Alpha",  result.get(1).getName()); // 30000 km/h
        assertEquals("Gamma",  result.get(2).getName()); // 50000 km/h
        assertEquals("Beta",   result.get(3).getName()); // 80000 km/h
    }

    // ── Test 2: Sort by size descending ─────────────────────────────────────

    @Test
    void getAsteroids_sortBySizeDescending_returnsSortedList() {
        when(nasaApiClient.fetchAsteroids("2025-01-15", "2025-01-16")).thenReturn(mockAsteroids);

        List<Asteroid> result = neoService.getAsteroids("2025-01-15", "2025-01-16", "size", "desc");

        assertEquals(4, result.size());
        assertEquals("Delta", result.get(0).getName()); // max diameter 2.0 km
        assertEquals("Beta",  result.get(1).getName()); // 1.2 km
        assertEquals("Alpha", result.get(2).getName()); // 0.5 km
        assertEquals("Gamma", result.get(3).getName()); // 0.2 km
    }

    // ── Test 3: Most dangerous — lowest miss_distance ────────────────────────

    @Test
    void getMostDangerous_returnsAsteroidWithLowestMissDistance() {
        when(nasaApiClient.fetchAsteroids("2025-01-15", "2025-01-16")).thenReturn(mockAsteroids);

        Asteroid result = neoService.getMostDangerous("2025-01-15", "2025-01-16");

        assertEquals("Delta", result.getName()); // miss_distance 80000 km — the lowest
        assertEquals(80000.0, result.getMissDistanceKm());
    }

    // ── Test 4: Most dangerous — empty range throws ──────────────────────────

    @Test
    void getMostDangerous_emptyList_throwsIllegalStateException() {
        when(nasaApiClient.fetchAsteroids("2025-01-15", "2025-01-16")).thenReturn(List.of());

        assertThrows(IllegalStateException.class,
                () -> neoService.getMostDangerous("2025-01-15", "2025-01-16"));
    }

    // ── Test 5: Date range > 7 days throws ──────────────────────────────────

    @Test
    void getAsteroids_dateRangeExceeds7Days_throwsIllegalArgumentException() {
        assertThrows(IllegalArgumentException.class,
                () -> neoService.getAsteroids("2025-01-01", "2025-01-10", null, "desc"));
    }

    // ── Test 6: Invalid sort_by value throws ─────────────────────────────────

    @Test
    void getAsteroids_invalidSortBy_throwsIllegalArgumentException() {
        when(nasaApiClient.fetchAsteroids("2025-01-15", "2025-01-16")).thenReturn(mockAsteroids);

        assertThrows(IllegalArgumentException.class,
                () -> neoService.getAsteroids("2025-01-15", "2025-01-16", "unknown", "desc"));
    }
}

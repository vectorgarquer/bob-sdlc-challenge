package com.equipo.neotracker.service;

import com.equipo.neotracker.model.Asteroid;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class WatchlistService {

    private final List<Asteroid> watchlist = new ArrayList<>();

    public List<Asteroid> getAll() {
        return List.copyOf(watchlist);
    }

    /**
     * Adds an asteroid to the watchlist.
     *
     * @throws IllegalStateException if the asteroid is already in the watchlist.
     */
    public void add(Asteroid asteroid) {
        boolean exists = watchlist.stream()
                .anyMatch(a -> a.getId().equals(asteroid.getId()));
        if (exists) {
            throw new IllegalStateException(
                    "El asteroide con id '" + asteroid.getId() + "' ya está en la watchlist.");
        }
        watchlist.add(asteroid);
    }

    /**
     * Removes an asteroid from the watchlist by its id.
     *
     * @throws IllegalStateException if the asteroid is not found.
     */
    public void remove(String asteroidId) {
        boolean removed = watchlist.removeIf(a -> a.getId().equals(asteroidId));
        if (!removed) {
            throw new IllegalStateException(
                    "El asteroide con id '" + asteroidId + "' no está en la watchlist.");
        }
    }
}

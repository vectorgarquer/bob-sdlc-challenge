package com.equipo.neotracker.service;

import com.equipo.neotracker.client.NasaApiClient;
import com.equipo.neotracker.model.Asteroid;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.Comparator;
import java.util.List;

@Service
public class NeoService {

    private final NasaApiClient nasaApiClient;

    public NeoService(NasaApiClient nasaApiClient) {
        this.nasaApiClient = nasaApiClient;
    }

    /**
     * Fetches asteroids for the given date range (max 7 days), with optional sorting.
     *
     * @param startDate start date in YYYY-MM-DD format
     * @param endDate   end date in YYYY-MM-DD format
     * @param sortBy    "size" or "velocity" (nullable — no sort applied if null)
     * @param order     "asc" or "desc" (default: "desc")
     * @return sorted list of asteroids
     */
    public List<Asteroid> getAsteroids(String startDate, String endDate, String sortBy, String order) {
        validateDateRange(startDate, endDate);

        List<Asteroid> asteroids = nasaApiClient.fetchAsteroids(startDate, endDate);

        if (sortBy == null || sortBy.isBlank()) {
            return asteroids;
        }

        Comparator<Asteroid> comparator = switch (sortBy.toLowerCase()) {
            case "size"     -> Comparator.comparingDouble(Asteroid::getEstimatedDiameterKmMax);
            case "velocity" -> Comparator.comparingDouble(Asteroid::getRelativeVelocityKmh);
            default -> throw new IllegalArgumentException(
                    "Valor inválido para sort_by: '" + sortBy + "'. Use 'size' o 'velocity'.");
        };

        if ("asc".equalsIgnoreCase(order)) {
            asteroids.sort(comparator);
        } else {
            asteroids.sort(comparator.reversed());
        }

        return asteroids;
    }

    /**
     * Returns the asteroid with the lowest miss_distance_km (most dangerous) in the date range.
     */
    public Asteroid getMostDangerous(String startDate, String endDate) {
        validateDateRange(startDate, endDate);

        List<Asteroid> asteroids = nasaApiClient.fetchAsteroids(startDate, endDate);

        return asteroids.stream()
                .min(Comparator.comparingDouble(Asteroid::getMissDistanceKm))
                .orElseThrow(() -> new IllegalStateException(
                        "No se encontraron asteroides para el rango de fechas indicado."));
    }

    private void validateDateRange(String startDate, String endDate) {
        LocalDate start = LocalDate.parse(startDate);
        LocalDate end   = LocalDate.parse(endDate);
        long days = ChronoUnit.DAYS.between(start, end);

        if (days < 0) {
            throw new IllegalArgumentException("start_date no puede ser posterior a end_date.");
        }
        if (days > 7) {
            throw new IllegalArgumentException("El rango de fechas no puede superar 7 días.");
        }
    }
}

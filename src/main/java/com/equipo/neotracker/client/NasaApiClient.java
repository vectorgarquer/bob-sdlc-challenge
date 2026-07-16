package com.equipo.neotracker.client;

import com.equipo.neotracker.model.Asteroid;
import com.fasterxml.jackson.databind.JsonNode;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.List;

@Component
public class NasaApiClient {

    private final RestTemplate restTemplate;

    @Value("${nasa.api.base-url}")
    private String baseUrl;

    @Value("${nasa.api.key}")
    private String apiKey;

    public NasaApiClient(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public List<Asteroid> fetchAsteroids(String startDate, String endDate) {
        String url = String.format("%s/feed?start_date=%s&end_date=%s&api_key=%s",
                baseUrl, startDate, endDate, apiKey);

        JsonNode root = restTemplate.getForObject(url, JsonNode.class);
        List<Asteroid> asteroids = new ArrayList<>();

        if (root == null || !root.has("near_earth_objects")) {
            return asteroids;
        }

        JsonNode neoByDate = root.get("near_earth_objects");
        neoByDate.fieldNames().forEachRemaining(date -> {
            JsonNode neoList = neoByDate.get(date);
            neoList.forEach(node -> asteroids.add(mapToAsteroid(node)));
        });

        return asteroids;
    }

    private Asteroid mapToAsteroid(JsonNode node) {
        String id = node.get("id").asText();
        String name = node.get("name").asText();
        boolean hazardous = node.get("is_potentially_hazardous_asteroid").asBoolean();

        JsonNode diameterKm = node.get("estimated_diameter").get("kilometers");
        double diamMin = diameterKm.get("estimated_diameter_min").asDouble();
        double diamMax = diameterKm.get("estimated_diameter_max").asDouble();

        JsonNode closeApproach = node.get("close_approach_data").get(0);
        String date = closeApproach.get("close_approach_date").asText();
        double velocity = Double.parseDouble(
                closeApproach.get("relative_velocity").get("kilometers_per_hour").asText());
        double missDistance = Double.parseDouble(
                closeApproach.get("miss_distance").get("kilometers").asText());

        return new Asteroid(id, name, diamMin, diamMax, velocity, missDistance, hazardous, date);
    }
}

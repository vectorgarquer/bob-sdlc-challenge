package com.equipo.neotracker.model;

public class Asteroid {

    private String id;
    private String name;
    private double estimatedDiameterKmMin;
    private double estimatedDiameterKmMax;
    private double relativeVelocityKmh;
    private double missDistanceKm;
    private boolean isPotentiallyHazardous;
    private String closeApproachDate;

    public Asteroid() {}

    public Asteroid(String id, String name, double estimatedDiameterKmMin, double estimatedDiameterKmMax,
                    double relativeVelocityKmh, double missDistanceKm,
                    boolean isPotentiallyHazardous, String closeApproachDate) {
        this.id = id;
        this.name = name;
        this.estimatedDiameterKmMin = estimatedDiameterKmMin;
        this.estimatedDiameterKmMax = estimatedDiameterKmMax;
        this.relativeVelocityKmh = relativeVelocityKmh;
        this.missDistanceKm = missDistanceKm;
        this.isPotentiallyHazardous = isPotentiallyHazardous;
        this.closeApproachDate = closeApproachDate;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public double getEstimatedDiameterKmMin() { return estimatedDiameterKmMin; }
    public void setEstimatedDiameterKmMin(double estimatedDiameterKmMin) { this.estimatedDiameterKmMin = estimatedDiameterKmMin; }

    public double getEstimatedDiameterKmMax() { return estimatedDiameterKmMax; }
    public void setEstimatedDiameterKmMax(double estimatedDiameterKmMax) { this.estimatedDiameterKmMax = estimatedDiameterKmMax; }

    public double getRelativeVelocityKmh() { return relativeVelocityKmh; }
    public void setRelativeVelocityKmh(double relativeVelocityKmh) { this.relativeVelocityKmh = relativeVelocityKmh; }

    public double getMissDistanceKm() { return missDistanceKm; }
    public void setMissDistanceKm(double missDistanceKm) { this.missDistanceKm = missDistanceKm; }

    public boolean isPotentiallyHazardous() { return isPotentiallyHazardous; }
    public void setPotentiallyHazardous(boolean potentiallyHazardous) { isPotentiallyHazardous = potentiallyHazardous; }

    public String getCloseApproachDate() { return closeApproachDate; }
    public void setCloseApproachDate(String closeApproachDate) { this.closeApproachDate = closeApproachDate; }
}

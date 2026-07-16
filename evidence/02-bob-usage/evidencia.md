# Evidencia — Etapa 2: Diseño de Arquitectura

## Prompt enviado a Bob (modo Ask)

> "Somos un equipo construyendo NeoTracker con Java 17+, Spring Boot 3.x, Maven, REST API.
> Las 4 capacidades requeridas son:
> 1. Consultar asteroides cercanos a la Tierra en un rango de fechas (máx. 7 días) — NASA NeoWs API.
> 2. Listar y ordenar por tamaño estimado (`estimated_diameter_km_max`) o velocidad relativa (`relative_velocity_kmh`).
> 3. Identificar el asteroide con menor `miss_distance_km` (el más peligroso).
> 4. Watchlist en memoria: agregar, eliminar y listar asteroides de interés.
>
> Propón: módulos/clases con responsabilidades, estructura de paquetes, endpoints REST, y los campos del JSON de NASA NeoWs que necesitamos mapear."

---

## Arquitectura Decidida

### Estructura de Paquetes

```
src/
└── main/
│   └── java/com/equipo/neotracker/
│       ├── NeoTrackerApplication.java       ← Entry point Spring Boot
│       ├── controller/
│       │   ├── NeoController.java            ← GET /api/neo/feed, GET /api/neo/most-dangerous
│       │   └── WatchlistController.java      ← GET/POST/DELETE /api/watchlist
│       ├── service/
│       │   ├── NeoService.java               ← Lógica: consulta NASA, ordenamiento, más peligroso
│       │   └── WatchlistService.java         ← Lógica: gestión de watchlist en memoria
│       ├── client/
│       │   └── NasaApiClient.java            ← HTTP client para NASA NeoWs API
│       ├── model/
│       │   └── Asteroid.java                 ← POJO/Record con campos mapeados
│       └── config/
│           └── AppConfig.java                ← Bean RestTemplate, nasa.api.key property
└── test/
    └── java/com/equipo/neotracker/
        ├── service/
        │   ├── NeoServiceTest.java
        │   └── WatchlistServiceTest.java
        └── controller/
            └── NeoControllerTest.java
```

---

### Responsabilidades por Módulo

| Clase | Responsabilidad |
|-------|----------------|
| `NeoTrackerApplication` | Punto de entrada `@SpringBootApplication` |
| `NeoController` | Expone endpoints de consulta de asteroides; delega en `NeoService` |
| `WatchlistController` | Expone endpoints CRUD de watchlist; delega en `WatchlistService` |
| `NeoService` | Llama a `NasaApiClient`, mapea la respuesta, ordena la lista, identifica el más peligroso |
| `WatchlistService` | Mantiene `List<Asteroid>` en memoria, valida duplicados y existencia |
| `NasaApiClient` | Construye la URL NASA, ejecuta el `GET` con `RestTemplate`, retorna el JSON crudo o mapeado |
| `Asteroid` | Modelo de datos con campos mapeados desde el JSON de NASA |
| `AppConfig` | Define el bean `RestTemplate`; lee `nasa.api.key` de `application.properties` |

---

### Endpoints REST

| Método | Path | Descripción |
|--------|------|-------------|
| `GET` | `/api/neo/feed` | Lista asteroides por rango de fechas. Params: `start_date`, `end_date`, `sort_by` (size\|velocity), `order` (asc\|desc) |
| `GET` | `/api/neo/most-dangerous` | Retorna el asteroide con menor `miss_distance_km`. Params: `start_date`, `end_date` |
| `GET` | `/api/watchlist` | Lista todos los asteroides en seguimiento |
| `POST` | `/api/watchlist/{asteroidId}` | Agrega un asteroide a la watchlist (requiere que el asteroide haya sido consultado antes) |
| `DELETE` | `/api/watchlist/{asteroidId}` | Elimina un asteroide de la watchlist |

---

### Campos del JSON NASA NeoWs a Mapear

Respuesta de `GET https://api.nasa.gov/neo/rest/v1/feed`:

```json
{
  "near_earth_objects": {
    "2025-01-15": [
      {
        "id": "3542519",
        "neo_reference_id": "3542519",
        "name": "(2010 PK9)",
        "is_potentially_hazardous_asteroid": false,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0531,
            "estimated_diameter_max": 0.1188
          }
        },
        "close_approach_data": [
          {
            "close_approach_date": "2025-01-15",
            "relative_velocity": {
              "kilometers_per_hour": "45123.456"
            },
            "miss_distance": {
              "kilometers": "1234567.89"
            }
          }
        ]
      }
    ]
  }
}
```

**Campos requeridos:**
| Campo NASA JSON | Campo en `Asteroid.java` |
|----------------|--------------------------|
| `id` | `id` |
| `name` | `name` |
| `is_potentially_hazardous_asteroid` | `isPotentiallyHazardous` |
| `estimated_diameter.kilometers.estimated_diameter_min` | `estimatedDiameterKmMin` |
| `estimated_diameter.kilometers.estimated_diameter_max` | `estimatedDiameterKmMax` |
| `close_approach_data[0].close_approach_date` | `closeApproachDate` |
| `close_approach_data[0].relative_velocity.kilometers_per_hour` | `relativeVelocityKmh` |
| `close_approach_data[0].miss_distance.kilometers` | `missDistanceKm` |

> Nota: `relative_velocity` y `miss_distance` vienen como **String** en el JSON de NASA — se deben parsear a `Double` al mapear.

---

### Configuración (`application.properties`)

```properties
nasa.api.key=DEMO_KEY
nasa.api.base-url=https://api.nasa.gov/neo/rest/v1
server.port=8080
```

---

## Status: ✅ Completada

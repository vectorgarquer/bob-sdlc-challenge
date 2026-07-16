# Evidencia — Etapa 1: Planificación

## Prompt enviado a Bob (modo Plan)

> "Actúa como Tech Lead de un equipo de 4 personas que construye el sistema NeoTracker.
> El requerimiento semilla es:
> 1. Consultar asteroides cercanos a la Tierra en un rango de fechas (máximo 7 días) vía NASA NeoWs API.
> 2. Listar y ordenar los resultados por tamaño estimado o velocidad relativa.
> 3. Identificar el más peligroso del rango: el que tenga menor miss_distance.
> 4. Mantener una lista de seguimiento (watchlist) en memoria: agregar y eliminar asteroides.
> Stack: Java 17+, Spring Boot 3.x, REST API, Maven.
> Genera: ≥4 historias de usuario con formato 'Como [rol], quiero [acción] para [beneficio]',
> criterios de aceptación por historia, y las entidades de datos principales."

---

## Historias de Usuario

### HU-01 — Consulta por rango de fechas
**Como** operador del Centro de Monitoreo Planetario,  
**quiero** consultar los asteroides cercanos a la Tierra en un rango de fechas (máximo 7 días),  
**para** obtener información actualizada de los objetos que se acercan al planeta en un período determinado.

**Criterios de Aceptación:**
- [ ] El sistema acepta `start_date` y `end_date` en formato `YYYY-MM-DD`.
- [ ] El rango máximo permitido es de 7 días; si se supera, el sistema retorna un error descriptivo.
- [ ] El endpoint `GET /api/neo/feed?start_date=...&end_date=...` retorna la lista de asteroides del período.
- [ ] Cada asteroide en la respuesta incluye: `id`, `name`, `estimated_diameter_km_min`, `estimated_diameter_km_max`, `relative_velocity_kmh`, `miss_distance_km`, `is_potentially_hazardous`.

---

### HU-02 — Listado ordenado
**Como** analista de riesgos,  
**quiero** listar los asteroides ordenados por tamaño estimado o por velocidad relativa,  
**para** priorizar rápidamente los objetos más relevantes según el criterio de análisis del momento.

**Criterios de Aceptación:**
- [ ] El endpoint acepta un parámetro `sort_by` con valores `size` o `velocity`.
- [ ] El parámetro `order` acepta `asc` o `desc` (por defecto `desc`).
- [ ] La ordenación por `size` usa `estimated_diameter_km_max`.
- [ ] La ordenación por `velocity` usa `relative_velocity_kmh`.
- [ ] Si `sort_by` tiene un valor inválido, el sistema retorna HTTP 400 con mensaje descriptivo.

---

### HU-03 — Identificar el más peligroso
**Como** director del Centro de Monitoreo Planetario,  
**quiero** que el sistema identifique automáticamente el asteroide con menor distancia de acercamiento (`miss_distance`) en el rango consultado,  
**para** conocer de inmediato cuál objeto representa el mayor riesgo de impacto.

**Criterios de Aceptación:**
- [ ] El endpoint `GET /api/neo/most-dangerous?start_date=...&end_date=...` retorna un único asteroide.
- [ ] El asteroide retornado es el que tiene el valor más bajo de `miss_distance_km` en el rango.
- [ ] Si el rango no contiene asteroides, el sistema retorna HTTP 404 con mensaje descriptivo.

---

### HU-04 — Gestión de Watchlist
**Como** investigador,  
**quiero** agregar y eliminar asteroides de una lista de seguimiento en memoria,  
**para** hacer un seguimiento personalizado de los objetos de mayor interés sin necesidad de consultar la NASA API repetidamente.

**Criterios de Aceptación:**
- [ ] `POST /api/watchlist/{asteroidId}` agrega el asteroide a la lista de seguimiento.
- [ ] Si el asteroide ya está en la watchlist, el sistema retorna HTTP 409 (Conflict).
- [ ] `DELETE /api/watchlist/{asteroidId}` elimina el asteroide de la lista.
- [ ] Si el asteroide no existe en la watchlist, el sistema retorna HTTP 404.
- [ ] `GET /api/watchlist` retorna todos los asteroides en seguimiento.
- [ ] La watchlist se mantiene en memoria (no persiste entre reinicios de la aplicación).

---

### HU-05 — Visualización de Watchlist
**Como** investigador,  
**quiero** consultar en cualquier momento la lista completa de asteroides que estoy siguiendo,  
**para** revisar de un vistazo todos los objetos bajo vigilancia activa.

**Criterios de Aceptación:**
- [ ] `GET /api/watchlist` retorna HTTP 200 con el array de asteroides (puede ser vacío `[]`).
- [ ] Cada item de la watchlist incluye los mismos campos que la respuesta del feed.

---

## Entidades de Datos Principales

### `Asteroid`
| Campo | Tipo | Fuente NASA |
|-------|------|-------------|
| `id` | String | `neo_reference_id` |
| `name` | String | `name` |
| `estimatedDiameterKmMin` | Double | `estimated_diameter.kilometers.estimated_diameter_min` |
| `estimatedDiameterKmMax` | Double | `estimated_diameter.kilometers.estimated_diameter_max` |
| `relativeVelocityKmh` | Double | `close_approach_data[0].relative_velocity.kilometers_per_hour` |
| `missDistanceKm` | Double | `close_approach_data[0].miss_distance.kilometers` |
| `isPotentiallyHazardous` | Boolean | `is_potentially_hazardous_asteroid` |
| `closeApproachDate` | String | `close_approach_data[0].close_approach_date` |

### `WatchlistItem`
Reutiliza la entidad `Asteroid` — la watchlist es una `List<Asteroid>` en memoria gestionada por `WatchlistService`.

---

## Decisiones de Equipo

| Decisión | Valor |
|----------|-------|
| Lenguaje | Java 17+ |
| Framework | Spring Boot 3.x |
| Build tool | Maven |
| Interfaz | REST API |
| Persistencia | Sin base de datos — watchlist en memoria |
| API Key NASA | `DEMO_KEY` (desarrollo) |
| Puerto | `8080` (por defecto Spring Boot) |

---

## Status: ✅ Completada

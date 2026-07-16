# NeoTracker — Sistema de Monitoreo de Asteroides Cercanos a la Tierra

Sistema REST API construido con Java 17 y Spring Boot 3.x que consume la [NASA NeoWs API](https://api.nasa.gov) para rastrear y analizar objetos cercanos a la Tierra (NEOs).

> Desarrollado por el **Equipo** como parte del NeoTracker Challenge — SDLC con IBM Bob.

---

## Tecnologías

| Tecnología | Versión |
|-----------|---------|
| Java | 17+ |
| Spring Boot | 3.2.0 |
| Maven | 3.8+ |
| JUnit 5 | incluido en spring-boot-starter-test |
| Mockito | incluido en spring-boot-starter-test |
| NASA NeoWs API | v1 |

---

## Instalación

### Prerrequisitos

- Java 17 o superior instalado (`java -version`)
- Maven 3.8 o superior instalado (`mvn -version`)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/neotracker-equipo.git
cd neotracker-equipo

# 2. Compilar el proyecto
mvn clean compile

# 3. Ejecutar la aplicación
mvn spring-boot:run
```

La aplicación estará disponible en `http://localhost:8080`.

---

## Configuración de la NASA API Key

Editar el archivo `src/main/resources/application.properties`:

```properties
# Usar DEMO_KEY para pruebas (limitado a ~30 peticiones/hora)
nasa.api.key=DEMO_KEY

# Para más llamadas, obtener una key gratuita en https://api.nasa.gov
# nasa.api.key=TU_API_KEY_AQUI

nasa.api.base-url=https://api.nasa.gov/neo/rest/v1
server.port=8080
```

Obtener una API key gratuita en [https://api.nasa.gov](https://api.nasa.gov) toma menos de 2 minutos.

---

## Endpoints Disponibles

### 1. Listar asteroides por rango de fechas

```
GET /api/neo/feed?start_date={YYYY-MM-DD}&end_date={YYYY-MM-DD}&sort_by={size|velocity}&order={asc|desc}
```

| Parámetro | Obligatorio | Descripción |
|-----------|-------------|-------------|
| `start_date` | ✅ | Fecha de inicio (YYYY-MM-DD) |
| `end_date` | ✅ | Fecha de fin (YYYY-MM-DD, máx. 7 días después de start) |
| `sort_by` | ❌ | `size` (tamaño) o `velocity` (velocidad) |
| `order` | ❌ | `asc` o `desc` (default: `desc`) |

**Ejemplo:**
```bash
curl "http://localhost:8080/api/neo/feed?start_date=2025-01-15&end_date=2025-01-20&sort_by=velocity&order=asc"
```

**Respuesta:**
```json
[
  {
    "id": "3542519",
    "name": "(2010 PK9)",
    "estimatedDiameterKmMin": 0.0531,
    "estimatedDiameterKmMax": 0.1188,
    "relativeVelocityKmh": 45123.45,
    "missDistanceKm": 1234567.89,
    "potentiallyHazardous": false,
    "closeApproachDate": "2025-01-15"
  }
]
```

---

### 2. Identificar el asteroide más peligroso

```
GET /api/neo/most-dangerous?start_date={YYYY-MM-DD}&end_date={YYYY-MM-DD}
```

Retorna el asteroide con la **menor distancia de acercamiento** (`missDistanceKm`) del rango indicado.

**Ejemplo:**
```bash
curl "http://localhost:8080/api/neo/most-dangerous?start_date=2025-01-15&end_date=2025-01-20"
```

**Respuesta:**
```json
{
  "id": "54321",
  "name": "(2022 XY1)",
  "estimatedDiameterKmMin": 0.8,
  "estimatedDiameterKmMax": 2.0,
  "relativeVelocityKmh": 99000.0,
  "missDistanceKm": 80000.0,
  "potentiallyHazardous": true,
  "closeApproachDate": "2025-01-16"
}
```

---

### 3. Ver la Watchlist

```
GET /api/watchlist
```

**Ejemplo:**
```bash
curl "http://localhost:8080/api/watchlist"
```

**Respuesta:** Array de asteroides (puede ser `[]` si está vacía).

---

### 4. Agregar a la Watchlist

```
POST /api/watchlist/{asteroidId}?start_date={YYYY-MM-DD}&end_date={YYYY-MM-DD}
```

Busca el asteroide en el feed de NASA para el rango dado y lo agrega a la watchlist.

**Ejemplo:**
```bash
curl -X POST "http://localhost:8080/api/watchlist/3542519?start_date=2025-01-15&end_date=2025-01-20"
```

| Código HTTP | Significado |
|-------------|-------------|
| 201 Created | Asteroide agregado exitosamente |
| 400 Bad Request | Parámetros inválidos o asteroide no encontrado en el rango |
| 409 Conflict | El asteroide ya está en la watchlist |

---

### 5. Eliminar de la Watchlist

```
DELETE /api/watchlist/{asteroidId}
```

**Ejemplo:**
```bash
curl -X DELETE "http://localhost:8080/api/watchlist/3542519"
```

| Código HTTP | Significado |
|-------------|-------------|
| 204 No Content | Asteroide eliminado exitosamente |
| 404 Not Found | El asteroide no existe en la watchlist |

---

## Ejecutar los Tests

```bash
mvn test
```

Los tests están ubicados en `src/test/java/` y usan datos mock — **no realizan llamadas reales a la NASA API**.

Casos de prueba cubiertos:
1. Ordenar por velocidad ascendente
2. Ordenar por tamaño descendente
3. Identificar el asteroide con menor `missDistanceKm`
4. Agregar asteroide a watchlist
5. Prevenir duplicados en watchlist
6. Eliminar asteroide de watchlist
7. Watchlist vacía retorna lista vacía
8. Rango de fechas > 7 días lanza excepción
9. Valor inválido de `sort_by` lanza excepción

---

## Estructura del Proyecto

```
neotracker-equipo/
├── pom.xml
├── README.md
├── README-solution.md                     ← Este archivo
├── neotracker-equipo-plan.md              ← Plan de acción del equipo
├── src/
│   ├── main/
│   │   ├── java/com/equipo/neotracker/
│   │   │   ├── NeoTrackerApplication.java
│   │   │   ├── config/AppConfig.java
│   │   │   ├── client/NasaApiClient.java
│   │   │   ├── model/Asteroid.java
│   │   │   ├── service/NeoService.java
│   │   │   ├── service/WatchlistService.java
│   │   │   ├── controller/NeoController.java
│   │   │   └── controller/WatchlistController.java
│   │   └── resources/application.properties
│   └── test/
│       └── java/com/equipo/neotracker/service/
│           ├── NeoServiceTest.java
│           └── WatchlistServiceTest.java
├── tests/
│   ├── NeoServiceTest.java                ← Copia de referencia
│   └── WatchlistServiceTest.java
└── evidence/
    ├── 01-sdlc-stages/evidencia.md
    ├── 02-bob-usage/evidencia.md
    ├── 03-bob-modes/evidencia.md
    ├── 04-bob-skills/evidencia.md
    └── 05-token-strategy/evidencia.md
```

---

## Notas

- La **watchlist** se mantiene en memoria — se reinicia al detener la aplicación.
- El rango de fechas máximo para la consulta NASA es **7 días**.
- Con `DEMO_KEY` hay un límite de ~30 peticiones/hora y 50/día. Para más llamadas, usar una key propia.

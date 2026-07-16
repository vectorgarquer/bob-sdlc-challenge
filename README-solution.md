# 🛰️ NeoTracker — Centro de Monitoreo de Objetos Cercanos a la Tierra

> Sistema de rastreo y análisis de asteroides NEO construido con Python, consumiendo la [NASA NeoWs API](https://api.nasa.gov).
> Desarrollado como parte del **NeoTracker Challenge — SDLC con IBM Bob**.

---

## 📋 Descripción

**NeoTracker** es una aplicación CLI que permite al Centro de Monitoreo Planetario:

- Consultar asteroides cercanos a la Tierra en un rango de fechas
- Listar y ordenar resultados por tamaño estimado o velocidad relativa
- Identificar el asteroide más peligroso (menor distancia de acercamiento)
- Mantener una lista de seguimiento en memoria

---

## 🧰 Tecnologías

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.9+ |
| HTTP client | `urllib` (stdlib — sin dependencias externas) |
| Tests | `unittest` (stdlib) + compatible con `pytest` |
| Interfaz | CLI (`argparse`) |
| Persistencia | En memoria (sin base de datos) |

---

## 🚀 Instalación y ejecución

### Requisitos

- Python 3.9 o superior
- Conexión a internet (para consultar la NASA API)

### Clonar y ejecutar

```bash
git clone https://github.com/TU_USUARIO/neotracker-TU_EQUIPO.git
cd neotracker-TU_EQUIPO
```

No hay dependencias externas — Python stdlib es suficiente.

---

## 🔑 Obtener API Key gratuita de NASA

1. Ve a [https://api.nasa.gov](https://api.nasa.gov) y haz clic en **"Generate API Key"**
2. Llena el formulario (nombre, email)
3. Recibirás tu key por email en segundos

> Para el challenge, `DEMO_KEY` es suficiente (límite: 30 req/hora, 50 req/día).

---

## 💻 Uso

Todos los comandos se ejecutan desde la carpeta `src/`:

```bash
cd src/
```

### Consultar asteroides en un rango de fechas

```bash
# Sin ordenamiento
python cli.py fetch --start 2025-01-01 --end 2025-01-07

# Ordenados por tamaño (mayor primero)
python cli.py fetch --start 2025-01-01 --end 2025-01-07 --sort size

# Ordenados por velocidad (menor primero)
python cli.py fetch --start 2025-01-01 --end 2025-01-07 --sort velocity

# Con tu propia API key
python cli.py --key TU_API_KEY fetch --start 2025-01-01 --end 2025-01-07
```

**Ejemplo de salida:**
```
📡 42 NEOs encontrados (2025-01-01 → 2025-01-07)

⚠️  (2015 TB145)                          Ø 0.5000 km  vel     82000 km/h  dist       500000 km  2025-01-03
   (2024 YR4)                             Ø 0.0450 km  vel     45000 km/h  dist      1200000 km  2025-01-04
```

> `⚠️` indica asteroide potencialmente peligroso (`is_potentially_hazardous_asteroid = true`).

---

### Identificar el asteroide más peligroso

El asteroide con la **menor distancia de acercamiento** (`miss_distance`) del rango consultado:

```bash
python cli.py danger --start 2025-01-01 --end 2025-01-07
```

**Ejemplo de salida:**
```
☄️  Asteroide más peligroso (2025-01-01 → 2025-01-07):

{
  "id": "3729835",
  "name": "(2015 XC352)",
  "diameter_km_avg": 0.0512,
  "is_potentially_hazardous": false,
  "relative_velocity_kmh": 67234.12,
  "miss_distance_km": 487234.50,
  "close_approach_date": "2025-01-03"
}
```

---

### Lista de seguimiento

```bash
# Agregar un asteroide (requiere su ID y el rango donde buscarlo)
python cli.py watch add 3729835 --start 2025-01-01 --end 2025-01-07

# Ver la lista
python cli.py watch list

# Eliminar un asteroide
python cli.py watch remove 3729835
```

---

## 📁 Estructura del proyecto

```
neotracker/
├── README-solution.md          # Este archivo
├── src/
│   ├── models.py               # Entidades: NearEarthObject, WatchList
│   ├── nasa_client.py          # Cliente HTTP para la NASA NeoWs API
│   ├── analyzer.py             # Lógica: ordenamiento, identificación del más peligroso
│   ├── watchlist_service.py    # Servicio de lista de seguimiento en memoria
│   └── cli.py                  # Interfaz de línea de comandos
└── tests/
    └── test_neotracker.py      # 17 tests unitarios con datos mock
```

---

## 🧪 Correr los tests

```bash
# Con pytest (recomendado)
pip install pytest
python -m pytest tests/ -v

# Con unittest (sin instalaciones adicionales)
python -m unittest discover tests -v
```

**Casos de prueba cubiertos:**

| # | Caso | Clase |
|---|------|-------|
| 1 | Ordenar por velocidad ascendente | `TestSortByVelocity` |
| 2 | Ordenar por velocidad descendente | `TestSortByVelocity` |
| 3 | Ordenar por tamaño descendente | `TestSortBySize` |
| 4 | Ordenar por tamaño ascendente | `TestSortBySize` |
| 5 | Identificar menor miss_distance | `TestFindMostDangerous` |
| 6 | Lista vacía lanza ValueError | `TestFindMostDangerous` |
| 7 | Comparación numérica (no string) | `TestFindMostDangerous` |
| 8 | Agregar a watchlist retorna True | `TestWatchListAdd` |
| 9 | El item queda en la lista | `TestWatchListAdd` |
| 10 | Duplicado retorna False | `TestWatchListDuplicate` |
| 11 | Tamaño no cambia tras duplicado | `TestWatchListDuplicate` |
| 12 | Eliminar existente retorna True | `TestWatchListRemove` |
| 13 | Item ya no está en lista | `TestWatchListRemove` |
| 14 | Eliminar no-existente retorna False | `TestWatchListRemove` |

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                         CLI                             │
│                      (cli.py)                           │
└────────────┬──────────────────────┬────────────────────┘
             │                      │
     ┌───────▼──────┐      ┌────────▼───────────┐
     │  nasa_client  │      │  watchlist_service  │
     │ (fetch_neos)  │      │  (add/remove/list)  │
     └───────┬───────┘      └────────┬────────────┘
             │                       │
     ┌───────▼──────┐       ┌────────▼──────┐
     │   analyzer    │       │    WatchList   │
     │ (sort, danger)│       │   (models.py)  │
     └───────┬───────┘       └───────────────┘
             │
     ┌───────▼──────────┐
     │  NearEarthObject  │
     │   (models.py)     │
     └───────────────────┘
```

**Flujo de datos:**
1. `cli.py` recibe argumentos y delega al servicio correspondiente
2. `nasa_client.fetch_neos()` llama a la API, parsea el JSON y retorna `List[NearEarthObject]`
3. `analyzer` aplica ordenamiento o identifica el más peligroso
4. `watchlist_service` gestiona la lista en memoria usando `WatchList`

---

## 📡 Endpoint de la NASA NeoWs API

```
GET https://api.nasa.gov/neo/rest/v1/feed
    ?start_date=YYYY-MM-DD
    &end_date=YYYY-MM-DD
    &api_key=DEMO_KEY
```

**Campos utilizados por NeoTracker:**

| Campo JSON | Uso |
|---|---|
| `id` | Identificador único del NEO |
| `name` | Nombre del asteroide |
| `estimated_diameter.kilometers.estimated_diameter_min/max` | Tamaño estimado |
| `is_potentially_hazardous_asteroid` | Bandera de peligrosidad |
| `close_approach_data[0].relative_velocity.kilometers_per_hour` | Velocidad relativa |
| `close_approach_data[0].miss_distance.kilometers` | Distancia de acercamiento |
| `close_approach_data[0].close_approach_date` | Fecha de acercamiento |

---

## 👥 Equipo

Challenge desarrollado con **IBM Bob** como asistente de IA en todas las etapas del SDLC.

---

## 📄 Licencia

MIT — uso libre para fines educativos.

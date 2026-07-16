# NASA NeoWs REST API 🚀

REST API construida con **Python + FastAPI** que consume la [NASA NeoWs API](https://api.nasa.gov/) para consultar, ordenar e identificar asteroides cercanos a la Tierra, con una lista de seguimiento en memoria.

---

## Requisitos

- Python 3.11+
- pip

---

## Instalación

```bash
# 1. Clona el repositorio y entra a la carpeta
cd nasa-neows-api

# 2. Crea y activa un entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Instala las dependencias
pip install -r requirements.txt
```

---

## Variables de entorno

Copia el archivo de ejemplo y ajusta tu API key:

```bash
cp .env.example .env
```

| Variable | Descripción | Default |
|---|---|---|
| `NASA_API_KEY` | API key de la NASA | `DEMO_KEY` |

> Obtén una key gratuita en [api.nasa.gov](https://api.nasa.gov/) en menos de 2 minutos.

---

## Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

Servidor disponible en: `http://localhost:8000`  
Documentación Swagger: `http://localhost:8000/docs`

---

## Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/health` | Health check |
| `GET` | `/asteroids` | Lista asteroides por rango de fechas (máx. 7 días) |
| `GET` | `/asteroids/most-dangerous` | Asteroide con menor distancia a la Tierra |
| `GET` | `/watchlist` | Lista de seguimiento actual |
| `POST` | `/watchlist/{asteroid_id}` | Agrega un asteroide a la lista |
| `DELETE` | `/watchlist/{asteroid_id}` | Elimina un asteroide de la lista |

---

## Ejemplos de uso

### Consultar asteroides con ordenamiento
```bash
curl "http://localhost:8000/asteroids?start_date=2024-01-01&end_date=2024-01-07&sort_by=velocity&order=desc"
```

### Identificar el más peligroso
```bash
curl "http://localhost:8000/asteroids/most-dangerous?start_date=2024-01-01&end_date=2024-01-07"
```

### Agregar a la lista de seguimiento
```bash
curl -X POST "http://localhost:8000/watchlist/3542519"
```

### Ver la lista de seguimiento
```bash
curl "http://localhost:8000/watchlist"
```

### Eliminar de la lista
```bash
curl -X DELETE "http://localhost:8000/watchlist/3542519"
```

---

## Estructura del proyecto

```
nasa-neows-api/
├── app/
│   ├── main.py              # Entry point FastAPI
│   ├── config.py            # Variables de entorno
│   ├── models/
│   │   └── asteroid.py      # Modelo NearEarthObject (Pydantic)
│   ├── routers/
│   │   ├── asteroids.py     # Endpoints de consulta
│   │   └── watchlist.py     # Endpoints de seguimiento
│   └── services/
│       ├── nasa_service.py      # Integración NASA NeoWs API
│       └── watchlist_service.py # Store en memoria
├── .env.example
├── requirements.txt
└── README.md
```

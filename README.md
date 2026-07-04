# 🚀 NeoTracker Challenge — SDLC con IBM Bob

![Luna y Tierra desde el espacio — NASA](images/art002e009285~large.jpg)
*Al borde de dos mundos — la Tierra en fase creciente asomándose detrás de la Luna, capturada por la tripulación de Artemis II durante su sobrevuelo lunar. El mismo tipo de objetos que rastrearás en este challenge se acercan peligrosamente a este planeta. Imagen: [NASA (art002e009285)](https://www.nasa.gov/image-detail/amf-art002e009285/)*

> **Equipos de 5 personas · ~60 minutos · Lenguaje libre**

[![IBM Bob](https://img.shields.io/badge/Powered%20by-IBM%20Bob-0f62fe?style=flat-square)](https://bob.ibm.com/docs/ide)
[![NASA API](https://img.shields.io/badge/API-NASA%20NeoWs-0b3d91?style=flat-square)](https://api.nasa.gov)
[![Lenguaje libre](https://img.shields.io/badge/Lenguaje-El%20que%20elijan-4caf50?style=flat-square)](#)

---

## 🧩 El Reto

El **Centro de Monitoreo Planetario** necesita un sistema para rastrear y analizar **objetos cercanos a la Tierra (NEOs)**. Tu equipo deberá construirlo en **~60 minutos** usando **IBM Bob como un asistente de IA para el ciclo de vida del desarrollo de software**.

> El objetivo no es solo que el código funcione — es demostrar cómo **Bob participó en cada decisión** del ciclo de vida del desarrollo de software.

---

## 📋 Requerimiento Semilla

El sistema debe tener las siguientes capacidades, consumiendo la [NASA NeoWs API](https://api.nasa.gov):

1. **Consultar asteroides** cercanos a la Tierra en un rango de fechas (máximo 7 días).
2. **Listar y ordenar** los resultados por tamaño estimado o velocidad relativa.
3. **Identificar el más peligroso** del rango consultado — el que tenga menor `miss_distance` (distancia de acercamiento a la Tierra).
4. **Mantener una lista de seguimiento** donde se puedan agregar y eliminar asteroides de interés (en memoria).
5. La interfaz puede ser CLI, REST API o web simple — **el equipo decide**.

> No se requiere autenticación propia, base de datos persistente ni UI elaborada.
> Usar `api_key=DEMO_KEY` es suficiente para el challenge. Para más llamadas, obtener una key gratuita en [api.nasa.gov](https://api.nasa.gov) toma menos de 2 minutos.

**Endpoint principal:**
```
GET https://api.nasa.gov/neo/rest/v1/feed?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&api_key=DEMO_KEY
```

---

## 🗺️ Mapa del Challenge (SDLC con Bob)

Sigue las guías en `docs/sdlc-guide/` en orden.

| # | Etapa | Modo Bob sugerido | Tiempo ⏱ |
|---|-------|-------------------|-----------|
| 1 | [📐 Planificación](docs/sdlc-guide/01-planning.md) | `Plan` | 8 min |
| 2 | [🏗️ Diseño](docs/sdlc-guide/02-design.md) | `Ask` | 8 min |
| 3 | [💻 Desarrollo](docs/sdlc-guide/03-development.md) | `Agent` | 20 min |
| 4 | [🧪 Pruebas](docs/sdlc-guide/04-testing.md) | `Agent` | 8 min |
| 5 | [📝 Documentación](docs/sdlc-guide/05-documentation.md) | `Agent` / `Ask` | 5 min |
| 6 | [🚀 Entrega](docs/sdlc-guide/06-delivery.md) | `Agent` (PR) | 5 min |
| 7 | [⚡ Estrategia de Tokens](docs/sdlc-guide/07-token-strategy.md) | Todos | continuo |

---

## 📁 Estructura esperada de tu repositorio

```
mi-equipo-neotracker/
├── README-solution.md                        # Documentación generada con Bob
├── src/                                      # Código fuente (lenguaje libre)
│   └── ...
├── tests/                                    # Unit tests generados con Bob
│   └── ...
└── evidence/
    ├── 01-sdlc-stages/evidencia.md           # Cómo pasaron por cada etapa del SDLC
    ├── 02-bob-usage/evidencia.md             # Cómo usaron Bob
    ├── 03-bob-modes/evidencia.md             # Cómo interactuaron con los modos de Bob
    ├── 04-bob-skills/evidencia.md            # Si usaron Skills de Bob
    └── 05-token-strategy/evidencia.md        # Estrategia para usar menos tokens
```

> **La carpeta `evidence/` es completamente libre.** No hay formato obligatorio.
> Documenten como prefieran: texto, screenshots, prompts usados, notas — lo que les sea más natural.

---

## 🏆 Rúbrica de Evaluación

La rúbrica la maneja el organizador del challenge. Los cinco rubros evaluados son:

| # | Rubro | Carpeta de evidencia |
|---|-------|----------------------|
| 1 | Cobertura del SDLC — pasar por todas las etapas | `evidence/01-sdlc-stages/` |
| 2 | Evidencia del uso de Bob — prompts, calidad, decisiones técnicas | `evidence/02-bob-usage/` |
| 3 | Uso de Modos de Bob — Plan, Ask, Agent y justificación | `evidence/03-bob-modes/` |
| 4 | Skills de Bob — identificación, creación y aplicación | `evidence/04-bob-skills/` |
| 5 | Estrategia de Tokens — reflexión y técnicas para reducir iteraciones | `evidence/05-token-strategy/` |

---

## 🚀 ¿Cómo empezar?

1. **Crea un fork** de este repositorio.
2. Renombra tu fork como `neotracker-[nombre-equipo]`.
3. Sigue las guías en `docs/sdlc-guide/` en orden.
4. Llena los archivos `evidence/*/evidencia.md` con lo que su equipo considere relevante.
5. Al finalizar, abre un **Pull Request** a este repo con el título `[EQUIPO: nombre] NeoTracker Challenge`.

---

## 🔗 Recursos

| Recurso | Link |
|---------|------|
| 🛰️ NASA NeoWs API Docs | https://api.nasa.gov |
| 🔑 Obtener API Key gratuita | https://api.nasa.gov/#signUp |
| 📖 IBM Bob Docs | https://bob.ibm.com/docs/ide |
| 🆓 Cómo obtener tu prueba gratuita de Bob (30 días) | https://medium.com/@victor.chequer/how-to-get-a-free-30-day-ibm-bob-trial-step-by-step-guide-5d2cdddea8f0 |
| 🧩 Modos y Skills de Bob | https://medium.com/@victor.chequer/ibm-bob-modes-vs-skills-the-complete-guide-to-reliable-ai-assisted-development-c5d528ff4fac |
| 🔌 MCP con Bob | https://medium.com/@victor.chequer/ibm-bob-driven-mcp-in-practice-concepts-use-cases-and-building-a-java-quarkus-mcp-server-8b43f379c051 |

---

## ⚠️ Reglas

- ✅ Pueden usar **cualquier lenguaje de programación**.
- ✅ Bob **debe participar** en cada etapa (evidencia obligatoria).
- ✅ Código generado con Bob **debe funcionar** — revísenlo siempre.
- ❌ No copiar código de fuentes externas que no sea Bob o la NASA API.
- ❌ No copiar evidencias entre equipos.

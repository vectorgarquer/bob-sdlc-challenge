# 🎮 PokéDev Challenge — SDLC con IBM Bob

> **Equipos de 5 personas · ~60 minutos · Lenguaje libre**

[![IBM Bob](https://img.shields.io/badge/Powered%20by-IBM%20Bob-0f62fe?style=flat-square)](https://bob.ibm.com/docs/ide)
[![PokéAPI](https://img.shields.io/badge/API-PokéAPI%20v2-ef5350?style=flat-square)](https://pokeapi.co)
[![Lenguaje libre](https://img.shields.io/badge/Lenguaje-El%20que%20elijan-4caf50?style=flat-square)](#)

---

## 🧩 El Reto

El **Profesor Oak** necesita un sistema para que los entrenadores Pokémon puedan **armar y gestionar su equipo de batalla**. Tu equipo deberá construirlo en **~60 minutos** usando **IBM Bob como copiloto en cada etapa del SDLC**.

> ⚡ El objetivo no es solo que el código funcione — es demostrar cómo **Bob participó en cada decisión** del ciclo de vida.

---

## 📋 Requerimiento Semilla

El sistema debe tener las siguientes capacidades:

1. **Buscar un Pokémon** por nombre y ver su información básica (tipo, habilidades, estadísticas base) consumiendo la [PokéAPI](https://pokeapi.co/docs/v2).
2. **Armar un equipo** de hasta 6 Pokémon (agregar / eliminar del equipo).
3. **Comparar dos Pokémon** mostrando cuál tiene mejores stats totales.
4. El equipo debe **persistir** mientras la aplicación esté corriendo (en memoria es suficiente).
5. La interfaz puede ser CLI, REST API o web simple — **el equipo decide**.

> No se requiere autenticación, base de datos persistente ni UI elaborada.

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
mi-equipo-pokedev/
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

La rúbrica la maneja el organizador del challenge. Los cinco rubros evaluados corresponden directamente a las carpetas de `evidence/`.

---

## 🚀 ¿Cómo empezar?

1. **Crea un fork** de este repositorio.
2. Renombra tu fork como `pokedev-[nombre-equipo]`.
3. Sigue las guías en `docs/sdlc-guide/` en orden.
4. Llena los archivos `evidence/*/evidencia.md` con lo que su equipo considere relevante.
5. Al finalizar, abre un **Pull Request** a este repo con el título `[EQUIPO: nombre] PokéDev Challenge`.

---

## 🔗 Recursos

| Recurso | Link |
|---------|------|
| PokéAPI Docs | https://pokeapi.co/docs/v2 |
| IBM Bob Docs | https://bob.ibm.com/docs/ide |
| Modos de Bob | https://medium.com/@victor.chequer/ibm-bob-modes-vs-skills-the-complete-guide-to-reliable-ai-assisted-development-c5d528ff4fac |
| MCP con Bob | https://medium.com/@victor.chequer/ibm-bob-driven-mcp-in-practice-concepts-use-cases-and-building-a-java-quarkus-mcp-server-8b43f379c051 |

---

## ⚠️ Reglas

- ✅ Pueden usar **cualquier lenguaje de programación**.
- ✅ Bob **debe participar** en cada etapa (evidencia obligatoria).
- ✅ Código generado con Bob **debe funcionar** — revísenlo siempre.
- ❌ No copiar código de fuentes externas que no sea Bob o la PokéAPI.
- ❌ No copiar evidencias entre equipos.

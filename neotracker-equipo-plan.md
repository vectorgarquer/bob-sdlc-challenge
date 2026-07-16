# Plan de Acción — NeoTracker Challenge · Equipo "Equipo"

## Visión General

El **Centro de Monitoreo Planetario** necesita un sistema para rastrear y analizar **objetos cercanos a la Tierra (NEOs)**. El **Equipo** (4 personas) deberá construir el sistema **NeoTracker** en ~60 minutos demostrando que IBM Bob participó activamente en **cada etapa del ciclo de vida del desarrollo de software (SDLC)**.

> El éxito no se mide únicamente por que el código funcione, sino por la evidencia de cómo Bob guió cada decisión técnica y de diseño.

**Repositorio de entrega:** Fork renombrado como `neotracker-equipo`.
**Pull Request final:** `[EQUIPO: Equipo] NeoTracker Challenge`
**Stack tecnológico:** Java 17+ · Spring Boot · Maven o Gradle · REST API · JUnit 5

---

## Asignación de Roles (4 personas)

| Persona | Rol principal |
|---------|---------------|
| Persona 1 | Tech Lead — dirige prompts en Plan/Ask, toma decisiones de arquitectura |
| Persona 2 | Developer — ejecuta prompts en Agent para código fuente (`src/`) |
| Persona 3 | QA — ejecuta prompts en Agent para pruebas (`tests/`) |
| Persona 4 | Documentador/Evidencia — llena archivos `evidence/`, README-solution.md y gestiona el PR |

> Los roles son flexibles; todos participan en revisión y validación.

---

## Sub-Tareas

---

### Sub-Tarea 1 — Planificación (Etapa 1)

- **Status:** `[ ] pending`
- **Modo Bob:** `Plan`
- **Tiempo objetivo:** 8 min
- **Responsable:** Persona 1

#### Intent
Transformar el requerimiento semilla del README en historias de usuario concretas, criterios de aceptación y entidades de datos principales. Esto sienta la base para todas las decisiones técnicas posteriores.

#### Expected Outcomes
- Al menos 4 historias de usuario redactadas con formato estándar.
- Criterios de aceptación definidos para cada historia.
- Entidades de datos principales identificadas (asteroide, watchlist).
- Archivo `evidence/01-sdlc-stages/evidencia.md` creado con los prompts y resultados usados.

#### Todo List
1. Asegurarse de estar en **modo Plan** de Bob.
2. Enviar un único prompt a Bob con el contenido del requerimiento semilla y pedir que genere ≥4 historias de usuario con formato `Como [rol], quiero [acción] para [beneficio]`.
3. Solicitar en el mismo prompt los criterios de aceptación y las entidades de datos.
4. Revisar el output en equipo; ajustar con un prompt de seguimiento si algo es ambiguo.
5. Decidir en equipo el **lenguaje de programación** (Python, Node.js, Go, etc.) y la **interfaz** (CLI, REST API o web simple).
6. Documentar historias, criterios, entidades y la decisión de tecnología en `evidence/01-sdlc-stages/evidencia.md`.

#### Relevant Context
- Requerimientos semilla: [`README.md`](README.md:24-33)
- Guía detallada de esta etapa: [`docs/sdlc-guide/01-planning.md`](docs/sdlc-guide/01-planning.md)
- Carpeta de evidencia: `evidence/01-sdlc-stages/`

---

### Sub-Tarea 2 — Diseño de Arquitectura (Etapa 2)

- **Status:** `[ ] pending`
- **Modo Bob:** `Ask`
- **Tiempo objetivo:** 8 min
- **Responsable:** Persona 1 + Persona 2

#### Intent
Definir los módulos del sistema, la estructura de la API de la NASA y el contrato interno del código antes de escribir una sola línea. Evita retrabajo durante el desarrollo.

#### Expected Outcomes
- Arquitectura de módulos/clases definida (p. ej. `api_client`, `asteroid_service`, `watchlist`, `cli` o `routes`).
- Campos relevantes del JSON de la NASA NeoWs identificados: `name`, `estimated_diameter`, `relative_velocity`, `miss_distance`, `is_potentially_hazardous_asteroid`.
- Stack tecnológico confirmado (lenguaje + librerías/framework).
- Decisiones de diseño documentadas en `evidence/01-sdlc-stages/evidencia.md` (o archivo separado si el equipo prefiere).

#### Todo List
1. Cambiar a **modo Ask** de Bob.
2. Enviar un único prompt describiendo: **Java 17+ con Spring Boot**, los 4 requerimientos funcionales y solicitar una propuesta de módulos/clases con responsabilidades (ej. `NeoController`, `NeoService`, `WatchlistService`, `NasaApiClient`, `Asteroid` model).
3. En el mismo prompt, pedir la estructura del JSON de respuesta de la NASA y los campos necesarios. Incluir la decisión de Maven o Gradle.
4. El equipo discute y valida el diseño propuesto.
5. Si hay cambios, hacer un único prompt de ajuste (no múltiples pequeños).
6. Guardar la arquitectura decidida en `evidence/02-bob-usage/evidencia.md` con los prompts usados.

#### Relevant Context
- Endpoint NASA: `GET https://api.nasa.gov/neo/rest/v1/feed?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&api_key=DEMO_KEY`
- Guía detallada: [`docs/sdlc-guide/02-design.md`](docs/sdlc-guide/02-design.md)
- Campos JSON importantes: `near_earth_objects`, `estimated_diameter.kilometers`, `close_approach_data[].relative_velocity.kilometers_per_hour`, `close_approach_data[].miss_distance.kilometers`

---

### Sub-Tarea 3 — Desarrollo del Código Fuente (Etapa 3)

- **Status:** `[ ] pending`
- **Modo Bob:** `Agent`
- **Tiempo objetivo:** 20 min
- **Responsable:** Persona 2 (Persona 1 supervisa)

#### Intent
Generar el código funcional del sistema NeoTracker en `src/` usando la arquitectura decidida en la Sub-Tarea 2. Bob en modo Agent puede crear y editar archivos directamente.

#### Expected Outcomes
- Código funcional en `src/` que cubra las 4 capacidades obligatorias:
  1. Consultar asteroides en rango de fechas (máx. 7 días) vía NASA NeoWs API.
  2. Listar y ordenar por tamaño estimado **o** velocidad relativa.
  3. Identificar el más peligroso (menor `miss_distance`).
  4. Watchlist en memoria: agregar y eliminar asteroides.
- La aplicación corre sin errores con `api_key=DEMO_KEY`.

#### Todo List
1. Cambiar a **modo Agent** de Bob.
2. Construir **un único prompt inicial grande** que incluya:
   - **Java 17+, Spring Boot 3.x**, `spring-boot-starter-web`, `RestTemplate` o `WebClient`.
   - Herramienta de build: Maven o Gradle.
   - Arquitectura de módulos definida en la Sub-Tarea 2 (Controller, Service, Model, etc.).
   - Los 4 requerimientos funcionales con detalle de campos NASA.
   - Estructura de carpetas estándar Spring Boot (`src/main/java/...`, `src/test/java/...`).
   - Indicación de NO usar base de datos ni autenticación propia (watchlist en `List<Asteroid>` en memoria).
3. Revisar el código generado archivo por archivo.
4. Si hay errores, hacer prompts quirúrgicos: describir el problema en la clase/método específico, no pedir reescritura total.
5. Levantar la app con `mvn spring-boot:run` o `./gradlew bootRun` y probar con una llamada real a la NASA API.
6. Documentar prompts clave y decisiones en `evidence/02-bob-usage/evidencia.md`.

#### Relevant Context
- Guía detallada: [`docs/sdlc-guide/03-development.md`](docs/sdlc-guide/03-development.md)
- Estructura esperada del repo: [`README.md`](README.md:58-73)
- api_key para pruebas: `DEMO_KEY` (límite de tasa bajo; obtener key gratuita en https://api.nasa.gov si se agotan las llamadas)
- Stack: Java 17+, Spring Boot 3.x, `spring-boot-starter-web`, `spring-boot-starter-test` (JUnit 5 + Mockito incluidos)
- Herramienta de build: Maven (`mvn spring-boot:run`) o Gradle (`./gradlew bootRun`)

---

### Sub-Tarea 4 — Pruebas Unitarias (Etapa 4)

- **Status:** `[ ] pending`
- **Modo Bob:** `Agent`
- **Tiempo objetivo:** 8 min
- **Responsable:** Persona 3

#### Intent
Generar y ejecutar ≥6 pruebas unitarias con datos mock (sin llamadas reales a la API) para validar la lógica de negocio del sistema.

#### Expected Outcomes
- ≥6 tests en `tests/` usando datos mock.
- Todos los tests pasan (0 fallos).
- Resultados de ejecución documentados en `evidence/01-sdlc-stages/evidencia.md`.

#### Todo List
1. Permanecer en **modo Agent** (ya tiene contexto del código generado).
2. Enviar **un único prompt** especificando los 6 casos de prueba obligatorios:
   1. Ordenar asteroides por velocidad relativa ascendente.
   2. Ordenar por tamaño estimado descendente.
   3. Identificar correctamente el asteroide con menor `miss_distance`.
   4. Agregar un asteroide al watchlist.
   5. Prevenir duplicados en el watchlist (o manejar el error).
   6. Eliminar un asteroide del watchlist.
3. Incluir en el prompt ejemplos de datos mock con la estructura JSON de la NASA.
4. Ejecutar los tests con el comando del framework elegido.
5. Si algún test falla, indicar a Bob exactamente qué falla con el stack trace — pedir fix quirúrgico.
6. Registrar output de los tests en `evidence/01-sdlc-stages/evidencia.md`.

#### Relevant Context
- Guía detallada: [`docs/sdlc-guide/04-testing.md`](docs/sdlc-guide/04-testing.md)
- El mock data debe simular la estructura real del JSON de la NASA (ver Sub-Tarea 2).

---

### Sub-Tarea 5 — Documentación (Etapa 5)

- **Status:** `[ ] pending`
- **Modo Bob:** `Agent` o `Ask`
- **Tiempo objetivo:** 5 min
- **Responsable:** Persona 4

#### Intent
Generar `README-solution.md` completo que permita a cualquier persona entender, instalar y usar el sistema NeoTracker sin haber participado en su construcción.

#### Expected Outcomes
- `README-solution.md` en la raíz del repositorio con:
  - Descripción del sistema.
  - Stack tecnológico.
  - Instrucciones de instalación paso a paso.
  - Instrucciones para configurar la NASA API key.
  - ≥2 ejemplos de uso reales con comandos o endpoints.
  - Funcionalidades disponibles.
  - Estructura del proyecto.

#### Todo List
1. Si el código ya está revisado → usar **modo Agent** (lee los archivos directamente).
   Si el tiempo es escaso → usar **modo Ask** y describir el código de forma resumida (consume menos tokens).
2. Enviar un prompt con todas las secciones requeridas listadas.
3. Revisar el README generado: verificar que los comandos de instalación sean correctos para el lenguaje elegido.
4. Ajustar con un único prompt de corrección si es necesario.
5. Guardar el archivo como `README-solution.md` en la raíz.

#### Relevant Context
- Guía detallada: [`docs/sdlc-guide/05-documentation.md`](docs/sdlc-guide/05-documentation.md)
- Estructura esperada del repo: [`README.md`](README.md:58-73)

---

### Sub-Tarea 6 — Evidencia de Bob, Modos y Skills (Transversal)

- **Status:** `[ ] pending`
- **Modo Bob:** Todos (se completa de forma continua)
- **Responsable:** Persona 4 (con aportes de todo el equipo)

#### Intent
Llenar los archivos de evidencia que la rúbrica evalúa directamente. Sin evidencia, el trabajo técnico no puntúa en los rubros 2, 3 y 4.

#### Expected Outcomes
- `evidence/02-bob-usage/evidencia.md` — prompts usados, calidad de outputs, decisiones técnicas guiadas por Bob.
- `evidence/03-bob-modes/evidencia.md` — qué modo se usó en cada etapa y por qué (Plan para planificación, Ask para diseño, Agent para código/tests/docs).
- `evidence/04-bob-skills/evidencia.md` — si el equipo usó o creó Skills de Bob (ej. `create-plan`, `xlsx-insights`), documentar cuáles y cómo.
- `evidence/05-token-strategy/evidencia.md` — reflexión sobre las técnicas de optimización de tokens aplicadas.

#### Todo List
1. Durante cada sub-tarea, Persona 4 copia los prompts usados y el output relevante.
2. Al finalizar el challenge, redactar en `evidence/03-bob-modes/evidencia.md` una tabla con: Etapa → Modo Bob → Justificación.
3. En `evidence/04-bob-skills/evidencia.md`, listar las Skills de Bob activadas (p. ej. `create-plan` fue usada en este mismo planning).
4. En `evidence/05-token-strategy/evidencia.md`, documentar al menos 3 técnicas aplicadas:
   - Uso del modo correcto por tarea.
   - Prompts únicos y completos vs. múltiples iteraciones.
   - Prompts quirúrgicos para fixes.
5. Revisar que los 5 archivos `evidence/*/evidencia.md` existan antes del PR.

#### Relevant Context
- Rúbrica de evaluación: [`README.md`](README.md:80-91)
- Guía de estrategia de tokens: [`docs/sdlc-guide/07-token-strategy.md`](docs/sdlc-guide/07-token-strategy.md)
- Skills usadas hasta ahora: `create-plan` (activada en esta sesión de planning)

---

### Sub-Tarea 7 — Entrega Final: Commit y Pull Request (Etapa 6)

- **Status:** `[ ] pending`
- **Modo Bob:** `Agent`
- **Tiempo objetivo:** 5 min
- **Responsable:** Persona 4 + Persona 1 (revisión)

#### Intent
Consolidar todo el trabajo en un commit limpio y abrir el Pull Request final al repositorio original del challenge.

#### Expected Outcomes
- Commit con mensaje en formato Conventional Commits generado por Bob.
- Pull Request abierto con título exacto: `[EQUIPO: Equipo] NeoTracker Challenge`.
- PR contiene: `src/`, `tests/`, `evidence/` (5 archivos), `README-solution.md`.
- Label `challenge-submission` aplicado al PR.

#### Todo List
1. Verificar que todos los archivos requeridos existen localmente.
2. En **modo Agent**, pedir a Bob que genere el mensaje de commit en Conventional Commits describiendo el trabajo realizado.
3. Ejecutar:
   ```
   git add .
   git commit -m "[mensaje generado por Bob]"
   git push origin main
   ```
4. Abrir el PR al repositorio original con:
   - Título: `[EQUIPO: Equipo] NeoTracker Challenge`
   - Descripción generada por Bob (resumen del sistema, stack, instrucciones rápidas).
   - Label: `challenge-submission`.
5. Verificar que el PR incluye todos los archivos requeridos navegando los changed files.

#### Relevant Context
- Guía detallada: [`docs/sdlc-guide/06-delivery.md`](docs/sdlc-guide/06-delivery.md)
- Workflow disponible: **Create Pull Request** (usar `start_workflow` con id `create_pr_workflow` en modo Agent)

---

## Estrategia de Tokens (Aplicar Continuamente)

| Técnica | Cuándo aplicarla |
|---------|-----------------|
| Usar **Plan/Ask** para análisis conceptual | Sub-Tareas 1 y 2 — nunca usar Agent para discutir ideas |
| **Un prompt gordo** en lugar de 10 pequeños | Al inicio de cada sub-tarea — incluir lenguaje, arquitectura, contexto y output esperado |
| **Prompts quirúrgicos** para fixes | Sub-Tareas 3 y 4 — señalar función y error exacto, no pedir reescritura |
| **Documentar en Ask** si se describe el código | Sub-Tarea 5 — si el tiempo es justo, Ask consume menos tokens que Agent leyendo archivos |

---

## Checklist Final de Entrega

- [ ] `src/` con código funcional cubriendo las 4 capacidades
- [ ] `tests/` con ≥6 tests que pasan (mock data)
- [ ] `README-solution.md` completo
- [ ] `evidence/01-sdlc-stages/evidencia.md`
- [ ] `evidence/02-bob-usage/evidencia.md`
- [ ] `evidence/03-bob-modes/evidencia.md`
- [ ] `evidence/04-bob-skills/evidencia.md`
- [ ] `evidence/05-token-strategy/evidencia.md`
- [ ] PR abierto con título y label correctos

---

## Flujo General del Challenge

```
[Plan] ST1: Planificación
    ↓
[Ask]   ST2: Diseño de Arquitectura
    ↓
[Agent] ST3: Desarrollo del Código Fuente
    ↓
[Agent] ST4: Pruebas Unitarias
    ↓
[Agent/Ask] ST5: Documentación
    ↓
[Continuo] ST6: Evidencia (Bob, Modos, Skills, Tokens)
    ↓
[Agent] ST7: Commit + Pull Request
```

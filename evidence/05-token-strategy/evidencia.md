# Evidencia — Estrategia de Tokens

## Reflexión del equipo

El consumo de tokens fue una preocupación desde el minuto 1 del challenge. Con 60 minutos
y el objetivo de cubrir todo el SDLC, cada iteración innecesaria con Bob era tiempo y
presupuesto desperdiciado.

---

## Estrategias aplicadas

### 1. Modo correcto para cada tarea

La primera decisión de ahorro de tokens fue la elección de modos:

| Etapa | Modo elegido | Tokens ahorrados vs. Agent |
|-------|-------------|---------------------------|
| Planificación | `Plan` | ~60% — no activa herramientas |
| Diseño | `Ask` | ~40% — no modifica archivos |
| Desarrollo | `Agent` | N/A — necesario |
| Tests | `Agent` | N/A — necesario |

> Usar `Agent` desde el principio habría triplicado el consumo en las etapas conceptuales.

---

### 2. Un prompt gordo al inicio de cada etapa

**Ejemplo de lo que NO hicimos (ineficiente):**
```
[Turno 1] Crea models.py con NearEarthObject
[Turno 2] Ahora agrega WatchList
[Turno 3] Agrega el método to_dict()
[Turno 4] Ahora crea nasa_client.py...
```
(4+ intercambios, Bob repregunta contexto en cada uno)

**Lo que hicimos (eficiente):**
```
[Turno único] Actúa como dev senior Python. Crea 5 archivos en src/ con esta
arquitectura: [detalle completo de los 5 módulos, endpoint, restricciones, tipos]
```
(1 intercambio → 5 archivos generados correctamente)

**Ahorro estimado:** ~3-4 turnos eliminados = ~1,000-1,500 tokens.

---

### 3. Contexto al inicio, no en el camino

En el prompt de desarrollo incluimos desde el principio:
- Lenguaje y versión (`Python 3.9+`)
- Restricción clave (`miss_distance` es string en el JSON — convertir a float)
- Módulos esperados (5 archivos listados)
- Endpoint exacto de la NASA
- Tipo de interfaz (CLI con argparse)

Esto evitó que Bob hiciera preguntas de seguimiento como:
- "¿Qué lenguaje usarás?"
- "¿Quieres un CLI o REST API?"
- "¿Qué campos del JSON necesitas?"

**Ahorro estimado:** ~3-5 preguntas de seguimiento eliminadas = ~500-800 tokens.

---

### 4. Correcciones quirúrgicas

Cuando hubo que corregir algo, identificamos exactamente el archivo, función y problema:

**Ineficiente:**
```
El código no funciona bien, rehazlo
```

**Eficiente:**
```
En src/analyzer.py, función find_most_dangerous():
verifica que miss_distance_km se compare como float.
Solo toca esa función.
```

Esto evita que Bob reescriba código correcto, perdiendo trabajo y tokens.

---

### 5. Skill para tests repetibles

Creamos una Skill `neotracker-unit-test` que encapsuló el patrón de tests del proyecto.
Cada nueva petición de tests ahorra ~130 tokens de contexto repetido.

**Ver:** `evidence/04-bob-skills/evidencia.md`

---

## Métricas de eficiencia

| Etapa | Turnos con Bob | Turnos estimados sin estrategia |
|-------|---------------|----------------------------------|
| Planificación | 1 | 3-4 |
| Diseño | 2 | 4-5 |
| Desarrollo | 1 (+ 1 corrección) | 8-10 |
| Tests | 1 | 6-8 |
| Documentación | 1 | 2-3 |
| **Total** | **~6 turnos** | **~23-30 turnos** |

**Reducción estimada: ~75% de los turnos necesarios.**

---

## Lección principal

> El token más barato es el que no se gasta.
> La mejor forma de ahorrar tokens no es escribir prompts cortos —
> es escribir **un prompt completo que no genere preguntas de seguimiento**.

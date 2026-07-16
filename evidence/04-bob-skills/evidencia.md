# Evidencia — Skills de Bob

## Skill identificada y creada

### Caso de uso identificado

Durante el desarrollo del challenge notamos que la generación de tests unitarios con
datos mock sigue **siempre el mismo patrón**:

1. Definir fixtures de datos mock (objetos del dominio)
2. Escribir tests de ordenamiento (asc/desc)
3. Escribir tests de casos borde (lista vacía, duplicados, no-existente)
4. Usar `unittest.TestCase` con `setUp`
5. Sin llamadas externas reales

Cada vez que le pedíamos a Bob un test seguíamos repitiendo contexto: el framework, la
restricción de no llamar APIs reales, la estructura del objeto mock. Esto es un candidato
perfecto para una **Skill**.

---

## Skill creada: `neotracker-unit-test`

La Skill encapsula las instrucciones necesarias para que Bob genere tests unitarios
consistentes con el patrón del proyecto sin necesidad de repetir contexto.

**Archivo:** `.bob/skills/neotracker-unit-test.md`

```markdown
---
name: neotracker-unit-test
description: Genera tests unitarios para NeoTracker con datos mock. Usa unittest (stdlib),
             fixtures de NearEarthObject, sin llamadas reales a la NASA API.
---

# NeoTracker — Test Generator

Cuando generes tests para este proyecto:

1. **Siempre importa desde `src/`**: `sys.path.insert(0, "../src")`
2. **Usa `unittest.TestCase`** — no pytest puro (solo stdlib)
3. **Crea fixtures con `make_neo()`** — helper function, no instanciar directamente
4. **No llames a `fetch_neos()`** en ningún test — solo prueba la lógica pura
5. **Casos borde obligatorios**: lista vacía, duplicados, IDs inexistentes
6. **Nombra las clases** como `Test<NombreModulo>` y los métodos como `test_<caso>`
7. **Un `setUp` por clase** si hay estado compartido (ej: WatchList)
```

---

## Cómo la Skill redujo repetición y mejoró el flujo

| Sin la Skill | Con la Skill |
|---|---|
| Prompt incluía: "usa unittest", "sin llamadas a API", "importa desde src/", "crea fixtures mock"... | Prompt simplificado: "Genera tests para `analyzer.py` usando la Skill `neotracker-unit-test`" |
| ~150 tokens de contexto repetido por cada petición de test | ~20 tokens — Bob ya tiene el patrón |
| Riesgo de olvidar alguna restricción (ej: importar desde src/) | Bob sigue el patrón consistentemente |
| Tests inconsistentes si se generan en diferentes momentos | Todos los tests siguen exactamente el mismo patrón |

**Ahorro estimado:** ~130 tokens por cada vez que se pide generar tests.
Con 3-4 iteraciones de tests durante el challenge: ~400-520 tokens ahorrados.

---

## Reflexión

La Skill fue especialmente valiosa porque el patrón de tests era repetible y tenía
varias restricciones no obvias (importar desde `src/`, no llamar a la API real, usar
fixtures en lugar de instanciar directamente). Sin la Skill, cualquier miembro del equipo
que pidiera un test nuevo podría haber olvidado alguna de estas restricciones y generado
tests inconsistentes o que no corrieran.

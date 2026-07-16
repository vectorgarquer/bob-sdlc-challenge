# Evidencia — Estrategia de Tokens

## Técnicas Aplicadas

### 1. Usar el modo correcto para cada tarea

El equipo utilizó conscientemente cada modo según la naturaleza del trabajo:

- **Plan** para discusión conceptual (historias de usuario, scope) → no consume tokens de acceso a archivos.
- **Ask** para preguntas técnicas de diseño → solo genera respuesta, no ejecuta comandos.
- **Agent** únicamente cuando se necesitaba crear/editar archivos o ejecutar comandos.

**Impacto:** Evitamos usar Agent en etapas conceptuales, donde su costo de tokens es mayor sin aportar valor adicional.

---

### 2. Prompts únicos y completos en lugar de múltiples prompts pequeños

En cada sub-tarea, se construyó **un único prompt inicial grande** que incluía:
- Lenguaje y stack (Java 17+, Spring Boot 3.x, Maven).
- Arquitectura de módulos decidida.
- Los 4 requerimientos funcionales con detalle de campos NASA.
- Estructura de carpetas esperada.
- Restricciones (sin base de datos, watchlist en memoria).

**Impacto:** Un prompt gordo con todo el contexto produce resultados completos en una sola iteración, evitando rondas de "ahora agrega X", "ahora también Y".

**Ejemplo aplicado (ST3 — Desarrollo):**
> En lugar de: "Crea el modelo Asteroid" → "Ahora el servicio" → "Ahora el controller" (3 rondas)
> Se usó: Un único prompt con toda la arquitectura, módulos y requerimientos → código completo en una iteración.

---

### 3. Prompts quirúrgicos para correcciones

Cuando se encontraban errores en el código generado, el equipo no pedía "reescribe todo", sino que indicaba:
- El nombre exacto de la clase o método con el bug.
- El comportamiento actual vs. el esperado.
- El error exacto (stack trace cuando aplica).

**Ejemplo:**
> ❌ "El código no funciona, arréglalo" (fuerza a Bob a re-leer todo)
> ✅ "En `NeoService.getAsteroids()`, el `Comparator` para `sort_by=size` debe usar `getEstimatedDiameterKmMax()` pero está usando el mínimo. Corrige solo ese comparator."

---

### 4. Incluir contexto relevante desde el primer prompt

Antes de pedir código o diseño, se proporcionó a Bob:
- El JSON real de la NASA NeoWs API con los campos exactos.
- La estructura de paquetes decidida.
- Las restricciones de negocio (máx. 7 días, sin BD, DEMO_KEY).

**Impacto:** Bob no tuvo que "inferir" la estructura del JSON ni preguntar por el stack — el primer output fue directamente utilizable.

---

### 5. Reutilización de contexto entre sub-tareas

Los archivos de evidencia generados en ST1 y ST2 fueron referenciados explícitamente en los prompts de ST3 y ST4, evitando repetir la misma información.

---

## Reflexión Final

La estrategia más efectiva fue la combinación de **modo correcto + prompt completo desde el inicio**. El mayor desperdicio de tokens en challenges como este ocurre cuando se usa Agent para tareas conceptuales o cuando se hace una pregunta pequeña sin contexto y luego se complementa con 3-4 prompts adicionales.

El uso de la skill `create-plan` al inicio también fue eficiente: cargarla una vez y seguir su estructura para todo el planning evitó iteraciones sobre cómo organizar el trabajo.

---

## Status: ✅ Completada

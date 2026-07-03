# 📐 Etapa 1 — Planificación

**Tiempo objetivo: ~8 minutos**
**Modo Bob recomendado: `Plan`**

---

## Objetivo

Transformar el requerimiento semilla en historias de usuario claras y definir el alcance de lo que van a construir.

---

## Instrucciones

### Paso 1 — Cambia Bob al modo `Plan`

En la barra lateral de Bob selecciona el modo **Plan**. Este modo está optimizado para pensar, analizar y estructurar sin escribir código aún.

### Paso 2 — Dale el requerimiento a Bob

Copia el requerimiento semilla del `README.md` y pégalo a Bob con este prompt:

```
Eres un analista de software. A partir del siguiente requerimiento, genera:
1. Una lista de historias de usuario en formato "Como [rol], quiero [acción] para [beneficio]"
2. Los criterios de aceptación de cada historia
3. Las entidades de datos principales que necesitaremos

Requerimiento:
[pega aquí el requerimiento semilla]
```

### Paso 3 — Refina con Bob

Si algo no queda claro, hazle preguntas de seguimiento a Bob. Ejemplo:

```
¿Qué casos borde debo considerar para la comparación de stats?
```

### Paso 4 — Guarda la evidencia

Copia la respuesta de Bob y llena la plantilla [`docs/evidence-templates/01-planning.md`](../evidence-templates/01-planning.md).

---

## ✅ Checklist de salida

- [ ] Al menos 3 historias de usuario documentadas
- [ ] Criterios de aceptación por historia
- [ ] Entidades identificadas (ej: `Pokemon`, `Team`)
- [ ] Evidencia guardada en `evidence/01-planning.md`

---

## 💡 Tip de tokens

En modo `Plan`, Bob no ejecuta herramientas — solo razona. Es el modo más barato en tokens. Aprovéchalo para toda la discusión conceptual antes de tocar código.

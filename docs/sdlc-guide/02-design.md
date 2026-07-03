# 🏗️ Etapa 2 — Diseño

**Tiempo objetivo: ~8 minutos**
**Modo Bob recomendado: `Ask`**

---

## Objetivo

Definir la arquitectura del sistema, los módulos principales y el contrato de la PokéAPI antes de escribir una sola línea de código.

---

## Instrucciones

### Paso 1 — Cambia Bob al modo `Ask`

El modo **Ask** es ideal para consultas técnicas, exploración de opciones y decisiones de arquitectura sin modificar archivos.

### Paso 2 — Consulta la arquitectura

```
Basándome en estas historias de usuario: [pega tus historias del paso anterior]

Voy a construir esto en [tu lenguaje elegido]. Propón:
1. Una arquitectura de módulos/clases para el sistema
2. Los endpoints o comandos que necesitaré exponer
3. Cómo estructurar las llamadas a la PokéAPI (https://pokeapi.co/docs/v2)
4. Un diagrama de flujo simple en texto (ASCII o mermaid)
```

### Paso 3 — Consulta los endpoints de la PokéAPI

```
De la PokéAPI, ¿qué endpoints necesito para:
- Obtener información básica de un Pokémon por nombre (tipo, habilidades, stats base)?
¿Cómo se ve la respuesta JSON? Dame un ejemplo resumido.
```

### Paso 4 — Decide con tu equipo

Discutan las propuestas de Bob. **Bob sugiere, el equipo decide.** Documenten la decisión final.

### Paso 5 — Guarda la evidencia

Llena la plantilla [`docs/evidence-templates/02-design.md`](../evidence-templates/02-design.md).

---

## ✅ Checklist de salida

- [ ] Arquitectura de módulos/clases decidida
- [ ] Endpoints o comandos definidos
- [ ] Endpoints de PokéAPI identificados
- [ ] Lenguaje y tipo de interfaz confirmados (CLI / REST / Web)
- [ ] Evidencia guardada en `evidence/02-design.md`

---

## 💡 Tip de tokens

En modo `Ask`, Bob no abre archivos ni ejecuta comandos. Si ya saben el lenguaje y la estructura, incluyan esa info en el prompt inicial para que Bob no tenga que inferirla — ahorran 1-2 llamadas de exploración.

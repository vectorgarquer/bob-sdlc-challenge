# ⚡ Etapa 7 — Estrategia de Tokens

**Tiempo: continuo durante todo el challenge**
**Aplica en todos los modos**

---

## ¿Por qué importa?

Cada mensaje que le mandas a Bob consume tokens. Cuantos más tokens uses, más lento y costoso es el proceso. Un equipo que usa tokens eficientemente termina más rápido y con mejores resultados.

Esta etapa **no tiene un momento fijo** — la estrategia de tokens se aplica desde el minuto 1.

---

## Estrategias clave

### 1. Usa el modo correcto para cada tarea

| Necesitas... | Modo ideal | ¿Por qué? |
|---|---|---|
| Planificar, analizar, decidir | `Plan` o `Ask` | No ejecuta herramientas, menos tokens |
| Escribir o editar código | `Agent` | Necesita acceso a archivos |
| Entender algo técnico | `Ask` | Solo responde, no actúa |

### 2. Un prompt gordo > muchos prompts chicos

❌ Ineficiente:
```
Crea la clase Pokemon
```
*(Bob pregunta qué atributos, luego pide el lenguaje, luego...)*

✅ Eficiente:
```
En Python, crea la clase Pokemon con atributos: name(str), types(list), 
abilities(list), base_stats(dict). Incluye __repr__ y un método 
total_stats() que sume todos los valores de base_stats.
```

### 3. Da contexto al inicio, no en el camino

En lugar de ir agregando contexto poco a poco, incluye en el **primer prompt** todo lo relevante: lenguaje, arquitectura decidida, lo que ya existe, lo que falta.

### 4. Sé quirúrgico en las correcciones

❌ Costoso:
```
El código no funciona, rehazlo
```

✅ Barato:
```
La función compare_pokemon() en src/team.py retorna siempre el primero. 
El bug está en la línea donde compara: debe comparar total_stats() de ambos.
```

### 5. Usa Skills si repites el mismo patrón

Si notan que le piden a Bob lo mismo varias veces (ej: "genera tests para esta función"), es candidato para una **Skill**. No es obligatorio en este challenge, pero suma puntos en la rúbrica.

---

## 📋 Qué documentar en tu evidencia

Llena `evidence/07-tokens.md` al final del challenge respondiendo:

1. ¿Qué modo usaron más? ¿Por qué?
2. ¿Tuvieron que repetir algún prompt? ¿Qué mejorarían?
3. ¿Usaron alguna Skill? Descríbela.
4. ¿Qué estrategia les funcionó mejor para reducir iteraciones con Bob?

---

## ✅ Checklist de salida

- [ ] `evidence/07-tokens.md` completado con reflexión honesta del equipo

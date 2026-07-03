# 🧪 Etapa 4 — Pruebas

**Tiempo objetivo: ~8 minutos**
**Modo Bob recomendado: `Agent`**

---

## Objetivo

Generar y ejecutar pruebas unitarias que validen la lógica del sistema.

---

## Instrucciones

### Paso 1 — Pide los tests a Bob

```
Genera pruebas unitarias para el módulo de gestión del equipo Pokémon.
Cubre estos casos:
1. Agregar un Pokémon al equipo (caso exitoso)
2. Intentar agregar un 7mo Pokémon (debe fallar / lanzar error)
3. Eliminar un Pokémon que existe en el equipo
4. Comparar dos Pokémon: el que tiene mayor suma de stats debe ganar

Usa el framework de testing estándar de [tu lenguaje].
Guarda los tests en la carpeta tests/.
```

### Paso 2 — Ejecuta los tests

```
Ejecuta las pruebas y muéstrame el resultado.
```

### Paso 3 — Corrige si hay fallos

Si algún test falla, pide a Bob que lo analice:

```
El test "agregar séptimo Pokémon" falla. Analiza el error y corrige 
el código fuente o el test según corresponda.
```

### Paso 4 — Guarda la evidencia

Copia el output de los tests y llena [`docs/evidence-templates/04-testing.md`](../evidence-templates/04-testing.md).

---

## ✅ Checklist de salida

- [ ] Al menos 4 tests escritos en `tests/`
- [ ] Todos los tests pasan (verde)
- [ ] Screenshot o texto del resultado en `evidence/04-testing.md`

---

## 💡 Tip de tokens

Pide todos los tests en **un solo prompt** especificando los casos. Es mucho más eficiente que pedir test por test.

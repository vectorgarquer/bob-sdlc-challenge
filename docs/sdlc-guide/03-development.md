# 💻 Etapa 3 — Desarrollo

**Tiempo objetivo: ~20 minutos**
**Modo Bob recomendado: `Agent`**

---

## Objetivo

Generar el código funcional del sistema usando Bob en modo `Agent`. Bob puede crear archivos, ejecutar comandos y navegar el proyecto directamente.

---

## Instrucciones

### Paso 1 — Cambia Bob al modo `Agent`

El modo **Agent** le da a Bob acceso a herramientas: puede crear archivos, leer el proyecto, ejecutar comandos de terminal y más.

### Paso 2 — Prompt de arranque

Dale a Bob el contexto completo de una sola vez para minimizar tokens:

```
Actúa como desarrollador senior en [lenguaje elegido].
Crea la estructura del proyecto con los siguientes módulos:
[pega aquí la arquitectura que definieron en el diseño]

Requisitos técnicos:
- Consume la PokéAPI en https://pokeapi.co/api/v2/pokemon/{name}
- Gestiona un equipo de hasta 6 Pokémon en memoria
- Implementa: buscar Pokémon, agregar al equipo, eliminar del equipo, comparar dos Pokémon por stats totales
- Interfaz: [CLI / REST API / web — la que eligieron]
- Sin base de datos, sin autenticación

Crea los archivos necesarios con el código funcional.
```

### Paso 3 — Itera con prompts específicos

Si algo falta o necesita corrección, sé específico:

```
El método de comparación no suma correctamente los stats. 
Arréglalo: debe sumar todos los valores del array "base_stat" de la PokéAPI.
```

### Paso 4 — Verifica que el código corra

Pide a Bob que lo ejecute:

```
Ejecuta el proyecto y muéstrame que funciona con un ejemplo usando "pikachu" y "charizard".
```

---

## ✅ Checklist de salida

- [ ] Código fuente en carpeta `src/`
- [ ] Búsqueda de Pokémon funciona con la PokéAPI real
- [ ] Agregar / eliminar del equipo funciona
- [ ] Comparación de stats funciona
- [ ] La app corre sin errores

---

## 💡 Tips de tokens

- **Un prompt grande al inicio** es más eficiente que 10 prompts pequeños.
- **Incluye el contexto** de diseño en el primer prompt para que Bob no tenga que preguntar.
- Si Bob se equivoca, **señala exactamente la línea o función** en lugar de pedir reescribir todo.
- Usa `# Solo modifica esta función:` para ediciones quirúrgicas.

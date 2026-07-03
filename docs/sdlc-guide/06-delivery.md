# 🚀 Etapa 6 — Entrega

**Tiempo objetivo: ~5 minutos**
**Modo Bob recomendado: `Agent`**

---

## Objetivo

Hacer commit del trabajo, subir los cambios y abrir el Pull Request final usando Bob.

---

## Instrucciones

### Paso 1 — Pide a Bob que genere el mensaje de commit

```
Revisa los archivos modificados en este proyecto y genera:
1. Un mensaje de commit descriptivo siguiendo Conventional Commits
2. Una descripción de Pull Request que incluya: qué se construyó, 
   tecnología usada, cómo probarlo, y los integrantes del equipo
```

### Paso 2 — Ejecuta el commit y push

Bob puede ejecutar los comandos si se lo pides, o puedes hacerlo manualmente:

```bash
git add .
git commit -m "[el mensaje que generó Bob]"
git push origin main
```

### Paso 3 — Abre el Pull Request

Ve a GitHub y crea el PR hacia el repositorio original con:

- **Título:** `[EQUIPO: nombre-equipo] PokéDev Challenge`
- **Descripción:** la que generó Bob
- **Labels:** `challenge-submission`

### Paso 4 — Verifica que el PR tenga todo

Antes de confirmar el PR, revisa:

- [ ] Carpeta `src/` con el código
- [ ] Carpeta `tests/` con los tests
- [ ] Carpeta `evidence/` con los 4 archivos de evidencia
- [ ] `README-solution.md` en la raíz

---

## ✅ Checklist de salida

- [ ] Commit con mensaje generado por Bob
- [ ] PR abierto con título correcto
- [ ] Descripción del PR generada con Bob
- [ ] Todos los archivos requeridos incluidos

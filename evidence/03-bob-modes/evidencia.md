# Evidencia — Modos de Bob

## Tabla de Uso de Modos por Etapa

| Etapa | Modo Bob | Justificación |
|-------|----------|---------------|
| ST1 — Planificación | `Plan` | Plan mode es el más eficiente para trabajo conceptual: genera historias de usuario, criterios de aceptación y entidades sin consumir tokens de acceso a archivos. Ideal para discutir ideas y tomar decisiones antes de tocar código. |
| ST2 — Diseño de Arquitectura | `Ask` | Ask mode permite hacer preguntas técnicas sobre la arquitectura, estructura de paquetes y el JSON de NASA sin ejecutar comandos ni modificar archivos. Respuesta-solamente = menos tokens. |
| ST3 — Desarrollo del Código | `Agent` | Agent mode es obligatorio para crear y editar archivos directamente (NeoTrackerApplication, NeoService, WatchlistService, NasaApiClient, controllers, pom.xml, application.properties). Solo Agent tiene acceso al sistema de archivos. |
| ST4 — Pruebas | `Agent` | Agent mode para crear los archivos de tests en `src/test/java/` y `tests/`. También puede ejecutar `mvn test` para validar que los tests pasen. |
| ST5 — Documentación | `Agent` | Agent mode para leer el código fuente generado y producir un README-solution.md preciso con comandos reales de Maven, estructura de proyecto y ejemplos verificados. |
| ST6 — Evidencia | Todos | La evidencia se genera de forma continua durante todas las etapas. Cada modo deja registro en su carpeta correspondiente. |
| ST7 — Entrega | `Agent` | Agent mode para generar el mensaje de commit en Conventional Commits y ejecutar `git add`, `git commit`, `git push` y crear el Pull Request. |

---

## Observaciones

- **Plan vs Ask:** Plan mode es mejor para estructurar el trabajo y definir el scope; Ask mode es mejor para preguntas técnicas puntuales (sin necesidad de ejecutar código).
- **Ask vs Agent para documentación:** Se eligió Agent en ST5 porque puede leer los archivos generados directamente y garantizar que los comandos de instalación y los paths sean correctos. Si el tiempo hubiera sido ajustado, Ask habría sido suficiente con una descripción resumida del código.
- **Evitar Agent para conceptos:** Usar Agent para discutir ideas o hacer preguntas es ineficiente — consume tokens de acceso a herramientas sin necesidad.

---

## Status: ✅ Completada

# Plan Integral de Pruebas del Sistema (QA)

## 1. Objetivo del Plan
Validar que el sistema "PartyPlanner" cumpla estrictamente con los requisitos funcionales y no funcionales definidos en la fase de análisis, garantizando la integridad de los datos durante el registro, el control de aforo y la autenticación de usuarios.

## 2. Alcance
El alcance de este plan de pruebas cubre los flujos críticos del negocio:
* Autenticación y control de acceso (Admin).
* Creación y configuración de eventos.
* Confirmación de asistencia (RSVP) por parte de los usuarios finales.
* Control de concurrencia y límites de aforo en la base de datos.

## 3. Estrategia de Pruebas
Se implementa una estrategia de pruebas de **Caja Negra**, ejecutando:
* **Pruebas Funcionales:** Validación de flujos de trabajo (ej. registrar un invitado).
* **Pruebas de Validación:** Respuestas del sistema ante entradas incorrectas (ej. inyección de datos nulos).
* **Pruebas de Límite:** Comportamiento del sistema al alcanzar el aforo máximo.

## 4. Casos de Prueba (Test Cases)

| ID | Módulo | Caso de Prueba | Entrada / Precondición | Resultado Esperado | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CP01** | Seguridad | Login Administrador | Credenciales correctas en `/admin`. | Acceso concedido al Dashboard. | Exitoso |
| **CP02** | Seguridad | Acceso no autorizado | Usuario anónimo intenta acceder a `/dashboard`. | Error 403 o Redirección al Login. | Exitoso |
| **CP03** | Frontend | Confirmación RSVP válida | Link válido, Nombre, Correo, Dieta. | Registro en BD y aforo actualizado. | Exitoso |
| **CP04** | Validación | Registro sin correo | Formulario RSVP enviado sin campo 'email'. | El sistema arroja error de validación visual. | Exitoso |
| **CP05** | Backend | Límite de Aforo (Estrés) | Evento con 0 cupos disponibles. Usuario intenta registro. | El sistema rechaza la petición: "Aforo completo". | Exitoso |

## 5. Evidencias de Ejecución
Las capturas de pantalla de los resultados de estas pruebas se encuentran documentadas en la ruta: `../evidencias/pruebas/`

* **Figura 1:** [Login / RSVP Exitoso](../evidencia/cp03_rsvp_exitoso.jpeg)
* **Figura 2:** [Error de Validación](../evidencia/cp04_error_validacion.jpeg)

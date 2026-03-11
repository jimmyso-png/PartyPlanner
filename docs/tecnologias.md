# Tecnologías Utilizadas y Justificación Técnica

El sistema "PartyPlanner" ha sido construido utilizando un *Stack* tecnológico moderno, garantizando seguridad, escalabilidad y un desarrollo ágil adaptado al patrón de arquitectura MVC (Modelo-Vista-Controlador).

## 1. Backend y Lógica de Negocio
* **Lenguaje:** Python
* **Framework:** Django
* **Justificación:** Django es un framework robusto de alto nivel que incluye un ORM (Object-Relational Mapping) seguro, previniendo inyecciones SQL por defecto. Además, su módulo integrado de administración acelera la entrega de valor al proporcionar un panel de control funcional (Dashboard) desde el Sprint 1.

## 2. Base de Datos
* **Motor:** PostgreSQL
* **Justificación:** Al manejar confirmaciones de asistencia concurrentes (RSVP), es vital contar con una base de datos relacional altamente confiable y escalable que cumpla con el estándar ACID. PostgreSQL garantiza la integridad referencial y previene el sobre-aforo mediante bloqueos transaccionales.

## 3. Frontend (Interfaz de Usuario)
* **Tecnologías:** HTML5, CSS3, JavaScript.
* **Framework UI:** Bootstrap 5.
* **Justificación:** Permite el desarrollo bajo el principio *Mobile-First*, garantizando que la plataforma sea 100% responsiva. JavaScript se utiliza para validaciones del lado del cliente, mejorando la experiencia de usuario (UX) sin sobrecargar el servidor.

## 4. Control de Versiones y Despliegue
* **Herramientas:** Git y GitHub.
* **Justificación:** Git permite un control estricto del historial de cambios del código fuente. GitHub facilita el trabajo colaborativo mediante ramificaciones (*Branching*) y *Pull Requests*, fungiendo además como el repositorio central de documentación e integración continua.

## 5. Gestión del Proyecto y Modelado
* **Metodología:** SCRUM.
* **Tablero Kanban:** Trello.
  * *Justificación:* Permite mapear las Historias de Usuario y gestionar los Sprints, garantizando entregas incrementales funcionales.
* **Modelado y Arquitectura:** Lucidchart y StarUML.
  * *Justificación:* Utilizados en la fase de análisis para diseñar los diagramas de Casos de Uso y el Diagrama Entidad-Relación (DER), mitigando errores estructurales antes de la fase de codificación.

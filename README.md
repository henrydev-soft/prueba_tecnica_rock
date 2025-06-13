# 📚 Proyecto de Gestión de Cursos (Prueba Técnica)

Aplicativo para la gestión de cursos y lecciones, este proyeto hace parte de la prueba técnica presentada para la vacante de FullStack Developer.

## 🚀 Descripción del Proyecto

Esta aplicación gestionar cursos y sus respectivas lecciones. Se desarrolló aplicando principios de diseño como **Clean Code**, **SOLID** y arquitectura **Hexagonal**, asegurando una separación clara entre dominio, infraestructura y aplicación. El backend está construido con **FastAPI** y **PostgreSQL**, mientras que el frontend está desarrollado en **React** y sigue un enfoque funcional con **Atomic Design**.

Se utilizó Docker Compose para orquestar los servicios, facilitando el despliegue y pruebas locales consistentes.

---

## ⚙️ Decisiones Técnicas

- **Arquitectura Hexagonal (Ports & Adapters) Backend**: separación clara entre lógica de negocio, controladores HTTP y persistencia.
    - **Domain**: define las entidades y reglas del negocio.
    - **Application**: contiene los casos de uso y la lógica de aplicación. 
    - **Infrastructure**: implementa Adaptadores Secundarios (Bases de Datos, ORM)
    - **Interfaces**: implementa Adapatadores Primarios (Interfaces de Entrada/Salida - HTTP, CLI, Etc..)
- **Frontend Atomic Design**: Se adoptó el enfoque de Atomic Design en el frontend para promover la reutilización de componentes, mejorar la escalabilidad y mantener una estructura clara, coherente y fácil de mantener en aplicaciones React.
- **Principios SOLID**: cada componente tiene una responsabilidad única, facilitando su testeo y mantenimiento.
- **Clean Code**: se prioriza la legibilidad, consistencia en nombres y estructuras autocontenidas.
- **FastAPI**: framework moderno, tipado y con documentación OpenAPI automática.
- **SQLAlchemy + Alembic**: ORM robusto para interactuar con PostgreSQL y controlar migraciones.
- **React**: Se eligió como biblioteca principal para el frontend debido a su rendimiento eficiente, su amplio ecosistema y la facilidad que ofrece para construir interfaces dinámicas y reutilizables. 
- **Tailwind CSS**: Se eligió por su eficiencia al construir interfaces modernas de forma rápida, reutilizable y con un alto grado de personalización sin necesidad de escribir CSS desde cero.
- **Testing completo**:
  - **Unitarios** (mockeando repositorios).
  - **Integración** (DB real con rollback por test).
- **Docker Compose**: para facilitar despliegue de PostgreSQL + Backend + Frontend.
- **OpenAPI/Swagger**: documentación generada automáticamente con FastAPI.

---

## 🐳 Instrucciones para Ejecutar con Docker Compose

1. **Clona el repositorio**:

```bash
git clone https://github.com/henrydev-soft/prueba_tecnica_rock.git
cd prueba_tecnica_rock
```

2. **Crea el archivo `.env` con tus variables** (basado en `.env.example`):

```env
APP_NAME=Course Manager
ENVIRONMENT=development
DEBUG=True
POSTGRES_USER=postgres
POSTGRES_PASSWORD=superpassword
POSTGRES_SERVER=db
POSTGRES_PORT=5432
POSTGRES_DB=courses_db
TEST_POSTGRES_DB=courses_db_test
VITE_API_BASE_URL=http://localhost:8000/api/v1 
```
**Nota**: Si se requiere agilidad en este proceso se puede cambiar el nombre del archivo `.env.example` -> `.env` 
para despliegue rápido en pruebas locales, por buena práctica no se deja el archivo `.env` para que por error no sea usado en producción.


3. **Levanta los contenedores**:

```bash
docker-compose up --build -d
```

4. **Accede a la Aplicación**:

- Frontend: [http://localhost:3000](http://localhost:3000) 
- Documentación Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📬 Endpoints Disponibles

### 📘 Cursos

- `GET /api/v1/courses/`  
  Lista todos los cursos.

- `POST /api/v1/courses/`  
  Crea un nuevo curso.  
  Requiere: `title`, `description`, `instructor`.

- `GET /api/v1/courses/{course_id}`  
  Obtiene los detalles de un curso, incluyendo sus lecciones.

- `PUT /api/v1/courses/{course_id}`  
  Actualiza un curso existente.

- `DELETE /api/v1/courses/{course_id}`  
  Elimina un curso.

---

### 🎥 Lecciones

- `POST /api/v1/courses/{course_id}/lessons/`  
  Crea una nueva lección en el curso indicado.  
  Requiere: `title`, `video_url`.

- `GET /api/v1/courses/{course_id}/lessons/{lesson_id}`  
  Obtiene una lección específica.

- `PUT /api/v1/courses/{course_id}/lessons/{lesson_id}`  
  Actualiza una lección.

- `DELETE /api/v1/courses/{course_id}/lessons/{lesson_id}`  
  Elimina una lección.

---

## 🧪 Pruebas

```bash
# Ejecutar tests si se conserva el nombre del contenedor backend fastapi_app
docker exec -it fastapi_app pytest -v
# Ejecutar tests en la consola del contenedor backend
pytest --cov=app
```

---

## 🏗️ Estructura del Proyecto

```
.
├── backend
│   └── app
│       ├── core/            # Configuración, logging, seguridad
│       ├── domain/          # Modelos de dominio y contratos de repositorio
│       ├── infrastructure/  # Implementaciones concretas (SQL) y acceso a datos
│       ├── application/     # Lógica de negocio (servicios y DTOs)
│       ├── interfaces/      # Entradas/salidas del sistema (API HTTP)
│       └── tests/           # Pruebas unitarias e integración
└── frontend
    └── src
        ├── api/             # Configuración de llamadas HTTP
        ├── assets/          # Recursos estáticos
        ├── components/      # Componentes UI (Atomic Design)
        │   ├── atoms/
        │   ├── molecules/
        │   └── organisms/
        ├── context/         # Manejo de estado global
        ├── hooks/           # Hooks personalizados
        ├── layouts/         # Layouts generales
        ├── pages/           # Vistas principales del sistema
        └── services/        # Comunicación con la API backend
```

---

# 🧠 Backend - Course Manager API

Este es el backend de la aplicación **Course Manager**, desarrollado con **FastAPI** siguiendo principios de **arquitectura hexagonal**, **Clean Code** y **SOLID**. La lógica de negocio está desacoplada de los detalles de infraestructura, facilitando el testeo, la mantenibilidad y la evolución del sistema.

## 🚀 Tecnologías

- **Python 3.12**
- **FastAPI** como framework web
- **SQLAlchemy** como ORM
- **PostgreSQL** como base de datos
- **Alembic** para migraciones
- **Pytest** para pruebas unitarias e integración
- **Docker** y **Docker Compose** para orquestación y despliegue
- **Pydantic** para validación y configuración basada en entorno

## 🧱 Arquitectura

El backend sigue un enfoque hexagonal (ports and adapters), separando:

- **Domain:** Modelos puros y contratos de repositorios.
- **Application:** Lógica de negocio y DTOs.
- **Infrastructure:** Implementaciones concretas como repositorios SQL y sesiones.
- **Interfaces:** Exposición de la API HTTP con FastAPI.

Esta separación favorece la escalabilidad, pruebas independientes y un control claro de dependencias.

## 🗂️ Estructura del Proyecto

```bash
backend/
├── alembic/                # Migraciones gestionadas con Alembic
├── alembic.ini             # Configuración de Alembic
├── app/
│   ├── core/               # Configuración, seguridad, logging
│   ├── domain/             # Modelos de dominio y contratos de repositorios
│   ├── application/        # Servicios de negocio y DTOs
│   ├── infrastructure/     # Implementación de repositorios con SQLAlchemy
│   ├── interfaces/         # API pública (HTTP REST con FastAPI)
│   ├── tests/              # Pruebas unitarias e integración
│   └── main.py             # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del backend
└── pytest.ini              # Configuración de pruebas
```

## 📦 Endpoints API Principales

Todos los endpoints están disponibles bajo el prefijo `/api/v1/`. La documentación automática se puede consultar en:

```
http://localhost:8000/docs
```

### 📘 Cursos

- `GET /api/v1/courses/` - Listar cursos
- `POST /api/v1/courses/` - Crear curso
- `GET /api/v1/courses/{id}` - Obtener curso por ID
- `PUT /api/v1/courses/{id}` - Actualizar curso
- `DELETE /api/v1/courses/{id}` - Eliminar curso

### 📗 Lecciones

- `GET /api/v1/lessons/` - Listar lecciones
- `POST /api/v1/lessons/` - Crear lección
- `GET /api/v1/lessons/{id}` - Obtener lección por ID
- `PUT /api/v1/lessons/{id}` - Actualizar lección
- `DELETE /api/v1/lessons/{id}` - Eliminar lección

## 🧪 Pruebas

Puedes ejecutar las pruebas unitarias y de integración con:

```bash
pytest
```

Incluye un entorno de testing con base de datos separada, limpieza automática y pruebas desacopladas gracias al uso de `dependency_overrides`.

## 🐳 Ejecutar con Docker Compose

Desde la raíz del proyecto, despues de configurar variables con el archivo `.env`:

```bash
docker-compose up --build
```

Esto levantará:

- `backend`: FastAPI en `http://localhost:8000`
- `frontend`: React App en `http://localhost:5173`
- `postgres`: Base de datos PostgreSQL en `localhost:5432`

## 👨‍💻 Autor

Desarrollado por **Henry Jiménez**, FullStack Developer.

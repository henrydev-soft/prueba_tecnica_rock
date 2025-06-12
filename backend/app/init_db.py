"""
Script de Inicialización de Base de Datos para el Proyecto

Este módulo realiza las siguientes tareas al iniciar el entorno:
1. Verifica si las bases de datos `courses_db` y `courses_db_test` existen en el servidor PostgreSQL.
2. Si no existen, las crea usando conexión directa con `psycopg2`.
3. Ejecuta las migraciones definidas en Alembic sobre la base principal (`courses_db`).
4. Inserta datos iniciales (semilla) si la base está vacía.

Este script puede ser invocado automáticamente al iniciar el contenedor
de la aplicación, garantizando que el entorno esté listo para operar.

Autor: Henry Jiménez
Fecha: 2025-06-11
"""
import psycopg2
from alembic.config import Config
from alembic import command
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.infrastructure.sql.session import SessionLocal
#from app.domain.models import Course
from app.infrastructure.sql.models import CourseModel, LessonModel
from app.core.logger import logger





def create_database_if_not_exists(db_name: str, user: str, password: str, host: str, port: str):
    """Crea una base de datos PostgreSQL si no existe."""
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
        exists = cursor.fetchone()
        if not exists:
            logger.info(f"Creando base de datos: {db_name}")
            cursor.execute(f"CREATE DATABASE {db_name}")
        else:
            logger.info(f"Base de datos '{db_name}' ya existe.")
        cursor.close()
        conn.close()
    except Exception as e:
        logger.error(f"Error al crear base de datos '{db_name}': {e}")
        raise


def run_migrations(db_url: str):
    """Ejecuta las migraciones de Alembic en la base de datos proporcionada."""
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)
    logger.info(f"Ejecutando migraciones en: {db_url}")
    command.upgrade(alembic_cfg, "head")


def seed_initial_data():
    """Inserta datos iniciales si la tabla `courses` está vacía."""
    db: Session = SessionLocal()
    try:
        if not db.query(CourseModel).first():
            #Datos de población iniciales. 
            courses_data = [
                {
                    "title": "Curso de Docker",
                    "description": "Contenerización de aplicaciones",
                    "instructor": "Nana Janashia",
                    "lessons": [
                        {"title": "Docker Tutorial for Beginners [FULL COURSE in 3 Hours]", "video_url": "https://youtu.be/3c-iBn73dDE"}
                    ]
                },
                {
                    "title": "Curso de Python",
                    "description": "Python es el lenguaje de programación más popular del año. Este es un curso desde cero para principiantes creado para aprender los fundamentos desde su base.",
                    "instructor": "Brais Moure",
                    "lessons": [
                        {"title": "Curso Completo en 1 Lección", "video_url": "https://www.youtube.com/watch?v=Kp4Mvapo5kc"}
                    ]
                },
                {
                    "title": "Curso de FastAPI",
                    "description": "Nuevo curso introductorio de FastAPI, uno de los frameworks más populares y recientes de Python para el desarrollo backend.",
                    "instructor": "Pablo Dev",
                    "lessons": [
                        {"title": "Presentación del Cruso", "video_url": "https://youtu.be/OKUDmlvB8Hk?list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R"}
                    ]
                },    
            ]
            logger.info("Insertando cursos iniciales de ejemplo...")
            for course_data in courses_data:
                course = CourseModel(
                    title=course_data["title"],
                    description=course_data["description"],
                    instructor=course_data["instructor"]
                )

                # Agregar lecciones asociadas
                for lesson_data in course_data["lessons"]:
                    lesson = LessonModel(
                        title=lesson_data["title"],
                        video_url=lesson_data["video_url"],
                        course=course  # Relación directa con el objeto padre
                    )
                    db.add(lesson)

                db.add(course)

            db.commit()
        else:
            logger.info("Datos iniciales ya presentes.")
    finally:
        db.close()


if __name__ == "__main__":
    settings = get_settings()

    # Crear las bases de datos si no existen
    create_database_if_not_exists(
        db_name=settings.POSTGRES_DB,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_SERVER,
        port=settings.POSTGRES_PORT,
    )

    create_database_if_not_exists(
        db_name=settings.TEST_POSTGRES_DB,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_SERVER,
        port=settings.POSTGRES_PORT,
    )

    # Ejecutar migraciones
    run_migrations(settings.DATABASE_URL)

    # Insertar datos iniciales
    seed_initial_data()

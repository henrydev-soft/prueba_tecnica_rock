import sys
import os
import configparser
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context


#Agregar app al patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

#Importa config y Base
from app.core.config import get_settings
from app.infrastructure.db.base import Base  # importa la instancia de declarative_base()
from app.infrastructure.db.models import course_model, lesson_model  # importa modelos

# Configura logging
fileConfig(context.config.config_file_name)

# Obtiene la configuración Alembic
config = context.config
config.file_config = configparser.ConfigParser(interpolation=None)

# Carga la URL desde la clase Settings
settings = get_settings()
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Conecta con la metadata de tus modelos
target_metadata = Base.metadata


# Función para ejecutar migraciones en modo offline (solo genera SQL, no ejecuta)
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# Función para ejecutar migraciones en modo online (con conexión a la DB)
def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# Lógica para ejecutar modo online u offline
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

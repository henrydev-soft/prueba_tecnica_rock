# backend/Dockerfile

FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia e instala dependencias de Python
COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Establece la variable de entorno PYTHONPATH
ENV PYTHONPATH=/app

# Instala netcat para hacer espera activa de PostgreSQL
RUN apt-get update && apt-get install -y netcat-openbsd

# Copia el resto del código
COPY . .



EXPOSE 8000

# Comando por defecto
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# Se una una imágen Nodejs para hacer el Build de la applicación
FROM node:22-alpine as build

# Declarar el argumento de construcción
ARG VITE_API_BASE_URL

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar package.json y package-lock.json e instalar dependencias
COPY package*.json ./
RUN npm install

# Copiar el resto del código del frontend
COPY . .

# Construir la aplicación React para producción
RUN npm run build

# Usar una imagen base de Nginx para servir la aplicación estática
FROM nginx:stable-alpine

# Copiar los archivos de la construcción al directorio de servicio de Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Copiar una configuración personalizada de Nginx (opcional, pero buena práctica para SPAs)
 COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 80 donde Nginx servirá la aplicación
EXPOSE 80

# Comando para que Nginx se ejecute en primer plano
CMD ["nginx", "-g", "daemon off;"]
# Frontend - Aplicación de Gestión de Cursos

Este directorio contiene el código fuente de la aplicación frontend para la gestión de cursos, desarrollada con **React.js** y **Vite**, y estilizada con **Tailwind CSS**. Se comunica con el API RESTful del backend para realizar todas las operaciones CRUD.

---

## 🚀 Tecnologías Utilizadas

* **Framework:** React.js
* **Build Tool:** Vite
* **Estilos:** Tailwind CSS
* **Consumo de API:** Axios
* **Iconos:** React Icons (`react-icons`)
* **Gestión de estado/lógica global:** React Context API (para notificaciones)

---

## ✨ Características y Decisiones Técnicas

* **Estructura de Componentes:** Sigue una metodología atómica (Atoms, Molecules, Organisms) para una mejor organización y reusabilidad del código.
* **Ruteo:** Implementado con `react-router-dom` para una navegación fluida entre las diferentes vistas de la aplicación.
* **Consumo de API:** Se utiliza `axios` para todas las peticiones HTTP al backend, con una configuración centralizada para la `baseURL`.
* **Gestión de Notificaciones/Alertas:** Se implementó un sistema de notificaciones internas utilizando el **Context API de React** y un **hook personalizado (`useNotification`)**. Esto reemplaza las alertas nativas del navegador (`alert()`) por un sistema más integrado y estético, mostrando mensajes de éxito o error en la interfaz de usuario.
* **Spinners de Carga:**
    * **Carga inicial de cursos:** Se muestra un spinner en la `HomePage` mientras se obtienen los datos de los cursos del backend.
    * **Carga de imágenes en tarjetas de curso:** Cada `CourseCard` muestra un spinner temporal mientras se carga su imagen de previsualización (generada por `Picsum Photos`). Esto mejora la percepción del rendimiento y la experiencia de usuario.
* **Manejo de URLs de Video:** Aunque el backend acepta URLs de video, el frontend no incluye un reproductor de video en la `CourseCard` principal para mantenerla ligera. La visualización detallada de lecciones con un reproductor de video embebido se maneja en la página `LessonDetailsPage`.
* **Validación de URLs de Video (a nivel de frontend):** El `LessonForm` (donde se añaden/editan lecciones) incluye una expresión regular para validar que la `video_url` ingresada sea válida para la demostración, aceptando formatos específicos como `https://www.youtube.com/...` o `https://youtu.be/...`. Esto es una validación de ejemplo para el requisito de la prueba.
* **Variables de Entorno:**
    * Gestionadas con Vite, accesibles a través de `import.meta.env.*`.
    * La `VITE_API_BASE_URL` para la comunicación con el backend se inyecta durante el proceso de **construcción (build time)** de Docker, asegurando que la URL de la API sea correcta (`http://backend:8000/api/v1`) cuando la aplicación se ejecuta dentro de los contenedores Docker Compose.

---

## ⚙️ Configuración y Ejecución (Solo Frontend)

Este `README.md` se enfoca en el frontend. Para ejecutar la aplicación completa (frontend + backend + Docker Compose), por favor, consulta el `README.md` principal en la raíz del repositorio.

Si deseas ejecutar o desarrollar solo el frontend de forma independiente (sin Docker Compose completo):

1.  **Navega a este directorio:**
    ```bash
    cd frontend
    ```
2.  **Instala las dependencias:**
    ```bash
    npm install
    ```
3.  **Configura las variables de entorno:**
    Crea un archivo `.env` en la raíz de este directorio (`frontend/.env`) con la URL de tu backend.
    Si tu backend está corriendo localmente en el puerto 8000:
    ```
    VITE_API_BASE_URL=http://localhost:8000/api/v1
    ```
4.  **Inicia el servidor de desarrollo:**
    ```bash
    npm run dev
    ```
    La aplicación estará disponible en `http://localhost:5173` (o el puerto que Vite asigne).

5.  **Para construir para producción (sin Docker):**
    ```bash
    npm run build
    ```
    Esto generará los archivos estáticos en la carpeta `dist/`.

---

## 📂 Estructura de Archivos
```
Claro, aquí tienes el contenido del README.md que te generé, listo para que lo copies y lo guardes en un archivo. No puedo generar un archivo de descarga directamente, pero puedes copiar el texto de abajo y pegarlo en un editor de texto (como VS Code, Notepad++, Sublime Text, o incluso el Bloc de Notas) y guardarlo con el nombre README.md en tu carpeta frontend/.

Markdown

# Frontend - Aplicación de Gestión de Cursos

Este directorio contiene el código fuente de la aplicación frontend para la gestión de cursos, desarrollada con **React.js** y **Vite**, y estilizada con **Tailwind CSS**. Se comunica con el API RESTful del backend para realizar todas las operaciones CRUD.

---

## 🚀 Tecnologías Utilizadas

* **Framework:** React.js
* **Build Tool:** Vite
* **Estilos:** Tailwind CSS
* **Consumo de API:** Axios
* **Iconos:** React Icons (`react-icons`)
* **Gestión de estado/lógica global:** React Context API (para notificaciones)

---

## ✨ Características y Decisiones Técnicas

* **Estructura de Componentes:** Sigue una metodología atómica (Atoms, Molecules, Organisms) para una mejor organización y reusabilidad del código.
* **Ruteo:** Implementado con `react-router-dom` para una navegación fluida entre las diferentes vistas de la aplicación.
* **Consumo de API:** Se utiliza `axios` para todas las peticiones HTTP al backend, con una configuración centralizada para la `baseURL`.
* **Gestión de Notificaciones/Alertas:** Se implementó un sistema de notificaciones internas utilizando el **Context API de React** y un **hook personalizado (`useNotification`)**. Esto reemplaza las alertas nativas del navegador (`alert()`) por un sistema más integrado y estético, mostrando mensajes de éxito o error en la interfaz de usuario.
* **Spinners de Carga:**
    * **Carga inicial de cursos:** Se muestra un spinner en la `HomePage` mientras se obtienen los datos de los cursos del backend.
    * **Carga de imágenes en tarjetas de curso:** Cada `CourseCard` muestra un spinner temporal mientras se carga su imagen de previsualización (generada por `Picsum Photos`). Esto mejora la percepción del rendimiento y la experiencia de usuario.
* **Manejo de URLs de Video:** Aunque el backend acepta URLs de video, el frontend no incluye un reproductor de video en la `CourseCard` principal para mantenerla ligera. La visualización detallada de lecciones con un reproductor de video embebido se maneja en la página `LessonDetailsPage`.
* **Validación de URLs de Video (a nivel de frontend):** El `LessonForm` (donde se añaden/editan lecciones) incluye una expresión regular para validar que la `video_url` ingresada sea válida para la demostración, aceptando formatos específicos como `https://www.youtube.com/...` o `https://youtu.be/...`. Esto es una validación de ejemplo para el requisito de la prueba.
* **Variables de Entorno:**
    * Gestionadas con Vite, accesibles a través de `import.meta.env.*`.
    * La `VITE_API_BASE_URL` para la comunicación con el backend se inyecta durante el proceso de **construcción (build time)** de Docker, asegurando que la URL de la API sea correcta (`http://backend:8000/api/v1`) cuando la aplicación se ejecuta dentro de los contenedores Docker Compose.

---

## ⚙️ Configuración y Ejecución (Solo Frontend)

Este `README.md` se enfoca en el frontend. Para ejecutar la aplicación completa (frontend + backend + Docker Compose), por favor, consulta el `README.md` principal en la raíz del repositorio.

Si deseas ejecutar o desarrollar solo el frontend de forma independiente (sin Docker Compose completo):

1.  **Navega a este directorio:**
    ```bash
    cd frontend
    ```
2.  **Instala las dependencias:**
    ```bash
    npm install
    ```
3.  **Configura las variables de entorno:**
    Crea un archivo `.env` en la raíz de este directorio (`frontend/.env`) con la URL de tu backend.
    Si tu backend está corriendo localmente en el puerto 8000:
    ```
    VITE_API_BASE_URL=http://localhost:8000/api/v1
    ```
4.  **Inicia el servidor de desarrollo:**
    ```bash
    npm run dev
    ```
    La aplicación estará disponible en `http://localhost:5173` (o el puerto que Vite asigne).

5.  **Para construir para producción (sin Docker):**
    ```bash
    npm run build
    ```
    Esto generará los archivos estáticos en la carpeta `dist/`.

---

## 📂 Estructura de Archivos
frontend/
├── public/                # Archivos estáticos
├── src/
│   ├── assets/            # Imágenes, íconos, etc.
│   ├── components/
│   │   ├── atoms/         # Elementos UI básicos (Button, Title, AppText, Spinner, Image, Notification)
│   │   ├── molecules/     # Combinación de átomos (CourseCard)
│   │   └── organisms/     # Combinación de moléculas/átomos (CourseList, LessonForm, etc.)
│   ├── context/           # Contextos globales (NotificationContext.jsx)
│   ├── hooks/             # Hooks personalizados (useNotification.js)
│   ├── layouts/           # Estructura de la aplicación (MainLayout.jsx)
│   ├── pages/             # Páginas/vistas principales de la aplicación
│   ├── services/          # Lógica para interactuar con la API (api.js, courseService.js, lessonService.js)
│   ├── utils/             # Funciones de utilidad (ej. validaciones, youtube.js si se usara)
│   ├── App.jsx            # Componente principal de React
│   └── main.jsx           # Punto de entrada de la aplicación
├── Dockerfile             # Configuración para construir la imagen Docker del frontend
├── nginx.conf             # Configuración de Nginx para servir la SPA en Docker
├── package.json           # Dependencias y scripts del proyecto
├── vite.config.js         # Configuración de Vite
└── .env                   # IMPORTANTE: Este archivo debe crearse para desarrollo en local con la variable VITE_API_BASE_URL=http://localhost:8000/api/v1.
```

**Nota**: Para desarrollo en local fuera de contenedores docker es importante crear el archivo .env en la estructura de carpetas del frontend con el contenido de
VITE_API_BASE_URL=http://localhost:8000/api/v1, esto para que la variable sea inyectada en el entonro de desarrollo. No es necesario crearlo para el despligue en Docker. 

---

## 🧠 Autor

**Henry Jiménez**  
_Software Engineer & FullStack Developer_

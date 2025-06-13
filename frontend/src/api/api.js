/**
 * Configuración centralizada del cliente HTTP para la comunicación con la API del backend.
 * 
 * Este archivo define una instancia de Axios con una URL base configurable mediante variables 
 * de entorno, lo que permite manejar distintos entornos (desarrollo, pruebas, producción).
 * 
 * Se establecen cabeceras comunes como 'Content-Type: application/json' para todas las solicitudes,
 * garantizando consistencia en las peticiones HTTP realizadas desde el frontend.
 */

import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1', // Ajusta esta URL a la de tu backend
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;
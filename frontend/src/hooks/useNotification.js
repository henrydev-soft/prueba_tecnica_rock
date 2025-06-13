
import { useContext } from 'react';
import { NotificationContext } from '../context/NotificationContext'; // Asegúrate de importar el contexto aquí

/**
 * Hook personalizado para acceder a las funciones de notificación.
 * @returns {Object} Un objeto con funciones para añadir y eliminar notificaciones.
 * @throws {Error} Si se usa fuera de un NotificationProvider.
 */
export const useNotification = () => {
  const context = useContext(NotificationContext);
  if (!context) {
    throw new Error('useNotification must be used within a NotificationProvider');
  }
  return context;
};
/*
* Este componente maneja el contexto de notificaciones de la aplicación
*/

import { createContext, useState, useContext, useCallback } from 'react';
import { v4 as uuidv4 } from 'uuid'; // Para generar IDs únicos
import Notification from '../components/atoms/Notification'; 

export const NotificationContext = createContext();

export const NotificationProvider = ({ children }) => {
  const [notifications, setNotifications] = useState([]);

  const addNotification = useCallback((message, type = 'info', duration = 5000) => {
    const id = uuidv4();
    setNotifications((prevNotifications) => [
      ...prevNotifications,
      { id, message, type, duration },
    ]);
    // Auto-cierre si no es manejado por el componente Notification (redundancia, pero buena práctica)
    if (duration > 0) {
      setTimeout(() => {
        removeNotification(id);
      }, duration);
    }
  }, []);

  const removeNotification = useCallback((id) => {
    setNotifications((prevNotifications) =>
      prevNotifications.filter((notification) => notification.id !== id)
    );
  }, []);

  return (
    <NotificationContext.Provider value={{ addNotification, removeNotification }}>
      {children}
      {/* Contenedor para las notificaciones */}
      <div className="fixed top-4 right-4 z-50 flex flex-col items-end space-y-3 max-w-sm">
        {notifications.map((notification) => (
          <Notification
            key={notification.id}
            id={notification.id}
            message={notification.message}
            type={notification.type}
            onClose={removeNotification}
          />
        ))}
      </div>
    </NotificationContext.Provider>
  );
};


/*
* Este componente representará una "tarjeta" de curso.
*/

import { useEffect, useState } from 'react';
import { MdCheckCircle, MdError, MdInfo, MdClose } from 'react-icons/md'; // Necesitarás instalar react-icons

// Colores y iconos basados en el tipo de notificación
const notificationStyles = {
  success: {
    bg: 'bg-green-100',
    text: 'text-green-800',
    border: 'border-green-500',
    icon: <MdCheckCircle className="text-green-500 text-xl" />,
  },
  error: {
    bg: 'bg-red-100',
    text: 'text-red-800',
    border: 'border-red-500',
    icon: <MdError className="text-red-500 text-xl" />,
  },
  info: {
    bg: 'bg-blue-100',
    text: 'text-blue-800',
    border: 'border-blue-500',
    icon: <MdInfo className="text-blue-500 text-xl" />,
  },
};

const Notification = ({ message, type, id, onClose }) => {
  const [isVisible, setIsVisible] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsVisible(false);
      // Permite que la animación de salida termine antes de removerla completamente
      const removalTimer = setTimeout(() => onClose(id), 500); // 500ms para animación
      return () => clearTimeout(removalTimer);
    }, 5000); // La notificación desaparece después de 5 segundos

    return () => clearTimeout(timer);
  }, [id, onClose]);

  const styles = notificationStyles[type] || notificationStyles.info; // Default a info

  if (!isVisible) return null;

  return (
    <div
      className={`relative p-4 mb-3 rounded-lg shadow-md border-l-4 transition-all duration-300 ease-in-out transform
        ${styles.bg} ${styles.text} ${styles.border}
        ${isVisible ? 'translate-y-0 opacity-100' : 'translate-y-4 opacity-0'}`}
      role="alert"
    >
      <div className="flex items-center">
        <div className="mr-3 flex-shrink-0">
          {styles.icon}
        </div>
        <div className="flex-grow">
          <p className="font-semibold">{message}</p>
        </div>
        <button
          onClick={() => { setIsVisible(false); onClose(id); }}
          className={`ml-4 p-1 rounded-full <span class="math-inline">\{styles\.text\} hover\:</span>{styles.text} hover:bg-opacity-50 transition-colors duration-200`}
          aria-label="Cerrar notificación"
        >
          <MdClose className="text-lg" />
        </button>
      </div>
    </div>
  );
};

export default Notification;
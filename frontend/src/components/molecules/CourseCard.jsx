/*
* Este componente representará una "tarjeta" de curso.
*/

import { useState } from 'react';
import { Link } from 'react-router-dom';
import Image from '../atoms/Image';
import Title from '../atoms/Title';
import AppText from '../atoms/AppText';
import Button from '../atoms/Button';
import Spinner from '../atoms/Spinner'; 

const CourseCard = ({ course, onEdit, onDelete }) => {

  const [imageLoaded, setImageLoaded] = useState(false);

  // Función para obtener una imagen de placeholder (a futuro se debería reemplazar por imágenes reales de los cursos)
  const getPlaceholderImage = (id) => {
    const images = [
      'https://picsum.photos/seed/course1/400/200',
      'https://picsum.photos/seed/course2/400/200',
      'https://picsum.photos/seed/course3/400/200',
      'https://picsum.photos/seed/course4/400/200',
      'https://picsum.photos/seed/course5/400/200',
      'https://picsum.photos/seed/course6/400/200',
      'https://picsum.photos/seed/course7/400/200',
      'https://picsum.photos/seed/course8/400/200',
      'https://picsum.photos/seed/course9/400/200',
      'https://picsum.photos/seed/course10/400/200',
      'https://picsum.photos/seed/course11/400/200',
    ];
    return images[id % images.length]; // Usa el ID para variar las imágenes
  };
  
  const handleImageLoad = () => {
    setImageLoaded(true); // Cuando la imagen carga, actualiza el estado a true
  };

  const handleImageError = () => {
    setImageLoaded(true); // También marca como cargado si hay un error para quitar el spinner
    // Opcional: se podría poner una imagen de placeholder genérica aquí si la URL falla
  };


  return (
    <div className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 flex overflow-hidden">
      {/* Parte de la imagen */}
      <div className="w-1/3 max-w-[150px] flex-shrink-0 relative"> {/* Añade 'relative' para posicionar el spinner */}
        {!imageLoaded && ( // <-- Muestra el spinner si la imagen no ha cargado
          <div className="absolute inset-0 flex items-center justify-center bg-gray-100 rounded-l-lg">
            <Spinner size="medium" className="text-blue-500" />
          </div>
        )}
        <Image
          src={getPlaceholderImage(course.id)}
          alt={course.title}
          className={`rounded-l-lg object-cover w-full h-full ${imageLoaded ? 'opacity-100' : 'opacity-0'}`} // Controla la opacidad
          onLoad={handleImageLoad} // <-- Manejador de carga
          onError={handleImageError} // <-- Manejador de error
          style={{ display: imageLoaded ? 'block' : 'none' }} // <-- Oculta completamente hasta que cargue
        />
      </div>

      {/* Contenido del texto y botones */}
      <div className="p-4 flex-grow flex flex-col justify-between min-w-0">
        <div>
          <Link to={`/courses/${course.id}`} className="block text-gray-900 hover:text-blue-600 transition-colors duration-200">
            <Title level={3} className="mb-1 leading-tight">
              {course.title}
            </Title>
          </Link>     
          <AppText className="text-sm text-gray-600 mb-2 break-words">
            {course.description}
          </AppText>
          <AppText className="text-xs text-gray-500">Instructor: {course.instructor}</AppText>
        </div>
        
        <div className="flex justify-end items-center mt-3 space-x-2 flex-wrap"> 
          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
            Activo
          </span>
          {onEdit && (
            <Button variant="ghost" onClick={() => onEdit(course.id)} className="text-sm">
              Editar
            </Button>
          )}
          {onDelete && (
            <Button variant="ghost" onClick={() => onDelete(course.id)} className="text-sm text-red-600">
              Eliminar
            </Button>
          )}
        </div>
      </div>
    </div>
  );
};

export default CourseCard;


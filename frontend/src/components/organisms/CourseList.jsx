/*
* Este organismo se encargará de mostrar la lista de CourseCard 
* y la barra de herramientas superior (Create)
*/


import Title from '../atoms/Title';
import Button from '../atoms/Button';
import CourseCard from '../molecules/CourseCard';
import { Link } from 'react-router-dom';
import AppText from '../atoms/AppText';
const CourseList = ({ courses, onEditCourse, onDeleteCourse }) => {
  return (
    <div className="space-y-6">
      {/* Encabezado con título y botón de crear curso */}
      <div className="flex items-center justify-between mb-6 flex-nowrap">
        <Title level={1} className="text-gray-900 flex-shrink-0 mr-4">
          Cursos
        </Title>
        <Link to="/courses/create" className="flex-shrink-0"> 
          <Button variant="primary">
            Crear Curso
          </Button>
        </Link>
      </div>

      {/* Lista de tarjetas de cursos */}
      {courses.length === 0 ? (
        <AppText className="text-center text-gray-600 text-lg py-10">No hay cursos disponibles. ¡Crea uno!</AppText>
      ) : (
        <div className="grid grid-cols-1 gap-6">
          {courses.map((course) => (
            <CourseCard
              key={course.id}
              course={course}
              onEdit={onEditCourse}
              onDelete={onDeleteCourse}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default CourseList;
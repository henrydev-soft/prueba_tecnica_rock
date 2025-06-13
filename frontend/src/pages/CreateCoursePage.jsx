/*
* Página para crear cursos
*/

import { useNavigate } from 'react-router-dom';
import CourseForm from '../components/organisms/CourseForm';
import { courseService } from '../services/courseService';
import { useNotification } from '../hooks/useNotification'; 

function CreateCoursePage() {
  const navigate = useNavigate();
  const { addNotification } = useNotification();

  const handleSubmit = async (courseData) => {
    try {
      const newCourse = await courseService.createCourse(courseData);
      addNotification('Curso creado con éxito.', 'success');
      navigate('/'); // Redirige a la página principal después de crear
    } catch (error) {
      console.error('Error al crear el curso:', error);
      addNotification('Hubo un error al crear el curso. Revisa la consola.', 'error');
    }
  };

  const handleCancel = () => {
    navigate('/'); // Vuelve a la página principal sin guardar
  };

  return (
    <CourseForm
      formTitle="Crear Nuevo Curso"
      onSubmit={handleSubmit}
      onCancel={handleCancel}
    />
  );
}

export default CreateCoursePage;
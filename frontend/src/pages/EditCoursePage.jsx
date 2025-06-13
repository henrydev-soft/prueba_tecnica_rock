/*
* Página para editar cursos
*/


import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import CourseForm from '../components/organisms/CourseForm';
import { courseService } from '../services/courseService';
import AppText from '../components/atoms/AppText';
import { useNotification } from '../hooks/useNotification'; 

function EditCoursePage() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { addNotification } = useNotification();

  useEffect(() => {
    const fetchCourse = async () => {
      try {
        setLoading(true);
        const data = await courseService.getCourseById(parseInt(courseId));
        setCourse(data);
      } catch (err) {
        console.error("Error fetching course for edit:", err);
        setError("Hubo un error al cargar el curso para edición.");
      } finally {
        setLoading(false);
      }
    };

    if (courseId) {
      fetchCourse();
    }
  }, [courseId]);

  const handleSubmit = async (courseData) => {
    try {
      await courseService.updateCourse(parseInt(courseId), courseData);
      addNotification('Curso actualizado con éxito!', 'success');
      navigate('/'); // Redirige a la página principal después de actualizar
    } catch (error) {
      console.error('Error al actualizar el curso:', error);
      addNotification('Hubo un error al actualizar el curso. Revisa la consola.', 'error');
    }
  };

  const handleCancel = () => {
    navigate('/'); // Vuelve a la página principal sin guardar
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <AppText>Cargando curso para edición...</AppText>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-96">
        <AppText className="text-red-500">{error}</AppText>
      </div>
    );
  }

  if (!course) {
    return (
      <div className="flex items-center justify-center h-96">
        <AppText className="text-gray-600">Curso no encontrado para edición.</AppText>
      </div>
    );
  }

  return (
    <CourseForm
      formTitle="Editar Curso"
      initialData={course}
      onSubmit={handleSubmit}
      onCancel={handleCancel}
    />
  );
}

export default EditCoursePage;
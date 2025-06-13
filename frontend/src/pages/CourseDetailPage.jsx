/*
* Página para mostrar los detalles de un curso y sus lecciones
*/

import { useEffect, useState } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { courseService } from '../services/courseService';
import { lessonService } from '../services/lessonService';
import Title from '../components/atoms/Title';
import AppText from '../components/atoms/AppText';
import Button from '../components/atoms/Button';
import LessonForm from '../components/organisms/LessonForm';
import { useNotification } from '../hooks/useNotification'; 

function CourseDetailsPage() {
  const { courseId } = useParams(); // Obtiene el ID del curso de la URL
  const navigate = useNavigate();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showLessonForm, setShowLessonForm] = useState(false);
  const [editingLesson, setEditingLesson] = useState(null);
  const { addNotification } = useNotification();


  const fetchCourseDetails = async () => {
    try {
      setLoading(true);
      const data = await courseService.getCourseById(parseInt(courseId));
      setCourse(data);
    } catch (err) {
      console.error("Error fetching course details:", err);
      setError("Hubo un error al cargar los detalles del curso.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (courseId) {
      fetchCourseDetails();
    }
  }, [courseId]); 

  const handleEditCourse = () => {
    navigate(`/courses/${course.id}/edit`); // Redirige a la página de edición
  };

  const handleDeleteCourse = async () => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este curso?')) {
      try {
        await courseService.deleteCourse(parseInt(courseId));
        addNotification('Curso eliminado con éxito.', 'success');
        navigate('/'); // Redirige a la página principal después de eliminar
      } catch (error) {
        console.error('Error al eliminar el curso:', error);
        addNotification('Hubo un error al eliminar el curso.', 'error');
      }
    }
  };

  // *** Lógica para Lecciones (Añadir/Editar/Eliminar) ***
  const handleAddLessonClick = () => {
    setEditingLesson(null);
    setShowLessonForm(true);
  };

  // Esta función ahora solo prepara el formulario para la edición, no navega
  const handleEditLessonClick = (lesson) => {
    setEditingLesson(lesson);
    setShowLessonForm(true);
  };

  const handleDeleteLesson = async (lessonId) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar esta lección?')) {
      try {
        await lessonService.deleteLesson(parseInt(courseId), lessonId);
        addNotification('Lección eliminada con éxito.', 'success');
        fetchCourseDetails(); // Llama a la función que ahora está definida en el ámbito correcto
      } catch (error) {
        console.error('Error al eliminar la lección:', error);
        addNotification('Hubo un error al eliminar la lección.', 'error');
      }
    }
  };

  const handleLessonFormSubmit = async (lessonData) => {
    try {
      if (editingLesson) {
        // Actualizar lección existente
        await lessonService.updateLesson(parseInt(courseId), editingLesson.id, lessonData);
        addNotification('Lección actualizada con éxito!', 'success');
      } else {
        // Crear nueva lección
        await lessonService.createLesson(parseInt(courseId), lessonData);
        addNotification('Lección creada con éxito!', 'success');
      }
      setShowLessonForm(false);
      setEditingLesson(null);
      fetchCourseDetails(); // Llama a la función que ahora está definida en el ámbito correcto
    } catch (error) {
      console.error('Error al guardar la lección:', error);
      addNotification('Hubo un error al guardar la lección. Revisa la consola.', 'error');
    }
  };

  const handleCancelLessonForm = () => {
    setShowLessonForm(false);
    setEditingLesson(null);
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <AppText>Cargando detalles del curso...</AppText>
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
        <AppText className="text-gray-600">Curso no encontrado.</AppText>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow-md p-6 max-w-4xl mx-auto">
      <nav className="text-sm text-gray-500 mb-4">
        <Link to="/" className="hover:underline">Cursos</Link> {'>'} <span className="font-semibold">{course.title}</span>
      </nav>

      <div className="flex justify-between items-center mb-4">
        <Title level={1} className="text-blue-700">{course.title}</Title>
        <div className="flex space-x-2">
          <Button variant="secondary" onClick={handleEditCourse}>
            Editar Curso
          </Button>
          <Button variant="danger" onClick={handleDeleteCourse}>
            Eliminar Curso
          </Button>
        </div>
      </div>
      <AppText className="text-gray-800 mb-2">{course.description}</AppText>
      <AppText className="text-gray-600 text-sm italic mb-6">Instructor: {course.instructor}</AppText>

      {/* Sección de Lecciones */}
      <div className="mt-8">
        <div className="flex justify-between items-center mb-4">
          <Title level={2} className="text-gray-800">Lecciones:</Title>
          <Button variant="primary" onClick={handleAddLessonClick}>
            Añadir Lección
          </Button>
        </div>

        {/* Formulario de Lección (Crear/Editar) */}
        {showLessonForm && (
          <div className="mb-6">
            <LessonForm
              formTitle={editingLesson ? 'Editar Lección' : 'Añadir Nueva Lección'}
              initialData={editingLesson}
              onSubmit={handleLessonFormSubmit}
              onCancel={handleCancelLessonForm}
            />
          </div>
        )}

        {course.lessons && course.lessons.length > 0 ? (
          <ul className="space-y-3">
            {course.lessons.map((lesson) => (
              <li key={lesson.id} className="bg-gray-50 p-3 rounded-md shadow-sm">
                <div className="flex justify-between items-center">
                  <Link to={`/courses/${course.id}/lessons/${lesson.id}`} className="text-lg font-semibold text-gray-900 hover:text-blue-700 transition-colors duration-200">
                    {lesson.title}
                  </Link>
                  <div className="flex space-x-2">
                    <Button variant="ghost" onClick={() => handleEditLessonClick(lesson)} className="text-sm">
                      Editar
                    </Button>
                    <Button variant="ghost" onClick={() => handleDeleteLesson(lesson.id)} className="text-sm text-red-600">
                      Eliminar
                    </Button>
                  </div>
                </div>
              </li>
            ))}
          </ul>
        ) : (
          <AppText className="text-gray-600">Este curso no tiene lecciones aún. ¡Añade una!</AppText>
        )}
      </div>
    </div>
  );
}

export default CourseDetailsPage;
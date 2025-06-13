/*
* Página principal, muestra el listado de Cursos
*/

import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import CourseList from '../components/organisms/CourseList';
import { courseService } from '../services/courseService'; 
import AppText from '../components/atoms/AppText';
import Spinner from '../components/atoms/Spinner';
import { useNotification } from '../hooks/useNotification'; 

function HomePage() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();
  const { addNotification } = useNotification();

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        setLoading(true);
        const data = await courseService.getAllCourses();
        setCourses(data);
      } catch (err) {
        console.error("Error fetching courses:", err);
        setError("Hubo un error al cargar los cursos.");
      } finally {
        setLoading(false);
      }
    };

    fetchCourses();
  }, []);


  const handleEditCourse = (id) => {
    navigate(`/courses/${id}/edit`); 
  };

  const handleDeleteCourse = async (id) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este curso?')) {
      try {
        await courseService.deleteCourse(id);
        addNotification('Curso eliminado con éxito.', 'success');
        setCourses(courses.filter(course => course.id !== id));
      } catch (error) {
        console.error('Error al eliminar el curso:', error);
        addNotification('Hubo un error al eliminar el curso.', 'error');
      }
    }
  };

  


  if (loading) {
    return (
      <div className="flex items-center justify-center h-full min-h-[300px]">
        <Spinner size="large" className="text-blue-600" /> 
        <AppText className="ml-3 text-lg text-gray-700">Cargando cursos...</AppText>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-full">
        <AppText className="text-red-500">{error}</AppText>
      </div>
    );
  }

  return (
    <CourseList
      courses={courses}
      onEditCourse={handleEditCourse}
      onDeleteCourse={handleDeleteCourse}
    />
  );
}

export default HomePage;
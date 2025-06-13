/*
* Página para mostrar el los detalles de una lección y el reproductor de Youtube
*/

import { useEffect, useState } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { lessonService } from '../services/lessonService';
import { courseService } from '../services/courseService'; // Necesario para obtener el nombre del curso para el breadcrumb
import Title from '../components/atoms/Title';
import AppText from '../components/atoms/AppText';
import Button from '../components/atoms/Button';
import YouTubePlayer from '../components/atoms/YouTubePlayer';

function LessonDetailsPage() {
  const { courseId, lessonId } = useParams();
  const navigate = useNavigate();
  const [lesson, setLesson] = useState(null);
  const [courseTitle, setCourseTitle] = useState('Cargando Curso...'); // Para el breadcrumb
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLessonDetails = async () => {
      try {
        setLoading(true);
        // Obtener la lección
        const lessonData = await lessonService.getLessonById(parseInt(courseId), parseInt(lessonId));
        setLesson(lessonData);

        // Obtener el título del curso para el breadcrumb
        const courseData = await courseService.getCourseById(parseInt(courseId));
        setCourseTitle(courseData.title);

      } catch (err) {
        console.error("Error fetching lesson details:", err);
        setError("Hubo un error al cargar los detalles de la lección.");
      } finally {
        setLoading(false);
      }
    };

    if (courseId && lessonId) {
      fetchLessonDetails();
    }
  }, [courseId, lessonId]);



  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <AppText>Cargando detalles de la lección...</AppText>
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

  if (!lesson) {
    return (
      <div className="flex items-center justify-center h-96">
        <AppText className="text-gray-600">Lección no encontrada.</AppText>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow-md p-6 max-w-4xl mx-auto">
      {/* Breadcrumbs */}
      <nav className="text-sm text-gray-500 mb-4">
        <Link to="/" className="hover:underline">Cursos</Link> &gt;
        <Link to={`/courses/${courseId}`} className="hover:underline ml-1">{courseTitle}</Link> &gt;
        <span className="font-semibold ml-1">{lesson.title}</span>
      </nav>

      <div className="flex justify-between items-center mb-4">
        <Title level={2} className="text-blue-700">{lesson.title}</Title>
      </div>

      <div className="mb-6">
        <YouTubePlayer videoUrl={lesson.video_url} className="w-full h-auto aspect-video" /> {/* Ajusta el tamaño del reproductor */}
      </div>
    </div>
  );
}

export default LessonDetailsPage;
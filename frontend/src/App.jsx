// src/App.jsx
import './App.css';
import { Routes, Route } from 'react-router-dom';

//Providers
import { NotificationProvider } from './context/NotificationContext';

//Layout
import MainLayout from './layouts/MainLayout';

//Importar Páginas
import HomePage from './pages/HomePage';
import CourseDetailsPage  from './pages/CourseDetailPage';
import CreateCoursePage  from './pages/CreateCoursePage';
import EditCoursePage from './pages/EditCoursePage';
import LessonDetailsPage from './pages/LessonDetailsPage';
import NotFoundPage from './pages/NotFoundPage';



function App() {
  return (
    <NotificationProvider>
      <MainLayout>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/courses/:courseId" element={<CourseDetailsPage />} />
          <Route path="/courses/create" element={<CreateCoursePage />} />
          <Route path="/courses/:courseId/edit" element={<EditCoursePage />} />
          <Route path="/courses/:courseId/lessons/:lessonId" element={<LessonDetailsPage />} />
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </MainLayout>
    </NotificationProvider>
  );
}

export default App;
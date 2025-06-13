/*
* Este es el componente principal del formulario para lecciones, 
* que se usa tanto para crear como para editar lecciones. Recibe los datos iniciales y una función onSubmit.
*/


import { useState, useEffect } from 'react';
import Input from '../atoms/Input';
import Button from '../atoms/Button';
import FormField from '../molecules/FormField';
import Title from '../atoms/Title';
import AppText from '../atoms/AppText';

const LessonForm = ({ initialData, onSubmit, onCancel, formTitle }) => {
  const [title, setTitle] = useState('');
  const [videoUrl, setVideoUrl] = useState('');
  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (initialData) {
      setTitle(initialData.title || '');
      setVideoUrl(initialData.video_url || '');
    }
  }, [initialData]);

  const validate = () => {
    const newErrors = {};
    if (!title.trim()) newErrors.title = 'El título de la lección es requerido.';

    // alidación más estricta para URLs 
    const validGoogleusercontentPattern = /^(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)[\w\-]{11}(\?.*)?$/;

    if (!videoUrl.trim()) {
        newErrors.videoUrl = 'La URL del video es requerida.';
    } else if (!validGoogleusercontentPattern.test(videoUrl)) {
        newErrors.videoUrl = 'Por favor, introduce una URL de video de ejemplo válida (ej. https://youtu.be/3c-iBn73dDE).';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      onSubmit({ title, video_url: videoUrl });
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6 max-w-lg mx-auto">
      <Title level={2} className="text-center mb-6">{formTitle}</Title>
      <form onSubmit={handleSubmit}>
        <FormField label="Título de la Lección" htmlFor="lesson-title" error={errors.title}>
          <Input
            id="lesson-title"
            type="text"
            placeholder="Ej. Introducción a Docker"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </FormField>

        <FormField label="URL del Video (YouTube)" htmlFor="video-url" error={errors.videoUrl}>
          <Input // Usamos Input, ya que la URL de video suele ser de una sola línea
            id="video-url"
            type="url" // Tipo url para validación básica del navegador
            placeholder="Ej. https://www.youtube.com/watch?v=..."
            value={videoUrl}
            onChange={(e) => setVideoUrl(e.target.value)}
          />
          <AppText className="text-xs text-gray-500 mt-1">Solo URLs de YouTube.</AppText>
        </FormField>

        <div className="flex justify-end space-x-3 mt-6">
          <Button type="button" variant="secondary" onClick={onCancel}>
            Cancelar
          </Button>
          <Button type="submit" variant="primary">
            {initialData ? 'Actualizar Lección' : 'Crear Lección'}
          </Button>
        </div>
      </form>
    </div>
  );
};

export default LessonForm;
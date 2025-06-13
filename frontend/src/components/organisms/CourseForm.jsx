/*
* Este es el componente principal del formulario para cursos, 
* que se usa tanto para crear como para editar cursos. Recibe los datos iniciales y una función onSubmit.
*/

import { useState, useEffect } from 'react';
import Input from '../atoms/Input';
import TextArea from '../atoms/TextArea';
import Button from '../atoms/Button';
import FormField from '../molecules/FormField';
import Title from '../atoms/Title';

const CourseForm = ({ initialData, onSubmit, onCancel, formTitle }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [instructor, setInstructor] = useState('');
  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (initialData) {
      setTitle(initialData.title || '');
      setDescription(initialData.description || '');
      setInstructor(initialData.instructor || '');
    }
  }, [initialData]);

  const validate = () => {
    const newErrors = {};
    if (!title.trim()) newErrors.title = 'El título es requerido.';
    if (!description.trim()) newErrors.description = 'La descripción es requerida.';
    if (!instructor.trim()) newErrors.instructor = 'El instructor es requerido.';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      onSubmit({ title, description, instructor });
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6 max-w-lg mx-auto">
      <Title level={2} className="text-center mb-6">{formTitle}</Title>
      <form onSubmit={handleSubmit}>
        <FormField label="Título del Curso" htmlFor="title" error={errors.title}>
          <Input
            id="title"
            type="text"
            placeholder="Ej. Curso de Docker"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </FormField>

        <FormField label="Descripción" htmlFor="description" error={errors.description}>
          <TextArea
            id="description"
            placeholder="Una descripción breve del curso."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            rows={4}
          />
        </FormField>

        <FormField label="Instructor" htmlFor="instructor" error={errors.instructor}>
          <Input
            id="instructor"
            type="text"
            placeholder="Ej. Nana Janashia"
            value={instructor}
            onChange={(e) => setInstructor(e.target.value)}
          />
        </FormField>

        <div className="flex justify-end space-x-3 mt-6">
          <Button type="button" variant="secondary" onClick={onCancel}>
            Cancelar
          </Button>
          <Button type="submit" variant="primary">
            {initialData ? 'Actualizar Curso' : 'Crear Curso'}
          </Button>
        </div>
      </form>
    </div>
  );
};

export default CourseForm;
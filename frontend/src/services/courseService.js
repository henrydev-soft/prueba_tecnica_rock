/**
 * Servicio de gestión de cursos: encapsula las operaciones CRUD sobre el recurso "curso" a través de la API.
 * 
 * Este módulo define funciones asíncronas que interactúan con el backend para obtener, crear, actualizar 
 * y eliminar cursos, incluyendo la obtención de cursos con sus lecciones asociadas.
 * 
 * Al centralizar las llamadas HTTP relacionadas con cursos, se mejora la reutilización del código,
 * se facilita el mantenimiento y se asegura una separación clara de responsabilidades en el frontend.
 */


import apiClient from '../api/api';

export const courseService = {
  /**
   * Obtiene todos los cursos.
   * @returns {Promise<Array<Object>>} Una promesa que resuelve con una lista de objetos de curso.
   * Ej: [{ id: 1, title: 'Curso A', description: '...', instructor: '...' }]
   */
  getAllCourses: async () => {
    const response = await apiClient.get('/courses/');
    return response.data;
  },

  /**
   * Obtiene un curso por su ID, incluyendo sus lecciones.
   * @param {number} id - El ID del curso.
   * @returns {Promise<Object>} Una promesa que resuelve con un objeto de curso con lecciones.
   * Ej: { id: 1, title: 'Curso A', lessons: [{ id: 101, title: 'Lección 1', video_url: '...' }] }
   */
  getCourseById: async (id) => {
    const response = await apiClient.get(`/courses/${id}`);
    return response.data;
  },

  /**
   * Crea un nuevo curso.
   * @param {Object} courseData - Los datos del curso a crear.
   * @param {string} courseData.title
   * @param {string} courseData.description
   * @param {string} courseData.instructor
   * @returns {Promise<Object>} Una promesa que resuelve con el objeto del curso creado.
   */
  createCourse: async (courseData) => {
    const response = await apiClient.post('/courses/', courseData);
    return response.data;
  },

  /**
   * Actualiza un curso existente.
   * @param {number} id - El ID del curso a actualizar.
   * @param {Object} courseData - Los datos del curso a actualizar (puede contener solo algunas propiedades).
   * @param {string} [courseData.title]
   * @param {string} [courseData.description]
   * @param {string} [courseData.instructor]
   * @returns {Promise<Object>} Una promesa que resuelve con el objeto del curso actualizado.
   */
  updateCourse: async (id, courseData) => {
    const response = await apiClient.put(`/courses/${id}`, courseData);
    return response.data;
  },

  /**
   * Elimina un curso por su ID.
   * @param {number} id - El ID del curso a eliminar.
   * @returns {Promise<void>} Una promesa que resuelve cuando el curso es eliminado.
   */
  deleteCourse: async (id) => {
    await apiClient.delete(`/courses/${id}`);
  },
};
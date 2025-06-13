/**
 * Servicio de gestión de lecciones: maneja operaciones CRUD sobre el recurso "lección" mediante llamadas a la API.
 * 
 * Este módulo proporciona funciones para crear, leer, actualizar y eliminar lecciones asociadas a cursos.
 * Las funciones están diseñadas para integrarse con el backend y encapsulan los detalles de las solicitudes HTTP,
 * promoviendo una arquitectura limpia y reutilizable en el frontend.
 */

import apiClient from '../api/api';

export const lessonService = {
  /**
   * Crea una nueva lección para un curso específico.
   * @param {number} courseId - El ID del curso al que se añadirá la lección.
   * @param {Object} lessonData - Los datos de la lección a crear.
   * @param {string} lessonData.title
   * @param {string} lessonData.video_url
   * @returns {Promise<Object>} Una promesa que resuelve con el objeto de la lección creada.
   */
  createLesson: async (courseId, lessonData) => {
    const response = await apiClient.post(`/courses/${courseId}/lessons/`, lessonData);
    return response.data;
  },

  /**
   * Obtiene una lección por su ID.
   * @param {number} courseId - El ID del curso al que pertenece la lección
   * @param {number} lessonId - El ID de la lección.
   * @returns {Promise<Object>} Una promesa que resuelve con un objeto de lección.
   * Ej: { id: 101, title: 'Lección 1', video_url: '...', course_id: 1 }
   */
  getLessonById: async (courseId, lessonId) => {
    const response = await apiClient.get(`/courses/${courseId}/lessons/${lessonId}`);
    return response.data;
  },

  /**
   * Actualiza una lección existente.
   * @param {number} courseId - El ID del curso al que pertenece la lección
   * @param {number} lessonId - El ID de la lección a actualizar.   * 
   * @param {Object} lessonData - Los datos de la lección a actualizar (puede contener solo algunas propiedades).
   * @param {string} [lessonData.title]
   * @param {string} [lessonData.video_url]
   * @returns {Promise<Object>} Una promesa que resuelve con el objeto de la lección actualizada.
   */
  updateLesson: async (courseId, lessonId, lessonData) => {
    const response = await apiClient.put(`/courses/${courseId}/lessons/${lessonId}`, lessonData);
    return response.data;
  },

  /**
   * Elimina una lección por su ID.
   * @param {number} lessonId - El ID de la lección a eliminar.
   * @returns {Promise<void>} Una promesa que resuelve cuando la lección es eliminada.
   */
  deleteLesson: async (courseId, lessonId) => {
    await apiClient.delete(`/courses/${courseId}/lessons/${lessonId}`);
  },
};
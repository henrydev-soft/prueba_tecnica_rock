/**
 * Layout principal de la aplicación: estructura base para todas las vistas.
 * 
 * Este componente define un contenedor común para las páginas del frontend,
 * incluyendo espacio para un encabezado y pie de página globales (comentados por ahora),
 * y un área principal donde se renderiza el contenido específico de cada ruta.
 * 
 * Utiliza utilidades de Tailwind CSS para asegurar un diseño responsivo y centrado.
 */


const MainLayout = ({ children }) => {
  return (
    // El contenedor principal para la aplicación.
    <div className="min-h-screen bg-gray-100 flex flex-col">
      {/* Aquí iría un posible "global header" si se necesitara en el futuro */}
      {/* Ejemplo: <header className="p-4 bg-white shadow-sm"></header> */}

      {/* El contenido principal de la ruta se renderizará aquí */}
      {/* El padding y mx-auto centrarán el contenido, similar al layout de la imagen */}
      <main className="flex-grow container mx-auto p-4">
        {children}
      </main>

      {/* Aquí iría un posible "global footer" si se nececitara en el futuro */}
      {/* Ejemplo: <footer className="p-4 bg-gray-800 text-white text-center"></footer> */}
    </div>
  );
};

export default MainLayout;
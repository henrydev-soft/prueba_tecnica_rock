/*
* Un componente para agrupar una etiqueta, un input y un mensaje de error opcional.
*/


const FormField = ({ label, children, error, htmlFor, className = '' }) => {
  return (
    <div className={`mb-4 ${className}`}>
      {label && (
        <label htmlFor={htmlFor} className="block text-gray-700 text-sm font-bold mb-2">
          {label}
        </label>
      )}
      {children}
      {error && <p className="text-red-500 text-xs italic mt-1">{error}</p>}
    </div>
  );
};

export default FormField;
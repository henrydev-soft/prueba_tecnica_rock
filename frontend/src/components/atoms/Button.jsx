/*
* Este será un botón genérico con estilos de Tailwind, adaptable a diferentes propósitos.
*/

const Button = ({ children, onClick, className = '', variant = 'primary', ...props }) => {
  let baseStyles = "px-4 py-2 rounded-md font-semibold transition duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-opacity-75";
  let variantStyles = "";

  switch (variant) {
    case 'primary':
      variantStyles = "bg-gray-900 text-white hover:bg-gray-800 focus:ring-gray-700";
      break;
    case 'secondary':
      variantStyles = "bg-gray-200 text-gray-800 hover:bg-gray-300 focus:ring-gray-400";
      break;
    case 'danger':
      variantStyles = "bg-red-600 text-white hover:bg-red-700 focus:ring-red-500";
      break;
    case 'outline':
        variantStyles = "bg-transparent border border-gray-400 text-gray-700 hover:bg-gray-200 focus:ring-gray-300";
        break;
    case 'ghost':
        variantStyles = "bg-transparent text-gray-700 hover:bg-gray-200 focus:ring-gray-300";
        break;
    default:
      variantStyles = "bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500";
  }

  return (
    <button
      onClick={onClick}
      className={`${baseStyles} ${variantStyles} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};

export default Button;
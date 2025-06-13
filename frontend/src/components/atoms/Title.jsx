/*
* Componente para títulos h1, h2, etc., con estilos de Tailwind.
*/

const Title = ({ children, level = 1, className = '', ...props }) => {
  const Tag = `h${level}`; // Determina el tag HTML (h1, h2, h3, etc.)

  let textStyles = "";
  switch (level) {
    case 1:
      textStyles = "text-4xl font-bold text-gray-900";
      break;
    case 2:
      textStyles = "text-2xl font-semibold";
      break;
    case 3:
      textStyles = "text-xl font-semibold";
      break;
    case 4:
      textStyles = "text-lg font-medium text-gray-700";
      break;
    default:
      textStyles = "text-xl font-semibold text-gray-800";
  }

  return (
    <Tag className={`${textStyles} ${className}`} {...props}>
      {children}
    </Tag>
  );
};

export default Title;
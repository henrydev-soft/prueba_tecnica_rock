/*
* Componente para párrafos y texto general.
*/

const AppText = ({ children, className = '', ...props }) => {
  return (
    <p className={`text-gray-700 ${className}`} {...props}>
      {children}
    </p>
  );
};

export default AppText;
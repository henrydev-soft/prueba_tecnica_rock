/*
* Para mostrar imágenes, con estilos responsivos.
*/

const Image = ({ src, alt, className = '', ...props }) => {
  return (
    <img
      src={src}
      alt={alt}
      className={`w-full h-full object-cover ${className}`} // `object-cover` para que la imagen no se distorsione
      {...props}
    />
  );
};

export default Image;
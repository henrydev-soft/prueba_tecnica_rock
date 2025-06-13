/*
* Componente para agregar video embebido
*/


const YouTubePlayer = ({ videoUrl, className = '' }) => {
  // Función para extraer el ID del video de YouTube de varias URLs
  const getYouTubeVideoId = (url) => {
    if (!url) return null;
    const regExp = /(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})/;
    const match = url.match(regExp);
    return (match && match[1].length === 11) ? match[1] : null;
  };

  const videoId = getYouTubeVideoId(videoUrl);

  if (!videoId) {
    return (
      <div className={`bg-gray-200 flex items-center justify-center text-gray-600 rounded-md ${className}`}>
        Video no disponible o URL inválida.
      </div>
    );
  }

  const embedUrl = `https://www.youtube.com/embed/${videoId}`;

  return (
    <div className={`relative w-full overflow-hidden rounded-md ${className}`} style={{ paddingTop: '56.25%' }}> {/* 16:9 Aspect Ratio */}
      <iframe
        className="absolute top-0 left-0 w-full h-full"
        src={embedUrl}
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
        title="Reproductor de YouTube"
      ></iframe>
    </div>
  );
};

export default YouTubePlayer;
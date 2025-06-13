/*
* Input de tipo Text Area
*/


const TextArea = ({ placeholder, value, onChange, className = '', rows = 4, ...props }) => {
  return (
    <textarea
      placeholder={placeholder}
      value={value}
      onChange={onChange}
      rows={rows}
      className={`w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent ${className}`}
      {...props}
    ></textarea>
  );
};

export default TextArea;
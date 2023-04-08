import React, { useState } from "react";
import axios from 'axios';

function FileUploader() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  // function handleFormSubmittion(e) {
  //   e.preventDefault();
  
  //   let formData = new FormData();
  //   formData.append('file', file);
  
  //   axios.post('http://localhost:5000/upload', formData)
  //     .then((res) => {
  //       setResponse(res.data);
  //       setError(null);
  //     })
  //     .catch((err) => {
  //       setError(err.message);
  //       setResponse(null);
  //     });
  // }
  

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  // return (
  //   <div>
  //     <form onSubmit={handleFormSubmittion}>
  //       <input type="file" onChange={handleFileChange} />
  //       <button type="submit">Upload</button>
  //     </form>
  //     {response && <p>Response: {response}</p>}
  //     {error && <p>Error: {error}</p>}
  //   </div>
  // );

  function handleFormSubmittion(e) {
    e.preventDefault();
  
    let formData = new FormData();
    formData.append('file', file);
  
    axios.post('http://localhost:5000/upload', formData)
      .then((res) => {
        setResponse(res.data.message);
        document.write("Uploaded Successfully!")
        setError(null);
      })
      .catch((err) => {
        setError(err.message);
        setResponse(null);
      });
  }
  
  return (
    <div>
      <form onSubmit={handleFormSubmittion}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      {response && <p>Response: {response}</p>}
      {error && <p>Error: {error}</p>}
    </div>
  );
  
}

export default FileUploader;

import React, { useState } from 'react';
import Axios from 'axios';

function UploadModel() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    try {
      const formData = new FormData();
      formData.append('model', file);

      const response = await Axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        }
      });

      // Handle successful upload
      console.log('Model uploaded successfully:', response.data);
    } catch (error) {
      // Handle upload error
      console.error('Error uploading model:', error);
    }
  };

  return (
    <div>
      <h1>Upload Deep Learning Model</h1>
      <input type="file" accept=".h5,.hdf5,.pb" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={!file}>Upload</button>
    </div>
  );
}

export default UploadModel;

import React, { useState } from "react";
import Axios from "axios";

function Predict() {
  const [disease, setDisease] = useState("");
  const [image, setImage] = useState(null);
  const [data, setData] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);

    const formData = new FormData();
    formData.append("disease", disease);
    formData.append("image", image);

    try {
      const response = await Axios.post("http://127.0.0.1:5000/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      console.log(response.data.outputClass)

      if (!response.data.success) {
        setData(response.data.outputClass);
        setIsLoading(false);
        return;
      }

      setData(response.data.message);
    } catch (error) {
      console.error("Error:", error);
      setData("Please try again!");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex-grow">
      <div className="max-w-xl p-4/3  bg-white border border-gray-500 rounded-lg shadow sm:p-6 md:p-8 dark:bg-gray-900 dark:border-gray-900">
        <form class="space-y-6" onSubmit={handleSubmit}>
          <label className="text-xl font-medium text-gray-900 dark:text-black" htmlFor="disease"> Select disease:</label>
          <select
            className="text-xl bg-gray-50 border border-gray-300 text-gray-900 rounded-lg  block w-full p-2.5 dark:bg-white dark:border-gray-500 dark:placeholder-gray-400 dark:text-black"
            id="disease" value={disease} onChange={(e) => setDisease(e.target.value)} >
            <option value="None">Select one</option>
            <option value="alzheimer">Alzheimer's</option>
            <option value="brain tumor">Brain Tumor</option>
            <option value="fracture">Fracture</option>
            <option value="kidney">Kidney</option>
            <option value="pneumonia">Pneumonia</option>
          </select>
          <br></br>
          <input className="text-xl pointer w-full text-white bg-black hover:bg-grey-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 text-center"
            type="file" id="image" accept="image/*" onChange={(e) => setImage(e.target.files[0])} />
          <button
            className="text-xl w-full text-white bg-black hover:bg-grey-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 text-center" type="submit" disabled={isLoading}> Submit </button>
        </form>
        {isLoading && <p className="text-xl font-medium text-gray-900 dark:text-black">Loading...</p>}
        {data && (
            <h1 className="text-xl font-bold text-gray-900 dark:text-black">{data}</h1>
        )}
      </div>
    </div>
  );
}

export default Predict;

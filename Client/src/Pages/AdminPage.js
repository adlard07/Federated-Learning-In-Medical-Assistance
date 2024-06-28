import React, { useState } from "react";
import Navbar from "../Components/navbar/navbar";
import Axios from "axios";

function AdminPage() {
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
      const response = await Axios.post("http://127.0.0.1:5000/send2db", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

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
    <div>
      <Navbar />
      <div className="pt-10">
        <h2 className="text-3xl text-center font-xl italic font-medium text-gray-900 dark:text-black">Admin</h2>
        <div className="pt-10 bg-white flex-grow justify-center items-center">
          <div className="max-w-md mx-auto">
            <form onSubmit={handleSubmit} className="space-y-6 p-6 rounded-xl bg-white shadow">
              <label htmlFor="disease" className="text-xl font-medium text-gray-900 dark:text-black">
                Select disease:
              </label>
              <select
                id="disease"
                value={disease}
                onChange={(e) => setDisease(e.target.value)}
                className="text-xl bg-gray-50 border border-gray-300 text-gray-900 rounded-lg w-full p-2.5 dark:bg-white dark:border-gray-500 dark:placeholder-gray-400 dark:text-black"
              >
                <option value="None">Select one</option>
                <option value="alzheimer">Alzheimer's</option>
                <option value="brain tumor">Brain Tumor</option>
                <option value="fracture">Fracture</option>
                <option value="kidney">Kidney</option>
                <option value="pneumonia">Pneumonia</option>
              </select>
              <input
                type="file"
                id="image"
                accept="image/*"
                onChange={(e) => setImage(e.target.files[0])}
                className="text-xl pointer w-full text-white bg-black hover:bg-grey-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 text-center"
              />
              <button
                type="submit"
                disabled={isLoading}
                className="text-xl w-full text-white bg-black hover:bg-grey-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 text-center"
              >
                {isLoading ? "Submitting..." : "Submit"}
              </button>
            </form>
            {data && <h1 className="text-xl font-bold text-gray-900 dark:text-black">{data}</h1>}
          </div>
        </div>
      </div>
    </div>
  );
}

export default AdminPage;

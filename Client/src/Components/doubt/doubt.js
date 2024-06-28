import React, { useState } from "react";
import Axios from "axios";

const Doubt = () => {
  const [prompt, setPrompt] = useState("");
  const [textData, setTextData] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    setError("");

    try {
      console.log("Sending request with prompt:", prompt);
      const response = await Axios.post("http://127.0.0.1:5000/doubt", { prompt });
      console.log("Response:", response);
      const resp = response.data.answer;
      setTextData(resp);
    } catch (error) {
      console.error("Error fetching data:", error);
      setError("An error occurred. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="w-full flex-grow">
      <div class=" max-w-xl p-4/3  bg-white border border-gray-500 rounded-lg shadow sm:p-6 md:p-8 dark:bg-gray-900 dark:border-gray-900">
        <form class="space-y-6" onSubmit={handleSubmit}>
          <label className="text-xl font-medium text-gray-900 dark:text-black">
            Ask your doubt here:
          </label>
            <div>
              <input type="text" placeholder="Enter your doubt"value={prompt} onChange={(e) => setPrompt(e.target.value)}
              className="text-lg bg-gray-50 border border-gray-300 text-gray-900 rounded-lg  block w-full p-2.5 dark:bg-white dark:border-gray-500 dark:placeholder-gray-400 dark:text-black" required />
            </div>
            <button type="submit" class="text-xl w-full text-white bg-black hover:bg-grey-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 text-center">
              {isLoading ? "Asking..." : "Ask"} 
            </button>
        </form>
        {error && <p className="text-red-600">{error}</p>}
        {textData && <p className="text-lg text-justify">{textData}</p>}
      </div>
    </div>
  );
};

export default Doubt;

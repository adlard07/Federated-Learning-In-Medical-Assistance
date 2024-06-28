import React, { useState } from "react";
import Axios from "axios";
import "../../Styles/hospitals.css";

const Hospital = () => {
  const [address, setAddress] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [hospitalData, setHospitalData] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    try {
      const response = await Axios.post('http://127.0.0.1:5000/hospitals', { address });
      const resp = response.data;
      setHospitalData(resp);
    } catch (error) {
      console.error('Error fetching hospital data:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex-grow w-full">
      <div className="bg-white border border-gray-500 rounded-xl shadow md:p-8 dark:bg-gray-900 dark:border-gray-900 overflow-hidden"> {/* Added overflow-hidden */}
        <form className="space-y-4" onSubmit={handleSubmit}>
          <label className="text-xl font-medium text-gray-900 dark:text-black">Search hospitals</label>
          <input className="text-xl bg-gray-50 border border-gray-300 text-gray-900 rounded-lg  block w-full dark:bg-white dark:border-gray-500 dark:placeholder-gray-400 dark:text-black"
            type="text" placeholder="Enter location" value={address} onChange={(e) => setAddress(e.target.value)} />
          <button className="text-xl w-full text-white bg-black hover:bg-grey-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg px-5 py-2.5 text-center"
            type="submit" >{isLoading ? "Searching..." : "Search"} </button>
        </form>
        <div className="flex pt-2 items-center">
          <div className="overflow-y-auto max-h-80">
            {hospitalData.map((hospital, index) => (
              <div className="shadow rounded-xl p-1 mb-4" key={index}>
                <div className="flex gap-2 items-center">
                  <img className="w-10 h-10 rounded-full" src={hospital.image} alt="Hospital" />
                  <p className="text-lg font-medium text-black truncate dark:black">{hospital.name}</p>
                </div>
                <p className="text-sm inline-flex items-center font-semibold text-gray-900 dark:text-black">Phone Number: {hospital.contact}</p>
                <p className="text-sm text-black dark:text-black">Address: {hospital.address}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Hospital;

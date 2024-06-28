import React from "react";
import Navbar from "../Components/navbar/navbar";

import Predict from "../Components/predict/Predict";
import Graph from "../Components/graph/graph";
import Hospital from "../Components/searchHospitals/Hospital";
import Doubt from "../Components/doubt/doubt";

function Dashboard() {
  return (
    <div className="">
      <Navbar />
      <h2 className="pt-3 text-3xl text-center font-xl italic font-medium text-gray-900 dark:text-black">Dashboard</h2>
      <div className="flex">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-4">
          <div className="p-4 flex-col">
            <Predict />
            <div className="mt-4">
              <Doubt />
            </div>
          </div>
          <div className="p-4 flex flex-col gap-4">
            <Graph />
            <div className="">
              <div className="">
                <Hospital />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;

# Project Name: Federated Disease Prediction System

## Overview
This project is a Federated Disease Prediction System that utilizes deep learning models to predict diseases based on medical images. It aggregates multiple models from various sources to create global models for enhanced accuracy and robustness. Additionally, it features a search bar functionality where users can input a location to retrieve a list of the top 20 hospitals nearby for testing related to their predicted disease.

## Features
1. **Model Aggregation:** Aggregates multiple models from different sources to create global models, improving prediction accuracy and reliability.
   
2. **Location-Based Hospital Search:** Offers a search bar where users can input their location to receive a list of the top 20 hospitals nearby for testing related to the predicted disease.

3. **Chatbot:** Integrated openai ChatGPT 3.5 by fine tuning it on custom data specialised on medical sector gathered from online sources like Data Search Engine (Google), Oxford, Wifipedia and Kaggle. This bot specialises in giving basic resolutions for any common disease and is capable on giving a generic solution on the medical queries asked. 

4. **Dashboard:** A dashboard is shown to display how many people have gained from the project using a graph.

## Description
The Federated Disease Prediction System is an innovative project that leverages deep learning models to predict diseases based on medical images. By aggregating multiple models from diverse sources, the system enhances prediction accuracy and reliability. Furthermore, it offers a user-friendly search bar feature where individuals can input their location to receive a curated list of the top 20 hospitals nearby for disease testing and consultation. This system aims to streamline the disease prediction process and provide users with convenient access to healthcare services based on their predicted health conditions.

## Methodology
1. **Data Collection:** Gather a diverse dataset of medical images related to various diseases for training the deep learning models from different data sources such as Kaggle on Alzheimer's, Brain Tumor, Breast Cancer, Fracture, Kidney, Pneumonia. For production multiple hospitals and clinics can colaborte contributing their own DL models providing a much effective way of targating this problem.
   
2. **Model Development:** Develop individual deep learning models for disease prediction using TensorFlow and PyTorch, ensuring high accuracy and performance.
   
3. **Model Aggregation:** Aggregate the individual models from different sources to create global models that combine the strengths of each, resulting in enhanced prediction capabilities.
   
4. **User Interface Development:** Create a user-friendly interface using Flask to allow users to upload medical images, view predicted diseases, and utilize the location-based search functionality.
   
5. **Location-Based Hospital Search:** Implement a search feature that integrates with location data to recommend the top 20 hospitals nearby based on the user's input for further testing and consultation.
   
6. **Testing and Validation:** Conduct rigorous testing to validate the accuracy and efficiency of the deep learning models and the overall system functionality.
   
7. **Deployment:** Deploy the system on a server to make it accessible to users, ensuring scalability and reliability for real-world usage.
   

## Installation
To run this project locally, follow these steps:
1. Clone the repository from GitHub.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Run the application using `python app.py`.
4. Then open a new terminal and enter the ReactApp/Client directory by running `cd ReactApp/Client` command in the terminal.
4. Run the frontend using  `npm start`.

## Usage
1. Access the application through the provided URL.
2. Upload a medical image for disease prediction.
3. View the predicted disease results generated by the deep learning models.
4. Enter your location in the search bar to find the top 20 hospitals nearby for further testing and consultation.

## Technologies Used
- Python
- Deep Learning (TensorFlow, Keras)
- Flask (Web Framework)
- React.js

## Contributors
- Bhavika Salvi
- Aron Menezes
- Adelard Dcunha 😎

## License
<!-- This project is licensed under the [License Name]. See the LICENSE file for more details. -->

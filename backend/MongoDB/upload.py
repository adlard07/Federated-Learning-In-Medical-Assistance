import pymongo
import cv2
import numpy as np
import io

class MongoDB:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["FederatedLearning"]
        self.databases = {
            "alzheimer": self.db['Alzheimer'],
            "brain_tumor": self.db["Brain Tumor"],
            "fracture": self.db["Fracture"],
            "kidney": self.db["Kidney"],
            "pneumonia": self.db["Pneumonia"],
        }

    def upload_img(self, image, disease):
        try:
            # Convert NumPy array to bytes
            image_bytes = cv2.imencode('.jpg', image)[1].tobytes()

            data = {
                "image_pixels": image_bytes,
                "disease": disease
            }

            # Insert data into the appropriate collection based on disease
            result = self.databases[disease].insert_one(data)

            response = {"message":"Image Uploaded"}
            return response

        except Exception as e:
            return str(e)


    def fetch_img(self, disease):
        try:
            # Find one document from the collection
            document = self.databases[disease].find_one()

            # Extract the image bytes from the document
            image_bytes = document["image_pixels"]

            # Convert the image bytes back to a NumPy array
            image_array = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

            return image_array

        except Exception as e:
            return None

if __name__ == "__main__":
    image_path = r'pneumonia_20.jpeg'
    image = cv2.imread(image_path)
    disease = 'pneumonia'

    # Upload image
    message = MongoDB().upload_img(image, disease)
    print(message)

    # Fetch image
    fetched_image = MongoDB().fetch_img(disease)
    print(fetched_image)

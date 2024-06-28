from tensorflow.keras.models import load_model
import numpy as np
import logging
import cv2
import os


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class Aggregate:
    def __init__(self):
        self.model_path = "objects/models"
        self.global_model_path = 'global_model.h5'
        self.image_class_model = 'image_classifier.h5'

        self.classes = {
            "alzheimer": ['Mild Dementia', 'Moderate Dementia', 'Non Dementia', 'Very Mild Dementia'],
            "brain tumor": ['Glioma Tumor', 'Meningioma Tumor', 'Pituitary Tumor'],
            "breast cancer": ['Benign', 'Malignant', 'Normal'],
            "fracture": ['Fractured', 'Not Fractured'],
            "kidney": ['Cyst', 'Tumor', 'Stone', 'Normal'],
            "pneumonia": ['PNEUMONIA', 'NORMAL']
        }
        self.image_classes = ['alzheimer', 'brain tumor', 'breast cancer', 'fracture', 'kidney', 'pneumonia']


    def valid_img_check(self, img):
        model = load_model(os.path.join(self.model_path, self.image_class_model))
        img = np.array(cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE))
        img = cv2.resize(img, (144, 144))
        img = img.reshape(-1, 144, 144, 1)
        pred = model.predict(img)[0]
        output_index = np.argmax(pred)
        image_class = self.image_classes[output_index]
        return image_class        


    def load_global_model(self, disease):
        global_model_path = os.path.join(self.model_path, disease, self.global_model_path)
        return load_model(global_model_path)



    def preprocess_image(self, disease, img, channels):
        disease = disease.lower()
        dimensions = {
            "alzheimer": (208, 176),
            "brain tumor": (150, 150),
            "breast cancer": (300, 300),
            "fracture": (224, 224),
            "kidney": (150, 150),
            "pneumonia": (224, 224)
        }
        width, height = dimensions.get(disease, (None, None))

        if width is None or height is None:
            logging.info("Unsupported disease")
            return None

        # if channels == 3:
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (width, height))
        image = np.expand_dims(image, axis=0)
        return image



    def confidence_thresholding(self, preds, threshold=0.7):
        max_confidence = np.max(preds)
        if max_confidence < threshold:
            logging.info("Anomaly detected: Low confidence")
            return None
        else:
            return preds


    def prediction(self, disease, img):
        disease = disease.lower()
        
        # Check if global model is loaded
        global_model = self.load_global_model(disease)  # Changed from Aggregate().load_global_model(disease)
        channels = global_model.input_shape[-1]
        
        if global_model is None:
            logging.error("Global model is not loaded.")
            return None
        

        # Get classes for the disease
        classes = self.classes.get(disease)
        if classes is None:
            logging.error("Classes not defined for the disease.")
            return None


        # if self.valid_img_check(img) != disease:
        #     return "Please upload valid image"
        
        # Preprocess image
        processed_image = self.preprocess_image(disease, img, channels)
        if processed_image is None:
            return None
        
        # Predict
        preds = global_model.predict(processed_image)[0]
        
        # # Apply confidence thresholding
        # preds = self.confidence_thresholding(preds)
        # if preds is None:
        #     return None

        output_index = np.argmax(preds)
        output_class = classes[output_index]
        return output_class



if __name__ == '__main__':
    disease = "fracture"
    # models_path = f'objects/models/{disease}/global_model.h5'
    image_path = r'objects\test\fractured_11.jpg' 
    image = cv2.imread(image_path)  
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = np.expand_dims(rgb_image, axis=0)
    
    predictor = Aggregate()
    output_class = predictor.prediction(disease, image)
    logging.info(output_class)

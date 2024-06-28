from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
from datetime import datetime
from flask_cors import CORS
import numpy as np
import logging
import cv2

from MySQLDB.insert_into import PushData, GraphData
from MongoDB.upload import MongoDB
from src.model_agregation.agregate import Aggregate
from src.chatbot.chatbot import Prompt
from src.gmaps.address import gmaps


app = Flask(__name__)  
CORS(app)
MySQLDB = PushData()
mongoDB = MongoDB()

####################################################### Login / Signup ##########################################################

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')
    
    if all([email, password, role]):
        table = list(MySQLDB.fetch_table(role=role))
        # print(table)
        for row in table:
            if row[2] == email:
                if row[3] == password:
                    message = f'{role} Login Successful!'
                    break
                else:
                    message = "Invalid credentials!"
            else:
                message = 'User not found!'
        logging.info(message)
    return message

@app.route('/register', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_pass = data.get('confirmation')
    role = data.get('role')
    if password == confirm_pass:
        if all([name, email, password, role]):
            message = MySQLDB.insert_values(role=role, values=(str(name), str(email), str(password)))
            logging.info(message)
            return message


####################################################### Google Maps API ########################################################

@app.route('/latlong', methods=['POST'])
def geocode_address():
    address = request.get_json()
    geolocator = Nominatim(user_agent="myapp")
    location = geolocator.geocode(address)
    if location:
        return jsonify({'latitude':location.latitude, 'logitude':location.longitude})
    else:
        return None
    
@app.route('/hospitals', methods=['POST'])
def hospitals():
    address = request.get_json().get('address')
    hospoital_data = gmaps(address)
    return jsonify(hospoital_data)


####################################################### Model Prediction #######################################################

@app.route('/predict', methods=['POST'])
def predict():
    disease = request.form.get('disease')
    image = request.files['image'].read()
    
    if disease=='None':
        return "Please provide a disease"
    
    nparr = np.frombuffer(image, np.uint8)
    img = np.array(cv2.imdecode(nparr, cv2.IMREAD_COLOR))
    
    disease_class = Aggregate().prediction(disease, img)
    
    day = datetime.today().weekday()

    if disease_class:
        GraphData().insert_graph_data(day)
        gen_text = Prompt().disease_description(disease, disease_class)

    return jsonify({
        "outputClass": disease_class,
        "generatedText":gen_text
        })


######################################################## Graph Data #################################################################

@app.route('/graph_data')
def graph_data():
    values, columns = GraphData().fetch_graph_data()
    return jsonify({
        'values': values,
        'columns': columns
        })


######################################################## Question Answering #################################################################

@app.route('/doubt', methods=['POST'])
def doubt():
    textData = request.get_json().get('prompt')
    answer = Prompt().doubt(textData)

    return jsonify({
        'answer' : answer
    })



####################################################### Upload Image ##########################################################

@app.route('/send2db', methods=['POST'])
def upload_model():
    disease = request.form.get('disease')
    image = request.files['image'].read()

    if disease=='None':
        return "Please provide a disease"
    
    message = mongoDB.upload_img(image, disease)

    return jsonify(message)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
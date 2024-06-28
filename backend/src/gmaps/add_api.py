from geopy.geocoders import Nominatim
from flask import Flask, jsonify, request
from flask_cors import CORS
from address import gmaps

app = Flask(__name__)
CORS(app)

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
    address = request.get_json()['hospitals']
    hospoital_data = gmaps(address)
    return jsonify(hospoital_data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
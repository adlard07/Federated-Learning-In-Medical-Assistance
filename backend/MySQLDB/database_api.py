from flask import Flask, request
from flask_cors import CORS
from insert_into import PushData
import logging

app = Flask(__name__)
CORS(app)
db = PushData()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if all([email, password]):
        table = list(db.fetch_table())
        for row in table:
            if row[1] == email:
                # table[0] = email
                message = 'Login Successful!'
                break
            else:
                message = 'User not found!'
        logging.info(message)
    return message


@app.route('/register', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if all([email, password]):
        message = db.insert_values(values=(str(email), str(password)))
        logging.info(message)
        return message


if __name__ == '__main__':
    app.run(debug=True, port=5000)
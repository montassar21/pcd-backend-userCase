from flask import Flask, jsonify, make_response, render_template, request

from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle
app = Flask(__name__)
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        # Handle preflight requests
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    
    # Handle actual POST requests
    form_data = request.get_json()
    input_data = np.array(list(form_data.values())).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({'prediction': str(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)

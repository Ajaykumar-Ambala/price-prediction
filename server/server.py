from flask import Flask, request, jsonify, render_template
import util
import os

app = Flask(__name__,
            template_folder="../UI/templates",
            static_folder="../UI/static")

# Load model on start
util.load_saved_artifacts()

# Serve UI
@app.route('/')
def serve_ui():
    return render_template('index.html')

# API: Get locations
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# API: Predict price
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():


    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Starting python flask server for home price prediction....")
    app.run(debug=True)
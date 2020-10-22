import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)

model = pickle.load(open('Ride_Predict', 'rb'))


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    x_values = [np.array(features)]
    predicted_value = model.predict(x_values)
    predicted_value = predicted_value.round(0)
    predicted_value = math.floor(predicted_value[0])
    ride = "The number of weekly rides will be: {}".format((predicted_value))
    print(str(predicted_value))
    return render_template('index.html', predicted_value=ride)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

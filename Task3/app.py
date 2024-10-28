from flask import Flask, render_template, request
import joblib
import numpy as np
from normalization import ozellik_normalizasyonu
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("multiple_linear_regression_model.pkl")
data = pd.read_csv('dataset/RealEstate.csv')
X = data[['Size', 'Bedrooms']].to_numpy()
x, mean, std = ozellik_normalizasyonu(X)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    bedrooms = int(request.form['bedrooms'])
    size = int(request.form['size'])

    # Prepare the feature vector for the model

    x1 = (size - mean[0]) / std[0]
    x2 = (bedrooms - mean[1]) / std[1]

    # Prepare the feature vector for the model
    features = np.array([[x1, x2]])

    # Predict the price
    prediction = model.predict(features)[0]

    # Return the result back to the template
    return render_template('index.html', price=f"{int(prediction[0]):,}".replace(",", "."))


if __name__ == '__main__':
    app.run(debug=True)

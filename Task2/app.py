from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("linear_regression_model.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    total_bill = float(request.form['total_bill'])
    size = int(request.form['size'])
    sex = request.form['sex']  # 'Male' or 'Female'
    smoker = request.form['smoker']  # 'Yes' or 'No'
    
    # Convert categorical values to the same format as training data (one-hot encoding)
    sex_Male = 1 if sex == 'Male' else 0
    smoker_Yes = 1 if smoker == 'Yes' else 0
    
    # Prepare the feature vector for the model
    features = np.array([[total_bill, sex_Male, smoker_Yes, size]])
    
    # Predict the tip
    predicted_tip = model.predict(features)[0]
    
    # Return the result back to the template
    return render_template('index.html', tip=round(predicted_tip[0], 3))

if __name__ == '__main__':
    app.run(debug=True)


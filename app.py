from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

rf_model = joblib.load('disease_rf_model.pkl')
labelEncoder = joblib.load('label_encoder.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        fever = 1 if data['fever'] == 'Yes' else 0
        cough = 1 if data['cough'] == 'Yes' else 0
        fatigue = 1 if data['fatigue'] == 'Yes' else 0
        breathing = 1 if data['breathing'] == 'Yes' else 0
        age = int(data['age'])
        gender = 1 if data['gender'] == 'Female' else 0
        bp = 1 if data['bp'] == 'Normal' else 0
        cholesterol_map = {'Low': 0, 'Normal': 1, 'High': 2}
        cholesterol = cholesterol_map.get(data['cholesterol'], 1)

        input_data = [[fever, cough, fatigue, breathing, age, gender, bp, cholesterol, 0]]

        prediction = rf_model.predict(input_data)[0]
        confidence = rf_model.predict_proba(input_data)[0][prediction]
        predicted_disease = labelEncoder.inverse_transform([prediction])[0]

        result = f"{predicted_disease} - Certeza: {round(confidence * 100, 2)}%"

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

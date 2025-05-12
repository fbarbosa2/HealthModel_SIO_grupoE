from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# Carregar modelo, label encoder e dataset
rf_model = joblib.load('disease_rf_model.pkl')
labelEncoder = joblib.load('label_encoder.pkl')
df = pd.read_csv("datasets/Disease and symptoms dataset.csv")

@app.route('/predict-complex', methods=['POST'])
def predict_complex():
    try:
        data = request.get_json()
        sintomas_paciente = data.get('sintomas', [])

        sintomas = df.columns[1:]
        input_data = [[1 if sintoma in sintomas_paciente else 0 for sintoma in sintomas]]

        prediction = rf_model.predict(input_data)[0]
        probs = rf_model.predict_proba(input_data)[0]
        class_index = list(rf_model.classes_).index(prediction)
        confidence = probs[class_index]

        predicted_disease = labelEncoder.inverse_transform([prediction])[0]
        result = f"{predicted_disease} - Certeza: {round(confidence * 100, 2)}%"

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

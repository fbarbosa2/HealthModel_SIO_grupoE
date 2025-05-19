from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

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
        sore_throat = 1 if data['sore_throat'] == 'Yes' else 0
        chest_pain = 1 if data['chest_pain'] == 'Yes' else 0
        skin_rash = 1 if data['skin_rash'] == 'Yes' else 0
        nausea = 1 if data['nausea'] == 'Yes' else 0
        muscle_pain = 1 if data['muscle_pain'] == 'Yes' else 0
        loss_of_appetite = 1 if data['loss_of_appetite'] == 'Yes' else 0
        dizziness = 1 if data['dizziness'] == 'Yes' else 0

        input_data = [[fever, cough, fatigue, breathing, age, gender, bp, cholesterol, sore_throat, chest_pain, skin_rash, nausea, muscle_pain, loss_of_appetite, dizziness,0]]

        prediction = rf_model.predict(input_data)[0]
        confidence = rf_model.predict_proba(input_data)[0][prediction]
        predicted_disease = labelEncoder.inverse_transform([prediction])[0]

        probs = rf_model.predict_proba(input_data)[0]  # vetor de probabilidades para cada classe
        top3_indices = np.argsort(probs)[-3:][::-1]        # índices das 3 classes com maior probabilidade

        top_predicted_diseases = labelEncoder.inverse_transform(top3_indices)  # nomes das doenças
        top_confidences = probs[top3_indices]                                   # probabilidades associadas

        frase = ""
        i = 1
        for disease, confidence in zip(top_predicted_diseases, top_confidences):
            frase += f"{i}º {disease}\n"
            i += 1
        
        result = f"Possiveis Doenças:\n{frase}"

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

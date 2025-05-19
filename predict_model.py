import joblib
import numpy as np

#Para carregar o modelo e o encoder guardados
disease_tree = joblib.load('disease_tree_model.pkl')
labelEncoder = joblib.load('label_encoder.pkl')

def predict(fever, cough, fatigue, breathing, age, gender, bp, cholesterol):
    fever = 1 if fever == 'Yes' else 0
    cough = 1 if cough == 'Yes' else 0
    fatigue = 1 if fatigue == 'Yes' else 0
    breathing = 1 if breathing == 'Yes' else 0
    gender = 1 if gender == 'Female' else 0
    bp = 1 if bp == 'Normal' else 0
    cholesterol_map = {'Low': 0, 'Normal': 1, 'High': 2}
    cholesterol = cholesterol_map.get(cholesterol, 1)  # valor por defeito: Normal

    input_data = [[fever, cough, fatigue, breathing, age, gender, bp, cholesterol, 0]]

    prediction = disease_tree.predict(input_data)[0]
    probs = disease_tree.predict_proba(input_data)[0]
    confidence = probs[prediction]

    predicted_disease = labelEncoder.inverse_transform([prediction])[0]


    probs = disease_tree.predict_proba(input_data)[0]  # vetor de probabilidades para cada classe
    top3_indices = np.argsort(probs)[-3:][::-1]        # índices das 3 classes com maior probabilidade

    top_predicted_diseases = labelEncoder.inverse_transform(top3_indices)  # nomes das doenças
    top_confidences = probs[top3_indices]                                   # probabilidades associadas

    frase = None
    for disease, confidence in zip(top_predicted_diseases, top_confidences):
        frase += "Doença: {disease}, Confiança: {confidence:.2f}\n"

    return predicted_disease + " Percentagem de Certeza: " + str(confidence) + "%\n" + frase


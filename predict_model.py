import joblib
import pandas as pd

#Para carregar o modelo e o encoder guardados
disease_tree = joblib.load('disease_tree_model.pkl')
labelEncoder = joblib.load('label_encoder.pkl')
df = pd.read_csv("datasets/Disease_and_symptoms_dataset_COMPLEX.csv")

def predict_complex(sintomas_paciente):

    sintomas = df.columns[1:]
    input_data = [[1 if sintoma in sintomas_paciente else 0 for sintoma in sintomas]]

    prediction = disease_tree.predict(input_data)[0]
    probs = disease_tree.predict_proba(input_data)[0]
    confidence = probs[prediction]

    # Traduz para o nome original da doença
    predicted_disease = labelEncoder.inverse_transform([prediction])[0]

    print(f"Doença prevista: {predicted_disease}")
    print(f"Percentagem de certeza: {(confidence * 100):.2f}")

def predict_simple(fever, cough, fatigue, breathing, age, gender, bp, cholesterol):
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


    return predicted_disease + " Percentagem de Certeza: " + str(confidence * 100) + "%"


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# Definir se usar dataset complexo
datasetComplex = True

labelEncoder = LabelEncoder()

# === Leitura e pré-processamento ===
if datasetComplex:
    dataset = pd.read_csv('datasets/Disease and symptoms dataset.csv')
    dataset['diseases'] = labelEncoder.fit_transform(dataset['diseases'])
    X = dataset.iloc[:, 1:].values
    Y = dataset['diseases']
    feature_names = dataset.columns[1:]

else:
    dataset = pd.read_csv('datasets/Disease_symptom_and_patient_profile_dataset.csv')

    dataset['Disease'] = labelEncoder.fit_transform(dataset['Disease'])
    dataset['Fever'] = np.where(dataset['Fever'] == 'Yes', 1, 0)
    dataset['Cough'] = np.where(dataset['Cough'] == 'Yes', 1, 0)
    dataset['Fatigue'] = np.where(dataset['Fatigue'] == 'Yes', 1, 0)
    dataset['Difficulty Breathing'] = np.where(dataset['Difficulty Breathing'] == 'Yes', 1, 0)
    dataset['Gender'] = np.where(dataset['Gender'] == 'Female', 1, 0)
    dataset['Blood Pressure'] = np.where(dataset['Blood Pressure'] == 'Normal', 1, 0)
    cholesterol_map = {'Low': 0, 'Normal': 1, 'High': 2}
    dataset['Cholesterol Level'] = dataset['Cholesterol Level'].map(cholesterol_map)
    dataset['Outcome Variable'] = np.where(dataset['Outcome Variable'] == 'Positive', 1, 0)

    X = dataset.iloc[:, 1:].values
    Y = dataset['Disease']
    feature_names = dataset.columns[1:]

# === Divisão treino/teste ===
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# === Modelo: Random Forest ===
rf_model = RandomForestClassifier(n_estimators=10, random_state=42)
rf_model.fit(X_train, Y_train)
Y_pred = rf_model.predict(X_test)

# === Avaliação ===
print("=== Random Forest ===")
print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))

# === Visualização da importância dos atributos ===
importances = rf_model.feature_importances_
plt.figure(figsize=(12, 6))
sns.barplot(x=importances, y=feature_names)
plt.title("Importância dos Atributos (Random Forest)")
plt.tight_layout()
plt.show()

# === Guardar modelo e encoder ===
joblib.dump(rf_model, 'disease_rf_model.pkl')
joblib.dump(labelEncoder, 'label_encoder.pkl')

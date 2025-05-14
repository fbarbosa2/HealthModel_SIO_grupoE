from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import joblib

# Carregar dataset
dataset = pd.read_csv('balanced_disease_dataset.csv')

# Codificar variáveis categóricas
labelEncoder = LabelEncoder()
dataset['Disease'] = labelEncoder.fit_transform(dataset['Disease'])
#print(labelEncoder.classes_)

dataset['Fever'] = np.where(dataset['Fever'] == 'Yes', 1, 0) #Yes 1 / No 0
dataset['Cough'] = np.where(dataset['Cough'] == 'Yes', 1, 0) #Yes 1 / No 0
dataset['Fatigue'] = np.where(dataset['Fatigue'] == 'Yes', 1, 0) #Yes 1 / No 0
dataset['Difficulty Breathing'] = np.where(dataset['Difficulty Breathing'] == 'Yes', 1, 0) #Yes 1 / No 0
dataset['Gender'] = np.where(dataset['Gender'] == 'Female', 1, 0) #Female 1 / Male 0
dataset['Blood Pressure'] = np.where(dataset['Blood Pressure'] == 'Normal', 1, 0) #Normal 1 / Low 0
dataset['Sore Throat'] = np.where(dataset['Sore Throat'] == 'Yes', 1, 0) #Yes 1 / No 0
dataset['Chest Pain'] = np.where(dataset['Chest Pain'] == 'Yes', 1, 0) #Yes 1 / No 0
dataset['Skin Rash'] = np.where(dataset['Skin Rash'] == 'Yes', 1, 0) #Yes 1 / No 0
dataset['Nausea or Vomiting'] = np.where(dataset['Nausea or Vomiting'] == 'Yes', 1, 0) #Yes 1 / No 0
dataset['Muscle Pain'] = np.where(dataset['Muscle Pain'] == 'Yes', 1, 0) #Yes 1 / No 0
dataset['Loss of Appetite'] = np.where(dataset['Loss of Appetite'] == 'Yes', 1, 0) #Yes 1 / No 0
dataset['Dizziness'] = np.where(dataset['Dizziness'] == 'Yes', 1, 0) #Yes 1 / No 0

cholesterol_map = {'Low': 0, 'Normal': 1, 'High': 2}
dataset['Cholesterol Level'] = dataset['Cholesterol Level'].map(cholesterol_map)

dataset['Outcome Variable'] = np.where(dataset['Outcome Variable'] == 'Positive', 1, 0) #Positive 1 / Negative 0

X = dataset.iloc[:, 1:].values
Y = dataset['Disease']


# Treino/teste split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Modelo
rf_model = RandomForestClassifier(n_estimators=30, random_state=42)
rf_model.fit(X_train, y_train)

# Avaliação
y_pred = rf_model.predict(X_test)
print(f"Acuracy: {accuracy_score(y_test, y_pred):.2f}")

# Salvar modelo e encoder
joblib.dump(rf_model, 'disease_rf_model.pkl')
joblib.dump(labelEncoder, 'label_encoder.pkl')
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import joblib

# Carregar dataset
df = pd.read_csv('balanced_disease_dataset.csv')

# Codificar variáveis categóricas
labelEncoder = LabelEncoder()
df['Disease'] = labelEncoder.fit_transform(df['Disease'])
df['Fever'] = (df['Fever'] == 'Yes').astype(int)
df['Cough'] = (df['Cough'] == 'Yes').astype(int)
df['Fatigue'] = (df['Fatigue'] == 'Yes').astype(int)
df['Difficulty Breathing'] = (df['Difficulty Breathing'] == 'Yes').astype(int)
df['Gender'] = (df['Gender'] == 'Female').astype(int)
df['Blood Pressure'] = (df['Blood Pressure'] == 'Normal').astype(int)
df['Cholesterol Level'] = df['Cholesterol Level'].map({'Low': 0, 'Normal': 1, 'High': 2})
df['Outcome Variable'] = (df['Outcome Variable'] == 'Positive').astype(int)

# Features e target
features = df.columns[df.columns != 'Disease']
X = df[features]
y = df['Disease']

# Treino/teste split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo
rf_model = RandomForestClassifier(n_estimators=30, random_state=42)
rf_model.fit(X_train, y_train)

# Avaliação
y_pred = rf_model.predict(X_test)
print(f"Acuracy: {accuracy_score(y_test, y_pred):.2f}")

# Salvar modelo e encoder
joblib.dump(rf_model, 'disease_rf_model.pkl')
joblib.dump(labelEncoder, 'label_encoder.pkl')
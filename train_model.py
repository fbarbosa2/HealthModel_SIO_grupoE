#import kagglehub
import graphviz
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.tree import export_graphviz
import joblib

# Download latest version
#path = kagglehub.dataset_download("uom190346a/disease-symptoms-and-patient-profile-dataset")

#print("Path to dataset files:", path)
#Change this to use the simpler or the more complex dataset
datasetComplex = True

labelEncoder = LabelEncoder()
X = None
Y = None

if(datasetComplex):
    dataset = pd.read_csv('datasets/Disease_and_symptoms_dataset_COMPLEX.csv')

    dataset['diseases'] = labelEncoder.fit_transform(dataset['diseases'])
    #print(labelEncoder.classes_)
    X = dataset.iloc[:, 1:].values
    Y = dataset['diseases']

    disease_tree = tree.DecisionTreeClassifier()
    disease_tree.fit(X, Y)

else:
    dataset = pd.read_csv('datasets/Disease_symptom_and_patient_profile_dataset.csv')

    #Disease,Fever,Cough,Fatigue,Difficulty Breathing,Age,Gender,Blood Pressure,Cholesterol Level,Outcome Variable

    """Conversão dos dados em numéricos para o scikit-learn"""

    dataset['Disease'] = labelEncoder.fit_transform(dataset['Disease'])
    #print(labelEncoder.classes_)

    dataset['Fever'] = np.where(dataset['Fever'] == 'Yes', 1, 0) #Yes 1 / No 0
    dataset['Cough'] = np.where(dataset['Cough'] == 'Yes', 1, 0) #Yes 1 / No 0
    dataset['Fatigue'] = np.where(dataset['Fatigue'] == 'Yes', 1, 0) #Yes 1 / No 0
    dataset['Difficulty Breathing'] = np.where(dataset['Difficulty Breathing'] == 'Yes', 1, 0) #Yes 1 / No 0
    dataset['Gender'] = np.where(dataset['Gender'] == 'Female', 1, 0) #Female 1 / Male 0
    dataset['Blood Pressure'] = np.where(dataset['Blood Pressure'] == 'Normal', 1, 0) #Normal 1 / Low 0

    cholesterol_map = {'Low': 0, 'Normal': 1, 'High': 2}
    dataset['Cholesterol Level'] = dataset['Cholesterol Level'].map(cholesterol_map)

    dataset['Outcome Variable'] = np.where(dataset['Outcome Variable'] == 'Positive', 1, 0) #Positive 1 / Negative 0

    X = dataset.iloc[:, 1:].values
    Y = dataset['Disease']

    disease_tree = tree.DecisionTreeClassifier()
    disease_tree.fit(X, Y)

#Saves the tree and the encoder for future use
joblib.dump(disease_tree, 'disease_tree_model.pkl')
joblib.dump(labelEncoder, 'label_encoder.pkl')

"""
print(tree.export_text(disease_tree))

# Exportar a árvore para o formato DOT
dot_data = export_graphviz(
    disease_tree,
    out_file=None,
    feature_names=dataset.columns[1:],  # Exclui 'Disease'
    class_names=[str(cls) for cls in labelEncoder.classes_],  # nomes das doenças
    filled=True,
    rounded=True,
    special_characters=True
)

# Mostrar com graphviz
graph = graphviz.Source(dot_data)
graph.render("disease_tree", format="png", cleanup=True)  # Cria o ficheiro disease_tree.png
graph.view()
"""


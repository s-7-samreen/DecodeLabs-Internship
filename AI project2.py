from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

print(df.head())
print(df.info())
print(df['species'].value_counts())

X = df.drop('species', axis=1)
y = df['species']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("Training data size:", X_train.shape)
print("Testing data size:", X_test.shape)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Model banao aur train karo
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Test data pe predict karo
predictions = model.predict(X_test)

# Result check karo
print("\nAccuracy:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))
# Naye/custom phool ka test
new_flower = [[5.0, 3.4, 1.5, 0.2]]  # sepal_length, sepal_width, petal_length, petal_width
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)

species_names = ['Setosa', 'Versicolor', 'Virginica']
print("\nPredicted species for new flower:", species_names[prediction[0]])
# Project 2: Data Classification Using AI
### DecodeLabs — Artificial Intelligence Internship (Batch 2026)

A supervised-learning classification project that predicts the species of an Iris flower from its measurements, using the K-Nearest Neighbors (KNN) algorithm.

---

## 📌 Objective

Build a basic classification model using a small dataset. This project covers the full pipeline of supervised learning:
- Loading and understanding a dataset
- Splitting data into training and testing sets
- Applying a classification algorithm
- Evaluating the model's performance

---

## 🛠️ Tools & Environment

| Component | Details |
|---|---|
| Language | Python 3.14 |
| Editor | Visual Studio Code |
| Libraries | `scikit-learn`, `pandas` |
| Dataset | Iris Dataset (built-in, via `scikit-learn`) |

---

## 📊 Dataset

The **Iris dataset** contains 150 samples, evenly split across 3 species:

- Setosa (50 samples)
- Versicolor (50 samples)
- Virginica (50 samples)

Each sample has 4 features:
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

---

## 🚀 Step 1 — Loading and Understanding the Dataset

```python
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

print(df.head())
print(df.info())
print(df['species'].value_counts())
```

**Output:**
```
150 entries, 5 columns (4 features + species)
dtypes: float64(4), int64(1)
species   0: 50   1: 50   2: 50   (balanced dataset)
```

📷 **Screenshot:**
![Step 1 Output](screenshots/step1_dataset.png)<img width="1366" height="768" alt="A" src="https://github.com/user-attachments/assets/3461ea93-de91-4ebd-bc9c-3412925e7ac0" />







## 🚀 Step 2 — Feature Scaling & Train-Test Split

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = df.drop('species', axis=1)
y = df['species']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print('Training data size:', X_train.shape)
print('Testing data size:', X_test.shape)
```

**Output:**
```
Training data size: (120, 4)
Testing data size:  (30, 4)
```

📷 **Screenshot:**
![Step 2 Output](screenshots/step2_split.png)
                     
<img width="1366" height="768" alt="A" src="https://github.com/user-attachments/assets/0056167c-5ac8-4bfa-8598-24913f39f6da" />

---

## 🚀 Step 3 — Model Training with K-Nearest Neighbors (KNN)

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print('Accuracy:', accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
```

📷 **Screenshot:**
![Step 3 Output](screenshots/step3_accuracy.png)

<img width="1366" height="768" alt="AI" src="https://github.com/user-attachments/assets/a7d9d8a9-345f-4bcb-82fd-74c08b633ef5" />


## 🎁 Bonus — Prediction on New/Custom Data

```python
new_flower = [[5.0, 3.4, 1.5, 0.2]]
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)

species_names = ['Setosa', 'Versicolor', 'Virginica']
print('Predicted species:', species_names[prediction[0]])
```

📷 **Screenshot:**
![Bonus Output](screenshots/bonus_prediction.png)
<img width="768" height="1366" alt="I" src="https://github.com/user-attachments/assets/785024b9-23f6-46d9-a76e-fb40713da76e" />


---

## 🧩 Pipeline Summary

| Stage | Detail |
|---|---|
| Input | Iris dataset — 150 samples, 4 features, 3 classes |
| Preprocessing | `StandardScaler` for feature normalization |
| Split | 80% training (120 samples) / 20% testing (30 samples) |
| Algorithm | K-Nearest Neighbors (k = 5) |
| Evaluation | Accuracy score, Confusion Matrix, Classification Report |
| Validation | Successful prediction on a new, custom data point |

---

## ✅ Conclusion

This project demonstrates a complete, working supervised-learning pipeline — from raw data to a trained, evaluated classification model. All required deliverables were successfully implemented and tested without errors, fulfilling the requirements of Project 2.

---

## 📁 Repository Structure

```
Project2-AI/
│
├── AI dataset.py          # Main Python script (full pipeline)
├── README.md               # This documentation
└── screenshots/            # Output screenshots
    ├── step1_dataset.png
    ├── step2_split.png
    ├── step3_accuracy.png
    └── bonus_prediction.png
```

---

**Intern:** Samreen
**Batch:** 2026 | Powered by DecodeLabs

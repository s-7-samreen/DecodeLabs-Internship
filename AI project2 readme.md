# Iris Flower Species Classification (KNN)

## Description
This project is a Machine Learning classification model that predicts the species of an Iris flower based on its physical measurements (sepal length, sepal width, petal length, petal width).

It uses the classic **Iris dataset** (built into scikit-learn) and trains a **K-Nearest Neighbors (KNN)** classifier to distinguish between three species:
- Setosa
- Versicolor
- Virginica

### What the script does
1. Loads the Iris dataset using `sklearn.datasets.load_iris()`
2. Converts it into a pandas DataFrame and explores it (`head()`, `info()`, `value_counts()`)
3. Splits features (`X`) and target labels (`y`)
4. Scales the features using `StandardScaler`
5. Splits the data into training (80%) and testing (20%) sets
6. Trains a `KNeighborsClassifier` (k=5) on the training data
7. Evaluates the model on test data using:
   - Accuracy Score
   - Confusion Matrix
   - Classification Report
8. Predicts the species of a new, custom flower sample based on user-defined measurements

## Requirements
- Python 3.x
- pandas
- scikit-learn

Install dependencies (if not already installed):
```bash
pip install pandas scikit-learn
```

## How to Run
1. Open a terminal and navigate to the project folder:
```bash
cd "C:\Users\w10\Desktop\DecodeLabs-Internship\AI project2"
```

2. Run the script:
```bash
python "AI project2.py"
```

## Sample Output
```
Training data size: (120, 4)
Testing data size: (30, 4)

Accuracy: 1.0

Confusion Matrix:
 [[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]

Predicted species for new flower: Setosa
```

## Notes
- The model achieves 100% accuracy on this test split, which is common for the Iris dataset due to its small size and clear class separation.
- To predict a different flower, edit the `new_flower` list in the script with your own sepal/petal measurements.

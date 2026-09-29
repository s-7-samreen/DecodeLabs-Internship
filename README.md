# DecodeLabs Internship — AI Track Projects

**Industrial Training Kit | Artificial Intelligence Track**

This repository contains four progressive AI/ML projects completed as part of the DecodeLabs Internship program. Each project explores a different area of Artificial Intelligence — from rule-based logic and supervised machine learning to NLP-based recommendation systems and computer vision (OCR).

---

## 📋 Table of Contents
1. [Project 1 — Rule-Based AI Chatbot](#project-1--rule-based-ai-chatbot)
2. [Project 2 — Iris Flower Species Classification (KNN)](#project-2--iris-flower-species-classification-knn)
3. [Project 3 — Tech Stack Recommender](#project-3--tech-stack-recommender)
4. [Project 4 — Image / Text Recognition (OCR)](#project-4--image--text-recognition-ocr)
5. [Overall Tech Stack](#overall-tech-stack)
6. [General Setup](#general-setup)

---

## Project 1 — Rule-Based AI Chatbot

### Description
A simple rule-based chatbot built in Python that uses `if-else` logic to match predefined user inputs and generate appropriate responses. It runs in a continuous loop in the terminal, allowing back-and-forth conversation until the user exits.

**Capabilities:**
- Greets the user (`hi`, `hello`, `hey`, `salam`, etc.)
- Responds to casual questions like *"how are you"*
- States its name and purpose when asked
- Explains its capabilities (`help`)
- Responds to thanks (`thank you`, `shukriya`)
- Ends the conversation on exit commands (`bye`, `exit`, `quit`, `goodbye`, `khuda hafiz`)

### Tech Stack
- Python 3

### How to Run
```bash
cd path\to\project1-folder
python chatbot.py
```

### Sample Interaction
```
=== Rule-Based AI Chatbot ===
You: Hi
Bot: Hello! How can I help you today?
You: What's your name?
Bot: My name is ChatBuddy!
You: bye
Bot: Goodbye! Have a great day. 👋
```

### Project Files
| File | Purpose |
|------|---------|
| `chatbot.py` | Main chatbot logic and terminal interface |

---

## Project 2 — Iris Flower Species Classification (KNN)

### Description
A supervised Machine Learning project that predicts the species of an Iris flower (**Setosa**, **Versicolor**, **Virginica**) based on its physical measurements (sepal length, sepal width, petal length, petal width), using the classic Iris dataset and a **K-Nearest Neighbors (KNN)** classifier.

### Pipeline
1. Loads the Iris dataset via `sklearn.datasets.load_iris()`
2. Converts it into a pandas DataFrame and explores it (`head()`, `info()`, `value_counts()`)
3. Splits features (`X`) and target labels (`y`)
4. Scales features using `StandardScaler`
5. Splits data into training (80%) and testing (20%) sets
6. Trains a `KNeighborsClassifier` (k=5)
7. Evaluates the model using Accuracy Score, Confusion Matrix, and Classification Report
8. Predicts the species of a new, custom flower sample

### Tech Stack
- Python 3.x
- pandas
- scikit-learn

### How to Run
```bash
pip install pandas scikit-learn
cd path\to\project2-folder
python "AI project2.py"
```

### Sample Output
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

> **Note:** 100% accuracy is expected on this dataset due to its small size and well-separated classes.

---

## Project 3 — Tech Stack Recommender

### Description
Recommends the most suitable job role based on a user's entered skills, using **TF-IDF (Term Frequency–Inverse Document Frequency)** and **Cosine Similarity**. It compares user-entered skills against a dataset of job roles (Data Scientist, DevOps Engineer, Backend Developer, Cloud Architect, Frontend Developer, Data Analyst) and returns the top 3 best-matching roles.

### How It Works
1. A dataset of job roles and required skills is created and stored in `raw_skills.csv`
2. Each job role's skills are vectorized using `TfidfVectorizer`
3. The user enters their own skills
4. User skills are transformed using the same vectorizer
5. Cosine similarity is calculated between the user's vector and each job role's vector
6. Job roles are ranked by similarity score; the top 3 are displayed

### Tech Stack
- Python
- pandas
- scikit-learn (`TfidfVectorizer`, `cosine_similarity`)

### How to Run
```bash
pip install pandas scikit-learn
python recommender.py
```
When prompted, enter 3 skills separated by commas:
```
Python, Cloud Computing, Automation
```

### Sample Output
```
--- Top Recommendations ---
          job_role  similarity
3  Cloud Architect    0.XX
1  DevOps Engineer    0.XX
0  Data Scientist     0.XX
```

---

## Project 4 — Image / Text Recognition (OCR)

### Description
Implements a basic **text recognition (OCR)** pipeline using a pre-trained OCR engine. The script loads a sample image containing text, pre-processes it, extracts the text, benchmarks recognition accuracy, and generates a visual output showing which words were detected and where.

### Pipeline
1. Loads a sample image (`sample.jpg`)
2. Pre-processes the image using OpenCV — grayscale conversion + adaptive thresholding
3. Runs OCR using **pytesseract** (Tesseract OCR wrapper) to extract text
4. Benchmarks accuracy by calculating the average confidence score, validated against a minimum threshold of **80%**
5. Generates a visual output (`output_annotated.jpg`) with bounding boxes and labels around each recognized word

### Tech Stack
- `pytesseract` — OCR engine wrapper
- `opencv-python (cv2)` — image processing and annotation
- Tesseract OCR engine (system-level install)

### How to Run
```bash
python -m pip install pytesseract pillow opencv-python
```
Install the Tesseract OCR engine separately: https://github.com/UB-Mannheim/tesseract/wiki

```bash
python text_recognizer.py
```

### Project Files
| File | Purpose |
|------|---------|
| `text_recognizer.py` | Main script — runs the full OCR pipeline |
| `sample.jpg` | Input image containing text |
| `output_annotated.jpg` | Output image with bounding boxes (generated on run) |

### Result
- **Average Confidence Score:** 82.91%
- **Accuracy Benchmark:** PASS (≥ 80%)
- **Visual Confirmation:** Generated successfully (`output_annotated.jpg`)

---

## Overall Tech Stack
- **Language:** Python 3
- **Libraries:** pandas, scikit-learn, OpenCV (cv2), pytesseract, Pillow
- **Engine:** Tesseract OCR
- **Concepts covered:** Rule-based logic, supervised classification (KNN), NLP-based recommendation (TF-IDF + Cosine Similarity), computer vision (OCR)

## General Setup
1. Ensure Python 3.x is installed:
   ```bash
   python --version
   ```
2. Navigate to the respective project folder before running any script.
3. Install each project's required libraries as listed in its section above.

---

**Author:** DecodeLabs Internship — AI Track (Projects 1–4)

# AI Project 3 — Tech Stack Recommender

A simple AI-based recommendation system that matches a user's skills to the most relevant job roles using **Content-Based Filtering** (TF-IDF + Cosine Similarity).

Built as part of the **DecodeLabs Artificial Intelligence Industrial Training Kit**.

---

## 📌 What It Does

- Takes at least 3 skills as input from the user (e.g., `Python, Cloud Computing, Automation`)
- Converts skills into numerical vectors using **TF-IDF**
- Compares the user's skill vector against a dataset of job roles using **Cosine Similarity**
- Returns the **Top 3** best-matching job roles, ranked by similarity score

---

## 🗂️ Files

| File | Description |
|---|---|
| `recommender.py` | Main Python script — runs the full recommendation pipeline |
| `raw_skills.csv` | Dataset mapping job roles to their required skills |
| `Project3_Documentation.docx` | Full project write-up: objective, methodology, results |

---

## ⚙️ How It Works (Pipeline)

1. **Ingestion** — User enters skills via terminal input
2. **Vectorization** — Skills are converted into TF-IDF weighted vectors
3. **Scoring** — Cosine Similarity is calculated between the user vector and every job role vector
4. **Sorting** — Job roles are ranked by similarity score (highest first)
5. **Filtering** — Only the Top 3 matches are shown to avoid choice overload

---

## 🧠 Techniques Used

- **TF-IDF (Term Frequency–Inverse Document Frequency)** — weights specific/rare skills higher than generic ones
- **Cosine Similarity** — measures the angle between vectors, independent of their length, giving a clean 0–1 match score

---

## ▶️ How to Run

Install dependencies:
```bash
python -m pip install pandas scikit-learn
```

Run the script:
```bash
python recommender.py
```

Enter your skills when prompted, comma-separated:
```
Apni 3 skills enter karo (comma se alag kar ke):
Example: Python, Cloud Computing, Automation
> Python, Cloud Computing, Automation
```

---

## ✅ Sample Output

**Input:** `Python, Cloud Computing, Automation`

| Job Role | Similarity Score | Match % |
|---|---|---|
| Cloud Architect | 0.6511 | 65.1% |
| DevOps Engineer | 0.1638 | 16.4% |
| Backend Developer | 0.1357 | 13.6% |

**Input:** `JavaScript, React, CSS`

Top Match: **Frontend Developer** — 70.7% similarity

---

## ⚠️ Notes & Limitations

- Matching is **keyword-based** — skills must be spelled correctly to match the dataset vocabulary (e.g., "python", not "pyhton")
- **Cold Start Problem**: if input skills don't overlap with any dataset vocabulary, all similarity scores will be near 0
- Future improvements could include fuzzy matching, synonym handling, and a larger job-role dataset

---

## 👤 Program

DecodeLabs — Artificial Intelligence Industrial Training Kit (Batch 2026)

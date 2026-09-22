 import pandas as pd

# Sample dataset: job roles aur unki required skills
data = {
    "job_role": [
        "Data Scientist",
        "DevOps Engineer",
        "Backend Developer",
        "Cloud Architect",
        "Frontend Developer",
        "Data Analyst"
    ],
    "skills": [
        "Python, SQL, Machine Learning, Data Analysis, Statistics",
        "AWS, Docker, Kubernetes, CI/CD, Automation",
        "Java, Python, SQL, APIs, Git",
        "AWS, Cloud Computing, Automation, Security, Networking",
        "JavaScript, React, HTML, CSS, UI/UX",
        "Python, SQL, Excel, Data Visualizatison, Statistics"
    ]
}

df = pd.DataFrame(data)
df.to_csv("raw_skills.csv", index=False)

print(df)
from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF vectorizer banao
vectorizer = TfidfVectorizer()

# Har job role ki skills ko numbers (vectors) mein convert karo
skill_vectors = vectorizer.fit_transform(df["skills"])

# Dekho kaunse unique words (features) mile
print("\nUnique Skills Found:")
print(vectorizer.get_feature_names_out())

print("\nVector Shape:", skill_vectors.shape)
from sklearn.metrics.pairwise import cosine_similarity

print("\nApni 3 skills enter karo (comma se alag kar ke):")
user_input_raw = input("Example: Python, Cloud Computing, Automation\n> ")

# User ke input ko list mein todo
user_skills = [skill.strip() for skill in user_input_raw.split(",")]
user_input = [", ".join(user_skills)]  # ek string mein convert karo

# User ki skills ko usi vectorizer se transform karo (fit nahi, sirf transform)
user_vector = vectorizer.transform(user_input)

# User vector ko har job role ke vector se compare karo
similarity_scores = cosine_similarity(user_vector, skill_vectors)

# Scores ko job roles ke sath jodo
df["similarity"] = similarity_scores[0]

# Highest score wale upar layo
recommendations = df.sort_values(by="similarity", ascending=False)

print("\n--- Top Recommendations ---")
print(recommendations[["job_role", "similarity"]].head(3))

# Project 3: Tech Stack Recommender

## Description
This project recommends the most suitable job role based on a user's skills using **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity**. It compares the user's entered skills against a dataset of job roles (Data Scientist, DevOps Engineer, Backend Developer, Cloud Architect, Frontend Developer, Data Analyst) and their required skill sets, then returns the top 3 best-matching job roles.

## How It Works
1. A sample dataset of job roles and their required skills is created and saved to `raw_skills.csv`.
2. Each job role's skills are converted into numerical vectors using `TfidfVectorizer`.
3. The user enters their own skills as input.
4. The user's skills are transformed into a vector using the same vectorizer.
5. Cosine similarity is calculated between the user's skill vector and each job role's skill vector.
6. The job roles are ranked by similarity score, and the top 3 recommendations are displayed.

## Tech Stack
- Python
- pandas
- scikit-learn (`TfidfVectorizer`, `cosine_similarity`)

## How to Run
1. Make sure Python is installed on your system.
2. Install the required libraries:
   ```
   pip install pandas scikit-learn
   ```
3. Run the script:
   ```
   python recommender.py
   ```
4. When prompted, enter 3 skills separated by commas, for example:
   ```
   Python, Cloud Computing, Automation
   ```
5. The program will display the top 3 recommended job roles based on your skills.

## Example Output
```
Apni 3 skills enter karo (comma se alag kar ke):
Example: Python, Cloud Computing, Automation
> Python, Cloud Computing, Automation

--- Top Recommendations ---
          job_role  similarity
3  Cloud Architect    0.XX
1  DevOps Engineer    0.XX
0  Data Scientist     0.XX
```

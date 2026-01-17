import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text.lower()

def match_resume_to_job(resume_text, job_desc):
    resume_text = clean_text(resume_text)
    job_desc = clean_text(job_desc)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    score = similarity[0][0] * 100

    return round(score, 2)

from rag.qa import InterviewQA


class JDMatchService:

    def __init__(self):
        self.qa = InterviewQA()

    def analyze(self, job_description):

        prompt = f"""
You are an expert ATS (Applicant Tracking System) evaluator.

The uploaded resume has already been provided as context.

Compare the uploaded resume against the following Job Description.

Job Description:

{job_description}

Generate a professional report.

Include exactly these sections:

Overall Match Score (%)

Matching Skills

Missing Skills

Strengths

Weaknesses

Resume Improvement Suggestions

Interview Questions likely for this Job Description

Do NOT invent resume information.

Base everything only on the uploaded resume and the provided Job Description.

Keep the report under 600 words.
"""

        return self.qa.chat(prompt)
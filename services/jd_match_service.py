from rag.qa import InterviewQA


class JDMatchService:

    def __init__(self):
        self.qa = None

    def get_qa(self):
        if self.qa is None:
            self.qa = InterviewQA()
        return self.qa

    def analyze(self, job_description):

        qa = self.get_qa()

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

        return qa.chat(prompt)
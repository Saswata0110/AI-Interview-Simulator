from rag.qa import InterviewQA


class ResumeService:

    def __init__(self):

        self.qa = InterviewQA()

    def analyze_resume(self):

        prompt = """
You are an ATS Resume Analyzer.

Analyze ONLY the uploaded resume.

Return exactly in this format.

ATS Score: XX/100

Strengths
- ...

Weaknesses
- ...

Missing Skills
- ...

Suggestions
- ...

Keep everything under 350 words.

Do not invent information.

Use only the resume context.
"""

        return self.qa.ask(prompt)
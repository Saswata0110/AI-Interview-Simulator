from rag.qa import InterviewQA


class InterviewService:

    def __init__(self):

        self.qa = InterviewQA()

    # ------------------------------------
    # Generate Interview Questions
    # ------------------------------------
    def generate_questions(self):

        prompt = """
You are a Senior Software Engineer interviewer.

Generate exactly 10 interview questions based ONLY on the uploaded resume.

Rules:

- Ask only resume-related questions.
- Mix technical, project and behavioral questions.
- One question per line.
- No numbering.
- No bullets.
- Return only questions.
"""

        result = self.qa.ask(prompt)

        questions = []

        for line in result.split("\n"):

            line = line.strip()

            if line:
                questions.append(line)

        return questions[:10]

    # ------------------------------------
    # Final Interview Report
    # ------------------------------------
    def final_report(self, questions, answers):

        interview = ""

        for i, (q, a) in enumerate(zip(questions, answers), start=1):

            interview += f"""
Question {i}
{q}

Candidate Answer
{a}

"""

        prompt = f"""
You are a Senior Software Engineer interviewer.

Below is the complete interview.

{interview}

Evaluate ONLY the candidate's answers.

Generate the report in exactly this format.

==================================================

OVERALL SCORE: XX/100

==================================================

Question-wise Evaluation

Question 1
Score: X/10
Feedback:

Question 2
Score: X/10
Feedback:

Continue for all questions.

==================================================

Technical Knowledge:
/10

Communication:
/10

Confidence:
/10

Problem Solving:
/10

==================================================

Strengths

- ...

Weaknesses

- ...

Topics to Improve

- ...

Final Recommendation

Hire / Borderline / Not Ready

Important Rules:

- Do NOT invent technologies.
- Do NOT invent projects.
- Evaluate only the provided answers.
- Keep the report under 700 words.
"""

        return self.qa.chat(prompt)
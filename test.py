from services.resume_parser import ResumeParser

parser = ResumeParser("uploads/resumes/sample_resume.pdf")

text = parser.extract_text()

print(text)
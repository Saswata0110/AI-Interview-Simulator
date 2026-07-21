from flask import Blueprint, render_template, session, redirect

from services.resume_service import ResumeService

resume_analysis = Blueprint(
    "resume_analysis",
    __name__
)


@resume_analysis.route("/resume_analysis")
def analyze_resume():

    if "user_id" not in session:
        return redirect("/login")

    service = ResumeService()

    report = service.analyze_resume()

    return render_template(
        "resume_analysis.html",
        report=report
    )
import os

from flask import (
    Blueprint,
    render_template,
    jsonify,
    request,
    session,
    redirect,
    url_for,
    Response,
    send_file,
    flash
)

from services.interview_service import InterviewService
from models.interview_history import InterviewHistory
from utils.pdf_report import create_pdf


# ==========================================
# Blueprint
# ==========================================

interview = Blueprint("interview", __name__)

service = InterviewService()



# ==========================================
# Interview Page
# ==========================================

@interview.route("/start_interview")
def start_interview():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("interview.html")


# ==========================================
# Generate Interview Questions
# ==========================================

@interview.route("/generate_questions")
def generate_questions():

    questions = service.generate_questions()

    session["questions"] = questions

    return jsonify(questions)


# ==========================================
# Evaluate Answer
# ==========================================

@interview.route(
    "/evaluate_answer",
    methods=["POST"]
)
def evaluate_answer():

    data = request.get_json()

    question = data.get("question")

    answer = data.get("answer")

    feedback = service.evaluate_answer(

        question,

        answer

    )

    return feedback


# ==========================================
# Final Report
# ==========================================

@interview.route(
    "/final_report",
    methods=["POST"]
)
def final_report():

    data = request.get_json()

    questions = data.get("questions", [])

    answers = data.get("answers", [])

    report = service.final_report(

        questions,

        answers

    )

    # ==========================================
    # Extract Score
    # ==========================================

    import re

    score = 0

    match = re.search(
        r"(\d+)\s*/\s*100",
        report
    )

    if match:

        score = int(match.group(1))

    # ==========================================
    # Save Report in Session
    # ==========================================

    session["final_report"] = report

    session["final_score"] = score

    session["total_questions"] = len(questions)

    session["answered_questions"] = len(

        [a for a in answers if a.strip()]

    )

    # ==========================================
    # Generate PDF
    # ==========================================

    if "user_id" in session:

        pdf_filename = (
            f"interview_report_user_{session['user_id']}.pdf"
        )

        pdf_path = create_pdf(

            report,

            pdf_filename

        )

        session["latest_pdf"] = pdf_path

    # ==========================================
    # Save Interview History
    # ==========================================

    if "user_id" in session:

        try:

            InterviewHistory.save(

                session["user_id"],

                score,

                report

            )

        except Exception as e:

            print("History Save Error:", e)

    return report


# ==========================================
# Interview Analytics
# ==========================================

@interview.route("/interview_report")
def interview_report():

    if "user_id" not in session:

        return redirect(url_for("auth.login"))

    return render_template(

        "interview_report.html",

        report=session.get(

            "final_report",

            ""

        ),

        score=session.get(

            "final_score",

            0

        ),

        total=session.get(

            "total_questions",

            0

        ),

        answered=session.get(

            "answered_questions",

            0

        )

    )


# ==========================================
# Interview History
# ==========================================

@interview.route("/history")
def history():

    if "user_id" not in session:

        return redirect(

            url_for("auth.login")

        )

    history = InterviewHistory.get_history(

        session["user_id"]

    )

    return render_template(

        "history.html",

        history=history

    )


# ==========================================
# View Interview Report
# ==========================================

@interview.route("/history/<int:report_id>")
def view_report(report_id):

    report = InterviewHistory.get_report(

        report_id

    )

    return render_template(

        "view_report.html",

        report=report

    )


# ==========================================
# Delete Interview Report
# ==========================================

@interview.route("/delete_report/<int:report_id>")
def delete_report(report_id):

    InterviewHistory.delete(report_id)

    return redirect(

        url_for("interview.history")

    )


# ==========================================
# Download PDF Report
# ==========================================

@interview.route("/download_report")
def download_report():

    if "user_id" not in session:

        return redirect(

            url_for("auth.login")

        )

    pdf_path = session.get("latest_pdf")

    if not pdf_path:

        flash(

            "No report available.",

            "warning"

        )

        return redirect(

            url_for("interview.history")

        )

    if not os.path.exists(pdf_path):

        flash(

            "Report file not found.",

            "danger"

        )

        return redirect(

            url_for("interview.history")

        )

    return send_file(

        pdf_path,

        as_attachment=True,

        download_name="AI_Interview_Report.pdf"

    )


# ==========================================
# Cleanup Camera on Exit
# ==========================================

import atexit

import atexit

@atexit.register
def cleanup():
    pass

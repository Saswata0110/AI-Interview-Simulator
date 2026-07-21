from flask import Blueprint, render_template, session, redirect, flash

from models.interview_history import InterviewHistory

history = Blueprint("history", __name__)


# ------------------------------------
# Interview History
# ------------------------------------
@history.route("/history")
def interview_history():

    if "user_id" not in session:
        return redirect("/login")

    interviews = InterviewHistory.get_all(
        session["user_id"]
    )

    return render_template(
        "history.html",
        interviews=interviews
    )


# ------------------------------------
# View Interview Report
# ------------------------------------
@history.route("/history/<int:interview_id>")
def view_report(interview_id):

    if "user_id" not in session:
        return redirect("/login")

    interview = InterviewHistory.get_by_id(
        interview_id,
        session["user_id"]
    )

    if interview is None:

        flash("Interview not found.", "danger")

        return redirect("/history")

    return render_template(
        "report.html",
        interview=interview
    )


# ------------------------------------
# Delete Interview
# ------------------------------------
@history.route("/history/delete/<int:interview_id>")
def delete_interview(interview_id):

    if "user_id" not in session:
        return redirect("/login")

    InterviewHistory.delete(
        interview_id,
        session["user_id"]
    )

    flash(
        "Interview deleted successfully.",
        "success"
    )

    return redirect("/history")
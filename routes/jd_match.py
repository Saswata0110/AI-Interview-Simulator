from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from services.jd_match_service import JDMatchService

jd_match = Blueprint("jd_match", __name__)

service = JDMatchService()


@jd_match.route("/jd_match", methods=["GET", "POST"])
def jd_match_page():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    report = None

    if request.method == "POST":

        job_description = request.form.get("job_description", "").strip()

        if job_description == "":
            flash("Please paste a Job Description.", "danger")
        else:
            report = service.analyze(job_description)

    return render_template(
        "jd_match.html",
        report=report
    )
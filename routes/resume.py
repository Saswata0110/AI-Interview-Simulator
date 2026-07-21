from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from database.db import mysql
from services.resume_parser import ResumeParser

import os
from werkzeug.utils import secure_filename
from rag.vector_store import ResumeVectorStore
resume = Blueprint("resume", __name__)

UPLOAD_FOLDER = "uploads/resumes"
ALLOWED_EXTENSIONS = {"pdf"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@resume.route("/upload_resume", methods=["GET", "POST"])
def upload_resume():

    if "user_id" not in session:
        flash("Please login first.", "danger")
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        if "resume" not in request.files:
            flash("No file selected.", "danger")
            return redirect(request.url)

        file = request.files["resume"]

        if file.filename == "":
            flash("Please choose a PDF file.", "danger")
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash("Only PDF files are allowed.", "danger")
            return redirect(request.url)

        filename = secure_filename(file.filename)

        filepath = os.path.join(UPLOAD_FOLDER, filename)

        file.save(filepath)

        cursor = mysql.connection.cursor()

        # -----------------------------
        # Save Resume Information
        # -----------------------------
        cursor.execute(
            """
            INSERT INTO resumes(user_id, file_name)
            VALUES(%s,%s)
            """,
            (
                session["user_id"],
                filename
            )
        )

        mysql.connection.commit()

        resume_id = cursor.lastrowid

        # -----------------------------
        # Extract Resume Text
        # -----------------------------
        parser = ResumeParser(filepath)

        extracted_text = parser.extract_text()
        
        vector_store = ResumeVectorStore()
        vector_store.create_vector_store(extracted_text)
        # -----------------------------
        # Save Extracted Text
        # -----------------------------
        cursor.execute(
            """
            INSERT INTO resume_data
            (resume_id, extracted_text)
            VALUES(%s,%s)
            """,
            (
                resume_id,
                extracted_text
            )
        )

        mysql.connection.commit()

        cursor.close()

        flash("Resume uploaded and parsed successfully!", "success")

        return redirect(url_for("dashboard.dashboard_home"))

    return render_template("upload_resume.html")
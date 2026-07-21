from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for
)

from database.db import mysql

profile = Blueprint("profile", __name__)


@profile.route("/profile", methods=["GET", "POST"])
def profile_page():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    cursor = mysql.connection.cursor()

    # -----------------------------
    # Update Profile
    # -----------------------------
    if request.method == "POST":

        full_name = request.form.get("full_name")
        email = request.form.get("email")

        cursor.execute("""
            UPDATE users
            SET full_name=%s,
                email=%s
            WHERE id=%s
        """, (
            full_name,
            email,
            session["user_id"]
        ))

        mysql.connection.commit()

        session["user_name"] = full_name

        flash("Profile updated successfully!", "success")

    # -----------------------------
    # User Details
    # -----------------------------
    cursor.execute("""
        SELECT full_name, email
        FROM users
        WHERE id=%s
    """, (session["user_id"],))

    user = cursor.fetchone()

    if user is None:
        user = {
            "full_name": "",
            "email": ""
        }

    # -----------------------------
    # Statistics
    # -----------------------------
    cursor.execute("""
        SELECT
            COUNT(*) AS total_interviews,
            IFNULL(MAX(score),0) AS best_score,
            IFNULL(ROUND(AVG(score)),0) AS average_score
        FROM interview_history
        WHERE user_id=%s
    """, (session["user_id"],))

    stats = cursor.fetchone()

    if stats is None:
        stats = {
            "total_interviews": 0,
            "best_score": 0,
            "average_score": 0
        }

    cursor.close()

    return render_template(
        "profile.html",
        user=user,
        total_interviews=stats["total_interviews"],
        best_score=stats["best_score"],
        average_score=stats["average_score"]
    )
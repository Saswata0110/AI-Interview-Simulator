from flask import Blueprint, render_template, redirect, url_for, flash, session
from database.db import mysql
from forms.auth_forms import RegisterForm, LoginForm
import bcrypt

auth = Blueprint("auth", __name__)


# -----------------------------
# Register
# -----------------------------
@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        full_name = form.full_name.data.strip()
        email = form.email.data.strip().lower()
        password = form.password.data

        cursor = mysql.connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) AS total FROM users WHERE email=%s",
            (email,)
        )

        count = cursor.fetchone()["total"]

        if count > 0:
            cursor.close()
            flash("Email already exists!", "danger")
            return redirect(url_for("auth.register"))

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        cursor.execute(
            """
            INSERT INTO users(full_name,email,password)
            VALUES(%s,%s,%s)
            """,
            (
                full_name,
                email,
                hashed_password
            )
        )

        mysql.connection.commit()
        cursor.close()

        flash("Registration Successful!", "success")

        return redirect(url_for("auth.login"))

    return render_template(
        "register.html",
        form=form
    )


# -----------------------------
# Login
# -----------------------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data.strip().lower()
        password = form.password.data

        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            SELECT id, full_name, email, password
            FROM users
            WHERE email=%s
            """,
            (email,)
        )

        user = cursor.fetchone()

        cursor.close()

        if user:

            if bcrypt.checkpw(
                password.encode("utf-8"),
                user["password"].encode("utf-8")
            ):

                session["user_id"] = user["id"]
                session["user_name"] = user["full_name"]

                flash("Login Successful!", "success")

                return redirect(url_for("dashboard.dashboard_home"))

        flash("Invalid Email or Password", "danger")

    return render_template(
        "login.html",
        form=form
    )


# -----------------------------
# Logout
# -----------------------------
@auth.route("/logout")
def logout():

    session.clear()

    flash("Logged Out Successfully!", "success")

    return redirect(url_for("auth.login"))
from flask import Flask, render_template
from config import Config
from database.db import mysql

# -----------------------------
# Import Blueprints
# -----------------------------
from routes.auth import auth
from routes.dashboard import dashboard
from routes.resume import resume
from routes.chat import chat
from routes.interview import interview

from routes.resume_analysis import resume_analysis
from routes.jd_match import jd_match
from routes.profile import profile

# -----------------------------
# Create Flask App
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Load Configuration
# -----------------------------
app.config.from_object(Config)

# -----------------------------
# Secret Key
# -----------------------------
app.secret_key = Config.SECRET_KEY

# -----------------------------
# MySQL Configuration
# -----------------------------
app.config["MYSQL_HOST"] = Config.MYSQL_HOST
app.config["MYSQL_USER"] = Config.MYSQL_USER
app.config["MYSQL_PASSWORD"] = Config.MYSQL_PASSWORD
app.config["MYSQL_DB"] = Config.MYSQL_DB

# Optional (recommended)
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# -----------------------------
# Initialize MySQL
# -----------------------------
mysql.init_app(app)

# -----------------------------
# Register Blueprints
# -----------------------------
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(resume)
app.register_blueprint(chat)
app.register_blueprint(interview)

app.register_blueprint(resume_analysis)
app.register_blueprint(jd_match)
app.register_blueprint(profile)

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
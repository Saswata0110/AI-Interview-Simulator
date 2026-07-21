from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for

from rag.qa import InterviewQA

chat = Blueprint("chat", __name__)

qa = InterviewQA()


@chat.route("/assistant")
def assistant():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("chat.html")


@chat.route("/chat", methods=["POST"])
def chat_with_ai():

    if "user_id" not in session:
        return jsonify(
            {
                "success": False,
                "message": "Please login first."
            }
        ), 401

    data = request.get_json()

    question = data.get("message", "").strip()

    if question == "":
        return jsonify(
            {
                "success": False,
                "message": "Question cannot be empty."
            }
        )

    try:

        answer = qa.ask(question)

        return jsonify(
            {
                "success": True,
                "answer": answer
            }
        )

    except Exception as e:

        return jsonify(
            {
                "success": False,
                "message": str(e)
            }
        ), 500
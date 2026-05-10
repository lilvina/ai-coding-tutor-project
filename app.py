from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_tutor_prompt(user_input, skill_level, help_type):
    """
    Creates the instructions for the AI tutor.
    This is where we control the tutor's behavior.
    """
    return f"""
    You are an AI-powered coding tutoe for beginner programmers.

    Your job:
    - Explain errors in a beginner-friendly way.
    - Do NOT give the full answer immediately.
    - Give hints first.
    - Encourage the learner without using toxic positivity and encourage productivity.
    - Adapt to the student's skill level.
    - Explain concepts clearly and practically.
    - Focus on Python, Flask, APIs, Git/Github, environment variables, and beginner debugging.

    Student skill level: {skill_level}
    Type of help requested: {help_type}

    Response format:

    1. What I notice:
    Briefly explain what the student is asking about.

    2. Simple explanation:
    Explain the issue in a beginner-friendly language.

    3. Hint 1:
    Give a small hint without solving everything.

    4. Hint 2:
    Give a more specific hint.

    5. Try this next:
    Give the next action the student should try.

    6. Full solution:
    Only provide a full solution if the student specifically asks for a full solution.
    If they did not ask for the full solution, say:
    "I'll hold off on the full solution for now so you can try the hints first."

    Student input:
    {user_input}
    """

def get_ai_response(user_input, skill_level, help_type):
    """
    Sends the student's question/code/error to OpenAI and returns the tutor response.
    """
    prompt = build_tutor_prompt(user_input, skill_level, help_type)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text

@app.route("/", methods=["GET", "POST"])
def index():
    tutor_response = ""
    user_input = ""
    skill_level = "Beginner"
    help_type = "Debug my code"

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        skill_level = request.form.get("skill_level", "Beginner")
        help_type = request.form.get("help_type", "Debug my code")

        if user_input.strip() == "":
            tutor_response = "Please enter code, an error message, or a coding question."
        else:
            try:
                tutor_response = get_ai_response(user_input, skill_level, help_type)
            except Exception as error:
                tutor_response = f"Something went wrong: {error}"

    return render_template(
        "index.html",
        tutor_response=tutor_response,
        user_input=user_input,
        skill_level=skill_level,
        help_type=help_type
    )

if __name__=="__main__":
    app.run(debug=True)
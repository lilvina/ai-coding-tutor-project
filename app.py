from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DEFAULT_TUTOR_RESPONSE = {
    "title": "",
    "what_i_notice": "",
    "simple_explanation": "",
    "hint_1": "",
    "hint_2": "",
    "try_this_next": "",
    "full_solution": "",
    "learning_objectives": [],
    "practice_exercise": "",
    "instructor_notes": ""
}

def detect_error_type(user_input):
    """
    Simple keyword-based error detection.
    This gives the app a helpful debugging label before the AI responds.
    """
    error_keywords = {
        "SyntaxError": "SyntaxError",
        "IndentationError": "IndentationError",
        "NameError": "NameError",
        "TypeError": "TypeError",
        "ValueError": "ValueError",
        "ModuleNotFoundError": "ModuleNotFoundError",
        "ImportError": "ImportError",
        "KeyError": "KeyError",
        "IndexError": "IndexError",
        "AttributeError": "AttributeError",
        "401": "API Authentication Error",
        "403": "API Permission Error",
        "404": "Not Found Error",
        "OPENAI_API_KEY": "Environment Variable Issue",
        ".env": "Environment Variable Issue",
        "git push": "Git/GitHub Issue",
        "push protection": "GitHub Secret Protection Issue",
        "merge conflict": "Git Merge Conflict"
    }

    for keyword, error_type in error_keywords.items():
        if keyword.lower() in user_input.lower():
            return error_type
        
    return "General Coding Question"

def build_tutor_prompt(user_input, skill_level, help_type, error_type):
    """
    Creates the instructions for the AI tutor.
    This is where we control the tutor's behavior.
    """
    return f"""
    You are an AI-powered coding tutor for beginner programmers.

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
    Detected error/topic type: {error_type}

    Return ONLY valid JSON. Do not use markdown, code fences, backticks, or extra explanation outside the JSON object.
    {{
        "title": "Short helpful title",
        "what_i_notice": "Briefly explain what the student is asking about.",
        "simple_explanation": "Explain the issue in beginner-friendly language.",
        "hint_1": "Give a small hint without solving everything.",
        "hint_2": "Give a more specific hint.",
        "try_this_next": "Give the next action the student should try.",
        "full_solution": "Only give a full solution if the help type is Ask for full solution. Otherwise say: I'll hold off on the full solution for now so you can try the hints first.",
        "learning_objectives": ["Objective 1", "Objective 2", "Objective 3"],
        "practice_exercise": "Create one short practice exercise related to the student's question.",
        "instructor_notes": "If an instructor were using this in class, suggest one discussion question or teaching move."
    }}

    Special behavior:
    - If help_type is "Explain it simpler", simplify the explanation with an analogy.
    - If help_type is "Generate practice exercise", focus more on practice_exercise.
    - If help_type is "Instructor mode", focus more on instructor notes, learning objective and classroom use.

    Student input:
    {user_input}
    """

def parse_ai_json(response_text):
    """
    Attempts to parse the AI response as JSON.
    If parsing fails, the app still displays the raw response instead of crashing.
    """
    try:
        data = json.loads(response_text)
        result = DEFAULT_TUTOR_RESPONSE.copy()
        result.update(data)
        return result, None
    except json.JSONDecodeError:
        fallback = DEFAULT_TUTOR_RESPONSE.copy()
        fallback["title"] = "Tutor Response"
        fallback["simple_explanation"] = response_text
        return fallback, "The AI response could not be parsed as JSON, so it was displayed as plain text."

def get_ai_response(user_input, skill_level, help_type, error_type):
    """
    Sends the student's question/code/error to OpenAI and returns the tutor response.
    """
    prompt = build_tutor_prompt(user_input, skill_level, help_type, error_type)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        text={
            "format": {
                "type": "json_object"
            }
        }
    )
    return parse_ai_json(response.output_text)

@app.route("/", methods=["GET", "POST"])
def index():
    tutor_response = None
    parser_warning = None
    user_input = ""
    skill_level = "Beginner"
    help_type = "Debug my code"
    error_type = ""

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        skill_level = request.form.get("skill_level", "Beginner")
        help_type = request.form.get("help_type", "Debug my code")
        error_type = detect_error_type(user_input)

        if user_input.strip() == "":
            tutor_response = DEFAULT_TUTOR_RESPONSE.copy()
            tutor_response["title"] = "Missing Input"
            tutor_response["simple_explanation"] = "Please enter code, an error message, or a coding question."
        else:
            try:
                tutor_response, parser_warning = get_ai_response(
                    user_input,
                    skill_level,
                    help_type,
                    error_type
                )
            except Exception as error:
                tutor_response = DEFAULT_TUTOR_RESPONSE.copy()
                tutor_response["title"] = "Something went wrong"
                tutor_response["simple_explanation"] = str(error)

    return render_template(
        "index.html",
        tutor_response=tutor_response,
        parser_warning=parser_warning,
        user_input=user_input,
        skill_level=skill_level,
        help_type=help_type,
        error_type=error_type
    )

if __name__=="__main__":
    app.run(debug=True)
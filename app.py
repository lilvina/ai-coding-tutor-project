from flask import Flask, render_template, request

app = Flask(__name__)

def build_tutor_prompt():
    pass

def get_ai_response():
    pass

@app.route("/", methods=["GET", "POST"])
def index():
    pass

if __name__=="__main__":
    app.run(debug=True)
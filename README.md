# AI DebugMentor

AI DebugMentor is an AI-Powered coding tutor built using Python, Flask and the OpenAI API. The application helps beginner programmers understand coding errors, debug problems, and learn programming concepts through guided explanations and hints instead of giving the full solutions. 

The goal of this project is to create a beginner-friendly learning experience that encourages problem-solving, debugging skills and independent learning.

---

## Features

### 1. Collapsible Hint System

AI DebugMentor uses progressive hints to support learning:

- Hint 1 gives a small clue.
- Hint 2 gives more specific guidance.
- Full Solution stays hidden until the learner chooses to open it.


This helps learners practice debugging instead of copying answers immediately.

### 2. AI-Generated Practice Exercises

The tutor can generate short practice exercises based on the learner's question.

### 3. Explain It Simpler Mode
Learners can select **Explain it simpler** when they need a concept broken down in a more beginner-friendly way.

### 4. Instructor Mode

Instructor Mode creates teaching support such as:

- learning objectives
- discussion questions
- classroom teaching moves
- concept reinforcement ideas

### 5. Debugging Coach

AI DebugMentor can help explain common beginner issues such as:

- `SyntaxError`
- `IndentationError`
- `NameError`
- `ModuleNotFoundError`
- API authentication errors
- `.env` setup problems
- Git/GiHub mistakes
- Github push protection

The app also includes simple error-type detection to label the likely issue before showing the AI response.

---

## Technologies Used

### Backend

- Python
- Flask

### AI Integration

- OpenAI API
- Prompt Engineering

### Frontend

- HTML
- CSS
- Jinja Templates

### Tools

- Git
- Github
- python-dotenv
- Virtual environments

---

## Project Structure

```
ai-debugmentor/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## How It Works
1. The user enters:
- code
- an error message
- or a coding question
2. User selects a skill level and tutor mode.
3. Flask sends the request to the OpenAI API.
4. The prompt instructs AI DebugMentor to respond as a beginner-friendly tutor.
5. The Flask/Jinja frontend displays the response in sections, including collapsible hints.

---

## Tutor Modes

AI DebugMentor includes multiple tutor modes:

- **Debug my code**
- **Explain an error**
- **Explain a concept**
- **Give me hints**
- **Explain it simpler**
- **Generate practice exercise**
- **Instructor mode**
- **Ask for full solution**

---

## Installation

### 1. Clone the Repository
```bash
git clone https://www.github.com/lilvina/ai-debugmentor.git
```

### 2. Navigate Into the Project Folder

```bash
cd ai-debugmentor
```

### 3. Create a Virtual Environment

Mac/Linux:

```bash
python3 -m venv venv
```

Windows:

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directly:

```text
OPENAI_API_KEY=your_api_key_here
```

Keep your real API key private. The `.env` file should never be committed to GitHub.

---

## Security Note

This project includes a `.gitignore` file that excludes:

```text
.env
venv/
__pycache__/
*.pyc
.DS_Store
```

This helps prevent API keys and local environment files from being exposed.

---

## Run the Application

```bash
python3 app.py
```

Then open:
```
http://127.0.0.1:5000
```

---

### Example Prompts

```text
Why am I getting a SyntaxError?
```

```text
Explain Python loops like I'm new to programming.
```

```text
Why is my OPENAI_API_KEY not working?
```

```text
Generate a beginner practice exercise about functions.
```

```text
Create instructor notes for teaching Flask routes.
```

---

### Educational Design Goals

AI DebugMentor focuses on:

- guided learning
- debugging confidence
- scaffolding
- reducing beginner frustration
- active problem-solving
- technical communication
- instructor support

The app helps learners understand what went wrong and what to try next instead of simply generating answers.

---

## Future Improvements

Possible future additions:

- Code execution sandbox
- Saved conversation
- Student progress tracking
- Quiz system
- Multi-language support
- Voice tutoring
- Deployment on Render or Railway

---

## Key Skills Demonstrated

This project demostrates:

- Flask development
- OpenAI API integration
- Prompt engineering
- AI-assisted education
- Backend development
- Technical curriculum thinking
- Debugging instruction
- Secure API key handling

---

## Author

- Davina Taylor
- Github: www.github.com/lilvina
- Link to website: ai-coding-tutor-project-production.up.railway.app

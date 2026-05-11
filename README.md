# AI DebugMentor

AI DebugMentor is an AI-Powered coding tutor built using Python, Flask and the OpenAI API. The application helps beginner programmers understand coding errors, debug problems, and learn programming concepts through guided explanations and hints instead of giving the full solutions. 

The goal of this project is to create a beginner-friendly learning experience that encourages problem-solving, debugging skills and independent learning.

# Features
## Beginner-Friendly Explanations
The tutor explains coding concepts and errors in simple, easy-to-understand language.

## Progressive Hint System
Instead of immediately revealing answers, the tutor provides:
- Hint 1
- Hint 2
- Next steps
- Full solution only if requested

## Debugging Coach
The application can help explain:
- Syntax errors
- Import errors
- API errors
- Environment variable issues
- Git/Github mistakes
- Virtual environment setup problems

## Skill-Level Adaptation
User can choose:
- Beginner
- Intermediate
- Advanced

The AI adjusts explanations based on the selected experience level.

# Technologies Used
## Backend
- Python
- Flask

## AI Integration
- OpenAI API
- Prompt Engineering

## Frontend
- HTML
- CSS
- Jinja Templates

## Tools
- Git
- Github
- python-dotenv

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
2. Flask sends the request to the OpenAI API.
3. The AI tutor generates:
- an explanation
- hints
- and recommended next steps
4. The response is displayed back to the learner in the web application.

## Example Questions
- Why am I getting a SyntaxError?
- What does ModuleNotFoundError mean?
- Why did Github block my push because of a secret?

# Installation
## 1. Clone the Repository
```bash
git clone https://www.github.com/lilvina/ai-debugmentor.git
```

## 2. Navigate Into the Project Folder
```bash
cd ai-debugmentor
```

## 3. Create a Virtual Environment
Mac/Linux:
```bash
python3 -m venv venv
```
Windows:
```bash
python -m venv venv
```

## 4. Activate the Virtual Environment
Mac/Linux
```bash
source venv/bin/activate
```
Windows:
```bash
venv\Scripts\activate
```

## 5. Install Dependencies
```bash
pip install -r requirements.txt
```

## Environment Variables
Create a .env file in the root directly:
```
OPENAI_API_KEY=your_api_key_here
```

## Security Note
The .env file is included in .gitignore to prevent API keys from being exposed publicly.

## Run the Application
```bash
python3 app.py
```
Then open:
```
http://127.0.0.1:5000
```

## Educational Design Goals
This project focuses on:
- guided learning
- debugging confidence
- scaffolding
- and reducing beginner frustration

The AI tutor encourages active participation and critical thinking.

## Future Improvements
Planned features include:
- Code execution sandbox
- Learning progress tracking
- AI-generated coding exercises
- Quiz system
- Multi-language support
- Voice tutoring
- Personalized learning pathways

## Key Skills Demonstrated
- Flask development
- OpenAI API integration
- Prompt engineering
- AI-assisted education
- Backend development
- Technical communication
- Educational UX design

## Author
- Davina Taylor
- Github: www.github.com/lilvina
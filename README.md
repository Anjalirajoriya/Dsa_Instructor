#  DSA Instructor AI

An AI-powered Data Structures & Algorithms tutor built with Flask + Groq API (LLaMA 3.3 70B). Get step-by-step explanations, code examples, dry runs, and Big O complexity analysis — all in a sleek dark-mode chat interface.

##  Features

-  Multi-turn conversation with memory
-  Python code examples with syntax highlighting
-  Big O time & space complexity analysis
-  Topic sidebar (Binary Search, DP, Trees, Graphs, and more)
-  Practice problems (Easy / Medium / Hard)
-  Dark mode UI

##  Tech Stack

- **Backend** — Python, Flask
- **AI** — Groq API (LLaMA 3.3 70B)
- **Frontend** — Vanilla JS, HTML/CSS
- **Markdown** — marked.js
- **Syntax highlighting** — highlight.js

##  Setup & Run

### 1. Clone the repo
\```bash
git clone https://github.com/Anjalirajoriya/Dsa_Instructor.git
cd Dsa_Instructor
\```

### 2. Install dependencies
\```bash
pip install flask groq python-dotenv
\```

### 3. Create a `.env` file
\```
GROQ_API_KEY=your_groq_api_key_here
\```

### 4. Run
\```bash
python app.py
\```

##  Project Structure

\```
dsa_instructure/
├── app.py              # Flask backend + Groq API
├── .env                # API key (never commit this!)
├── .gitignore
├── README.md
└── templates/
    └── index.html      # Frontend UI
\```

## ⚠️ Important

Never commit your `.env` file. It contains your secret API key.
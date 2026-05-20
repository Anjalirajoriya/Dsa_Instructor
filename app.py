from flask import Flask, request, jsonify, render_template, session
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()  # reads your .env file

app = Flask(__name__)
app.secret_key = os.urandom(24)  # for session

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are an expert DSA instructor. Explain concepts clearly 
with step-by-step breakdowns, Python code examples, dry runs, and Big O analysis. 
Use markdown formatting."""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "").strip()
    if not user_msg:
        return jsonify({"error": "Empty message"}), 400

    # Keep conversation history in session
    if "history" not in session:
        session["history"] = []

    session["history"].append({"role": "user", "content": user_msg})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *session["history"]    # send full conversation
            ],
            max_tokens=2048,
            temperature=0.7,
        )
        reply = response.choices[0].message.content
        session["history"].append({"role": "assistant", "content": reply})
        session.modified = True        # tell Flask session was updated
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/reset", methods=["POST"])
def reset():
    session.pop("history", None)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
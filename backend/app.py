from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("questions.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return "Ascent Backend API is running!"


@app.route("/api/questions")
def get_questions():
    conn = get_db_connection()

    questions = conn.execute("""
        SELECT id, section, category, topic, question,
               option_a, option_b, option_c, option_d, difficulty
        FROM questions
    """).fetchall()

    conn.close()

    return jsonify([dict(question) for question in questions])


@app.route("/api/questions/<category>")
def get_questions_by_category(category):
    conn = get_db_connection()

    questions = conn.execute("""
        SELECT id, section, category, topic, question,
               option_a, option_b, option_c, option_d, difficulty
        FROM questions
        WHERE category = ?
    """, (category,)).fetchall()

    conn.close()

    return jsonify([dict(question) for question in questions])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
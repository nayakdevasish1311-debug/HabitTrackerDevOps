
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
habits = []
next_id = 1

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Habit Tracker V2</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2ff;
            max-width: 650px;
            margin: 50px auto;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
        }
        h1 { color: #3730a3; }
        input, button { padding: 10px; margin: 5px; }
        button {
            background: #4f46e5;
            color: white;
            border: none;
            cursor: pointer;
        }
        .done { color: green; font-weight: bold; }
    </style>
</head>
<body>
<div class="container">
    <h1>Habit Tracker</h1>
    <h3>Version 2 - Track Completion</h3>

    <form method="POST" action="/add">
        <input name="habit" placeholder="Enter a habit" required>
        <button type="submit">Add Habit</button>
    </form>

    <h3>My Habits</h3>
    <ul>
        {% for h in habits %}
        <li>
            {{ h.name }} -
            {% if h.done %}
                <span class="done">Completed</span>
            {% else %}
                Pending
                <form method="POST" action="/complete/{{ h.id }}">
                    <button type="submit">Mark Complete</button>
                </form>
            {% endif %}
        </li>
        {% else %}
        <li>No habits added yet.</li>
        {% endfor %}
    </ul>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, habits=habits)

@app.route("/add", methods=["POST"])
def add():
    global next_id
    name = request.form.get("habit", "").strip()

    if name:
        habits.append({
            "id": next_id,
            "name": name,
            "done": False
        })
        next_id += 1

    return redirect("/")

@app.route("/complete/<int:habit_id>", methods=["POST"])
def complete(habit_id):
    for h in habits:
        if h["id"] == habit_id:
            h["done"] = True
            break

    return redirect("/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

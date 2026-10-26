
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
habits = []
next_id = 1

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Habit Tracker V3</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2ff;
            max-width: 700px;
            margin: 40px auto;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
        }
        h1 { color: #3730a3; }
        .dashboard {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .card {
            background: #e0e7ff;
            padding: 15px;
            border-radius: 8px;
            flex: 1;
            min-width: 100px;
        }
        input, button {
            padding: 10px;
            margin: 5px;
        }
        button {
            background: #4f46e5;
            color: white;
            border: none;
            cursor: pointer;
        }
        .done { color: green; font-weight: bold; }
        progress { width: 100%; height: 22px; }
    </style>
</head>
<body>
<div class="container">
    <h1>Habit Tracker</h1>
    <h3>Version 3 - Progress Dashboard</h3>

    <div class="dashboard">
        <div class="card">
            <h3>{{ total }}</h3>
            <p>Total Habits</p>
        </div>
        <div class="card">
            <h3>{{ completed }}</h3>
            <p>Completed</p>
        </div>
        <div class="card">
            <h3>{{ pending }}</h3>
            <p>Pending</p>
        </div>
    </div>

    <h3>Overall Progress: {{ percent }}%</h3>
    <progress value="{{ percent }}" max="100"></progress>

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
    total = len(habits)
    completed = sum(1 for h in habits if h["done"])
    pending = total - completed
    percent = round(completed / total * 100) if total else 0

    return render_template_string(
        HTML,
        habits=habits,
        total=total,
        completed=completed,
        pending=pending,
        percent=percent
    )

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

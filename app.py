
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

habits = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Habit Tracker V1</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2ff;
            margin: 50px auto;
            max-width: 650px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
        }
        h1 {
            color: #3730a3;
        }
        input, button {
            padding: 12px;
            margin: 5px;
        }
        button {
            background: #4f46e5;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Habit Tracker</h1>
        <h3>Version 1 - Create a Habit</h3>

        <form method="POST">
            <input name="habit"
                   placeholder="Enter your daily habit"
                   required>
            <button type="submit">Add Habit</button>
        </form>

        <h3>My Habits</h3>
        <ul>
            {% for habit in habits %}
                <li>{{ habit }}</li>
            {% else %}
                <li>No habits added yet.</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        habit = request.form.get("habit", "").strip()
        if habit:
            habits.append(habit)
        return redirect("/")

    return render_template_string(HTML, habits=habits)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

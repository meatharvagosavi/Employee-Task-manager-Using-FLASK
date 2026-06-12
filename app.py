from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database
def init_db():
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee TEXT,
        task TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()

    conn.close()

    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():

    if request.method == 'POST':

        employee = request.form['employee']
        task = request.form['task']

        conn = sqlite3.connect("tasks.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO tasks(employee, task, status) VALUES (?, ?, ?)",
            (employee, task, "Pending")
        )

        conn.commit()
        conn.close()

        return redirect('/')

    return render_template("add_task.html")

@app.route('/update/<int:id>')
def update(id):

    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()

    cur.execute(
        "UPDATE tasks SET status='Completed' WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):

    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM tasks WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------------------
# DATABASE INITIALIZATION
# ---------------------------
def init_db():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            note TEXT,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()


# ---------------------------
# HOME PAGE - SHOW ALL EXPENSES
# ---------------------------
@app.route("/")
def index():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    conn.close()

    total = sum([r[1] for r in rows])  # total amount

    return render_template("index.html", expenses=rows, total=total)


# ---------------------------
# ADD EXPENSE - FORM PAGE
# ---------------------------
@app.route("/add")
def add_expense():
    return render_template("add.html")


# ---------------------------
# ADD EXPENSE - HANDLE FORM SUBMISSION
# ---------------------------
@app.route("/save", methods=["POST"])
def save_expense():
    amount = request.form["amount"]
    category = request.form["category"]
    note = request.form["note"]
    date = request.form["date"]

    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses(amount, category, note, date) VALUES (?, ?, ?, ?)",
                (amount, category, note, date))
    conn.commit()
    conn.close()

    return redirect("/")


# ---------------------------
# DELETE AN EXPENSE
# ---------------------------
@app.route("/delete/<int:id>")
def delete_expense(id):
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")


# ---------------------------
# RUN FLASK APP
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)

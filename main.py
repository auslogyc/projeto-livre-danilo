from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret_key"  # Chave para gerenciamento de sessões.

# Dados em memória
users = {"admin": "password"}  # Usuário e senha fictícios.
tasks = []  # Lista de tarefas.

@app.route("/")
def index():
    if "user" in session:
        return render_template("index.html", tasks=tasks)
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("index"))
        return "Usuário ou senha inválidos!"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/add", methods=["POST"])
def add_task():
    if "user" in session:
        task = request.form["task"]
        tasks.append(task)
        return redirect(url_for("index"))
    return redirect(url_for("login"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if "user" in session:
        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)
        return redirect(url_for("index"))
    return redirect(url_for("login"))

@app.route("/private")
def private():
    if "user" in session:
        return render_template("private.html", user=session["user"])
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
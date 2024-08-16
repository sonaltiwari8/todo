from database.database import db
from models.todo import Todo
from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def render_main():
    pending_todos = []
    completed_todos = []

    todos = Todo.get_all_todos()
    for todo in todos:
        if todo.status == 'pending':
            pending_todos.append(todo)
        else:
            completed_todos.append(todo)
    return render_template("index.html", completed_todos=completed_todos, pending_todos=pending_todos)


app.run('localhost', 4000, debug=True)

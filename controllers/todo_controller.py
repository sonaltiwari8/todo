from models.todo import Todo
from flask import render_template


def render_main_page():
    pending_todos = []
    completed_todos = []

    todos = Todo.get_all_todos()

    for todo in todos:
        if todo.status == 'pending':
            pending_todos.append(todo)
        else:
            completed_todos.append(todo)

    return render_template("index.html", completed_todos=completed_todos, pending_todos=pending_todos)

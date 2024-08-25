# controllers will contains only application logic it doesn't care who is calling this function

from models.todo import Todo
from flask import render_template, request


def render_main_handler():
    pending_todos = []
    completed_todos = []

    todos = Todo.get_all_todos()

    for todo in todos:
        if todo.status == 'pending':
            pending_todos.append(todo)
        else:
            completed_todos.append(todo)

    return render_template("index.html", completed_todos=completed_todos, pending_todos=pending_todos)


def create_todo_handler():
    # request is a object provided by flask framework, it contains all the information about the request (eg. endpoint, method, base_url, form, files)

    form = request.form

    todo = Todo(todo_name=form.get("todo_name"),
                priority_level=form.get("priority_level"),
                deadline_date=form.get("deadline_date"),
                deadline_time=form.get("deadline_time"),
                status="pending")

    todo.create_todo()

    return render_main_handler()


def delete_todo_handler():
    id = request.args.get("todo_id")
    Todo.delete_todo(id)
    return render_main_handler()


def complete_todo_handler():
    id = request.args.get("todo_id")
    Todo.complete_todo(id)
    return render_main_handler()

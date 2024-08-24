from controllers.todo_controller import create_todo_handler, render_main_page
from flask import Flask

from models.todo import Todo

# app -> controller -> models -> database

app = Flask(__name__)

# model => database related logic
# controller => application related logic

# flask will call the render_main function automatically whenever there is GET request on the / endpoint


@app.get("/")
def render_main():
    return render_main_page()

# flask will call the create_todo function automatically whenever there is POST request on the /todos endpoint


@app.post("/todos")
def create_todo():
    return create_todo_handler()


app.run('localhost', 4000, debug=True)

from controllers.todo_controller import create_todo_handler, delete_todo_handler, render_main_handler,  complete_todo_handler
from flask import Flask

# app -> controller -> models -> database

app = Flask(__name__)

# model => database related logic
# controller => application related logic

# flask will call the render_main function automatically whenever there is GET request on the / endpoint, whatever render_main function will return flask will send that to the client


@app.get("/")
def render_main():
    return render_main_handler()

# flask will call the create_todo function automatically whenever there is POST request on the /todos endpoint


@app.post("/todos")
def create_todo():
    return create_todo_handler()


@app.get("/todos/delete")
def delete_todo():
    return delete_todo_handler()


@app.get("/todos/complete")
def update_todo():
    return complete_todo_handler()


app.run('localhost', 4000, debug=True)

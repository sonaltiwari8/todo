from controllers.todo_controller import render_main_page
from flask import Flask


app = Flask(__name__)

# model => database related logic
# controller => application related logic

# flask will call the render_main function automatically whenever there is GET request on the / endpoint


@app.get("/")
def render_main():
    return render_main_page()


app.run('localhost', 4000, debug=True)

from flask import Flask, render_template
from markupsafe import escape
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/<name>")
def test(name):
    return f"Test, {escape(name)}"

@app.route("/post/<int:post_id>")
def post(post_id): 
    return f'Post {post_id}'

@app.route("/home")
def home():
    uuidOne = uuid.uuid1()
    return f'{uuidOne}'

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f'The subpath you just entered is {escape(subpath)}'

@app.route("/nothing/")
def about():
    return "Nothing here"

if __name__ == "__main__":
    app.run(debug=True)


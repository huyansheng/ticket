from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

@app.route('/name/<name>')
def name(name):
    return f"Hello {escape(name)}"

@app.route('/test_url_for')
def test_url_for():
    return (f"url_for('index') = {url_for('index')}\n"
            f"url_for('name', name='Hys') = {url_for('name', name='Hys')}\n"
            f"url_for('name', name='John') = {url_for('name', name='John')}\n"
            f"url_for('test_url_for') = {url_for('test_url_for')}")

if __name__ == '__main__':
    app.run(debug=True)

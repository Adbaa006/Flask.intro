
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "It works! Bytt meg gjerne til render_template('index.html')."

if __name__ == "__main__":
    app.run(debug=True)

app.run()

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

posts [
   [1, "Første innlegg", "<p>Hei! 1</p>"]
   [2, "Andre innlegg", "<p>Hei! 2</p>"]
   [3, "Tredje innlegg", "<p>Hei! 3</p>"]
]

if __name__ == "__main__":
    app.run(debug=True)

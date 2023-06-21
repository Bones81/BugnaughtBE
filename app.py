from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# a good way to run program via python command rather than flask run command
if(__name__ == "__main__"):
    app.run(host="0.0.0.0", port=3000, debug=True)
from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {
        "_id": 1,
        "first_name": "Nathan",
        "last_name": "Freeman",
        "roles": ["admin","developer","manager","lead"]
    },
    {
        "_id": 2,
        "first_name": "Sujan",
        "last_name": "Trivedi",
        "roles": ["developer","manager","lead"]
    },
    {
        "_id": 3,
        "first_name": "Jeff",
        "last_name": "Kitrosser",
        "roles": ["developer","manager"]
    },
    {
        "_id": 4,
        "first_name": "Olivia",
        "last_name": "Wills",
        "roles": ["developer"]
    },
]

@app.route("/")
def hello_world():
    return "<p>Hello, Nate!</p>"

@app.route("/api/users")
def get_users():
    return jsonify(USERS)

# a good way to run program via python command rather than flask run command
if(__name__ == "__main__"):
    app.run(host="0.0.0.0", port=3000, debug=True)
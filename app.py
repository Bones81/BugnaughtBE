from flask import Flask, jsonify, render_template
from flask_cors import CORS
from database import load_users_from_db, load_projects_from_db, load_bugs_from_db, load_comments_from_db

app = Flask(__name__)
CORS(app)

API_URL = 'https://bugnaughtbe.onrender.com/api/'

# PROJECTS = [
#     {
#         "_id": 1,
#         "name": "Bug Tracker App",
#         "bugs": [1, 2, 3],
#         "assigned_devs": [1, 2, 3]
#     },
#     {
#         "_id": 2,
#         "name": "Portfolio Site",
#         "bugs": [4, 5, 6],
#         "assigned_devs": [1, 2, 3, 4]
#     },
#     {
#         "_id": 3,
#         "name": "Actor Website",
#         "bugs": [7, 8, 9],
#         "assigned_devs": [1, 3, 4]
#     },
# ]


@app.route("/")
def hello_world():
    return render_template('index.html', API_URL=API_URL)

@app.route("/api/users")
def get_users():
    users = load_users_from_db()
    return jsonify(users)

@app.route("/api/projects")
def get_projects():
    projects = load_projects_from_db()
    return jsonify(projects)

@app.route("/api/bugs")
def get_bugs():
    bugs = load_bugs_from_db()
    return jsonify(bugs)

@app.route("/api/comments")
def get_comments():
    comments = load_comments_from_db()
    return jsonify(comments)

# a good way to run program via python command rather than flask run command
if(__name__ == "__main__"):
    app.run(host="0.0.0.0", port=3000, debug=True)
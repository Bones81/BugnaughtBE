from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os

# engine creation: format of connection string-- "mysql+pymysql://<username>:<password>@<hostname>/<db_name>?charset=utf8mb4"
db_conn_string = f"mysql+pymysql://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}/{os.getenv('DATABASE')}?charset=utf8mb4&ssl=true"

engine = create_engine(
    db_conn_string, 
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

# USER functions
def load_users_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))

        users = []
        for row in result.all():
            users.append((dict(row._mapping)))
        return users
    
def load_single_user(user_id):
    try: 
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT * FROM users WHERE id = {user_id}"))
            row = result.all()[0]
            user_dict = dict(row._mapping)
            return user_dict
    except Exception as e:
        return str(e)

# PROJECT functions
def load_projects_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM projects"))

        projects = []
        for row in result.all():
            projects.append((dict(row._mapping)))
        return projects

# BUG functions
def load_bugs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM bugs"))

        bugs = []
        for row in result.all():
            bugs.append((dict(row._mapping)))
        return bugs

# COMMENT functions
def load_comments_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM comments"))

        comments = []
        for row in result.all():
            comments.append((dict(row._mapping)))
        return comments

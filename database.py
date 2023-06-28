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

def load_users_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))

        users = []
        for row in result.all():
            users.append((dict(row._mapping)))
        return users
    
def load_projects_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM projects"))

        projects = []
        for row in result.all():
            projects.append((dict(row._mapping)))
        return projects
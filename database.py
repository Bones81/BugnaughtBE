from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()
import os

# engine creation: format of connection string-- "mysql+pymysql://<username>:<password>@<hostname>/<db_name>?charset=utf8mb4"
db_conn_string = f"mysql+pymysql://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}/{os.getenv('DATABASE')}?charset=utf8mb4"

engine = create_engine(
    db_conn_string, 
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    }
)

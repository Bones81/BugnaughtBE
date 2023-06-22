from sqlalchemy import create_engine, text
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

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users"))
    # print("type(result):", type(result))
    result_all = result.all()
    # print("type(result.all()):", type(result.all()))
    first_result = result_all[0]
    
    print(type(result_all[0])) # results in SQLAlchemy row type, which can be converted into dict w/ ._mapping property
    first_result_dict = result_all[0]._mapping
    print("type of first_result_dict:", type(first_result_dict))
    print(first_result_dict)
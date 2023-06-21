from sqlalchemy import create_engine, text

# engine creation: format of connection string-- "mysql+pymysql://<username>:<password>@<hostname>/<db_name>?charset=utf8mb4"

db_conn_string = "mysql+pymysql://iamzt7rxtuqn4l1qm23v:pscale_pw_DI2bxknV2sS5y08jdOQY6MAUsXYbNXd5C0BsgbKzMhR@aws.connect.psdb.cloud/bugnaught?charset=utf8mb4"
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
    print(result.all())
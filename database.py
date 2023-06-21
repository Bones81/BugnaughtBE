from sqlalchemy import create_engine

# engine creation: format of connection string-- "mysql+pymysql://<username>:<password>@<hostname>/<db_name>?charset=utf8mb4"
engine = create_engine("mysql+pymysql://x414bwf9vek8uggv0kbx:pscale_pw_3BQq9kkcdTh0o78rIp8KnHAajpH438XlLfJVK3aGdWT@aws.connect.psdb.cloud/bugnaught?charset=utf8mb4")
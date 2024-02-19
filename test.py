from sqlalchemy import create_engine

# Set up the connection to the database
engine = create_engine('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db', pool_pre_ping=True)

# Drop the database
engine.execute("DROP DATABASE IF EXISTS hbnb_dev_db")

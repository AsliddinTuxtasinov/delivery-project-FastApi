from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Replace with your actual credentials and database details
db_username = "postgres"
db_password = "asliddin"
db_host = "0.0.0.0"  # Use the actual IP address of your PostgreSQL container
db_port = "5432"
db_name = "asliddin"

# SQLAlchemy's connection URL
# The URL format is: "postgresql+psycopg2://username:password@host:port/database_name"
connection_url = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create an SQLAlchemy engine to connect to the PostgresSQL database.
engine = create_engine(
    connection_url,
    echo=True  # Setting this to True will print SQL statements for testing purposes. Not recommended for deployment
)

# Create a base class for declarative SQLAlchemy models.
Base = declarative_base()

# Create a session-maker to create database sessions.
session = sessionmaker()

# Here, you've set up the basic components for interacting with the PostgresSQL database:
# - `engine` to connect to the database
# - `Base` as the base class for declarative models
# - `Session` to create database sessions

# You can now define your SQLAlchemy models using the `Base` class, and use the `Session` to interact with the database.

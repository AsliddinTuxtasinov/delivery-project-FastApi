from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Create an SQLAlchemy engine to connect to the PostgresSQL database.
# The URL format is: "postgresql+psycopg2://username:password@host:port/database_name"
engine = create_engine(
    "postgresql+psycopg2://postgres:asliddin@delivery_project:5432/asliddin",
    echo=True  # Setting this to True will print SQL statements for testing purposes. Not recommend for deployment
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

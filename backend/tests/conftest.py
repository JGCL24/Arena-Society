import os
import importlib
import pytest

# Use in-memory SQLite for tests
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

# Reload database module so engine picks up test DATABASE_URL
import app.database as database
importlib.reload(database)

# Ensure tables are created before tests
database.create_db_and_tables()

# Reload main to bind to the (new) database engine
import app.main as main
importlib.reload(main)

from fastapi.testclient import TestClient

@pytest.fixture
def client():
    # create tables for each test to ensure isolation
    database.create_db_and_tables()
    with TestClient(main.app) as c:
        yield c

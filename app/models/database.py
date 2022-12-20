from os import environ

import databases

DB_USER = environ.get("DB_USER", "robohome")
DB_PASSWORD = environ.get("DB_PASSWORD", "spark2022")
DB_HOST = environ.get("DB_HOST", "79.141.71.61")

TESTING = environ.get("TESTING")

if TESTING:
    # Use separate DB for tests
    DB_NAME = "robohome-test"
    TEST_SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    )
    database = databases.Database(TEST_SQLALCHEMY_DATABASE_URL)
else:
    DB_NAME = "robohome"
    SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    )
    database = databases.Database(SQLALCHEMY_DATABASE_URL)

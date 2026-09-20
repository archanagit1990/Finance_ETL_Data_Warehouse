import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from dotenv import load_dotenv
import os


load_dotenv("config/.env")


def get_engine():

    connection_url = URL.create(
        "postgresql+psycopg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME")
    )

    return create_engine(connection_url)


def load_to_database(
    customers,
    accounts,
    branches,
    transactions
):

    engine = get_engine()

    customers.to_sql(
        "stg_customers",
        engine,
        if_exists="replace",
        index=False
    )

    accounts.to_sql(
        "stg_accounts",
        engine,
        if_exists="replace",
        index=False
    )

    branches.to_sql(
        "stg_branches",
        engine,
        if_exists="replace",
        index=False
    )

    transactions.to_sql(
        "stg_transactions",
        engine,
        if_exists="replace",
        index=False
    )

    print("Staging data loaded successfully")
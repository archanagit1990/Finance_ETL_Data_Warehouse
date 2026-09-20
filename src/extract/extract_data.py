import pandas as pd


BASE_PATH = "data/raw"


def extract_data():

    customers = pd.read_csv(
        f"{BASE_PATH}/customers.csv"
    )

    accounts = pd.read_csv(
        f"{BASE_PATH}/accounts.csv"
    )

    branches = pd.read_csv(
        f"{BASE_PATH}/branches.csv"
    )

    transactions = pd.read_csv(
        f"{BASE_PATH}/transactions.csv"
    )

    status_reference = pd.read_csv(
        f"{BASE_PATH}/reference/transaction_status.csv"
    )

    print("Source data extracted successfully")

    return (
        customers,
        accounts,
        branches,
        transactions,
        status_reference
    )
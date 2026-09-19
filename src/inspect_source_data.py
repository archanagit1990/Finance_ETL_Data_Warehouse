from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"


transactions = pd.read_csv(
    RAW_DIR / "transactions.csv"
)

customers = pd.read_csv(
    RAW_DIR / "customers.csv"
)

accounts = pd.read_csv(
    RAW_DIR / "accounts.csv"
)


print("SOURCE DATA SUMMARY")
print("=" * 50)

print(f"Customers    : {len(customers):,}")
print(f"Accounts     : {len(accounts):,}")
print(f"Transactions : {len(transactions):,}")


print()
print("Transaction Columns")
print("-" * 50)

print(
    transactions.columns.tolist()
)


print()
print("Transaction Null Counts")
print("-" * 50)

print(
    transactions.isnull().sum()
)


print()
print("Duplicate Transaction IDs")
print("-" * 50)

print(
    transactions[
        transactions["transaction_id"].duplicated(
            keep=False
        )
    ][
        ["transaction_id"]
    ]
)


print()
print("Negative Transaction Amounts")
print("-" * 50)

print(
    transactions[
        transactions[
            "transaction_amount"
        ] < 0
    ][
        [
            "transaction_id",
            "transaction_amount",
        ]
    ]
)
#python
import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


# =========================================================
# 1. PROJECT CONFIGURATION
# =========================================================

random.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
REFERENCE_DIR = BASE_DIR / "data" / "reference"

RAW_DIR.mkdir(parents=True, exist_ok=True)
REFERENCE_DIR.mkdir(parents=True, exist_ok=True)

CUSTOMER_COUNT = 1000
ACCOUNT_COUNT = 1500
TRANSACTION_COUNT = 10000


# =========================================================
# 2. SAMPLE MASTER DATA
# =========================================================

first_names = [
    "Arun",
    "Rahul",
    "Anjali",
    "Priya",
    "Neha",
    "Vivek",
    "Amit",
    "Sneha",
    "Kiran",
    "Meera",
    "Ravi",
    "Divya",
    "Suresh",
    "Lakshmi",
    "Nikhil",
]

last_names = [
    "Nair",
    "Menon",
    "Sharma",
    "Kumar",
    "Patel",
    "Reddy",
    "Iyer",
    "Das",
    "Thomas",
    "Joseph",
    "Singh",
    "Verma",
]

cities = [
    "Kochi",
    "Trivandrum",
    "Bangalore",
    "Chennai",
    "Hyderabad",
    "Mumbai",
    "Pune",
    "Delhi",
    "Kolkata",
    "Ahmedabad",
]

states = {
    "Kochi": "Kerala",
    "Trivandrum": "Kerala",
    "Bangalore": "Karnataka",
    "Chennai": "Tamil Nadu",
    "Hyderabad": "Telangana",
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Delhi": "Delhi",
    "Kolkata": "West Bengal",
    "Ahmedabad": "Gujarat",
}


# =========================================================
# 3. BRANCH DATA
# =========================================================

branches = [
    ("B001", "Kochi Central", "Kochi", "Kerala", "South"),
    ("B002", "Trivandrum Main", "Trivandrum", "Kerala", "South"),
    ("B003", "Bangalore Central", "Bangalore", "Karnataka", "South"),
    ("B004", "Chennai Main", "Chennai", "Tamil Nadu", "South"),
    ("B005", "Hyderabad Central", "Hyderabad", "Telangana", "South"),
    ("B006", "Mumbai Main", "Mumbai", "Maharashtra", "West"),
    ("B007", "Pune Central", "Pune", "Maharashtra", "West"),
    ("B008", "Delhi Central", "Delhi", "Delhi", "North"),
    ("B009", "Kolkata Main", "Kolkata", "West Bengal", "East"),
    ("B010", "Ahmedabad Central", "Ahmedabad", "Gujarat", "West"),
]

branch_df = pd.DataFrame(
    branches,
    columns=[
        "branch_id",
        "branch_name",
        "city",
        "state",
        "region",
    ],
)

branch_df.to_csv(
    RAW_DIR / "branches.csv",
    index=False,
)


# =========================================================
# 4. CUSTOMER DATA
# =========================================================

customer_types = [
    "Standard",
    "Premium",
    "Corporate",
]

customers = []

for i in range(1, CUSTOMER_COUNT + 1):

    customer_id = f"C{i:05d}"

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    customer_name = f"{first_name} {last_name}"

    city = random.choice(cities)

    registration_date = (
        datetime.now()
        - timedelta(
            days=random.randint(30, 2500)
        )
    ).date()

    date_of_birth = (
        datetime.now()
        - timedelta(
            days=random.randint(
                21 * 365,
                70 * 365,
            )
        )
    ).date()

    email = (
        f"{first_name.lower()}."
        f"{last_name.lower()}"
        f"{i}@example.com"
    )

    customers.append(
        {
            "customer_id": customer_id,
            "customer_name": customer_name,
            "date_of_birth": date_of_birth,
            "gender": random.choice(
                ["Male", "Female", "Other"]
            ),
            "city": city,
            "country": "India",
            "customer_type": random.choice(
                customer_types
            ),
            "email": email,
            "registration_date": registration_date,
        }
    )

customer_df = pd.DataFrame(customers)

customer_df.to_csv(
    RAW_DIR / "customers.csv",
    index=False,
)


# =========================================================
# 5. ACCOUNT DATA
# =========================================================

account_types = [
    "Savings",
    "Current",
    "Salary",
    "Business",
]

account_statuses = [
    "Active",
    "Inactive",
    "Closed",
]

customer_ids = customer_df[
    "customer_id"
].tolist()

branch_ids = branch_df[
    "branch_id"
].tolist()

accounts = []

for i in range(1, ACCOUNT_COUNT + 1):

    account_id = f"A{i:06d}"

    account_open_date = (
        datetime.now()
        - timedelta(
            days=random.randint(
                30,
                2500,
            )
        )
    ).date()

    accounts.append(
        {
            "account_id": account_id,
            "customer_id": random.choice(
                customer_ids
            ),
            "account_type": random.choice(
                account_types
            ),
            "account_open_date": account_open_date,
            "branch_id": random.choice(
                branch_ids
            ),
            "account_status": random.choice(
                account_statuses
            ),
            "balance": round(
                random.uniform(
                    1000,
                    500000,
                ),
                2,
            ),
        }
    )

account_df = pd.DataFrame(accounts)

account_df.to_csv(
    RAW_DIR / "accounts.csv",
    index=False,
)


# =========================================================
# 6. TRANSACTION DATA
# =========================================================

transaction_types = [
    "Deposit",
    "Withdrawal",
    "Transfer",
    "Payment",
    "Fee",
    "Interest",
]

channels = [
    "Online",
    "Mobile",
    "ATM",
    "Branch",
]

transaction_statuses = [
    "SUCCESS",
    "FAILED",
    "PENDING",
]

account_ids = account_df[
    "account_id"
].tolist()

transactions = []

start_date = datetime.now() - timedelta(
    days=730
)

for i in range(1, TRANSACTION_COUNT + 1):

    transaction_id = f"T{i:07d}"

    transaction_date = (
        start_date
        + timedelta(
            days=random.randint(0, 729),
            seconds=random.randint(
                0,
                86399,
            ),
        )
    )

    transactions.append(
        {
            "transaction_id": transaction_id,
            "account_id": random.choice(
                account_ids
            ),
            "transaction_date": transaction_date,
            "transaction_type": random.choice(
                transaction_types
            ),
            "transaction_amount": round(
                random.uniform(
                    100,
                    250000,
                ),
                2,
            ),
            "currency": "INR",
            "transaction_status": random.choice(
                transaction_statuses
            ),
            "channel": random.choice(
                channels
            ),
        }
    )

transaction_df = pd.DataFrame(
    transactions
)


# =========================================================
# 7. INJECT DATA QUALITY ISSUES
# =========================================================

# ---------------------------------------------------------
# Issue 1: Duplicate Transaction IDs
# ---------------------------------------------------------

for i in range(5):

    transaction_df.loc[
        100 + i,
        "transaction_id",
    ] = transaction_df.loc[
        i,
        "transaction_id",
    ]


# ---------------------------------------------------------
# Issue 2: Negative Transaction Amounts
# ---------------------------------------------------------

for i in range(5):

    transaction_df.loc[
        200 + i,
        "transaction_amount",
    ] = -5000


# ---------------------------------------------------------
# Issue 3: Invalid Account IDs
# ---------------------------------------------------------

for i in range(5):

    transaction_df.loc[
        300 + i,
        "account_id",
    ] = f"A9999{i}"


# ---------------------------------------------------------
# Issue 4: Invalid Transaction Status
# ---------------------------------------------------------

for i in range(5):

    transaction_df.loc[
        400 + i,
        "transaction_status",
    ] = "UNKNOWN"


# ---------------------------------------------------------
# Issue 5: Future Transaction Dates
# ---------------------------------------------------------

future_date = datetime.now() + timedelta(
    days=30
)

for i in range(5):

    transaction_df.loc[
        500 + i,
        "transaction_date",
    ] = future_date


# ---------------------------------------------------------
# Issue 6: Missing Account IDs
# ---------------------------------------------------------

for i in range(5):

    transaction_df.loc[
        600 + i,
        "account_id",
    ] = None


# Save transactions

transaction_df.to_csv(
    RAW_DIR / "transactions.csv",
    index=False,
)


# =========================================================
# 8. TRANSACTION STATUS REFERENCE DATA
# =========================================================

status_df = pd.DataFrame(
    [
        (
            "SUCCESS",
            "Successful Transaction",
        ),
        (
            "FAILED",
            "Failed Transaction",
        ),
        (
            "PENDING",
            "Pending Transaction",
        ),
    ],
    columns=[
        "status_code",
        "status_description",
    ],
)

status_df.to_csv(
    REFERENCE_DIR / "transaction_status.csv",
    index=False,
)


# =========================================================
# 9. GENERATION SUMMARY
# =========================================================

print()
print("=" * 60)
print("FINANCE SOURCE DATA GENERATION COMPLETED")
print("=" * 60)

print(f"Customers       : {len(customer_df):,}")
print(f"Accounts        : {len(account_df):,}")
print(f"Transactions    : {len(transaction_df):,}")
print(f"Branches        : {len(branch_df):,}")

print()
print("Intentional Data Quality Issues")
print("-" * 40)
print("Duplicate transaction IDs : 5")
print("Negative amounts          : 5")
print("Invalid account IDs       : 5")
print("Invalid statuses          : 5")
print("Future transaction dates  : 5")
print("Missing account IDs       : 5")

print()
print(f"Raw data location       : {RAW_DIR}")
print(f"Reference data location : {REFERENCE_DIR}")
print("=" * 60)

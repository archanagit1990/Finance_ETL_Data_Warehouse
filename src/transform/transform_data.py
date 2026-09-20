import pandas as pd


def transform_data(
    customers,
    accounts,
    branches,
    transactions,
    status_reference
):

    # Create copies to avoid modifying source DataFrames
    customers = customers.copy()
    accounts = accounts.copy()
    branches = branches.copy()
    transactions = transactions.copy()

    # =========================================================
    # 1. DATE TRANSFORMATION
    # =========================================================

    accounts["opening_date"] = pd.to_datetime(
        accounts["account_open_date"]
    )

    transactions["transaction_date"] = pd.to_datetime(
        transactions["transaction_date"]
    )

    # =========================================================
    # 2. CUSTOMER TRANSFORMATION
    # =========================================================

   # Customer transformation
    customers["customer_name"] = (
    customers["customer_name"]
    .str.strip()
    .str.title()
    )

# Source-to-target mapping
    customers["customer_segment"] = (
    customers["customer_type"]
    .str.strip()
    .str.title()
    )

    # =========================================================
    # 3. ACCOUNT TRANSFORMATION
    # =========================================================

    accounts["account_type"] = (
        accounts["account_type"]
        .str.upper()
    )

    # =========================================================
    # 4. TRANSACTION SOURCE-TO-TARGET MAPPING
    # =========================================================

    # Source: transaction_amount
    # Target: amount
    transactions["amount"] = (
        transactions["transaction_amount"]
    )

    # Source: transaction_status
    # Target: status
    transactions["status"] = (
        transactions["transaction_status"]
        .str.upper()
    )

    # Standardize transaction type
    transactions["transaction_type"] = (
        transactions["transaction_type"]
        .str.upper()
    )

    # =========================================================
    # 5. JOIN TRANSACTION WITH ACCOUNT
    # =========================================================

    transaction_enriched = transactions.merge(
        accounts[
            [
                "account_id",
                "customer_id",
                "branch_id"
            ]
        ],
        on="account_id",
        how="left"
    )

    # =========================================================
    # 6. JOIN CUSTOMER
    # =========================================================

    transaction_enriched = transaction_enriched.merge(
        customers[
            [
                "customer_id",
                "customer_name",
                "customer_segment"
            ]
        ],
        on="customer_id",
        how="left"
    )

    # =========================================================
    # 7. JOIN BRANCH
    # =========================================================

    transaction_enriched = transaction_enriched.merge(
        branches[
            [
                "branch_id",
                "branch_name",
                "city",
                "state"
            ]
        ],
        on="branch_id",
        how="left"
    )

    # =========================================================
    # 8. JOIN TRANSACTION STATUS REFERENCE
    # =========================================================

    transaction_enriched = transaction_enriched.merge(
        status_reference,
        left_on="status",
        right_on="status_code",
        how="left"
    )

    # =========================================================
    # 9. CREATE SIGNED TRANSACTION AMOUNT
    # =========================================================

    transaction_enriched["signed_amount"] = (
        transaction_enriched.apply(
            lambda row:
            -row["amount"]
            if row["transaction_type"] == "WITHDRAWAL"
            else row["amount"],
            axis=1
        )
    )

    print("Transformation completed")

    return (
        customers,
        accounts,
        branches,
        transaction_enriched
    )
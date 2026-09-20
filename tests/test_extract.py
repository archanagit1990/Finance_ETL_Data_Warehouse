
from src.extract.extract_data import (
    extract_accounts,
    extract_branches,
    extract_customers,
    extract_transactions,
)


def test_customer_extraction():

    df = extract_customers()

    assert not df.empty
    assert "customer_id" in df.columns


def test_account_extraction():

    df = extract_accounts()

    assert not df.empty
    assert "account_id" in df.columns


def test_transaction_extraction():

    df = extract_transactions()

    assert not df.empty
    assert "transaction_id" in df.columns


def test_branch_extraction():

    df = extract_branches()

    assert not df.empty
    assert "branch_id" in df.columns


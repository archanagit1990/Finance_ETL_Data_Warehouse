CREATE TABLE IF NOT EXISTS stg_customers (
    customer_id VARCHAR(20),
    customer_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    customer_segment VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS stg_accounts (
    account_id VARCHAR(20),
    customer_id VARCHAR(20),
    branch_id VARCHAR(20),
    account_type VARCHAR(50),
    opening_date DATE,
    account_status VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS stg_branches (
    branch_id VARCHAR(20),
    branch_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS stg_transactions (
    transaction_id VARCHAR(20),
    account_id VARCHAR(20),
    transaction_date DATE,
    transaction_type VARCHAR(30),
    amount NUMERIC(18,2),
    status VARCHAR(30),
    customer_id VARCHAR(20),
    branch_id VARCHAR(20),
    customer_name VARCHAR(100),
    customer_segment VARCHAR(50),
    branch_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    status_description VARCHAR(100),
    signed_amount NUMERIC(18,2)
);
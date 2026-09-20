CREATE TABLE IF NOT EXISTS dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_id VARCHAR(20) UNIQUE,
    customer_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    customer_segment VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS dim_branch (
    branch_key SERIAL PRIMARY KEY,
    branch_id VARCHAR(20) UNIQUE,
    branch_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dim_account (
    account_key SERIAL PRIMARY KEY,
    account_id VARCHAR(20) UNIQUE,
    customer_id VARCHAR(20),
    branch_id VARCHAR(20),
    account_type VARCHAR(50),
    opening_date DATE,
    account_status VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    month_name VARCHAR(20),
    quarter INTEGER
);

CREATE TABLE IF NOT EXISTS fact_transaction (
    transaction_key SERIAL PRIMARY KEY,
    transaction_id VARCHAR(20) UNIQUE,
    account_id VARCHAR(20),
    customer_id VARCHAR(20),
    branch_id VARCHAR(20),
    transaction_date DATE,
    transaction_type VARCHAR(30),
    amount NUMERIC(18,2),
    signed_amount NUMERIC(18,2),
    status VARCHAR(30)
);
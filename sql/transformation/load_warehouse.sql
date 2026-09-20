INSERT INTO dim_customer (
    customer_id,
    customer_name,
    city,
    state,
    customer_segment
)
SELECT
    customer_id,
    customer_name,
    city,
    state,
    customer_segment
FROM stg_customers
ON CONFLICT (customer_id)
DO NOTHING;


INSERT INTO dim_branch (
    branch_id,
    branch_name,
    city,
    state
)
SELECT
    branch_id,
    branch_name,
    city,
    state
FROM stg_branches
ON CONFLICT (branch_id)
DO NOTHING;


INSERT INTO dim_account (
    account_id,
    customer_id,
    branch_id,
    account_type,
    opening_date,
    account_status
)
SELECT
    account_id,
    customer_id,
    branch_id,
    account_type,
    opening_date,
    account_status
FROM stg_accounts
ON CONFLICT (account_id)
DO NOTHING;


INSERT INTO fact_transaction (
    transaction_id,
    account_id,
    customer_id,
    branch_id,
    transaction_date,
    transaction_type,
    amount,
    signed_amount,
    status
)
SELECT
    transaction_id,
    account_id,
    customer_id,
    branch_id,
    transaction_date,
    transaction_type,
    amount,
    signed_amount,
    status
FROM stg_transactions
ON CONFLICT (transaction_id)
DO NOTHING;
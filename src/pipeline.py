from src.extract.extract_data import extract_data
from src.transform.transform_data import transform_data
from src.load.load_data import load_to_database


def run_pipeline():

    print("\n==============================")
    print("FINANCE ETL PIPELINE STARTED")
    print("==============================")

    (
        customers,
        accounts,
        branches,
        transactions,
        status_reference
    ) = extract_data()

    (
        customers,
        accounts,
        branches,
        transaction_enriched
    ) = transform_data(
        customers,
        accounts,
        branches,
        transactions,
        status_reference
    )

    load_to_database(
        customers,
        accounts,
        branches,
        transaction_enriched
    )

    print("\n==============================")
    print("FINANCE ETL PIPELINE COMPLETED")
    print("==============================")


if __name__ == "__main__":
    run_pipeline()
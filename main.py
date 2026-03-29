from extract import extract_data
from load import load_to_bigquery

# Main runner for the ELT pipeline.
# Ideally this would be an automated function using a cloud scheduler.
def run_pipeline():
    df = extract_data()

    if df is not None:
        load_to_bigquery(df)

if __name__ == "__main__":
    run_pipeline()
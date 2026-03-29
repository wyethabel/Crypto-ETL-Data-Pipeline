import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Local key bypass due to issues with Google ADC
key = r"C:\BigQuery\key.json"
credentials = service_account.Credentials.from_service_account_file(key)

# BigQuery project details
PROJECT_ID = "crypto-data-491219"
DATASET_ID = "raw_crypto_data"
TABLE_ID = "raw_crypto_data"
FULL_TABLE_ID = f"{PROJECT_ID}.{DATASET_ID}. {TABLE_ID}"

# Initialize the BigQuery client
client = bigquery.Client(credentials = credentials, project = credentials.project_id)

# Table schema
schema = [
    bigquery.SchemaField("coin_id", "STRING"),
    bigquery.SchemaField("symbol", "STRING"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("current_price", "FLOAT"),
    bigquery.SchemaField("market_cap", "FLOAT"),
    bigquery.SchemaField("total_volume", "FLOAT"),
    bigquery.SchemaField("price_change_24h", "FLOAT"),
    bigquery.SchemaField("ingested_at", "TIMESTAMP")
]

"""
Primary load function that accepts the dataframe, designates the BigQuery job
configuration, and runs the job to load the data into the cloud platform. 
"""
def load_to_bigquery(df: pd.DataFrame):
    try:
        if df is None or df.empty:
            return
        df = df.rename(columns = {
            "id": "coin_id",
            "price_change_percentage_24h": "price_change_24h"
        })

        job_config = bigquery.LoadJobConfig(
            schema = schema,
            write_disposition = "WRITE_APPEND",
            time_partitioning = bigquery.TimePartitioning(field = "ingested_at")
        )

        job = client.load_table_from_dataframe(
            df,
            FULL_TABLE_ID,
            job_config = job_config
        )

        job.result()

    except Exception as e:
        print(f"Error: {e}")
        return None
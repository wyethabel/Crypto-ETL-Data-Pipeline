# Crypto-ETL-Data-Pipeline

This project focused on implementing an ETL (Extract, Transform, Load) data pipeline
utilizing multiple technologies and skills to form the foundation for an 
automated crypto visualization.

Data Pipeline Guide: CoinGecko API -> BigQuery -> Tableau

This process begins with requesting the data from the CoinGecko API seen in
the extract file which generates a Pandas DataFrame. This dataframe is then
loaded into BigQuery utilizing the BigQuery client seen in the load file. 
This process is facilitated by main with daily run specifications performed 
in the Google Cloud Scheduler. While this run process was performed daily,
this could be used with increased intensity with paid features for the API
and Google. 

Once the data is in BigQuery, it is then initially inserted into a raw
housing dataset as a raw data table. This is then cleaned and appended 
into a clean dataset and table, allowing for running or hot data. 

![Alt text](/Big_Query_1.png?raw=true "Optional Title")

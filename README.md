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

![Image](https://github.com/wyethabel/Crypto-ETL-Data-Pipeline/blob/main/ReadMe%20Images/Big%20Query%201.png)

Next I performed independent validity checks for Null values to identify 
if any inputs were being caught by the safe casts, finding out that the API 
was providing some outputs as Null automatically for specific coins. I
opted to remove these entries as they are unusable. Next I implemented a break-out 
table intended to add a snapshot of daily rankings based on market volume.

![Image](https://github.com/wyethabel/Crypto-ETL-Data-Pipeline/blob/main/ReadMe%20Images/Big%20Query%202.png)

Lastly, I expanded on this table by adding a column that defines tier brackets
in order to simplify use in a visualization tool such as Power BI or Tableau.

![Image](https://github.com/wyethabel/Crypto-ETL-Data-Pipeline/blob/main/ReadMe%20Images/Big%20Query%203.png)

This process from raw data to a table ready for use utilizes the BigQuery 
query scheduling feature to allow them to be run shortly after data is imported.

Finally, this data is connected to Tableau and utilized to produce a basic dashboard
regarding the current top 10 coins by market cap. It is important to note that Tableau 
offers only a paid connection to BigQuery which would allow for full automation
and a viz that constantly features up-to-date info. 

![Image](https://github.com/wyethabel/Crypto-ETL-Data-Pipeline/blob/main/ReadMe%20Images/Tableau%201.png)

At the time of publishing, there is limited data to perform an over-time analysis
so I took a greater focus on top-10 statistics. Ultimately, this project focus was
on the coming-together of technologies and how a pipeline functions for data automation.

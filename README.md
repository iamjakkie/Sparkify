The project loads the .json log and song data from sparkify music streaming platform.
The star schema has been implemented along with ETL process to load the data into postgresql schema.
The schema uses four dimensions: time, user, song and artist and one fact table - songplays.
Duplicates and NULL values are handled in ETL process with pandas functions like dropna() or drop_duplicates(). 
This data warehouse will allow us to perform various analysis, for example we could find the most repeated song in the dataset.
Star schema allows quick data querying, the data from json was modeled in a way allowing further analysis. ETL

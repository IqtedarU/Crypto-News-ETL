# Crypto-News-ETL-Database

This is a introductionary Project going through Data Mining and Sentiment Analysis. I mine data and get the title, date, content for a specific coin.
This used to be a project mainly looking into crypto news sentiment through pre-trained libraries. I am switching this into a Data Engineering project.
This is still in-progress as I just made the switch, but the plan it to go through the whole process to get the idea.

# Steps:

## Step 1: Data Retrieval 
Web-Scrape Data on the internet for cypto-news from sources. I currently web scrape 1 to get an idea on hwo to interact with database.

## Step 2: Data Preprocessing
Clean the data in the format I want it to be. In this case we have Source, Url, Date, Time, Tag, Title, Content

## Step 3: Database design and integration
Since this is a fixed schema a SQL database is best. I am currently using NoSql mainly because AWS has limits on free, and I would like to get testing out of the way.

There will we two datatables. One will be sources keeping track of sources used. the other will be Articles keeping track of all articles. We can use SQL to query efficiently

## Step 4: AWS automation and Pyspark
AWS is mainly to get experience on AWS and know more on how to use it. I will use it to automate the script, and populate the SQL Database.
AWS RDS is used for database, Apache Airflow is used to automate script and adding to script. maybe look into Pyspark incase big data used in future.
This project won't use big data, as I will become poor :( .

## Step 5 Querying or future steps:
I will make queries for looking for specific tags, dates, or authors. Maybe look into information retrieval to search for specific articles in a big database


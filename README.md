# Crypto-News-ETL-Database

This is a introductionary Project going through Data Mining and Sentiment Analysis. I mine data and get the title, date, content for a specific coin.
This used to be a project mainly looking into crypto news sentiment through pre-trained libraries. I am switching this into a Data Engineering project.


# Steps:

## Step 1: Data Retrieval 
Web-Scrape Data on the internet for cypto-news from sources. I currently web scrape 1 to get an idea on hwo to interact with database.

## Step 2: Data Preprocessing
Clean the data in the format I want it to be. In this case we have Source, Url, Date, Time, Tag, Title, Content

## Step 3: Database design and integration
Since this is a fixed schema a SQL database is best. I am currently using NoSql mainly because AWS has limits on the free version, and I would like to get to testing. This will basically function as a dimensional database, but in noSQL. this is just for testing, as you would implement a actual dimensional database in a practical setting

There will we two datatables. One will be sources keeping track of sources used. the other will be Articles keeping track of all articles. We can use SQL to query efficiently

## Step 4: AWS automation and Pyspark
AWS is mainly to get experience on AWS and know more on how to use it. I will use Apache and Dockers to automate the script, and populate the SQL Database.
AWS RDS is used for database, Apache Airflow is used to automate script and adding to script. maybe look into Pyspark incase big data used in future.
This project won't use big data, as I will become poor :( .

## Step 5 Querying or future steps:
I will make queries for looking for specific tags, dates, or authors. Maybe look into information retrieval to search for specific articles in a big database

Maybe Use Pyspark, just to test optimization of speed, since this is still relatively small dataset.

## To build:

You can use Dockerfile to make sure the scripts are copied into the Docker Container. The DAG contains the automation, while crypto_scraper has the database population and querying. It is missing AWS key, which you have yo put your own. You also have to make the inital database in AWS first. once its setup, populating can be automated through the DAG

First build in here
docker build -t my_airflow_image .

Run from here
docker run -d -p 8080:8080 my_airflow_image

Check if Dag is running
http://localhost:8080

Check if AWS if recieving the entries. Then you these entries for another purpose, or improve speed and processing.

## References:
https://airflow.apache.org/docs/apache-airflow/2.3.1/start/docker.html
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
Chatgpt also used to check understanding and logic of code. Also used at the start to understand documentation a bit better.

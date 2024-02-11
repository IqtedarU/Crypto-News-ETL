# Crypto-News-ETL-Database

This is a introductionary Project going through Data Mining and Sentiment Analysis. I mine data and get the title, date, content for a specific coin.
This used to be a project mainly looking into crypto news sentiment through pre-trained libraries. I am switching this into a Data Engineering project.
This is still in-progress as I just made the switch, but the plan it to go through the whole process to get the idea.

# Steps:

## Step 1: Data Retrieval 
Web-Scrape Data on the internet for cypto-news from sources. I currently have a few, but right now, I want this to automate and then get to adding more sources if needed.

## Step 2: Data Preprocessing
Clean the data in the format I want it to be. In this case it would be Ticker, date, Title of article, and then content of article.
additionally, I might consider adding the source as a column. 

## Step 3: Database design and integration
Since this is unstructered data, a NoSQL Database should be used. The Design can have different schemas, maybe sorting by each sources, but i will currently put in one. 

## Step 4: AWS automation and Pyspark
AWS is mainly to get experience on AWS and know more on how to use it. I will use it to automate the script, and populate the NoSQL database. 
Pyspark is also used for experience since having access to big data is hard.

## Step 5 Querying or future steps:
Mabe get into MongoDB to make queries for experience, or look more into on how to expand this project


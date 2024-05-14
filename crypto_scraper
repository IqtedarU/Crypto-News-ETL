import logging
from urllib.request import urlopen, Request
import os
import boto3 as boto3
import pyarrow
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

def scrape_articles():

    os.environ['AWS_ACCESS_KEY_ID'] = ''
    os.environ['AWS_SECRET_ACCESS_KEY'] = ''


    region_name = 'us-east-2'
    dynamodb = boto3.resource('dynamodb', region_name=region_name)


    table_name = 'Cryptocurrency-News-Database'
    table = dynamodb.Table(table_name)


    crypto_slate_url = 'https://cryptoslate.com/news/'

    # Webscrape for cryptoslate
    page_number = 100
    while True:
       try:
        # Open page of news article
        url = f'{crypto_slate_url}/page/{page_number}' if page_number > 1 else crypto_slate_url
        response = requests.get(url)
        if response.status_code != 200:
           print('error')
           break

       # Get area where News data are listed
        soup = BeautifulSoup(response.content, 'html.parser')
        # parse to get to featured news
        top_element = soup.find(id='top')
        news_archive_element = top_element.find(class_='news-archive')
        list_feed_element = news_archive_element.find(class_='list-feed slate')
        list_posts = list_feed_element.find_all(class_='list-post')

       # Go through Individual News Articles on Page
        for list_post in list_posts:
           title_element = list_post.find('h2')
           title = title_element.text.strip()
           # Extract the URL from the 'href' attribute of the 'a' tag
           url = list_post.find('a').get('href')
           # Find the tag and date within the 'post-meta' div
           post_meta = list_post.find('div', class_='post-meta')
           span_elements = post_meta.find_all('span')
           # Initialize the tag variable
           tag = None
           # Loop through the span elements and extract the tag
           for i, span in enumerate(span_elements):
               tag_text = span.text.strip()
               if tag_text.startswith('Contributor'):
                   if i + 1 < len(span_elements):
                       tag = span_elements[i + 1].text.strip()
                   # Exit the loop
                   break
               else:
                   tag = span_elements[0].text.strip()
           if(tag == 'Ad'): # not keeping any Ads
               continue
           # Check Duplicates
           response = table.get_item(
               Key={
                   'URL': url
               }
           )

           # If item with the same URL already exists, skip inserting it
           if 'Item' in response:
               print(f"Article with URL '{url}' already exists. Skipping insertion.")
               exit(0)
           # Check if article is not already in the set
           else:
               # Go to article page
               response2 = requests.get(url)
               if response2.status_code != 200:
                   print('error')
                   break

               soup = BeautifulSoup(response2.content, 'html.parser')
               article_top_element = soup.find(id='top')
               article_main = article_top_element.find(id='main')
               article_post_container = article_main.find(class_ = 'post-container')

               author_box = article_post_container.find(class_ = 'post-meta-single')
               author_info = author_box.find(class_='author-info')
               author = author_info.find("a").text
               date_time = author_info.find(class_ = 'post-date').text.split()  # Join components 3-5 as the date
               date, time = " ".join(date_time[0:3]), " ".join(date_time[4:6])

               article_post = article_post_container.find(class_ = 'post')
               article_post_content = article_post.find(class_ = 'post-box clearfix')
               if (article_post_content != None):
                post_content = article_post_content.find('div', {'data-mash-reactions': 'enabled'})
                text_content = ''
                for child in post_content.children:
                   if child.name == 'p':
                       # Extract text from <p> elements
                       text_content += child.get_text(separator=' ',
                                                      strip=True) + ' '  # Add space after each <p> element
                   elif child.name == 'blockquote':
                       # Extract text from <blockquote> elements
                       text_content += child.get_text(separator=' ',
                                                      strip=True) + ' '  # Add space after each <blockquote> element
                   elif child.name == 'a':
                       # Extract text from linked elements
                       linked_text = child.get_text(separator=' ', strip=True)
                       text_content += linked_text + ' '  # Add space after each linked element
                item = {
                    'Date': date,
                    'Time': time,
                    'Tag': tag,
                    'Free': 'False',
                    'Title': title,
                    'Content': text_content,
                    'URL': url

                }


                # Insert item into DynamoDB table
                table.put_item(Item=item)
               elif (article_post_content == None):
                article_post_content = article_post.find(class_='post-box clearfix cs-box') #Premium Content
                post_content = article_post_content.find('article')
                text_content = ''
                for child in post_content.children:
                   if child.name == 'p':
                       # Extract text from <p> elements
                       text_content += child.get_text(separator=' ',
                                                      strip=True) + ' '  # Add space after each <p> element

                #If item with the same URL already exists, skip inserting it
                if 'Item' in response:
                    print(f"Article with URL '{url}' already exists. Skipping insertion.")
                    exit(0)
                item = {
                   'Date': date,
                   'Time': time,
                   'Tag': tag,
                   'Free': 'True',
                   'Title': title,
                   'Content': text_content,
                   'URL': url

                }

            #Insert item into DynamoDB table
                table.put_item(Item=item)
        if( page_number == 1709):
           break
        page_number+=1
       except Exception as e:
        #  Any errors, skip adding and continue adding artciles
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"An error occurred at {current_datetime}: {str(e)}"
        logging.error(error_message)

        # If available, log additional information such as article URL, name, and page number
        if url:
            logging.error(f"Article URL: {url}")
        if title:
            logging.error(f"Article Name: {title}")
        if page_number:
            logging.error(f"Page Number: {page_number}")

        # Continue with the loop execution
        continue

if __name__ == "__main__":
    scrape_articles()

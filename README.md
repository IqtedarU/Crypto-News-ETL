# Crypto-News-Sentiment

This Is A introductionary Project going through Data Mining and Sentiment Analysis. I mine data and get the title, date, content for a specific coin. 

I then run a pretrained library to graph sentiments

This Model also compares the Log Returns with the average sentiment direction to see direction matches. The accuracy was %50, which Is expected because this is basically a random guess. There is no flats days in this which reduces accuracy. I will try to implement LDA or QDA to add this. Getting more data is another issue and some dates have no data because of the sources used. Ensuring data quality is also needed, because some data shows negative sentiment during a positive day.

Future Ideas:

  - Get more Data
  - See if this can be used as a signal to trade when new news comes out.(since it's general, get more specific)
  - See how long news reaction(if any) stay in the market and for how long
  - See how variations of the same news from different sources affect sentiment and markets
  - Use Finbert or other libraries and compare sentiments and see accuracy differences

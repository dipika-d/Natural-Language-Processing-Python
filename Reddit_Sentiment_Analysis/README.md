This script has two parts:
* **subredditscraper.py** makes a call to the website http://redditmetrics.com and scrapes the names of the top 100 subreddits at the given point of time and stores them in a text file. 
* **sentiment_analyzer.py** scrapes the top 100 comments in each subreddit from the 'hot' section and computes the overall sentiment of the subreddit 

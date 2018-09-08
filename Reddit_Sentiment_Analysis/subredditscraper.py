# Author : Dipika Desaboyina

# This is a script to scrape http://redditmetrics.com to get the names of all the top subreddits at a given point of time

from bs4 import BeautifulSoup
import urllib.request

url = urllib.request.urlopen("http://redditmetrics.com/top").read().decode('utf-8')
#print(url)

soup = BeautifulSoup(url,'html.parser')

with open('topsubreddits.txt','w') as f:
	for subreddit in soup.find_all('a'):
		try:
			if '/r' in subreddit.string:
				f.write(subreddit.string[3:]+'\n')
		except:
			TypeError 

# Author: Dipika Desaboyina
"""
This is a script that will take the list of top 100 subreddits, scrape the comments and output the net sentiment
in the subreddit. I am using the praw and textblob packages to scrape and analyze sentiment respectively.
"""

import praw
from textblob import TextBlob 
import math

# #insert your own client_id and clinet_secret obtained from https://www.reddit.com/prefs/apps
reddit = praw.Reddit(client_id="asdf",client_secret="asdf",user_agent="asdf") 

with open('topsubreddits.txt') as f:
	for line in f:
		subreddit = reddit.subreddit(line.strip())
		sub_submissions = subreddit.hot(limit=100) # taking the top 100 comments in the 'hot' section of each subreddit
		sub_sentiment = 0
		num_comments = 0
		net_sent = 0
		for submission in sub_submissions:
			if not submission.stickied:
				# this is make sure we don't stop at the inital comments
				# and that we get more than the top ones
				submission.comments.replace_more(limit=0) 
				for comment in submission.comments.list():
					blob = TextBlob(comment.body)
					# here we are obtaining the number of comments and sentiment per comment, later we're going to take 
					# an average of this to see what the overall sentiment is like 
					sub_sentiment = blob.sentiment.polarity
					#print(sub_sentiment)
					num_comments += 1
					net_sent += sub_sentiment

		ratio = net_sent/num_comments*100
		print(subreddit.display_name)
		try:
			print("Ratio: "+ratio)
		except:
			print('No comment sentiment')
			ZeroDivisionError 

"""
Output looks like this:
announcements
6.740830469727617
funny
5.204884174075801
AskReddit
5.81095886185114
todayilearned
6.120467900262697
science
5.670702922908796
worldnews
4.357127679128236
pics
9.107396933756341
"""

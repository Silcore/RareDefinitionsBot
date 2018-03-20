'''
Written by /u/SIllycore

This module is used as storage for the bot credentials when initializing a Reddit instance.
The necessary values are hidden from the Github repository to prevent external access to the bot.
'''

import praw

def login():
	reddit = praw.Reddit(
		user_agent = "Rare-Definitions: v1.0 (by /u/Sillycore)",
		client_id = "b4uHvPbegZuMbA",
		client_secret = "JbJVwESjoqi3niQyrWN2-nYupec",
		username = "ResourcefulRobot",
		password = "ZgnG^Z&&edw(7^z&)((@*4&bJ"
	)
	
	return reddit

# Provides a list of top 25 hottest threads from designated subreddit list.
def getThreads(reddit):
	# User-defined list of subreddits for the bot to check.
	subreddits = ["InforMe"]
	threads = []
	
	for name in subreddits:
		threads.extend(reddit.subreddit(name).hot(limit = 25))
	
	return threads

def getUsername():
	return "ResourcefulRobot"
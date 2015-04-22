import tweepy

def getApi():
	consumer_key = 'VCas6wXVF8oRqa6uoyKu5TGbE'
	consumer_secret = 'Wzsxl3GjFwuMvXyG77A74OjLghXvB0aqVwqOMhSigjNy8hBJeN'
	access_token = '3141936503-0YtwM3s8pCawkodRhbB1rVUpWaSz19VBO3oWvaF'
	access_token_secret = '81CU09s8gPSKHYK4FkU08ZVf9U1PtOeFKw2Elqc42xJ43'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return tweepy.API(auth)

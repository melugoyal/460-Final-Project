import tweepy,sys,time,datetime,operator

consumer_key = 'VCas6wXVF8oRqa6uoyKu5TGbE'
consumer_secret = 'Wzsxl3GjFwuMvXyG77A74OjLghXvB0aqVwqOMhSigjNy8hBJeN'

access_token = '3141936503-0YtwM3s8pCawkodRhbB1rVUpWaSz19VBO3oWvaF'
access_token_secret = '81CU09s8gPSKHYK4FkU08ZVf9U1PtOeFKw2Elqc42xJ43'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_id = 'courtneylmarin'

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
	 #   print tweet.text

tweets = api.user_timeline(id=user_id, count=200)
maxID = tweets[len(tweets)-1].id
while (1):
	response = api.user_timeline(id=user_id, count=200, max_id=maxID)
	tweets.extend(response) 
	if len(response) <= 1:
		break
	maxID = response[len(response)-1].id

tweets = [x for x in tweets if x.text[:2] != "RT"]
tweets = [x for x in tweets if x.place != None]

loc_dict = {}
date_dict = {}

for tweet in tweets:
	if tweet.place.name not in loc_dict:
		loc_dict[tweet.place.name] = 1
	else:
		loc_dict[tweet.place.name] = loc_dict[tweet.place.name] + 1
	date_dict[tweet.created_at] = tweet.place.name

home_location = max(loc_dict.iteritems(), key=operator.itemgetter(1))[0]

sorted_date_dict = sorted(date_dict.items(), key=operator.itemgetter(0))
last_date = sorted_date_dict[len(sorted_date_dict)-1][0]
last_location = sorted_date_dict[len(sorted_date_dict)-1][1]
current = datetime.datetime.now()

days = (current - last_date).days

print home_location
print last_location

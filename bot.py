import tweepy,sys,time,datetime,operator
from auth import getApi
import urllib, json
import pprint

api = getApi()

def getLocationData(username):

	user_id = username

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

	if not tweets:
		return None, None, None

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

	return home_location, last_location, days

def attack(username):
	home_location, last_location, days = getLocationData(username)
	if home_location == None or last_location == None:
		status = 'Victim: @' + username + '. Insufficient location data but he still got punked.' 
	else:
		robbing_chance = 100 - days
		if locator(home_location, last_location) == True or robbing_chance < 0:
			robbing_chance = 0
		status = 'Victim: @' + username + '. Location: ' + last_location + ' ' + str(days) + ' days ago. Home: ' + home_location + '. Robbing chances: ' + str(robbing_chance) + '%.'
	api.update_status(status=status)

def locator(loc1, loc2):
	URL2 = "http://maps.googleapis.com/maps/api/geocode/json?address="+loc1+"&sensor=false"
	googleResponse = urllib.urlopen(URL2)
	jsonResponse = json.loads(googleResponse.read())
	for iter in jsonResponse['results']:
		for location in iter['address_components']:
			if(location['long_name'] == loc2):
				return True

	URL2 = "http://maps.googleapis.com/maps/api/geocode/json?address="+loc2+"&sensor=false"
	googleResponse = urllib.urlopen(URL2)
	jsonResponse = json.loads(googleResponse.read())
	for iter in jsonResponse['results']:
		for location in iter['address_components']:
			if(location['long_name'] == loc1):
				return True

	return False

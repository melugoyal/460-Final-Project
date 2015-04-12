from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def loginTwitter(username, password):
	browser = webdriver.Firefox()
	browser.get('https://www.twitter.com')
	assert 'Twitter' in browser.title
	elem = browser.find_element_by_id('signin-email')
	elem.send_keys(username)
	elem2 = browser.find_element_by_id('signin-password')
	elem2.send_keys(password + Keys.RETURN)
	successful = 'Login' not in browser.title
	browser.quit()
	return successful

def tweet(username, password, tweet):
	browser = webdriver.Firefox()
	browser.get('https://www.twitter.com')
	assert 'Twitter' in browser.title
	elem = browser.find_element_by_id('signin-email')
	elem.send_keys(username)
	elem2 = browser.find_element_by_id('signin-password')
	elem2.send_keys(password + Keys.RETURN)
	elem3 = browser.find_element_by_id('tweet-box-home-timeline')
	elem3.click()
	elem3.send_keys(tweet)
	elem4 = browser.find_element_by_class_name('tweeting-text')
	elem4.click()
	browser.quit()

print loginTwitter('abcd', 'rr32r3r3')
print loginTwitter('robberbot', 'Class_Test_2015')
tweet('robberbot', 'Class_Test_2015', 'selenium is sick')

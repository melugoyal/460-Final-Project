from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def loginTwitter(username, password):
	browser = webdriver.PhantomJS(executable_path="./phantomjs") # we built phantomjs v2.0 locally, but any version should work
	browser.get('https://twitter.com')
	assert 'Twitter' in browser.title
	elem = browser.find_element_by_id('signin-email')
	elem.send_keys(username)
	elem2 = browser.find_element_by_id('signin-password')
	elem2.send_keys(password + Keys.RETURN)
	if 'Login' in browser.title:
		return False
	tweet = 'I just got punked by @robberbot. I solemnly swear to be more careful from now on.'
	elem3 = browser.find_element_by_id('tweet-box-home-timeline')
	elem3.click()
	elem3.send_keys(tweet)
	elem4 = browser.find_element_by_class_name('tweeting-text')
	elem4.click()
	return True

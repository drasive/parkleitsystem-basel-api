from collections import namedtuple
from datetime import datetime
import html

import requests
import xml.etree.ElementTree as etree


### Internal Methods
def _get_rss_feed(timeout):
	"""
	Returns an xml.etree element that represents the content of the RSS feed at
	http://www.parkleitsystem-basel.ch/rss_feed.php
	
	If the HTTP GET request fails or has a non successfull status code,
	an error is raised.
	
	The timeout parameter specifies the timeout of the HTTP GET request
	to the RSS feed in seconds.
	"""
	
	request = requests.get(
		"http://www.parkleitsystem-basel.ch/rss_feed.php", timeout=timeout)
	request.raise_for_status()
	
	return etree.fromstring(request.text)


def _parse_free_spaces(string):
	"""
	Parses the free spaces string and returns the free spaces as integer.
	
	Input example (without quotes): "Anzahl freie Parkpl&auml;tze: 134"
	"""
	
	last_space_index = string.rindex(" ")
	return int(string[last_space_index+1:])

def _parse_publishing_date(string):
	"""
	Parses the publishing date string and returns the publishing date
	as datetime.
	
	Input example (without quotes): "Wed, 09 Nov 2016 17:11:56 +0100"
	"""
	
	return datetime.strptime(string,"%a, %d %b %Y %H:%M:%S +0100")


### Public Methods
def get_car_parks(timeout):
	"""
	Retrieves the car park statuses from the officiel RSS feed at
	http://www.parkleitsystem-basel.ch/rss_feed.php and returns the parsed
	result as a named tuple
	(title:string, link:string, free_spaces:integer, last_update:datetime)
	
	The timeout parameter specifies the timeout of the HTTP GET request
	to the RSS feed in seconds.
	
	If the HTTP GET request fails or has a non successfull status code,
	an error is raised.
	"""
	
	# Get raw data
	rss_feed = _get_rss_feed(timeout)
	
	# Parse raw data
	car_parks = []
	
	for car_park_raw in rss_feed.findall("channel//item"):
		title = html.unescape(car_park_raw.findtext("title"))
		
		link = html.unescape(car_park_raw.findtext("link"))
		
		free_spaces_raw = html.unescape(car_park_raw.findtext("description"))
		free_spaces = _parse_free_spaces(free_spaces_raw)
		
		last_update_raw = html.unescape(car_park_raw.findtext("pubDate"))
		last_update = _parse_publishing_date(last_update_raw)
		
		# Instantiate named tuple
		CarPark = namedtuple('CarPark', ['title', 'link', "free_spaces", "last_update"])
		car_parks.append(CarPark(title, link, free_spaces, last_update))
	
	return car_parks

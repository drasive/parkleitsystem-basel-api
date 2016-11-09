# parkleitsystem-basel-api

A simple API for the Parkleitsystem (traffic routing system) in Basel, Switzerland.  
All information is retrieved from [http://www.parkleitsystem-basel.ch/rss_feed.php](http://www.parkleitsystem-basel.ch/rss_feed.php).

## Usage
The API currently only supports one method: ```get_car_parks(timeout)```  

It retrieves the car park statuses from the officiel RSS feed at [http://www.parkleitsystem-basel.ch/rss_feed.php](http://www.parkleitsystem-basel.ch/rss_feed.php)
and returns the parsed result as a named tuple:	(title:string, link:string, free_spaces:integer, last_update:datetime)  
	
The timeout parameter specifies the timeout of the HTTP GET request to the RSS feed in seconds.  
If the HTTP GET request fails or has a non successfull status code, an error is raised.

A usage example can be found in [example.py](example.py). 

## Installation
1. Place the file [parkleitsystem_basel_api.py](parkleitsystem_basel_api.py) in your project directory
2. Import the module into your python script with ```import parkleitsystem_basel_api``` 

## Requirements
- Python 3
- Python packages listed in [requirements.txt](requirements.txt)

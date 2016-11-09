# Import the module
import parkleitsystem_basel_api

# Retrieve the car park data
timeout = 30
car_parks = parkleitsystem_basel_api.get_car_parks(timeout)

# Sort the car parks by the amount of free spaces descending
car_parks.sort(key = lambda x: x.free_spaces, reverse=True)

# Output the car park attributes
for car_park in car_parks:
	print("\nTitle: " + car_park.title)
	print("Link: " + car_park.link)
	print("Free Spaces: " + str(car_park.free_spaces))
	print("Last Updated: " + car_park.last_update.strftime("%Y-%m-%d %H:%M:%S"))

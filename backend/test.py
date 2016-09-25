from flight import Flight
from places_integration import Places_Integration

flight = Flight(['2203', '2016-09-26'])

places = Places_Integration.placeList(flight, "entertainment")

print places[2].name

from flight import Flight
from duration import Duration
from terminal_time import Terminal_Time
from places_integration import Places_Integration
from weather_info import Weather_Info

flight = Flight(['2203', '2016-09-26'])

places = Places_Integration.placeList(flight, "entertainment")
duration = Duration.getDriveTime(flight)
terminal = Terminal_Time.terminalWaitList(flight)
weather = Weather_Info.getWeather(flight)

print places
print terminal
print duration
print weather

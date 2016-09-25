from flight import Flight
from duration import Duration
from terminal_time import Terminal_Time
from places_integration import Places_Integration
from weather_info import Weather_Info
from flight_dump import Flight_Dump

flight = Flight(['2203', '2016-09-26'])

places = Places_Integration.placeList(flight, "entertainment")
duration = Duration.getDriveTime(flight)
terminal = Terminal_Time.terminalWaitList(flight)
weather = Weather_Info.getWeather(flight)
flight_info = Flight_Dump.getFlightInfo(flight)

print places
print terminal
print duration
print weather
print flight_info

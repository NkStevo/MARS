from flight import Flight
from duration import Duration
from terminal_time import Terminal_Time
from places_integration import Places_Integration

flight = Flight(['2203', '2016-09-26'])

places = Places_Integration.placeList(flight, "entertainment")
duration = Duration.getDriveTime(flight)
terminal = Terminal_Time.terminalWaitList(flight)

print places[2].name
print terminal
print duration

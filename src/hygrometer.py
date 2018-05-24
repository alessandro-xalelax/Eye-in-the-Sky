import sys
import Adafruit_DHT
from datetime import datetime

sensor = Adafruit_DHT.DHT11

pin = 17

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

try:
    filepath = sys.argv[1]
except IndexError:
    print("No parameters passed")
    sys.exit(0)


datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filepath, "a") as f:
        f.write(now + " " + str(temperature) + " " + str(humidity) + "\n")

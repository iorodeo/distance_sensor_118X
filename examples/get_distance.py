"""
Performs a simple one shot distance measurement
"""
from distance_sensor_118X import DistanceSensor

sensor = DistanceSensor('/dev/ttyUSB0')
sensor.open()
value = sensor.getDistance(convert='float')
print 'Distance:', value
sensor.close()

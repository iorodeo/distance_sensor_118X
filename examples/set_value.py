"""
Example demonstrating how to set device values.
"""
from distance_sensor_118X import DistanceSensor

sensor = DistanceSensor('/dev/ttyUSB0')
sensor.open()

value = sensor.getDistOffset()
print 'Dist offset:', value

sensor.setDistOffset(10.0)
value = sensor.getDistOffset()
print 'Dist offset:', value

sensor.setDistOffset(0.0)
value = sensor.getDistOffset()
print 'Dist offset:', value

sensor.close()


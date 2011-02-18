
"""
Prints the values of the current settings in the device.
"""
from distance_sensor_118X import DistanceSensor

sensor = DistanceSensor('/dev/ttyUSB0')
sensor.open()
sensor.printSettings()
sensor.close()

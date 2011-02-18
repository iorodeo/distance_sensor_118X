"""
Querying the device for various values. Note, setting values is similar.
"""
from distance_sensor_118X import DistanceSensor

sensor = DistanceSensor('/dev/ttyUSB0')
sensor.open()

value = sensor.getDistance(convert='float')
print 'Distance:', value

value = sensor.getInternalTemp()
print 'Internal Temp:', value

value = sensor.getAveraging()
print 'Averaging:', value

value = sensor.getDisplayFormat()
print 'Display format:', value

value = sensor.getMeasurementTime()
print 'Measurement time:', value

value = sensor.getScaleFactor()
print 'Scale factor:', value

value = sensor.getErrorMode()
print 'Error mode:', value

value = sensor.getAlarmCenter()
print 'Alarm center:', value

value = sensor.getAlarmHysteresis()
print 'Alarm hysteresis:', value

value = sensor.getAlarmWidth()
print 'Alarm width:', value

value = sensor.getIoutBeginDist()
print 'Iout begin dist:', value

value = sensor.getIoutEndDist()
print 'Iout end dist:', value

value = sensor.getRemoveMeasurement()
print 'Remove measurement:', value

value = sensor.getRemoteTrig()
print 'Remote Trig:', value

value = sensor.getAutoStartTrig()
print 'AutoStartTrig:', value

value = sensor.getBaudrate()
print 'Baudrate:', value

value = sensor.getAutoStartCmd()
print 'AutoStartCmd:', value

value = sensor.getDistOffset()
print 'Dist offset:', value

sensor.close()

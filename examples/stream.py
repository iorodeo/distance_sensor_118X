"""
A simple example of streaming data from the sensor at 50Hz.
"""
import sys
from distance_sensor_118X import DistanceSensor
try:
    import pylab
    has_pylab = True
except:
    has_pylab = False

if len(sys.argv) > 1:
    N = int(sys.argv[1])
else:
    N = 100

scale_factor = 1000.0
sensor = DistanceSensor('/dev/ttyUSB0')
sensor.open()
sensor.setScaleFactor(scale_factor)
sensor.startDistTracking('50hz')

t = []
data = []
t_cur = 0.0

for i in range(0,N):
    value = sensor.readSample(convert='float')
    if not value is None:
        data.append(value/scale_factor)
    else:
        data.append(0.0)
    t.append(t_cur)
    t_cur += 0.02
    print t_cur, value 

sensor.laserOff()
sensor.close()

# If pylab is installed plot the data
if has_pylab:
    pylab.figure(1)
    pylab.plot(t,data)
    pylab.xlabel('time (s)')
    pylab.ylabel('distance (m)')
    pylab.show()


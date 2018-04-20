from cmps10 import *

compass = CMPS10()

compass.factoryReset()
#compass.calibrate()
#compass.changeAddress(0)

print "Version ",  compass.softwareVersion()
print "Bearing(255) ", compass.bearing255()
print "Bearing(360.0) ", compass.bearing3599()
print "Pitch ", compass.pitch()
print "Roll ", compass.roll()

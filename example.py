from cmps10 import *

compass = CMPS10()

compass.factoryReset()
compass.calibrate()
compass.changeAdress(0)

print compass.softwareVersion()
print compass.bearing255()
print compass.bearing3599()
print compass.pitch()
print compass.roll()
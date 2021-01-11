import time
import datetime
import bme680
import math

newTime = datetime.datetime.now()
sensor = bme680.BME680()

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_temp_offset(0.0)

if sensor.get_sensor_data():
    temperature = sensor.data.temperature
    pressure = sensor.data.pressure
    relHumidity = sensor.data.humidity
    temporary = math.exp(17.62*temperature/(243.12+temperature))
    absHumidity = 611200 * temporary * relHumidity / 46150 / (273.15 + temperature)
else:
    temperature = NaN
    pressure = NaN
    relHumidity = NaN
    absHumidity = NaN

#print(newTime)
#print('{:04.1f}*C {:04.1f}hPa {:04.1f}%rH'.format(temperature, pressure, humidity))

with open("/var/www/html/temp.json", "r") as file:
    oldStr = file.read()

newList = oldStr.split(',')
lastNum = newList[287].split(']')[0]
del newList[287]
del newList[0]
newList.append(lastNum)
newList.append(str('{:04.1f}'.format(temperature)))
newTempStr = "[" + ','.join(newList) + "]"

with open("/var/www/html/pressure.json","r") as file:
    oldStr = file.read()

newList = oldStr.split(',')
lastNum = newList[287].split(']')[0]
del newList[287]
del newList[0]
newList.append(lastNum)
newList.append(str('{:04.1f}'.format(pressure)))
newPressureStr = "[" + ','.join(newList) + "]"

with open("/var/www/html/absHumidity.json","r") as file:
    oldStr = file.read()

newList = oldStr.split(',')
lastNum = newList[287].split(']')[0]
del newList[287]
del newList[0]
newList.append(lastNum)
if (absHumidity<10.0):
    newList.append(str('{:04.2f}'.format(absHumidity)))
else:
    newList.append(str('{:05.2f}'.format(absHumidity)))

newAbsHumidityStr = "[" + ','.join(newList) + "]"

with open("/var/www/html/relHumidity.json","r") as file:
	oldStr = file.read()

newList = oldStr.split(',')
lastNum = newList[287].split(']')[0]
del newList[287]
del newList[0]
newList.append(lastNum)
newList.append(str('{:05.2f}'.format(relHumidity)))
newRelHumidityStr = "[" + ','.join(newList) + "]"

with open("/var/www/html/time.json","r") as file:
    oldStr = file.read()

newList = oldStr.split('},{')
lastTime = newList[287].split('}]')[0]
del newList[287]
del newList[0]
newList.append(lastTime)
newList.append(str(newTime.strftime("\"y\":\"%Y\",\"mnth\":\"%m\",\"d\":\"%d\",\"h\":\"%H\",\"mnte\":\"%M\"")))
newTimeStr = "[{" + '},{'.join(newList) + "}]"
with open("/var/www/html/time.json", "w") as file:
    file.write(newTimeStr)

with open("/var/www/html/temp.json","w") as file:
    file.write(newTempStr)

with open("/var/www/html/pressure.json","w") as file:
    file.write(newPressureStr)

with open("/var/www/html/absHumidity.json","w") as file:
    file.write(newAbsHumidityStr)

with open("/var/www/html/relHumidity.json","w") as file:
	file.write(newRelHumidityStr)

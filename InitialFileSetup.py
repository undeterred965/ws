#!/usr/bin/env python3

import time, datetime, random, bme680, math

initTime = datetime.datetime.now()
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

strInitTempC = str(temperature)
newStr = "[" + strInitTempC
for i in range(1,288):
    newStr = newStr + "," + strInitTempC

with open("/var/www/html/temp.json","w") as file:
    file.write(newStr + "]")

strInitPressure = str(pressure)
newStr = "[" + strInitPressure
for i in range(1,288):
    newStr = newStr + "," + strInitPressure

with open("/var/www/html/pressure.json","w") as file:
    file.write(newStr + "]")

strInitAbsHumidity = str(absHumidity)
newStr = "[" + strInitAbsHumidity
for i in range(1,288):
    newStr = newStr + "," + strInitAbsHumidity

with open("/var/www/html/absHumidity.json","w") as file:
    file.write(newStr + "]")

strInitRelHumidity = str(relHumidity)
newStr = "[" + strInitRelHumidity
for i in range(1,288):
	newStr = newStr + "," + strInitRelHumidity

with open("/var/www/html/relHumidity.json","w") as file:
	file.write(newStr + "]")

strInitTime = "{" + str(initTime.strftime("\"y\":\"%Y\",\"mnth\":\"%m\",\"d\":\"%d\",\"h\":\"%H\",\"mnte\":\"%M\"")) +"}"
newStr = "[" + strInitTime
for i in range(1,288):
    newStr = newStr + "," + strInitTime

with open("/var/www/html/time.json","w") as file:
    file.write(newStr + "]")


# Indoors Weather Station (ws)
### Monitors temperature, pressure, humidity
Weather Station webpages served by a Pi. Sensor is a BME680 by Pimoroni

The html and php files are placed in /var/www/html. The py and sh files are placed in /home/pi/scripts.

The webpages are served by Apache2 which must be setup along with the BME680 python library from Pimoroni.

The executable envDataToJson.sh must be called every 10 minutes so that the graphs will display 2 days worth of 'weather' data.

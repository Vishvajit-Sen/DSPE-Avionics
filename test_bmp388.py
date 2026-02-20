import time
import board
import busio
import adafruit_bmp3xx

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create BMP388 object
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

# Set sea level pressure (adjust if needed)
bmp.sea_level_pressure = 1013.25

while True:
    print("Temperature: %.2f C" % bmp.temperature)
    print("Pressure: %.2f hPa" % bmp.pressure)
    print("Altitude: %.2f meters" % bmp.altitude)
    print("-----------------------------")
    time.sleep(2)
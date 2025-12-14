import time
import board
import adafruit_fxos8700
from picamera2 import Picamera2
import time

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_fxos8700.FXOS8700(i2c)

camera = Picamera2()

while True:
    accel_x, accel_y, accel_z = sensor.accelerometer
    print('Acceleration (m/s^2): ({0:0.3f}, {1:0.3f}, {2:0.3f})'.format(accel_x, accel_y, accel_z))
    time.sleep(1.0)
    if accel_x >= 0.7 or accel_y >=0.7 or accel_z >= 0.7:
        print("imu shaking")
        time.sleep(3)
        camera.start()

        time.sleep(2)  # camera warm-up
        camera.capture_file("photo.jpg")

        camera.stop()


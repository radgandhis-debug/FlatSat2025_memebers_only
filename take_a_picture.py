from picamera2 import Picamera2
import time

camera = Picamera2()
camera.start()

time.sleep(2)          # camera warm-up
camera.capture_file("photo.jpg")

camera.stop()

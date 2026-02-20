from picamera2 import Picamera2
from time import sleep

#create a camera object
picam2 = Picamera2()

#configure for still capture
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, buffer_count=1)
picam2.configure(camera_config)

picam2.start()

#wait for the camera to adjust its light levels
sleep(2)

#capture the image
picam2.capture_file("test_photo.jpg")

picam2.stop()
print("Photo captured as test_photo.jpg")
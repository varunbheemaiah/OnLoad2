from picamera import PiCamera, Color



camera = PiCamera()
camera.rotation = 180
camera.vflip=True
#camera.hflip=True
camera.color_effects = (128,128)
camera.start_preview()
camera.image_effect = 'negative'
camera.start_preview()
i = 0
arr = []
try:
        while True:
        pass
except KeyboardInterrupt:
        pass
camera.stop_preview()

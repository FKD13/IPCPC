import urllib.request

import cv2
import numpy as np
from virtualvideo import FakeVideoDevice, VideoSource
import tqdm


class IPSource(VideoSource):
    def __init__(self, url: str):
        self.url: str = url
        self.bar = tqdm.tqdm(total=0, unit=' frames')
        self.image = self.get_image()

    def img_size(self):
        return self.image.shape[1], self.image.shape[0]

    def fps(self):
        return 30

    def get_image(self):
        resp = urllib.request.urlopen(self.url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        self.bar.set_description(f"{image.size} bytes")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        self.bar.update(1)
        return image

    def generator(self):
        while True:
            yield self.get_image()


fvd = FakeVideoDevice()
fvd.init_input(IPSource("http://192.168.178.22:8080/shot.jpg"))
fvd.init_output(0, 1280, 720, fps=20)
fvd.run()

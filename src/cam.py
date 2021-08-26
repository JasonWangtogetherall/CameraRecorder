import threading
import time
import cv2

from settings import WINDOW_HEIGHT, WINDOW_WIDTH, FPS, CAMERA_IP, CAMERA_PASSWORD, CAMERA_USER_NAME
from utils.logger import logger


class StreamerBase(threading.Thread):

    def __init__(self):
        super().__init__()
        self.frame = None
        self._stopped = threading.Event()
        self._stopped.clear()
        logger.debug(f"Initialized {self.__class__.__name__}")

    def read(self):
        return self.frame

    def stop(self):
        self._stopped.set()
        self.join(1)


class PTZcamStreamer(StreamerBase):

    def run(self) -> None:
        _cap = None
        while not self._stopped.is_set():
            if _cap is not None:
                ret, frame = _cap.read()
                if ret:
                    self.frame = frame
                else:
                    logger.error("Failed to grab video frame from web camera!")
                    self.frame = None
                    _cap = None
            else:
                _cap = cv2.VideoCapture(f"rtsp://{CAMERA_USER_NAME}:{CAMERA_PASSWORD}@{CAMERA_IP}")
                # _cap = cv2.VideoCapture(0)
                _cap.set(cv2.CAP_PROP_FRAME_WIDTH, WINDOW_WIDTH)
                _cap.set(cv2.CAP_PROP_FRAME_HEIGHT, WINDOW_HEIGHT)
                _cap.set(cv2.CAP_PROP_FPS, FPS)
                # _cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
            time.sleep(.01)
        if _cap is not None:
            _cap.release()

import multiprocessing
import threading
import time

from utils.logger import logger
from settings import FPS


class CamProcessor(threading.Thread):

    def __init__(self, cam=None, result_signal=None):
        super().__init__()
        self.cam = cam
        self.result_signal = result_signal
        self._b_stop = threading.Event()
        self._b_stop.clear()
        self.pool = multiprocessing.Pool(2)
        self._b_pause = threading.Event()
        self._b_pause.set()

    def run(self) -> None:
        while not self._b_stop.is_set():
            s_time = time.time()
            if self.is_paused():
                frame = self.cam.read()
                if frame is not None:
                    self.result_signal.emit({'frame': frame})

            elapsed = time.time() - s_time
            if elapsed < 1 / FPS:
                time.sleep((1 / FPS - elapsed) / 2.)

    def pause(self):
        logger.debug("=== Pausing Pill Detector")
        self._b_pause.set()

    def resume(self):
        logger.debug("=== Resuming Pill Detector")
        if self.is_paused():
            self._b_pause.clear()

    def is_paused(self):
        return self._b_pause.is_set()

    def stop(self):
        self.pause()
        self.cam.stop()
        self.cam.join(.5)
        self._b_stop.set()
        self.pool.close()
        self.pool.join()

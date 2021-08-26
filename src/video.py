import cv2
import qimage2ndarray

from PySide2 import QtGui
from PySide2.QtCore import QTimer, QSize
from settings import CAMERA_IP, CAMERA_USER_NAME, CAMERA_PASSWORD, FPS, WINDOW_WIDTH, WINDOW_HEIGHT


class VideoWidget:

    def __init__(self):
        super().__init__()

        # self.parent=parent
        self._frame = None
        self._stopped = False
        self.capture = cv2.VideoCapture(f"rtsp://{CAMERA_USER_NAME}:{CAMERA_PASSWORD}@{CAMERA_IP}")
        #self.capture = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.video_size = QSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setup_camera()

    def change_video_size(self,w,h):
        self.video_size = QSize(w, h)
        #self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        #self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
    
    def change_camera(self,camera_username,camera_password,camera_ip):
        if self.capture.isOpened():
            self.capture.release()
            self.timer.stop()
            self.timer.timeout.disconnect(self.get_video_frame)

        self.capture = cv2.VideoCapture(f"rtsp://{camera_username}:{camera_password}@{camera_ip}")
        self.setup_camera()

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())
        # cam_thread = threading.Thread(target=self.get_video_frame)
        # cam_thread.start()

        self.timer.timeout.connect(self.get_video_frame)
        self.timer.start(FPS)
        print("[INFO] Start Camera Capture")

    def get_video_frame(self):
        """
            Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        t_w, t_h = self.video_size.width(), self.video_size.height()
        frame = cv2.resize(frame, (t_w, t_h))

        template = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(template)
        self._frame = image.copy()

    def get_frame(self):
        return self._frame

    def hideEvent(self, event: QtGui.QHideEvent):
        self.timer.stop()
        super(VideoWidget, self).hideEvent(event)

    def pause(self):
        self._stopped = True

    def resume(self):
        self._stopped = False

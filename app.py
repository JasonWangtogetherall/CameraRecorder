import os
os.environ["QT_DRIVER"] = "PySide2"

import shutil
import sys
import time
import threading
import requests
import cv2
import qimage2ndarray

from PySide2.QtCore import QTimer, Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from queue import Queue
from functools import partial
from ui.ui_ptz_camera_controller import Ui_PTZCameraController
from src.dialog.settings import SettingsDialog
from src.video import VideoWidget
from utils.logger import logger
from settings import CAMERA_PASSWORD, CAMERA_USER_NAME, ICO_FILE_PATH, FPS, PRE_RECORD_SECS, MOVING_SPEED, ZOOM_SPEED, CAMERA_IP, WINDOW_HEIGHT, \
    WINDOW_WIDTH

from qt_material import apply_stylesheet

def hook_style():
    filename = apply_stylesheet.__code__.co_filename
    module_dir=os.path.dirname(filename)
    to_be_replaced = os.path.join(module_dir,'material.css.template')
   
    this_dir= os.path.dirname(os.path.realpath(__file__))
    replacee = os.path.join(this_dir,'material.css.template')
    shutil.copy(replacee, to_be_replaced)

class PTZController(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_PTZCameraController()

        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.ui.settings.clicked.connect(self.set_config)
        self.ui.record.clicked.connect(self.record_video)
        self.ui.pan_minus.pressed.connect(partial(self.control_pan, False))
        self.ui.pan_plus.pressed.connect(partial(self.control_pan, True))
        self.ui.tilt_minus.pressed.connect(partial(self.control_tilt, True))
        self.ui.tilt_plus.pressed.connect(partial(self.control_tilt, False))
        self.ui.zoom_minus.pressed.connect(partial(self.control_zoom, False))
        self.ui.zoom_plus.pressed.connect(partial(self.control_zoom, True))
        self.ui.pan_minus.released.connect(self.stop_pan_tilt)
        self.ui.pan_plus.released.connect(self.stop_pan_tilt)
        self.ui.tilt_minus.released.connect(self.stop_pan_tilt)
        self.ui.tilt_plus.released.connect(self.stop_pan_tilt)
        self.ui.zoom_minus.released.connect(self.stop_zoom)
        self.ui.zoom_plus.released.connect(self.stop_zoom)

        self.video_widget = VideoWidget()


        self.camera_ip = CAMERA_IP
        self.camera_pass = CAMERA_PASSWORD
        self.camera_username= CAMERA_USER_NAME

        self.moving_cmd = f"http://{self.camera_ip}/cgi-bin/ptzctrl.cgi?ptzcmd&"
        self.video_ret = False
        self.record_ret = False
        self.video_thread = None
        self.record_thread = None
        self.camera_width = WINDOW_WIDTH
        self.camera_height = WINDOW_HEIGHT
        self.record_file_path = ""
        self.pre_record_secs = PRE_RECORD_SECS
        self.pre_records = Queue(int(PRE_RECORD_SECS) * FPS)


        self.fps=FPS

        self.record_timeout= QTimer()
        self.record_timeout.timeout.connect(self.record_video)

        self.start_video_frame()
    
    def re_adjust_camera(self,camera_ip,camera_username,camera_pass):
        self.camera_ip = camera_ip
        self.camera_pass = camera_pass
        self.camera_username= camera_username
        self.moving_cmd = f"http://{self.camera_ip}/cgi-bin/ptzctrl.cgi?ptzcmd&"

        self.video_widget.change_camera(camera_username,camera_pass,camera_ip)


    def set_fps(self,fps):
        self.fps=fps
        global FPS
        FPS=self.fps

    def set_resolution(self,rw,rh):
        self.rw=rw
        self.rh=rh
        self.camera_width = rw
        self.camera_height= rh
        self.video_widget.change_video_size(rw,rh)

    def control_pan(self, direction):
        if direction:
            moving_url = f"{self.moving_cmd}up&{MOVING_SPEED}"
        else:
            moving_url = f"{self.moving_cmd}down&{MOVING_SPEED}"
        requests.get(moving_url)

    def control_tilt(self, direction):
        if direction:
            moving_url = f"{self.moving_cmd}left&{MOVING_SPEED}"
        else:
            moving_url = f"{self.moving_cmd}right&{MOVING_SPEED}"
        requests.get(moving_url)

    def control_zoom(self, direction):
        if direction:
            moving_url = f"{self.moving_cmd}zoomin&{ZOOM_SPEED}"
        else:
            moving_url = f"{self.moving_cmd}zoomout&{ZOOM_SPEED}"
        requests.get(moving_url)

    def stop_pan_tilt(self):
        time.sleep(0.1)
        stop_url = f"{self.moving_cmd}ptzstop"
        requests.get(stop_url)

    def stop_zoom(self):
        stop_url = f"{self.moving_cmd}zoomstop"
        requests.get(stop_url)

    def set_config(self):
        SettingsDialog(parent=self).exec_()

    def record_video(self):
        if self.record_file_path == "":
            QMessageBox.warning(self, "Warning", "Please set video file path to record by clicking setting icon")
        else:
            if not self.record_ret:
                QMessageBox.about(self, "Note", f"Recording Starts for {self.pre_record_secs} seconds...")

                self.record_ret = True
                self.record_timeout.setInterval((self.pre_record_secs-2)*1000)
                
                self.record_thread = threading.Thread(target=self.record_video_frame)
                self.record_thread.start()
                
                self.record_timeout.start()

                
            else:
                self.record_ret = False
                self.record_thread.join()
                QMessageBox.about(self, "Note", "Recording Ends...")
                self.record_timeout.stop()

                print(f"[INFO] Successfully saved into {self.record_file_path}")

    def record_video_frame(self):
        ext = self.record_file_path.split('.')[-1]
        if ext.lower().startswith('mp4'):
            codec=cv2.VideoWriter_fourcc(*'MP4V')
            #codec=cv2.VideoWriter_fourcc(*'DIVX')
        elif ext.lower().startswith('avi'):
            codec=cv2.VideoWriter_fourcc(*'XVID')

        out = cv2.VideoWriter(self.record_file_path, codec, FPS,
                              (self.camera_width, self.camera_height))
        while self.record_ret:
            if not self.pre_records.empty():
                recorded_frame = self.pre_records.get()
                if self.pre_records.qsize() <= self.pre_record_secs * FPS:
                    #print(f'size={self.pre_records.qsize()} | {self.pre_record_secs * FPS}')
                    nd_frame = qimage2ndarray.rgb_view(recorded_frame)
                    out.write(cv2.cvtColor(nd_frame, cv2.COLOR_RGB2BGR))
            time.sleep(0.001)
        out.release()

    def display_video_frame(self):
        while self.video_ret:
            frame = self.video_widget.get_frame()
            if frame is not None:
                if not self.pre_records.full():
                    self.pre_records.put(frame)
                    #print('==============')
                else:
                    self.pre_records.get()
                    self.pre_records.put(frame)
                    
                self.ui.video_frame.setPixmap(QPixmap.fromImage(frame))
            time.sleep(1 / FPS)

    def start_video_frame(self):
        """
            Read frame from camera and repaint QLabel widget.
        """
        self.video_ret = True
        self.video_thread = threading.Thread(target=self.display_video_frame)
        self.video_thread.start()

    def closeEvent(self, event):
        print("[INFO] End process...")
        self.video_widget.pause()
        self.video_ret = False
        self.record_ret = False
        if self.video_thread is not None:
            self.video_thread.join()
        if self.record_thread is not None:
            self.record_thread.join()

        event.accept()


if __name__ == '__main__':

    logger.info('========== Starting PTZCameraController Application ==========')

    sys._excepthook = sys.excepthook


    def exception_hook(exctype, value, tb):
        logger.error("=========== Crashed!", exc_info=(exctype, value, tb))
        getattr(sys, "_excepthook")(exctype, value, tb)
        sys.exit(1)


    sys.excepthook = exception_hook

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(ICO_FILE_PATH))
    THEME_LIGHT_XML='dark_blue.xml'
    hook_style()
    apply_stylesheet(app, theme=THEME_LIGHT_XML)
    ex = PTZController()
    ex.show()
    sys.exit(app.exec_())

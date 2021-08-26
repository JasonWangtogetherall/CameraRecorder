import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WSDL_DIR = os.path.join(BASE_DIR, 'utils', 'wsdl')

ICO_FILE_PATH = os.path.join(BASE_DIR, 'utils', 'ptz_camera.ico')

FPS = 20
PRE_RECORD_SECS = 20
WINDOW_WIDTH = 640#1920
WINDOW_HEIGHT = 480#1080
MOVING_SPEED = 20
ZOOM_SPEED = 5

CAMERA_IP = "192.168.100.101"
CAMERA_CONTROL_PORT = 80
CAMERA_USER_NAME = "guest"
CAMERA_PASSWORD = "Video for Artem!"
# CAMERA_IP = "192.168.1.6"
# CAMERA_CONTROL_PORT = 80
# CAMERA_USER_NAME = "admin"
# CAMERA_PASSWORD = "admin"

from PySide2.QtWidgets import QFileDialog
from ui.ui_settings import Ui_Settings
from src.dialog.base import DialogBase
from settings import CAMERA_IP, CAMERA_PASSWORD, CAMERA_USER_NAME, PRE_RECORD_SECS


class SettingsDialog(DialogBase):

    resolution_to_index ={
        1920:0,1280:1,640:2,320:3,
    }
    index_to_resoltion={
        0: (1920,1080),
        1: (1280,720),
        2: (640,480),
        3: (320,240),
    }
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.ui.pre_record.setText(str(PRE_RECORD_SECS))
        self.ui.file_path.setText(str(self.parent.record_file_path))
        self.ui.dlg_cancel.released.connect(self.close)
        self.ui.dlg_ok.released.connect(self.get_config)
        self.ui.file_browser.released.connect(self.set_record_file_path)
        
        self.latched_camera_data =()
        self.populate_defaults()

        

    def populate_defaults(self):
        self.ui.txt_fps.setText(str(self.parent.fps))
        self.ui.pre_record.setText(str(self.parent.pre_record_secs))
        self.ui.comboBox.setCurrentIndex(self.resolution_to_index[self.parent.camera_width])
        self.ui.txt_addr.setText(str(CAMERA_IP))
        self.ui.txt_user.setText(str(CAMERA_USER_NAME))
        self.ui.txt_password.setText(str(CAMERA_PASSWORD))


        camera_ip= str(self.ui.txt_addr.text())
        camera_username= str(self.ui.txt_user.text())
        camera_pass= str(self.ui.txt_password.text())

        self.latched_camera_data=(camera_ip,camera_username,camera_pass)

    def get_config(self):
        self.parent.pre_record_secs = int(self.ui.pre_record.text())
        self.parent.record_file_path = self.ui.file_path.text()

        fps=int(self.ui.txt_fps.text())
        self.parent.set_fps(fps)
        idx=self.ui.comboBox.currentIndex()

        self.parent.set_resolution(*self.index_to_resoltion[idx])
        camera_ip= str(self.ui.txt_addr.text())
        camera_username= str(self.ui.txt_user.text())
        camera_pass= str(self.ui.txt_password.text())

        if camera_ip!=self.latched_camera_data[0] or camera_username!=self.latched_camera_data[1] or camera_pass!=self.latched_camera_data[2]:
            self.parent.re_adjust_camera(camera_ip,camera_username,camera_pass)
            self.latched_camera_data=(camera_ip,camera_username,camera_pass)

        self.close()

    def set_record_file_path(self):
        file_name, _ = QFileDialog.getSaveFileName(self, caption="Record camera stream to File",
                                                   filter= "MP4 (*.mp4);;AVI(*.avi)"
                                                   )
        self.ui.file_path.setText(file_name)

import zeep
from onvif import ONVIFCamera
from settings import CAMERA_IP, CAMERA_CONTROL_PORT, CAMERA_USER_NAME, CAMERA_PASSWORD, WSDL_DIR
from sensecam_control import onvif_control

ptz = None
active = False


def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue


zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue


class CameraController:

    presets = []
    status = None

    def __init__(self):
        self.ptz_cam = onvif_control.CameraControl(CAMERA_IP, CAMERA_USER_NAME, CAMERA_PASSWORD)

    def get_current_preset(self):
        mycam = ONVIFCamera(CAMERA_IP, CAMERA_CONTROL_PORT, CAMERA_USER_NAME, CAMERA_PASSWORD, WSDL_DIR)
        # Create media service object
        media = mycam.create_media_service()
        print("setup_move {} {}", mycam, media)
        # Create ptz service object

        ptz_service = mycam.create_ptz_service()
        # Get target profile
        media_profile = media.GetProfiles()
        print(media_profile)
        profile_token = media_profile.token

        # GetStatus
        print("GetStatus")
        self.status = ptz_service.GetStatus({'ProfileToken': profile_token})
        print('status {} {} {}   ? => {}'.format(self.status.Position.PanTilt.x, self.status.Position.PanTilt.y,
                                                 self.status.Position.Zoom.x,
                                                 self.status.MoveStatus.PanTilt))

        return self.status.MoveStatus.PanTilt


if __name__ == '__main__':
    CameraController().get_current_preset()

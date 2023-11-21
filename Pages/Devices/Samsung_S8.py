import time

from Config.Helper import *
from Pages.Devices.BaseDevices import *
class samsung_SMG950F:

    def __init__(self,permission_page):
        self.RECORD_AUDIO_PERMISSION_SAMSUNG = None
        self.permission_page = permission_page
        self.Base_devices = BaseDevices(permission_page)

    def set_all_permissions_to_allow_v2(self):

        permissions = {
                         "Allow Asound to record audio?": self.Base_devices.set_allow_samsung,
                         "Allow Asound to make and manage phone calls?": self.Base_devices.set_allow_samsung,
                        "Allow Asound to access this device', \"'\", 's location?": self.Base_devices.set_allow_samsung,
                        "Usage access move": self.Base_devices.continue_special_access,
                        "Click On Asound":self.Base_devices.click_on_Asound,
                        "Widget": self.Base_devices.click_allow_usage_huawei_devices,
                        "Click On Asound!": self.Base_devices.click_on_Asound2,
                        "Allow?": self.Base_devices.set_allow_samsung,
                        "Back":self.permission_page.click_back,
        }

        if not self.permission_page.device["isQA"]:
            del permissions["permission photos media"]

        for key, to_do in permissions.items():
            print_title(key)
            if not to_do():
                return False
            time.sleep(2)

        if self.permission_page.check_current_page_activity(self.Base_devices.check_home_page_activity()):
            return True
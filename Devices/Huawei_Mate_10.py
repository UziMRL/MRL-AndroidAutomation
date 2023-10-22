from Pages.Devices.BaseDevices import *
class Huawei_Mate_10(BaseDevices):

    def __init__(self, permission_page):
        self.permission_page = permission_page
        self.Base_devices = BaseDevices(permission_page)



    def set_all_permissions_to_allow_v2(self):

        print_title("set_all_permissions_to_allow")
        if self.permission_page.device["isQA"]:
            permissions = {"permission photos media": self.Base_devices.set_permission_photos_media_allow_android_v9,
                           "permission to record audio": self.Base_devices.set_permission_to_record_audio_allow_samsung_devices,
                           "permission to make and manage phone calls": self.Base_devices.set_phone_calls_allow,
                           "permission to device location": self.Base_devices.set_location_allow,
                           "continue special access": self.Base_devices.continue_special_access,
                           "usage access for asound page 1/2": self.Base_devices.click_on_Asound,
                           "usage access for asound page 2/2": self.Base_devices.click_allow_usage_huawei_devices,
                           "click_back":self.permission_page.click_back,
                           "click_back_2": self.permission_page.click_back,
                           "click_ok":self.Base_devices.click_ok,
                           "click_back_3": self.permission_page.click_back,
                           "click_back_4": self.permission_page.click_back,
                           #"notification access page": self.Base_devices.click_on_Asound,
                          # "notification popup": self.Base_devices.set_allow_notification_popup
                           }

        for key, to_do in permissions.items():
            print_title(key)
            if "isCAP" in str(to_do.__code__.co_varnames):
                if not to_do(isCAP=True):
                    return False

            elif not to_do():
                return False
            time.sleep(2)

        if self.permission_page.check_current_page_activity("com.mobileresearchlabs.asound.HomeActivity"):
            return True
        return False




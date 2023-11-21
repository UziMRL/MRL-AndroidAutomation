

from Config.Helper import *
from Pages.Devices.BaseDevices import *
import time


class MI_POCO_F3:

    def __init__(self, permission_page):
        self.permission_page = permission_page
        self.Base_devices = BaseDevices(permission_page)

    def set_all_permissions_to_allow_v2(self):
        print_title("set_all_permissions_to_allow")
        permissions = {"permission photos media": self.Base_devices.set_permission_photos_media_allow,
                       "permission to record audio": self.Base_devices.set_permission_to_record_audio_allow,
                       "permission to make and manage phone calls": self.Base_devices.set_phone_calls_allow,
                       "permission to device location": self.Base_devices.set_location_allow,
                       "msg location collection": self.Base_devices.msg_location_after_allow,
                       "permission location all the time": self.Base_devices.set_location_permission_all_the_time,
                       "permission physical activity": self.Base_devices.set_physical_activity_permission_allow,
                       "continue special access": self.Base_devices.continue_special_access,
                       "usage access for asound":"usage_access",
                       "notification access for asound":"notification_access",
                       "auto start":self.Base_devices.auto_start_phones
                       }

        if not self.permission_page.device["isQA"]:
            del permissions["permission photos media"]

        for key, to_do in permissions.items():
            print_title(key)

            if type(to_do) == str:
                if not self.Base_devices.permission_for_mi_phones(to_do):
                    return False

            else:
                if "isCAP" in str(to_do.__code__.co_varnames):
                    if not to_do(isCAP=True):
                        return False

                else:
                    if not to_do():
                        return False

            time.sleep(2)

        if self.permission_page.check_current_page_activity(self.Base_devices.check_home_page_activity()):
            return True
        else:
            return False





    def set_all_permissions_to_allow(self):
        print_title("set_all_permissions_to_allow")
        permissions = {
            "permission_photos_media": {"to_check": self.permission_page.PHOTO_MEDIA_PERMISSION,
                                        "to_click": self.permission_page.click_allow},
            "permission_to_record_audio": {"to_check": self.permission_page.RECORD_AUDIO_PERMISSION,
                                           "to_click_by": self.permission_page.WHILE_USING_THE_APP_TEXT_CAP},
            "permission_to_phone_calls": {"to_check": self.permission_page.PHONE_CALL_PERMISSION,
                                          "to_click": self.permission_page.click_allow},
            "permission_to_device_location": {"to_check": self.permission_page.PERMISSION_TEXT_LOCATION_Android_11,
                                              "to_click_by": self.permission_page.WHILE_USING_THE_APP_TEXT_CAP},
            "msg location collection": {"to_check": self.permission_page.PERMISSION_TEXT_LOCATION_MSG,
                                        "to_click_by": self.permission_page.OK_TEXT_CAP},
            "permission_location_all_the_time": {"to_click_by": self.permission_page.ALLOW_ALL_THE_TIME_TEXT,
                                                 "go_back": self.permission_page.click_back},
            "permission_physical_activity": {"to_check": self.permission_page.PERMISSION_PHYSICAL_ACTIVITY,
                                             "to_click": self.permission_page.click_allow},
            "continue_special_access": {"to_check": self.permission_page.SPECIAL_ACCESS,
                                        "to_click_by": self.permission_page.AGREE_AND_CONTINUE_TEXT},
            "usage access page": {"to_check": self.permission_page.USAGE_PAGE_TEXT,
                                  "to_click_by": self.permission_page.APP_NAME},
            "usage access for asound": {"to_check": self.permission_page.USAGE_PAGE_TEXT,
                                        "to_click_by": self.permission_page.USAGE_PAGE_PERMIT,
                                        "to_click_aware":"",
                                        "to_click_ok": "",
                                        "go_back": self.permission_page.click_back},


            "notification access page": {"to_check": self.permission_page.NOTIFICATION_ACCESS,
                                         "to_click_by": self.permission_page.APP_NAME},
            "notification access for asound": {"to_check": self.permission_page.NOTIFICATION_ACCESS,
                                               "to_click_by": self.permission_page.PERMISSION_TEXT_NOTIFICATION_ACCESS,"to_click_aware":"",
                                        "to_click_ok": "","go_back": self.permission_page.click_back},
            'auto start permission': {
                                   "to_click_by": self.permission_page.APP_NAME,
                                   "go_back": self.permission_page.click_back}
        }
        if not self.permission_page.device["isQA"]:
            del permissions["permission_photos_media"]




        try:

            for key,permission in permissions.items():

                print_title(key)
                if "to_check" in permission:
                    if not self.permission_page.check_text(permission["to_check"]):
                        to_print = str(permission)
                        assert False

                if "to_click" in permission:
                        permission["to_click"](isCap=True)

                if "to_click_by" in permission:
                    self.permission_page.click_by(permission["to_click_by"],"txt")



                if "to_click_aware" in permission:
                    self.permission_page.click_by(
                        "com.miui.securitycenter:id/intercept_warn_content_end", "id")

                if "to_click_ok" in permission:
                    self.permission_page.click_by(self.permission_page.OK_TEXT_CAP, "txt")

                if "go_back" in permission:
                    permission["go_back"]()
                time.sleep(2)

            return True

        except AssertionError as e:
            print_failed(to_print)
            print_failed("function "+ self.set_all_permissions_to_allow.__name__)
            return False

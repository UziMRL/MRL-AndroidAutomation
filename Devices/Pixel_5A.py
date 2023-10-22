import time

from Config.Helper import *
from Pages.Devices.BaseDevices import *
class Pixel_5A:



    def __init__(self,permission_page):
        self.permission_page = permission_page
        self.Base_devices = BaseDevices(permission_page)

    def set_all_permissions_to_allow_v3(self):
        permissions = [
                       ("permission to record audio",self.Base_devices.set_permission_to_record_audio_allow),
                       ("permission to device location",self.Base_devices.set_location_allow),
                       ("msg location collection", self.Base_devices.msg_location_after_allow),
                       ("set permission location to all the time",self.Base_devices.set_location_permission_all_the_time),
                       ("permission physical activity",self.Base_devices.set_physical_activity_permission_allow),
                       ("permission find, connect to, and determine the relative position of nearby devices?",self.Base_devices.set_permission_nearby_device),
                       ("notification popup", self.Base_devices.set_allow_notifications_google),
                       ("continue special access", self.Base_devices.continue_special_access),
                       ("overlay permission", self.Base_devices.set_overlay_permission),
                       ("display over other apps", self.Base_devices.click_on_Asound),
                       ("set allow display over other apps", self.Base_devices.set_allow_display_over_other_apps),
                       ("usage access for asound page 1/2",self.Base_devices.click_on_Asound),
                       ("usage access for asound page 2/2", self.Base_devices.click_allow_usage),
                       ("notification access page", self.Base_devices.click_on_Asound),
                       ("notification popup", self.Base_devices.set_allow_notification_popup)
                       ]

        for permission in permissions:
            key=permission[0]
            func = permission[1]

            print_title(key)
            if not func():
                return False
            sleep_time_for(3)


        if not self.permission_page.check_current_page_activity(self.Base_devices.check_home_page_activity()):
            self.Base_devices.check_if_in_Asound_settings_page()
            self.permission_page.open_asound_from_background_v2()
        if self.permission_page.check_current_page_activity(self.Base_devices.check_home_page_activity()):
              return True

        return False




    def set_deny_audio_recording_v3(self):
        permissions = [
                       ("deny permission to record audio", self.Base_devices.set_permission_to_record_audio_deny,{"isCap":True}),
                       ("msg after deny",self.Base_devices.click_ok_msg_after_deny_audio),
                       ("deny permission to record audio", self.Base_devices.set_permission_to_record_audio_deny,{"isCap":True}),
                       ("msg after deny attempt 2", self.Base_devices.click_ok_msg_after_deny_audio_num_2),
                       ("check strict to app settings (app name)",self.Base_devices.check_if_in_Asound_settings_page)]


        for permission in permissions:
            key = permission[0]
            func = permission[1]
            if len(permission) > 2:
                extra = permission[2]
                print_title(key)
                if not func(extra["isCap"]):
                    return False
            else:
                print_title(key)
                if not func():
                    return False

        return True




    def set_deny_location_v2(self):
        permissions = [
                       ("permission to record audio", self.Base_devices.set_permission_to_record_audio_allow),
                       ("deny location permission",self.Base_devices.set_location_permission_dont_allow),
                       ("msg after deny location",self.Base_devices.msg_after_deny_location),
                       ("check strict to app settings (app name)", self.Base_devices.check_if_in_Asound_settings_page)]

        for permission in permissions:
            key = permission[0]
            func = permission[1]

            print_title(key)
            if not func():
                return False

        return True

    def set_deny_location(self):
        if self.permission_page.device["isQA"]:
            permissions = {
                "permission_photos_media": {"to_check": self.permission_page.PHOTO_MEDIA_PERMISSION,
                                            "to_click": self.permission_page.click_allow},
                "permission_to_record_audio": {"to_check": self.permission_page.RECORD_AUDIO_PERMISSION,
                                               "to_click_by": self.permission_page.WHILE_USING_THE_APP_TEXT},

                "permission_to_device_location": {"to_check": self.permission_page.PERMISSION_TEXT_LOCATION_Android_11,
                                                  "to_click_by": self.permission_page.DONT_ALLOW_CAP},
                "check strict to app settings (page)": {
                    "to_check": self.permission_page.MSG_AFTER_DENY_LOCATION,
                    "to_click_by": self.permission_page.OK_TEXT_CAP},
                "check strict to app settings (app name)": {"to_check": self.permission_page.APP_NAME}
            }

        try:

            for key, permission in permissions.items():

                print_title(key)
                if "to_check" in permission:
                    if not self.permission_page.check_text(permission["to_check"]):
                        to_print = str(permission)
                        assert False

                if "to_click" in permission:
                    permission["to_click"](isCap=False)

                if "to_click_by" in permission:
                    self.permission_page.click_by(permission["to_click_by"], "txt")

            return True

        except AssertionError as e:
            print_failed(str(e))
            return False



    def set_deny_physical_activity_v2(self):

        permissions = [
                       ("permission to record audio", self.Base_devices.set_permission_to_record_audio_allow),
                       ("permission to device location", self.Base_devices.set_location_allow),
                       ("msg location collection", self.Base_devices.msg_location_after_allow),
                       ("set permission location to all the time",self.Base_devices.set_location_permission_all_the_time),
                       ("set physical activity to deny",self.Base_devices.set_physical_activity_permission_dont_allow,{"isCap":True})]

        for permission in permissions:
            key = permission[0]
            func = permission[1]
            if len(permission) > 2:
                extra = permission[2]
                print_title(key)
                if not func(extra["isCap"]):
                    return False
            else:
                print_title(key)
                if not func():
                    return False

        return True



    def set_deny_appear_on_top(self):
        permissions = [("permission photos media", self.Base_devices.set_permission_photos_media_allow),
                       ("permission to record audio", self.Base_devices.set_permission_to_record_audio_allow),
                       ("permission to device location", self.Base_devices.set_location_allow),
                       ("msg location collection", self.Base_devices.msg_location_after_allow),
                       ("set permission location to all the time",
                        self.Base_devices.set_location_permission_all_the_time),
                       ("permission physical activity", self.Base_devices.set_physical_activity_permission_allow),
                       ("continue special access", self.Base_devices.continue_special_access),
                       ("overlay permission", self.Base_devices.set_overlay_permission),
                       ("go back",self.permission_page.click_back),
                       ("go back", self.permission_page.click_back),
                       ("usage_permission_deny_msg", self.Base_devices.check_if_usage_permission_deny_msg)]



        for permission in permissions:
            key = permission[0]
            func = permission[1]
            if len(permission) > 2:
                extra = permission[2]
                print_title(key)
                if not func(extra["isCap"]):
                    return False
            else:
                print_title(key)
                if not func():
                    return False

        return True
    def set_deny_usage(self):
        permissions = [("permission photos media", self.Base_devices.set_permission_photos_media_allow),
                       ("permission to record audio", self.Base_devices.set_permission_to_record_audio_allow),
                       ("permission to device location", self.Base_devices.set_location_allow),
                       ("msg location collection", self.Base_devices.msg_location_after_allow),
                       ("set permission location to all the time",
                        self.Base_devices.set_location_permission_all_the_time),
                       ("permission physical activity", self.Base_devices.set_physical_activity_permission_allow),
                       ("continue special access", self.Base_devices.continue_special_access),
                       ("overlay permission", self.Base_devices.set_overlay_permission),
                       ("display over other apps", self.Base_devices.click_on_Asound),
                       ("set allow display over other apps", self.Base_devices.set_allow_display_over_other_apps),
                       ("usage access for asound page 1/2", self.Base_devices.click_on_Asound),
                       ("go back", self.permission_page.click_back),
                       ("check usage msg after not giving permission",self.Base_devices.check_if_usage_permission_deny_msg),
                       ("go back", self.permission_page.click_back)]

        for permission in permissions:
            key = permission[0]
            func = permission[1]
            if len(permission) > 2:
                extra = permission[2]
                print_title(key)
                if not func(extra["isCap"]):
                    return False
            else:
                print_title(key)
                if not func():
                    return False

        return True

    def set_deny_notification(self):
        permissions = [("permission photos media", self.Base_devices.set_permission_photos_media_allow),
                       ("permission to record audio", self.Base_devices.set_permission_to_record_audio_allow),
                       ("permission to device location", self.Base_devices.set_location_allow),
                       ("msg location collection", self.Base_devices.msg_location_after_allow),
                       ("set permission location to all the time",
                        self.Base_devices.set_location_permission_all_the_time),
                       ("permission physical activity", self.Base_devices.set_physical_activity_permission_allow),
                       ("continue special access", self.Base_devices.continue_special_access),
                       ("overlay permission", self.Base_devices.set_overlay_permission),
                       ("display over other apps", self.Base_devices.click_on_Asound),
                       ("set allow display over other apps", self.Base_devices.set_allow_display_over_other_apps),
                       ("usage access for asound page 1/2", self.Base_devices.click_on_Asound),
                       ("usage access for asound page 2/2", self.Base_devices.click_allow_usage),
                       ("go back", self.permission_page.click_back),
                       ("check notification msg after not giving permission",self.Base_devices.check_if_notification_deny_msg),
                       ("go back", self.permission_page.click_back)
                       ]

        for permission in permissions:
            key = permission[0]
            func = permission[1]
            if len(permission) > 2:
                extra = permission[2]
                print_title(key)
                if not func(extra["isCap"]):
                    return False
            else:
                print_title(key)
                if not func():
                    return False

        if self.permission_page.check_current_page_activity(self.Base_devices.check_home_page_activity()):
            return True

        return False
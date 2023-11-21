
from Config.Helper import *
import time

class BaseDevices:
    def __init__(self, permission_page):
        self.RECORD_AUDIO_PERMISSION_SAMSUNG = None
        self.permission_page = permission_page

    def check_home_page_activity(self):
        if self.permission_page.IS_QA:
            HOME_PAGE_ACTIVITY = "com.mobileresearchlabs.asound.HomeActivity"
            if self.permission_page.IS_KOTLIN:
                HOME_PAGE_ACTIVITY = "com.mobileresearchlabs.asound.ui.HomeActivity"

        else:
            HOME_PAGE_ACTIVITY = ".HomeActivity"


        return HOME_PAGE_ACTIVITY

    def set_permission_photos_media_allow(self,isCAP=False):
        if self.permission_page.check_text(self.permission_page.PHOTO_MEDIA_PERMISSION):
            if self.permission_page.click_allow(isCap=isCAP):
                return True

        return False

    def set_permission_photos_media_allow_android_v9(self,isCAP=False):
        if self.permission_page.check_text(self.permission_page.PHOTO_MEDIA_PERMISSION_Android_v9):
            if self.permission_page.click_allow(isCap=isCAP):
                return True

        return False

    def set_allow_samsung(self,isCAP=False):
        if self.permission_page.check_text(self.permission_page.RECORD_AUDIO_PERMISSION_SAMSUNG):
            if self.permission_page.click_allow(isCap=isCAP):
                return True

        return False

    def set_usage_access_samsung(self,isCAP=False):
        if self.permission_page.check_text(self.permission_page.SAMSUNG_USAGE_ACCESS_CONTINUE):
            if self.permission_page.click_allow(isCap=isCAP):
                return True

        return False

    def set_permission_to_record_audio_allow(self,isCAP=False):
        if self.permission_page.check_text(self.permission_page.RECORD_AUDIO_PERMISSION):
            if isCAP:
                if self.permission_page.click_by(self.permission_page.WHILE_USING_THE_APP_TEXT_CAP,"txt"):
                    return True
            else:
                if self.permission_page.click_by(self.permission_page.WHILE_USING_THE_APP_TEXT,"txt"):
                    return True

        return False

    def set_permission_to_record_audio_deny(self,isCAP=False):
        if self.permission_page.check_text(self.permission_page.RECORD_AUDIO_PERMISSION):

            if self.permission_page.click_by(self.permission_page.DONT_ALLOW_RES_ID,"id") or self.permission_page.click_by(self.permission_page.DONT_ALLOW_RES_ID_V2, "id"):
                return True

            if isCAP:
                if self.permission_page.click_by(self.permission_page.DONT_ALLOW_CAP, "txt") or self.permission_page.click_by(self.permission_page.DONT_ALLOW_CAP.upper(), "txt") or self.permission_page.click_by(self.permission_page.DONT_ALLOW_CAP_v2,"txt") or self.permission_page.click_by(self.permission_page.DONT_ALLOW_CAP_v2.upper(),"txt") :
                    return True
            else:
                if self.permission_page.click_by(self.permission_page.DONT_ALLOW, "txt"):
                    return True

        return False


    def click_ok_msg_after_deny_audio(self):

        if self.permission_page.check_text(self.permission_page.MSG_AFTER_DENY_RECODING):
            if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP, "txt"):
                return True
        return False

    def click_ok_msg_after_deny_audio_num_2(self):
        if self.permission_page.check_text(self.permission_page.MSG_AFTER_DENY_RECODING_TO_SETTINGS):
            if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP, "txt"):
                return True
            return False

    def set_permission_to_record_audio_allow_samsung_devices(self,isCAP=False):
        if self.permission_page.check_text(self.permission_page.RECORD_AUDIO_PERMISSION):
            if self.permission_page.click_allow(isCAP):
                return True

        return False

    def set_phone_calls_allow(self,isCAP=False):

        if self.permission_page.check_text(self.permission_page.PHONE_CALL_PERMISSION):
            if self.permission_page.click_allow(isCap=isCAP):
                 return True

        return False

    def set_location_allow(self,isCAP=False):
        if self.permission_page.check_text(self.permission_page.PERMISSION_TEXT_LOCATION_Android_11,timeout=5) or \
                self.permission_page.check_text(self.permission_page.PERMISSION_TEXT_LOCATION_Android_10,timeout=5) or \
                self.permission_page.check_text(self.permission_page.PERMISSION_TEXT_LOCATION_Android_08,timeout=5) or\
                self.permission_page.check_text_by_res_id(self.permission_page.LOCATION_RES_ID,timeout=5):
            if isCAP:
                if self.permission_page.click_by(self.permission_page.WHILE_USING_THE_APP_TEXT_CAP, "txt"):
                    return True

                elif self.permission_page.click_allow(isCAP):
                    return True

            else:
                if self.permission_page.click_by(self.permission_page.WHILE_USING_THE_APP_TEXT, "txt"):
                    return True

                elif self.permission_page.click_allow(isCAP):
                    return True

        return False



    def set_location_permission_all_the_time(self):

        if self.permission_page.click_by(self.permission_page.ALLOW_ALL_THE_TIME_TEXT,"txt"):
            if self.permission_page.click_back():
                return True
        return False

    def msg_location_after_allow(self):
        if self.permission_page.check_text(self.permission_page.PERMISSION_TEXT_LOCATION_MSG) :
            if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP, "txt"):
                return True
        return False

    def set_location_permission_dont_allow(self,isCAP=False):

        if self.permission_page.check_text(self.permission_page.PERMISSION_TEXT_LOCATION_Android_11):
            if self.permission_page.click_by(self.permission_page.DONT_ALLOW_CAP,"txt") or self.permission_page.click_by(self.permission_page.DONT_ALLOW_RES_ID,"id"):
                return True

        return False

    def msg_after_deny_location(self):

        if self.permission_page.check_text(self.permission_page.MSG_AFTER_DENY_LOCATION):
            if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP,"txt"):
                return True
        return False



    def set_physical_activity_permission_allow(self,isCAP=False):

        if self.permission_page.check_text(self.permission_page.PERMISSION_PHYSICAL_ACTIVITY):
            if self.permission_page.click_allow(isCap=isCAP):
                return True

        return False

    def set_physical_activity_permission_dont_allow(self,isCAP=False):
        if self.permission_page.check_text(self.permission_page.PERMISSION_PHYSICAL_ACTIVITY):
            self.permission_page.print_current_page_source()
            if self.permission_page.click_by(self.permission_page.DONT_ALLOW_CAP,"txt") or self.permission_page.click_by(self.permission_page.DONT_ALLOW_CAP_v2,"txt"):
                return True

        return False

    def continue_special_access(self):

        if self.permission_page.check_text(self.permission_page.SPECIAL_ACCESS):
            self.permission_page.scroll_down()
            if self.permission_page.click_by(self.permission_page.AGREE_AND_CONTINUE_TEXT,"txt"):
                return True

        return False



    def click_on_Asound(self):
        if self.permission_page.click_by(self.permission_page.APP_NAME, "txt"):
            return True
        elif self.permission_page.click_by(self.permission_page.APP_PACKAGE_NAME, "txt"):
            return True
        return False
        return False
    def click_information(self):
        if self.permission_page.click_by(self.InformationPage, "txt"):
            if self.permission_page.click_back():
                return True
        return False
    def click_on_Asound2(self):
        if self.permission_page.click_by(self.permission_page.APP_NAME, "txt"):
            return True
        return False
    def click_ok(self):
        if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP,"txt"):
            return True
        return False

    def click_allow_usage(self):
        if self.permission_page.click_by(self.permission_page.USAGE_PAGE_PERMIT, "txt"):
            if self.permission_page.click_back():
                return True
        return False

    def click_allow_usage_google(self):
        if self.permission_page.click_by(self.permission_page.USAGE_PAGE_PERMIT_3, "txt"):
            if self.permission_page.click_back():
                return True
        return False


    def click_allow_usage_samsung_devices(self):
        if self.permission_page.click_by(self.permission_page.USAGE_PAGE_PERMIT_2, "txt"):
            if self.permission_page.click_back():
                return True
        return False

    def click_allow_usage_huawei_devices(self):
        if self.permission_page.click_by(self.permission_page.USAGE_PAGE_ALLOW_ID,"id"):
            time.sleep(10)

            if self.permission_page.click_back():
                return True
        return False


    def set_allow_notifications_google(self, isCAP=False):
        if self.permission_page.check_text(self.permission_page.NOTIFICATION_POPUP_ALLOW,
                                           timeout=10) or self.permission_page.check_text(
                self.permission_page.NOTIFICATION_POPUP_ALLOW, timeout=10):
            if self.permission_page.click_allow(isCap=isCAP):
                return True
        return False
    def set_allow_notification_popup(self,isCAP=False):

        if self.permission_page.click_by(self.permission_page.PERMISSION_TEXT_NOTIFICATION_ACCESS, "txt"):
            if self.permission_page.click_allow(isCap=isCAP):
                time.sleep(2)
                if self.permission_page.click_back():
                    return True

        if self.permission_page.click_allow(isCap=isCAP):
            time.sleep(2)
            if self.permission_page.click_back():
                return True
        return False

    def usage_access_mi_phones(self):
        if self.permission_page.check_text(self.permission_page.USAGE_PAGE_TEXT):
            if self.click_on_Asound():
                if self.permission_page.click_by(self.permission_page.USAGE_PAGE_PERMIT, "txt"):
                    if self.permission_page.click_by("com.miui.securitycenter:id/intercept_warn_content_end", "id"):
                        if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP,"txt"):
                            if self.permission_page.click_back():
                                return True
        return False

    def permission_for_mi_phones(self,permission_type):

        if permission_type == "usage_access":
            to_check = self.permission_page.USAGE_PAGE_TEXT
            to_click = self.permission_page.USAGE_PAGE_PERMIT

        elif permission_type == "notification_access":
            to_check = self.permission_page.NOTIFICATION_ACCESS
            to_click = self.permission_page.PERMISSION_TEXT_NOTIFICATION_ACCESS

        if self.permission_page.check_text(to_check):
            if self.click_on_Asound():
                 if self.permission_page.click_by(to_click, "txt"):
                    if self.permission_page.click_by("com.miui.securitycenter:id/intercept_warn_content_end", "id"):
                        if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP, "txt"):
                             if self.permission_page.click_back():
                                return True
        return False

    def auto_start_phones(self):
        if self.click_on_Asound():
            if self.permission_page.click_back():
                return True
        return False

    def set_overlay_permission(self):
        if self.permission_page.check_text(self.permission_page.MSG_OVERLAY_PERMISSION):
            if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP,"txt"):
                return True
        return False
    def set_allow_display_over_other_apps(self):
        if self.permission_page.click_by(self.permission_page.ALLOW_DISPLAY_OVER_OTHER_APPS,"txt"):
            if self.permission_page.click_back():
                self.permission_page.click_back()
                return True
        return False

    def check_if_in_Asound_settings_page(self):

        if self.permission_page.check_text(self.permission_page.APP_NAME) and self.permission_page.check_content_desc(self.permission_page.APP_INFO_STRCIT):
            return True
        return False

    def check_if_audio_record_permission_deny_msg(self):
        if self.permission_page.check_text(self.permission_page.MSG_AFTER_DENY_RECODING):
            if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP,"txt"):
                return True
        return False

    def check_if_audio_record_permission_deny_to_settings(self):
        if self.permission_page.check_text(self.permission_page.MSG_AFTER_DENY_RECODING_TO_SETTINGS):
            if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP,"txt"):
                return True
        return False

    def check_if_usage_permission_deny_msg(self):
        if self.permission_page.check_text(self.permission_page.USAGE_MSG_AFTER_DENY):
            if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP, "txt"):
                return True
        return False

    def check_if_notification_deny_msg(self):
        if self.permission_page.check_text(self.permission_page.NOTIFICATION_ACCESS_PERMISSION_POPUP):
            if self.permission_page.click_by(self.permission_page.OK_TEXT_CAP, "txt"):
                return True
        return False

    def set_permission_nearby_device(self,isCAP=False):
        if self.permission_page.check_text(self.permission_page.NEARBY_DEVICES_PERMISSION,timeout=10) or self.permission_page.check_text(self.permission_page.NEARBY_DEVICES_PERMISSION_V2,timeout=10):
            if self.permission_page.click_allow(isCap=isCAP):
                return True
        return False



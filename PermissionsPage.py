from Pages.StartPage import *
from Config.configuration import *
import pytest
from Pages.Devices.Sony import *
from Pages.Devices.Pixel_5A import *
from Pages.Devices.MI_POCO_F3 import *
from Pages.Devices.Pixel_3A import *
from Pages.Devices.Samsung_S8 import *
from Pages.Devices.Nokia_G10 import *
from Pages.Devices.Huawei_Mate_10 import *


class PermissionsPage(StartPage):
    PHOTO_MEDIA_PERMISSION = "Allow Asound to access photos and media on your device?"
    PHOTO_MEDIA_PERMISSION_Android_v9 = "Allow Asound to access photos, media, and other files on your device?"
    RECORD_AUDIO_PERMISSION = "Allow Asound to record audio?"
    RECORD_AUDIO_PERMISSION_SAMSUNG = "Allow"
    PHONE_CALL_PERMISSION = "Allow Asound to make and manage phone calls?"

    PERMISSION_TEXT_LOCATION_Android_11 = """Allow Asound to access this device’s location?"""
    PERMISSION_TEXT_LOCATION_Android_10 = """Allow Asound to access this device's location?"""
    PERMISSION_TEXT_LOCATION_Android_08 = "Allow Asound to access this device's location?"
    LOCATION_RES_ID = "com.android.packageinstaller:id/permission_message"
    PERMISSION_TEXT_LOCATION_MSG = "This app collects location data to allow us to visualize your sound exposure on a map." \
                                   " Location will be captured even when the app is in the background"
    PRECISE_LOCATION = "Precise"
    APPROXIMATE_LOCATION = "Approximate"

    USAGE_PERMISSION_TEXT = "Usage data access"
    USAGE_PAGE_TEXT = "Usage access"
    USAGE_PAGE_PERMIT = "Permit usage access"
    USAGE_PAGE_PERMIT_2 = "Allow usage tracking"
    USAGE_PAGE_PERMIT_3 = "Usage access"
    USAGE_PAGE_ALLOW = "Allow usage access"
    USAGE_PAGE_ALLOW_ID = "android:id/switch_widget"
    USAGE_MSG_AFTER_DENY = "Asound must have Usage access permission in order to stop recording when another app requests the microphone."

    PERMISSION_PHYSICAL_ACTIVITY = "Allow Asound to access your physical activity?"

    SPECIAL_ACCESS = "Special Access"
    BODY_TEXT_SPECIAL_ACCESS = "IMPORTANT The following Access Permissions require us to redirect you to your device&apos;s setting." \
                               " Please find Asound in the list of apps and toggle "'ON'" the permission.&#10;&#10;" \
                               "After allowing each permission please return to the app using the "'Back'" button.\n\nIf you get lost you can always return to the app by clicking the Asound icon on your home screen."
    USAGE_ACCESS_SPECIAL_ACCESS = "Usage Access - To seamlessly allow you to use other apps without interference"
    NOTIFICATION_SPECIAL_ACCESS = "Notification Access - To release the microphone for VOIP calls from your favorite messaging apps"

    NEARBY_DEVICES_PERMISSION = "Allow Asound to find, connect to, and determine the relative position of nearby devices?"
    NEARBY_DEVICES_PERMISSION_V2 = "Allow Asound to find, connect to and determine the relative position of nearby devices?"
    SAMSUNG_USAGE_ACCESS_CONTINUE = "Agree & Continue"
    MSG_OVERLAY_PERMISSION = "Asound must have Manage Overaly permission in order to start the app when reboot."
    ALLOW_DISPLAY_OVER_OTHER_APPS = "Allow display over other apps"

    PERMISSION_TEXT_NOTIFICATION_ACCESS = "Allow notification access"
    NOTIFICATION_ACCESS = "Notification access"
    NOTIFICATION_POPUP_ALLOW = "Allow"
    NOTIFICATION_ACCESS_ANDROID_12 = "Device & app notifications"
    NOTIFICATION_ACCESS_TITLE_MSG = "Allow Asound to send you notifications?"
    NOTIFICATION_ACCESS_TITLE_Body = ""
    NOTIFICATION_ACCESS_PERMISSION_POPUP = "Asound would like you to allow it notification access, this is to allow it to make sure it does not interfere with incoming VOIP calls from your favorite messaging apps."

    # MSG AFTER DENY RECORDING
    MSG_AFTER_DENY_RECODING = "For the successful operation of this app we require certain access permissions.\n" \
                              "We respect your privacy and would like to assure that none of the Information is saved nor is it sent over the internet."
    MSG_AFTER_DENY_RECODING_TO_SETTINGS = "Asound must have recording audio permission, please go to settings to allow this permission and restart the app"

    # MSG AFTER DENY PHONE CALL
    MSG_AFTER_DENY_PHONE_CALL = "The following permission is needed to assure the Asound will not interfere in phone calls"
    MSG_AFTER_DENY_PHONE_CALL_TO_SETTINGS = "Asound must have manage phone calls permission in order to stop recording while a phone call is in progress, please go to settings to allow this permission and restart the app"
    # Settings of app
    APP_INFO_SETTINGS = "App info"

    # MSG AFTER DENY LOCATION
    MSG_AFTER_DENY_LOCATION = "To visualize the sound data on a map, Asound must have access to your location as always on, we recommend you tap setting to allow/adjust this permission."

    def __init__(self, driver, device_name, run_begin=True):
        super().__init__(driver, device_name)
        if run_begin:
            if not self.run_beginning_until_permission_page():
                assert False

    def run_set_allow_all_permissions_by_device(self):

        if self.DEVICE_NAME == "Sony_XQ-AU52":
            if Sony(self).set_all_permissions_to_allow_v3():
                return True

        elif self.DEVICE_NAME == "google_Pixel_5a":
            if Pixel_5A(self).set_all_permissions_to_allow_v3():
                # self.open_asound_from_home()
                return True

        elif self.DEVICE_NAME == "pixel_3a":
            if Pixel_3A(self).set_all_permissions_to_allow_v2():
                # self.open_asound_from_home()
                return True

        elif self.DEVICE_NAME == "mi_poco":
            if MI_POCO_F3(self).set_all_permissions_to_allow_v2():
                return True

        elif self.DEVICE_NAME == "samsung_SM-G950F":
            if samsung_SMG950F(self).set_all_permissions_to_allow_v2():
                return True

        elif self.DEVICE_NAME == "nokia_g10":
            if Nokia_G10(self).set_all_permissions_to_allow_v2():
                return True

        elif self.DEVICE_NAME == "huawei_mate_10":
            if Huawei_Mate_10(self).set_all_permissions_to_allow_v2():
                return True
        else:
            print_warning(self.DEVICE_NAME + " not implemented ")

        return False

    def run_set_permission_record_audio_deny_by_device(self):

        if self.DEVICE_NAME == "Sony_XQ-AU52":
            if Sony(self).set_deny_audio_recording_v2():
                return True
        elif self.DEVICE_NAME == "google_Pixel_5a":
            if Pixel_5A(self).set_deny_audio_recording_v3():
                return True
        else:
            print_warning(self.DEVICE_NAME + " not implemented yet")

        return False

    def run_set_permissions_phone_calls_deny_by_device(self):
        if self.DEVICE_NAME == "Sony_XQ-AU52":
            if Sony(self).set_deny_phone_calls():
                return True


        else:
            print_warning(self.DEVICE_NAME + " not implemented yet")

        return False

    def run_set_permissions_location_deny_by_device(self):
        if self.DEVICE_NAME == "Sony_XQ-AU52":
            if Sony(self).set_deny_location_v2():
                return True
        elif self.DEVICE_NAME == "google_Pixel_5a":
            if Pixel_5A(self).set_deny_location_v2():
                return True
        else:
            print_warning(self.DEVICE_NAME + " not implemented yet")
        return False

    def run_set_permissions_physical_activity_deny_by_device(self):
        if self.DEVICE_NAME == "Sony_XQ-AU52":
            if Sony(self).set_deny_physical_activity_v2():
                return True
        elif self.DEVICE_NAME == "google_Pixel_5a":
            if Pixel_5A(self).set_deny_physical_activity_v2():
                return True
        else:
            print_warning(self.DEVICE_NAME + " not implemented yet")
        return False

    def run_set_permission_appear_on_top_deny_by_device(self):

        if self.DEVICE_NAME == "google_Pixel_5a":
            if Pixel_5A(self).set_deny_appear_on_top():
                return True
        elif self.DEVICE_NAME == "Sony_XQ-AU52":
            if Sony(self).set_deny_appear_on_top():
                return True
        else:
            print_warning(self.DEVICE_NAME + " not implemented yet")
        return False

    def run_set_permission_usage_deny_by_device(self):
        if self.DEVICE_NAME == "google_Pixel_5a":
            if Pixel_5A(self).set_deny_usage():
                return True

        else:
            print_warning(self.DEVICE_NAME + " not implemented yet")
        return False

    def run_set_permission_notification_deny_by_device(self):

        if self.DEVICE_NAME == "google_Pixel_5a":
            if Pixel_5A(self).set_deny_notification():
                return True

        else:
            print_warning(self.DEVICE_NAME + " not implemented yet")
            return False

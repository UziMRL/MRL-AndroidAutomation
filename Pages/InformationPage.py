from Pages.HomePage import *
from Config.configuration import *
import pytest
from Config.Helper import *


class InformationPage(HomePage):

    PAGE_ACTIVITY_SOURCE ="com.mobileresearchlabs.asound.ui.InformationActivity"

    INFORMATION_TITLE_TEXT = "Information"
    Information_TTITLE_TEXT_SAMSUNG = "com.mobileresearchlabs.asound.q:id/warp_information"
    ABOUT_TEXT = "About "
    SAVE_PCM = "Save PCM"

    BODY_TEXT_INFO_PAGE_TEXT = "Asound is a sound meter designed to run in the background of your personal device giving you access to the 'Sound Map' of your day to day life. Allowing you to adopt a healthier hearing regime"
    BODY_2_TEXT_INFO_PAGE_TEXT = "The information contained and gathered by Asound is for educational and informational purposes only and is not intended as health or medical advice. Please always consult a physician or other qualified health provider regarding any questions you may have about a medical condition or health objectives."
    MEMBER_ID_TEXT = "Member ID"
    APP_VERSION_TEXT = "App Version"
    LATEST_CONTENT_UPDATE_TEXT = "Latest Content Update"
    NEXT_CONTENT_UPDATE_TEXT = "Next Content Update"
    CACHE_TEXT = "Cache"
    LATEST_UPLOAD_TEXT = "Latest Upload"
    ENGINES_TEXT = "Engines"
    PRIVACY_POLICY_TEXT = "Privacy Policy"
    EMAIL_US_TEXT = "Email us"


    GMAIL = "Gmail"
    GMAIL_SEND_RES_ID ="com.google.android.gm:id/send"

    ENGINE_ELM_RES_ID = "com.mobileresearchlabs.asound.q:id/informationQaEngines"

    def __init__(self, driver, device_name):
        super().__init__(driver, device_name)
        if self.device["iskotlin"]:
            self.PAGE_ACTIVITY_SOURCE = "com.mobileresearchlabs.asound.ui.InformationActivity"

    def run_send_email_us(self):
        print_title("send email us")

        if self.check_current_page_activity(self.PAGE_ACTIVITY_SOURCE):
            self.scroll_down()
            self.scroll_down()
            if not self.click_by(self.EMAIL_US_TEXT,"txt"):
                return False
            if not self.click_by(self.GMAIL,"txt"):
                return False
            time.sleep(5)
            if not self.click_by(self.GMAIL_SEND_RES_ID,"id"):
                return False

            return True
        return False

    def run_save_PCM(self):
        print_title("run_save_PCM")
        if self.check_current_page_activity(self.PAGE_ACTIVITY_SOURCE):
            if not self.click_by(self.SAVE_PCM,"txt"):
                return False
        else:
            if self.click_by(self.INFORMATION_BUTTON_TEXT,"txt"):
                if not self.click_by(self.SAVE_PCM, "txt"):
                    return False

        return True




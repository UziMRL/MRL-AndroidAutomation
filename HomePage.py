from Pages.PermissionsPage import *
from Config.configuration import *
import pytest
from Config.Helper import *

class HomePage(PermissionsPage):



    SOUND_LEVEL_TEXT = "Sound Level"
    DB_VALUE_TEXT = "dB"
    OFF_TEXT = "Off"
    DB_VALUE_ID_RES = "com.mobileresearchlabs.asound.q:id/main_txt"


    DB_BUBBLE_MSG_TITLE_NOT_SAFE = "Average Sound Level is Loud"
    DB_BUBBLE_MSG_NOT_SAFE = "Repeated long-term exposure to sounds above 70 dB could affect your hearing"
    DB_TITLE_ID_RES = "com.mobileresearchlabs.asound.q:id/speechBubbleTitle"

    DB_BUBBLE_MSG_TITLE_SAFE = "Average Sound Level is Safe"
    DB_BUBBLE_MSG_SAFE ="Long term listening at this level should not affect your hearing"
    DB_BUBBLE_MSG_ID = "com.mobileresearchlabs.asound.q:id/speechBubbleMessage"

    MUTE_BUTTON_RES_ID ="com.mobileresearchlabs.asound.q:id/homeMuteIcon"
    MUTE_TITLE_TEXT = "Select mute period"
    MUTE_SUB_TITLE_TEXT = "Please select how long you want to mute for"


    MUTE_MSG = "Asound was paused and will resume at "
    MUTE_MSG_PART_2 = " Click on the icon to start now"

    def __init__(self, driver, device_name):
        super().__init__(driver, device_name)




    def get_mute_list(self):

        if self.device["isQA"]:
            config_by_customer_dict = DataBase(True).get_config_by_customerID(self.CUSTOMER_ID,self.PANELIST_ID)
            mute_list_to_check,result_for_after_mute = parser_config_mute(config_by_customer_dict["default_mute"],self.DEVICE_NAME)

            if mute_list_to_check == False or result_for_after_mute == False:
                return False,False

            return mute_list_to_check,result_for_after_mute







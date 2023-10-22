import time
import unittest
from Pages.InformationPage import *
from Tests.conftest import *
from DataBase.DataBase import *
from Config.Helper import *
from Pages.BasePage import *

class Detection_AM_General_Test(unittest.TestCase):



    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.infoPage = InformationPage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1])
        if not self.infoPage.run_set_allow_all_permissions_by_device():
            assert False



    @pytest.mark.order(1)
    def test_one_ad_detection_AM_on_foreground(self):

        if not self.infoPage.click_by(self.infoPage.Information_TTITLE_TEXT_SAMSUNG, "id"):
            assert False

        if self.infoPage.IS_QA:
            if not self.infoPage.run_save_PCM():
                assert False

        if self.infoPage.test_ad_detection("Bezeq_Kupa_Rashit_1_30_min - AM",sleep_for_=200):
            if get_if_KotlinRecord_dir_exist(device_id=self.infoPage.device["device_id"]):
                copy_PCMs(self.infoPage.device["device_id"])


        if not self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT,"txt"):
            assert False
        if not self.infoPage.run_send_email_us():
            assert False

    @pytest.mark.order(2)
    def test_one_ad_detection_AM_on_mute(self):
        if not self.infoPage.click_by(self.infoPage.MUTE_BUTTON_RES_ID, "id"):
            assert False

        mute_list_to_check, result_for_after_mute = self.infoPage.get_mute_list()

        if mute_list_to_check == False:
            print_failed("error to parse mute list")
            assert False

        for to_mute in mute_list_to_check:
            print(to_mute)
            if self.infoPage.click_by(to_mute, "txt"):
                break
        if self.infoPage.test_ad_detection("AA_04 - AM"):
            print_failed("Find an ad while Asound was in mute")
            assert False
        else:
            print_pass("Asound didnt found ad in mute")

    @pytest.mark.order(3)
    def test_one_ad_detection_AM_on_background(self):

        t1 = threading.Thread(target=self.infoPage.put_app_to_background, args=(120,))
        t2 = threading.Thread(target=self.infoPage.test_ad_detection, args=("WStarbucks - AM",))

        # starting thread 1
        t1.start()
        # starting thread 2
        t2.start()

        # wait until thread 1 is completely executed
        t1.join()
        # wait until thread 2 is completely executed
        t2.join()



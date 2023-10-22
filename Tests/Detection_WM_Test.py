import time
import unittest
from Pages.InformationPage import  *
from Tests.conftest import *
from DataBase.DataBase import *
from Config.Helper import *



class Detection_WM_Test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.infoPage = InformationPage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1])
        if not self.infoPage.run_set_allow_all_permissions_by_device():
            assert False


    @pytest.mark.order(1)
    def test_multiple_wm_flavors(self):
        to_play = ["Emmi - WM.mp3", "Emmi - WM2.mp3"]

        print_title("playing {0}  in row without_gap".format(str(to_play)))

        if not self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            assert False

        if self.infoPage.IS_QA:
            if not self.infoPage.run_save_PCM():
                assert False

            if not self.infoPage.check_if_download_ads_qa():
                return False

        else:
            print_title("upload content...")
            time.sleep(60)

        flag,msg=self.infoPage.test_multi_ads_detections(to_play, with_gap=10, sleep_before_detections=300)

        if self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            self.infoPage.run_send_email_us()

        if get_if_KotlinRecord_dir_exist(device_id=self.infoPage.device["device_id"]):
            copy_PCMs(self.infoPage.device["device_id"],self.test_multiple_wm_flavors.__name__)

        if not flag:
            assert False,msg
        else:
            assert True,msg

    @pytest.mark.order(2)
    def test_multi_ads_detections_without_gap(self):
        gap = 0
        play_from = "wm_ads"
        sleep_before_detections = 300
        to_play = get_ads_to_play_from_dir(play_from)

        print_title("playing {0}  in row with gap of {1}".format(str(to_play), gap / 60))

        if not self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            assert False

        if self.infoPage.IS_QA:
            if not self.infoPage.device["iskotlin"]:
                if not self.infoPage.run_save_PCM():
                    assert False

            if not self.infoPage.check_if_download_ads_qa():
                assert False


        else:
            print_title("upload content...")
            time.sleep(60)

        flag, msg = self.infoPage.test_multi_ads_detections(to_play, play_from, with_gap=gap,
                                                            sleep_before_detections=sleep_before_detections)

        if self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            self.infoPage.run_send_email_us()

        if get_if_KotlinRecord_dir_exist(device_id=self.infoPage.device["device_id"]):
            copy_PCMs(self.infoPage.device["device_id"],self.test_multi_ads_detections_without_gap.__name__)

        if not flag:
            assert False, msg
        else:
            assert True, msg

    @pytest.mark.order(3)
    def test_multi_ads_detections_with_10_sec_gap(self):
        gap = 10
        play_from = "wm_ads"
        sleep_before_detections = 300
        to_play = get_ads_to_play_from_dir(play_from)

        print_title("playing {0}  in row with gap of {1}".format(str(to_play), gap / 60))

        if not self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            assert False

        if self.infoPage.IS_QA:
            if not self.infoPage.device["iskotlin"]:
                if not self.infoPage.run_save_PCM():
                    assert False

            if not self.infoPage.check_if_download_ads_qa():
                assert False


        else:
            print_title("upload content...")
            time.sleep(60)

        flag, msg = self.infoPage.test_multi_ads_detections(to_play, play_from, with_gap=gap,
                                                            sleep_before_detections=sleep_before_detections)

        if self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            self.infoPage.run_send_email_us()

        if get_if_KotlinRecord_dir_exist(device_id=self.infoPage.device["device_id"]):
            copy_PCMs(self.infoPage.device["device_id"],self.test_multi_ads_detections_with_10_sec_gap.__name__)

        if not flag:
            assert False, msg
        else:
            assert True, msg

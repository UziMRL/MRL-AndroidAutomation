import time
import unittest
from Pages.InformationPage import *
from Tests.conftest import *
from DataBase.DataBase import *
from Config.Helper import *
from Pages.BasePage import *

class Detection_AM_Mix_Ads_Test(unittest.TestCase):



    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.infoPage = InformationPage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1])
        if not self.infoPage.run_set_allow_all_permissions_by_device():
            assert False


    @pytest.mark.order(1)
    def test_multi_ads_detections_AM_diff_ads_2_min_gap(self):
        gap = 120
        play_from = "mix_ads"
        sleep_before_detections = 360
        to_play = get_ads_to_play_from_dir(play_from)

        print_title("playing {0}  in row with gap of {1}".format(str(to_play), gap / 60))

        if not self.infoPage.click_by(self.infoPage.Information_TTITLE_TEXT_SAMSUNG, "id"):
            assert False

        if self.infoPage.IS_QA:
            if not self.infoPage.run_save_PCM():
                assert False

            if not self.infoPage.check_if_download_ads_qa():
                assert False


        else:
            print_title("upload content...")
            time.sleep(60)

        flag,msg = self.infoPage.test_multi_ads_detections(to_play, play_from, with_gap=gap,
                                                       sleep_before_detections=sleep_before_detections)

        if self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            self.infoPage.run_send_email_us()

        if get_if_KotlinRecord_dir_exist(device_id=self.infoPage.device["device_id"]):
            copy_PCMs(self.infoPage.device["device_id"],self.test_multi_ads_detections_AM_diff_ads_2_min_gap.__name__)

        if not flag:
            assert False, msg
        else:
            assert True, msg

    @pytest.mark.order(2)
    def test_multi_ads_detections_AM_diff_ads_1_min_gap(self):
        gap = 60
        play_from = "mix_ads"
        sleep_before_detections = 360
        to_play = get_ads_to_play_from_dir(play_from)

        print_title("playing {0}  in row with gap of {1}".format(str(to_play), gap / 60))

        if not self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            assert False

        if self.infoPage.IS_QA:
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
            copy_PCMs(self.infoPage.device["device_id"],self.test_multi_ads_detections_AM_diff_ads_1_min_gap.__name__)

        if not flag:
            assert False, msg
        else:
            assert True, msg

    @pytest.mark.order(3)
    def test_multi_ads_detections_AM_diff_ads_30_sec_gap(self):
        gap = 30
        play_from = "mix_ads"
        sleep_before_detections = 360
        to_play = get_ads_to_play_from_dir(play_from)

        print_title("playing {0}  in row with gap of {1}".format(str(to_play),gap/60))

        if not self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            assert False

        if self.infoPage.IS_QA:
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
            copy_PCMs(self.infoPage.device["device_id"])

        if not flag:
            assert False, msg
        else:
            assert True, msg

    @pytest.mark.order(4)
    def test_multi_ads_detections_AM_diff_ads_5_sec_gap(self):
        gap = 5
        play_from = "mix_ads"
        sleep_before_detections = 360
        to_play = get_ads_to_play_from_dir(play_from)

        print_title("playing {0}  in row with gap of {1}".format(str(to_play), gap / 60))

        if not self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            assert False

        if self.infoPage.IS_QA:
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
            copy_PCMs(self.infoPage.device["device_id"],self.test_multi_ads_detections_AM_diff_ads_5_sec_gap.__name__)

        if not flag:
            assert False, msg
        else:
            assert True, msg

    @pytest.mark.order(5)
    def test_multi_ads_detections_AM_diff_ads_no_gap(self):
        gap = 0
        play_from = "mix_ads"
        sleep_before_detections = 360
        to_play = get_ads_to_play_from_dir(play_from)

        print_title("playing {0}  in row with gap of {1}".format(str(to_play), gap / 60))

        if not self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            assert False

        if self.infoPage.IS_QA:
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
            copy_PCMs(self.infoPage.device["device_id"],self.test_multi_ads_detections_AM_diff_ads_no_gap.__name__)

        if not flag:
            assert False, msg
        else:
            assert True, msg


import unittest
from Pages.InformationPage import *
from Tests.conftest import *

from Pages.BasePage import *

class Detection_Cable_AM_Visualizer_Test(unittest.TestCase):



    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.infoPage = InformationPage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1])
        # if not self.infoPage.run_set_allow_all_permissions_by_device():
        #     assert False


    @pytest.mark.order(1)
    def test_multi_ad_detection_AM_visualizer_with_cable(self):


        ads_to_play = [("WStarbucks - AM.mp3",62),("SH_26 - AM.mp3",8),("MM_43 - AM.mp3",32),("SH_08 - AM.mp3",12),("asia_mac - AM.mp3",165),("SH_15 - AM.mp3",8),("SH_13 - AM.mp3",8),("SH_11 - AM.mp3",10)]

        print_warning(
            "!!! For this test - must be headset/headphone cable  to the phone - you have 30 sec to plug in!!!  ")
        sleep_time_for(30)
        using = get_device_using_headphone(device_id=self.infoPage.device["device_id"])
        if not using:
            assert False, "not using cable headphone"

        if not self.infoPage.run_set_allow_all_permissions_by_device():
            assert False, "failed to set all permissions"

        if self.infoPage.IS_QA:
            if not self.infoPage.run_save_PCM():
                assert False
            if not self.infoPage.check_if_download_ads_qa():
                assert False

        else:
            print_title("waiting for upload content")
            sleep_time_for(60)

        if not self.infoPage.click_back_to_home_page():
            assert False

        played_ads = []
        for ad,length in ads_to_play:
            print_title("Play ad - " + ad+" length - "+str(length))
            start_to_play = str(datetime.datetime.utcnow().replace(microsecond=0))
            played_ads.append({"ad_name":ad,"ad_len":length,"play_time":start_to_play})
            if not self.infoPage.click_by(ad, "txt"):
                assert False
            sleep_time_for(length)
            self.infoPage.click_back()



        print_title("wait to upload detections")
        sleep_time_for(360)
        if self.infoPage.open_asound_from_background():
            if self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
                 self.infoPage.run_send_email_us()


        db_con = DataBase(isQA=self.infoPage.IS_QA)
        count_detection = 0
        for p in played_ads:
            if ".mp3" in p["ad_name"]:
                splited = p["ad_name"].split(".mp3")
                p["ad_name"] = splited[0]
            if not db_con.get_ad_detection(self.infoPage.CUSTOMER_ID, self.infoPage.PANELIST_ID, p["ad_name"], p["play_time"],
                                           str(p["ad_len"])):
                print_failed("Not finding detection")

            else:
                count_detection += 1

        if get_if_KotlinRecord_dir_exist(device_id=self.infoPage.device["device_id"]):
            copy_PCMs(self.infoPage.device["device_id"],
                      self.test_multi_ad_detection_AM_visualizer_with_cable.__name__)

        if count_detection == 0:
            assert False,"Not finding detection"
        elif count_detection == len(ads_to_play):
            assert True
        elif count_detection < len(ads_to_play):
            assert False,"detected {0}/{1}".format(count_detection,len(ads_to_play))

    @pytest.mark.order(2)
    def test_full_recording_6_sec_ads_detection_visualizer_with_cable_headphone_AM(self):

        full_ads_to_play = get_ads_to_play_from_dir(path_name="full_recoding/6_sec_ads")
        len_ = 360

        ads_to_check = get_ads_list_from_csv(path_name="full_recoding/6_sec_ads")

        print_warning(
            "!!! For this test - must be cable headphone connected to the phone - you have 30 sec to plug in!!!  ")
        sleep_time_for(30)

        using = get_device_using_headphone(device_id=self.infoPage.device["device_id"])
        if not using:
            assert False, "not using cable headphone"

        if not self.infoPage.run_set_allow_all_permissions_by_device():
            assert False, "failed to set all permissions"

        if self.infoPage.IS_QA:
            if not self.infoPage.run_save_PCM():
                assert False
            if not self.infoPage.check_if_download_ads_qa():
                assert False

        else:
            print_title("waiting for upload content")
            sleep_time_for(60)

        if not self.infoPage.click_back_to_home_page():
            assert False

        start_to_play = datetime.datetime.utcnow().replace(microsecond=0)
        for ad_to_play in full_ads_to_play:
            if ad_to_play.endswith(".mp3"):
                if not self.infoPage.click_by(ad_to_play, "txt"):
                    assert False
            sleep_time_for(len_)
            end_time = start_to_play + timedelta(seconds=len_)
            end_time = end_time.replace(microsecond=0)
            self.infoPage.click_back()

        print_title("wait to upload detections")
        sleep_time_for(360)

        if self.infoPage.open_asound_from_background():
            if self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
                self.infoPage.run_send_email_us()

        print_title("start search for detections")
        db_con = DataBase(isQA=self.infoPage.IS_QA)

        all_detections = db_con.get_all_ads_detections_between_times(self.infoPage.CUSTOMER_ID,
                                                                     self.infoPage.PANELIST_ID, str(start_to_play),
                                                                     str(end_time))

        count_detections = 0
        detected_ads = {}
        for detection in all_detections:
            ad_id = detection[0]
            ad_name = detection[1]
            detectionTS = detection[2]
            duration = detection[3]

            for ad_to_check, length in ads_to_check:

                if ad_name in ad_to_check:
                    if ad_name not in detected_ads:
                        detected_ads[ad_name] = 1
                    else:
                        detected_ads[ad_name] += 1
                    count_detections += 1
                    print_pass("Detected => ad id = {0}, ad name = {1}, detectionTS = {2}, duration = {3}".format(ad_id,
                                                                                                                  ad_name,
                                                                                                                  detectionTS,
                                                                                                                  duration))

        not_detected = []
        for ad_to_check, duration in ads_to_check:
            ad_to_check_ = ad_to_check.split(".mp3")

            detected_list = detected_ads.keys()
            detected_list = list(detected_list)

            if ad_to_check_[0] not in detected_list:
                not_detected.append(ad_to_check_[0])



        if get_if_KotlinRecord_dir_exist(device_id=self.infoPage.device["device_id"]):
            copy_PCMs(self.infoPage.device["device_id"],
                      self.test_full_recording_6_sec_ads_detection_visualizer_with_cable_headphone_AM.__name__)

        if count_detections == len(ads_to_check):
            print_pass("detected all ads")
            print_title(str(detected_ads))
        elif count_detections < len(ads_to_check):
            print_failed("detcted {0}/{1}".format(len(detected_ads), len(ads_to_check)))
            print_title("detected => " + str(detected_ads))
            print_warning("didnt detected =>" + str(not_detected))
            assert False, "detcted {0}/{1}".format(len(detected_ads), len(ads_to_check))

    @pytest.mark.order(3)
    def test_full_recording_mix_ads_detection_visualizer_with_cable_headphone_AM(self):

        full_ads_to_play = get_ads_to_play_from_dir(path_name="full_recoding/mix_ads_for_visualizer")
        len_ = 360

        ads_to_check = get_ads_list_from_csv(path_name="full_recoding/mix_ads_for_visualizer")

        print_warning(
            "!!! For this test - must be bluetooth headphone connected to the phone - you have 30 sec to plug in!!!  ")
        sleep_time_for(30)

        print_title("ads to check " + str(ads_to_check))

        using = get_device_using_headphone(device_id=self.infoPage.device["device_id"])
        if not using:
            assert False, "not using cable headphone"

        if not self.infoPage.run_set_allow_all_permissions_by_device():
            assert False, "failed to set all permissions"

        if self.infoPage.IS_QA:
            if not self.infoPage.run_save_PCM():
                assert False

            if not self.infoPage.check_if_download_ads_qa():
                assert False

        else:
            print_title("waiting for upload content")
            sleep_time_for(60)

        if not self.infoPage.click_back_to_home_page():
            assert False

        start_to_play = datetime.datetime.utcnow().replace(microsecond=0)
        for ad_to_play in full_ads_to_play:
            if ad_to_play.endswith(".mp3"):
                if not self.infoPage.click_by(ad_to_play, "txt"):
                    assert False
            sleep_time_for(len_)
            end_time = start_to_play + timedelta(seconds=len_)
            end_time = end_time.replace(microsecond=0)
            self.infoPage.click_back()

        print_title("wait to upload detections")
        sleep_time_for(300)

        if self.infoPage.open_asound_from_background():
            if self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
                self.infoPage.run_send_email_us()

        print_title("start search for detections")
        db_con = DataBase(isQA=self.infoPage.IS_QA)

        all_detections = db_con.get_all_ads_detections_between_times(self.infoPage.CUSTOMER_ID,
                                                                     self.infoPage.PANELIST_ID, str(start_to_play),
                                                                     str(end_time))

        count_detections = 0
        detected_ads = {}
        for detection in all_detections:
            ad_id = detection[0]
            ad_name = detection[1]
            detectionTS = detection[2]
            duration = detection[3]

            for ad_to_check, length in ads_to_check:

                if ad_name in ad_to_check:
                    if ad_name not in detected_ads:
                        detected_ads[ad_name] = 1
                    else:
                        detected_ads[ad_name] += 1
                    count_detections += 1
                    print_pass("Detected => ad id = {0}, ad name = {1}, detectionTS = {2}, duration = {3}".format(ad_id,
                                                                                                                  ad_name,
                                                                                                                  detectionTS,
                                                                                                                  duration))

        not_detected = []
        for ad_to_check, duration in ads_to_check:

            ad_to_check_ = ad_to_check.split(" - AM.mp3")
            detected_list = detected_ads.keys()
            detected_list = list(detected_list)

            if ad_to_check_[0] in detected_list:
                pass
            else:
                not_detected.append(ad_to_check_[0])

        if get_if_KotlinRecord_dir_exist(device_id=self.infoPage.device["device_id"]):
            copy_PCMs(self.infoPage.device["device_id"],
                      "test_full_recording_mix_ads_detection_visualizer_with_cable_headphone_AM")

        if count_detections == len(ads_to_check):
            print_pass("detected all ads")
            print_title(str(detected_ads))

        elif count_detections < len(ads_to_check):
            print_failed("detcted {0}/{1}".format(len(detected_ads), len(ads_to_check)))
            print_title("detected => " + str(detected_ads))
            print_warning("not detected =>" + str(not_detected))
            assert False, "detcted {0}/{1}".format(len(detected_ads), len(ads_to_check))





import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from Config.android_keys import *
from Config.Helper import *
from Config.configuration import *
import sys
import re
from DataBase.DataBase import *
"""This class is the parent of all pages"""


class BasePage:
    #device = device_to_run(device_name="pixel_2_qa")
    #PANELIST_ID = device["panelistid"]

    APP_NAME = "Asound"
    HOME_BUTTON_TEXT = "Home"
    INFORMATION_BUTTON_TEXT = "Information"
    HISTORY_BUTTON_TEXT = "History"
    APP_PACKAGE_NAME = "com.mobileresearchlabs.asound.q"

    ALLOW_TEXT = "Allow"
    ALLOW_TEXT_CAP = "ALLOW"

    DENY_TEXT = "Deny"
    DENY_TEXT_CAP = "DENY"

    WHILE_USING_THE_APP_TEXT = "While using the app"
    WHILE_USING_THE_APP_TEXT_CAP = "WHILE USING THE APP"

    ONLY_THIS_TIME = "Only this time"
    ONLY_THIS_TIME_CAP = "ONLY THIS TIME"

    AGREE_AND_CONTINUE_TEXT = "Agree & Continue"


    OK_TEXT_CAP = "OK"
    CANCEL_TEXT = "Cancel"

    ALLOW_ALL_THE_TIME_TEXT = "Allow all the time"
    DONT_ALLOW = "don't allow"
    DONT_ALLOW_CAP = "Don’t allow"
    DONT_ALLOW_CAP_v2 = "DON'T ALLOW"
    DONT_ALLOW_RES_ID = "com.android.permissioncontroller:id/permission_deny_button"
    DONT_ALLOW_RES_ID_V2 = "com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button"

    ENGINE_ELM_RES_ID_QA = "com.mobileresearchlabs.asound.q:id/informationQaEngines"
    ENGINE_ELM_RES_ID = "com.mobileresearchlabs.asound.q:id/informationEngines"

    INFO_PAGE_ACTIVITY_SOURCE ="com.mobileresearchlabs.asound.InformationActivity"

    APP_INFO_STRCIT = "App info"

    def __init__(self,driver,device_name):

        self.device = device_to_run(device_name=device_name)
        self.PANELIST_ID = self.device["panelistid"]
        self.CUSTOMER_ID = self.device["customerid"]
        self.ACTIVATION_CODE = self.device["activation_code"]
        self.DEVICE_NAME = self.device["device_name"]
        self.IS_QA = self.device["isQA"]
        self.IS_KOTLIN = self.device["iskotlin"]




        if self.IS_KOTLIN:
            self.INFO_PAGE_ACTIVITY_SOURCE = 'com.mobileresearchlabs.asound.ui.InformationActivity'
        else:
            self.INFO_PAGE_ACTIVITY_SOURCE = "com.mobileresearchlabs.asound.InformationActivity"

        self.driver = driver

    def check_text_by_res_id(self,res_id,timeout=60,val_to_check=False):
        elm = "//*[@resource-id='" + res_id + "']"
        try:
            w = WebDriverWait(self.driver, timeout=timeout)
            result = w.until(EC.presence_of_element_located((By.XPATH, elm)))


            flag = result.is_displayed()

            if flag:
                print_pass("check_text_by_res_id: " + res_id)
                if val_to_check:
                    print_warning("res from elm = "+result.text)
                    return result.text
                return True

            print_failed("check_text_by_res_id: " + res_id)
            return False

        except Exception as e:
            print_failed("check_text_by_res_id: " + res_id)
            return False

    def check_text(self, txt, timeout=60):
        elm = "//*[@text='" + txt + "']"
        try:
            w = WebDriverWait(self.driver, timeout=timeout)
            result = w.until(EC.presence_of_element_located((By.XPATH, elm)))

            flag = result.is_displayed()

            if flag:
                print_pass("check_text: "+txt)
                return True

            print_failed("check_text: "+txt)
            return False

        except Exception as e:
            print_failed("check_text: " + txt)
            return False

    def check_content_desc(self,txt,timeout=60):
        elm = "//*[@content-desc='" + txt + "']"
        try:
            w = WebDriverWait(self.driver, timeout=timeout)
            result = w.until(EC.presence_of_element_located((By.XPATH, elm)))
            flag = result.is_displayed()

            if flag:
                print_pass("check_content_desc: " + txt)
                return True

            print_failed("check_content_desc: " + txt)
            return False

        except Exception as e:
            print_failed("check_content_desc: " + txt)
            return False

    def print_current_page_source(self):
        print(self.driver.current_activity)
        print(self.driver.current_context)
        print(self.driver.page_source)

    def check_current_page_activity(self,activity):
        print_warning("current page activity = "+self.driver.current_activity)
        if self.driver.current_activity == activity:
            print_pass("check_current_page_activity: "+activity)
            return True
        print_failed("check_current_page_activity: "+activity)
        return False

    def click_by_text(self,txt):
        elm = "//*[@text='"+txt+"']"
        try:
            w = WebDriverWait(self.driver,timeout=30)
            result = w.until(EC.presence_of_element_located((By.XPATH, elm)))
            result.click()
            print_pass(self.click_by_text.__name__ +" : "+txt)
            return True
        except Exception as e:
            print_failed(self.click_by_text.__name__ +" : "+txt)
            return False

    def click_by_id(self,id_):
        elm = "//*[@resource-id='" + id_ + "']"
        try:
            w = WebDriverWait(self.driver,timeout=60)
            result = w.until(EC.presence_of_element_located((By.XPATH, elm)))
            result.click()
            print_pass(self.click_by_id.__name__ + ":" + id_)
            return True
        except Exception as e:
            print_failed(self.click_by_id.__name__ + ":" + id_)
            return False

    def fill_textfield(self, txt):
        try:
            elm = "android.widget.EditText"
            w = WebDriverWait(self.driver, timeout=60)
            result = w.until(EC.presence_of_element_located((By.CSS_SELECTOR, elm)))
            result.send_keys(txt)
            print_pass(self.fill_textfield.__name__ + ":" + txt)
            return True
        except Exception as e:
            print_failed(self.fill_textfield.__name__ + ":" + txt)
            return False

    def click_by_class(self,class_):
        elm = "//*[@class='" + class_ + "']"
        try:
            w = WebDriverWait(self.driver, timeout=60)
            result = w.until(EC.presence_of_element_located((By.XPATH, elm)))
            result.click()
            print_pass(self.click_by_id.__name__ + ":" + class_)
        except Exception as e:
            print_failed(self.click_by_id.__name__ + ":" + class_)

    def click_by_content_desc(self,content_desc_):
        elm = "//*[@content-desc='" + content_desc_ + "']"
        try:
            w = WebDriverWait(self.driver, timeout=60)
            result = w.until(EC.presence_of_element_located((By.XPATH, elm)))
            result.click()
            print_pass(self.click_by_id.__name__ + ":" + content_desc_)
        except Exception as e:
            print_failed(self.click_by_id.__name__ + ":" + content_desc_)

    def check_by_class(self,class_name):
        elm = "//*[@class='" + class_name + "']"
        try:
            w = WebDriverWait(self.driver, timeout=60)
            result = w.until(EC.presence_of_element_located((By.XPATH, elm)))
            if result.is_displayed():
                print_pass(self.check_by_class.__name__ + ":" + class_name)
                return True
            else:
                print_failed(self.check_by_class.__name__ + ":" + class_name)
                return False
        except Exception as e:
            print_failed(self.check_by_class.__name__ + ":" + class_name)
            return False

    def click_back(self):
        try:
            self.driver.press_keycode(android_keys["BACK"])
            print_pass(self.click_back.__name__)
            return True
        except Exception as e:
            print_failed(self.click_back.__name__)
            return False

    def click_back_to_home_page(self):
        try:
            #self.driver.press_keycode(82)
            self.driver.press_keycode(3)
            print_pass(self.click_back_to_home_page.__name__)
            return True
        except Exception as e:
            print_failed(self.click_back_to_home_page.__name__)
            return False

    def close_app(self):
        self.driver.close_app()

    def open_app(self):
        self.driver.launch_app()

    def toggle_wifi(self):
        self.driver.toggle_wifi()

    def volume_up(self):
        print_title("volume_up")
        self.driver.press_keycode(android_keys["VOLUME_UP"])

    def volume_down(self):
        print_title("volume_down")
        self.driver.press_keycode(android_keys["VOLUME_DOWN"])

    #driver.swipe(start_x, start_y, end_x, end_y, duration)
    def scroll_down(self):
        print_title("Scroll down")
        window_size = self.driver.get_window_size()
        height = window_size["height"]
        width = window_size["width"]

        self.driver.swipe(250, 500, 500,0)

    def sleep_for(self,for_):
        self.driver.implicitly_wait(for_)

    def getOrientation(self):
        print(self.driver.getOrientation())

    def open_notification_center(self):
        print_title("open notification center")
        self.driver.open_notifications()

    def put_app_to_background(self,for_time=10):
        print_title("put_app_to_background for:{0} sec".format(for_time))
        self.driver.background_app(for_time)

    def switch_app(self):
        print_title("open switch app")
        self.driver.press_keycode(android_keys["APP_SWITCH"])

    def scroll_left(self,id_):
        print_title("scroll left from "+id_)
        try:
            actions = TouchAction(self.driver)

            el = self.driver.find_element_by_accessibility_id(id_)
            actions.press(el).move_to(x=-100, y=-1000).release().perform()
            return True
        except Exception as e:
            print_failed(str(e))
            return False

    def set_location(self,latitude,longitude,altitude):
        """
        latitude	number	The desired geolocation latitude
        longitude	number	The desired geolocation longitude
        altitude	number	The desired geolocation altitude (optional. altitude works on real Android devices only)
        """
        print_title("set_location ({0},{1},{2})".format(str(latitude),str(longitude),str(altitude)))
        self.driver.set_location(latitude,longitude,altitude)

    def take_screenshots_and_send_by_mail(self):
        print_title("take_screenshots_and_send_by_mail")
        screenshotBase64 = self.driver.get_screenshot_as_base64()
        convert_base64_to_pic(screenshotBase64,file_name=self.DEVICE_NAME + "_"+self.PANELIST_ID+"_"+self.CUSTOMER_ID+"_")

    def launch_app(self):
        self.driver.launch_app()

    def open_asound_from_home(self):
        self.driver.press_keycode(12)
        android_keys

    def click_by(self,text,opt):

        if opt == "txt":
            if self.check_text(text):
                self.click_by_text(text)
                return True

        elif opt == "class":
             self.click_by_class(text)
             return True

        elif opt == "id":
            if self.click_by_id(text):
                return True

        elif opt == "cd":
            self.click_by_content_desc(text)
            return True

        return False

    def click_allow(self,isCap):
        if isCap:
           if self.click_by(self.ALLOW_TEXT_CAP,"txt"):
               return True
        else:
            if self.click_by(self.ALLOW_TEXT,"txt"):
                return True
        return False

    def click_deny(self,isCap):
        if isCap:
            self.click_by(self.DENY_TEXT_CAP,"txt")
            return True
        else:
            self.click_by(self.DENY_TEXT,"txt")
            return True

        return False

    def click_agree_and_continue(self):
        if self.click_by(self.AGREE_AND_CONTINUE_TEXT):
            return True
        return False

    def check_if_download_ads_qa(self):
        #add until by conig time if not click refresh
        p = '[\d]+'
        count_of_ads_on_deck = DataBase(isQA=True).get_count_of_ads_on_engine(self.CUSTOMER_ID,
                                                                              self.device["projectid"])
        flag = True


        while flag:

            self.click_by(self.INFORMATION_BUTTON_TEXT, "txt")
            if not self.check_current_page_activity(self.INFO_PAGE_ACTIVITY_SOURCE):
                self.click_by(self.INFORMATION_BUTTON_TEXT, "txt")
            self.scroll_down()

            engines_from_device = self.check_text_by_res_id(res_id=self.ENGINE_ELM_RES_ID_QA,
                                                            val_to_check=True)

            if engines_from_device == False:
                print_failed("cannot parse engines_from_device")
                return False
            engines_from_device = parser_engines_from_device(engines_from_device)

            if re.search(p, engines_from_device["onDeckMatch"]) is not None:
                for catch in re.finditer(p, engines_from_device["onDeckMatch"]):
                    if str(catch[0]) < str(count_of_ads_on_deck):
                        print_warning("device download {0}/{1} ads".format(catch[0], count_of_ads_on_deck))
                    elif str(catch[0]) == str(count_of_ads_on_deck):
                        print_pass("device download all ads {0}/{1}".format(catch[0], count_of_ads_on_deck))
                        flag = False
                        return True

                self.click_by(self.HOME_BUTTON_TEXT, "txt")
            else:
                print_failed("device didnt download ads")
                flag = False
                return False
            time.sleep(5)

    def test_ad_detection(self,ad_name,sleep_for_=300):
        print_title("upload content...")
        self.click_by(self.INFORMATION_BUTTON_TEXT, "txt")


        if self.IS_QA:

            if not self.check_if_download_ads_qa():
                return False

            play_time, ad_len = play_ad(ad_name + ".mp3")
            if play_time == False:
                return False

            print_title("upload detections...\nwaiting for {0} sec".format(sleep_for_))
            sleep_time_for(sleep_for_)

            db_con = DataBase(isQA=True)
            print_title("Search for detection")
            if not db_con.get_ad_detection(self.CUSTOMER_ID, self.PANELIST_ID, ad_name, play_time,
                                           str(ad_len)):
                print_failed("Not finding detection")
                return False
            return True



        else:
            print_title("wait 1 min to upload content")
            sleep_time_for()

            print_title("done upload")

            play_time, ad_len = play_ad(ad_name + ".mp3")
            if play_time == False:
                return False

            print_title("upload detections...\nwaiting for {0} sec".format(sleep_for_))
            sleep_time_for(sleep_for_)
            db_con = DataBase(isQA=False)
            print_title("Search for detection")
            if not db_con.get_ad_detection(self.CUSTOMER_ID, self.PANELIST_ID, ad_name, play_time,
                                           str(ad_len)):
                print_failed("Not finding detection")
                return False
            return True

    def test_multi_ads_detections(self,ads_names,dir_play = "",with_gap=0,sleep_before_detections =120):
        print_title("ads to play - "+str(ads_names))



        if type(ads_names) != list:
            print_failed("ads_names must be type of list")
            return False

        played = []
        for ad_name in ads_names:
            play_time, ad_len = play_ad(ad_name,dir_play)
            if play_time == False:
                return False
            played.append({"play_time":play_time,"ad_name":ad_name,"ad_len":ad_len})
            if with_gap > 0:
                sleep_time_for(with_gap)

        if self.device["isQA"]:
            print_title("upload detections...")
            sleep_time_for(sleep_before_detections)
            db_con = DataBase(isQA=True)
            print_title("Search for detection")

        else:
            print_title("upload detections...")
            sleep_time_for(sleep_before_detections)
            db_con = DataBase(isQA=False)
            print_title("Search for detection")


        count_detection = 0
        for p in played:
            if ".mp3" in p["ad_name"]:
              splited = p["ad_name"].split(".mp3")
              p["ad_name"] = splited[0]
            if not db_con.get_ad_detection(self.CUSTOMER_ID, self.PANELIST_ID, p["ad_name"], p["play_time"],
                                           str(p["ad_len"])):
                print_failed("Not finding detection")

            else:
                count_detection+=1

        if count_detection == len(ads_names):
            print_pass("detect all ads")
            return True,"detect all ads"

        elif count_detection < len(ads_names) and count_detection!=0:
            print_warning("detected ({0}/{1})".format(count_detection,len(ads_names)))
            return False,"detected ({0}/{1})".format(count_detection,len(ads_names))
        elif count_detection == 0:
            print_failed("not detection for ads - "+str(ads_names))
            return False,"not detection for ads - "+str(ads_names)

    def test_full_recording_ads(self,dir_files):

        start_to_play, end_play, length = play_large_ads_file(dir_files)

        if self.device["isQA"]:
            print_title("upload detections...")
            sleep_time_for(120)
            db_con = DataBase(isQA=True)
            print_title("Searching for detections")
            result = db_con.get_all_ads_detections_between_times(self.CUSTOMER_ID,self.PANELIST_ID,start_to_play,end_play)
            if not result:
                return False
            compare_result_with_indexes(dir_files,result)

    def open_asound_from_background(self):
        self.switch_app()

        if not self.click_by(self.APP_NAME, "cd"):
            time.sleep(2)
            if not self.scroll_left("Drive") or self.scroll_left("File Manager +"):
                 return False
            time.sleep(2)
            if not self.click_by(self.APP_NAME, "cd"):
                return False
        else:
            return True

    def open_asound_from_background_v2(self):
        self.switch_app()
        if not self.click_by(self.APP_NAME, "cd"):
            return False
        return True
















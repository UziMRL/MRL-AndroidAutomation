import unittest
from Pages.InformationPage import *
from Tests.conftest import *
from DataBase.DataBase import *
import re

class InformationPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.information_page = InformationPage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1])
        self.information_page.run_set_allow_all_permissions_by_device()

    #@pytest.mark.skip()
    @pytest.mark.order(1)
    def test_information_page_texts(self):
        print_title("Home page")
        if not self.information_page.click_by(self.information_page.INFORMATION_BUTTON_TEXT, "txt"):
            assert False


        print_title("Information Page")
        if self.information_page.device["isQA"]:
            texts_to_check = [self.information_page.INFORMATION_TITLE_TEXT,
                              self.information_page.ABOUT_TEXT,
                              #self.information_page.BODY_TEXT_INFO_PAGE_TEXT,
                              self.information_page.BODY_2_TEXT_INFO_PAGE_TEXT,
                              self.information_page.MEMBER_ID_TEXT,
                              self.information_page.PANELIST_ID,
                              self.information_page.APP_VERSION_TEXT,
                              self.information_page.LATEST_CONTENT_UPDATE_TEXT,
                              self.information_page.NEXT_CONTENT_UPDATE_TEXT,
                              self.information_page.CACHE_TEXT,
                              self.information_page.LATEST_CONTENT_UPDATE_TEXT,
                              self.information_page.ENGINES_TEXT,
                              #self.information_page.PRIVACY_POLICY_TEXT,
                              self.information_page.Copyright_TEXT,
                              self.information_page.HOME_BUTTON_TEXT,
                              self.information_page.INFORMATION_BUTTON_TEXT,
                              ]

            for text in texts_to_check:
                if not self.information_page.check_text(text):
                    assert False

            # check if email us exist
            self.information_page.scroll_down()
            if not self.information_page.check_text(self.information_page.EMAIL_US_TEXT) and not self.information_page.check_text(self.information_page.PRIVACY_POLICY_TEXT):
                assert False

    @pytest.mark.order(2)
    def test_engines_text(self):

        if not self.information_page.click_by(self.information_page.INFORMATION_BUTTON_TEXT, "txt"):
            assert False

        if self.information_page.check_current_page_activity(self.information_page.PAGE_ACTIVITY_SOURCE):
            self.information_page.scroll_down()

            if not self.information_page.IS_QA:
                if self.information_page.click_by(self.information_page.INFORMATION_BUTTON_TEXT,"txt"):
                    if self.information_page.check_current_page_activity(self.information_page.PAGE_ACTIVITY_SOURCE):
                        self.information_page.scroll_down()

                if self.information_page.check_text(self.information_page.ENGINES_TEXT):
                    print_failed("should not be engines text on prod version!")
                    assert False

            if self.information_page.IS_QA:
                if not self.information_page.check_if_download_ads_qa():
                    assert False

                db = DataBase(isQA=True)
                signatureUploadPlan, samplingPlan, use_shepherd, use_spotter, use_watermark = db.get_engine_config(
                    self.information_page.CUSTOMER_ID, self.information_page.PANELIST_ID)

                engines_from_device = self.information_page.check_text_by_res_id(res_id=self.information_page.ENGINE_ELM_RES_ID,
                                                                         val_to_check=True)

                engines_from_device = parser_engines_from_device(engines_from_device)

                if self.information_page.click_by(self.information_page.INFORMATION_BUTTON_TEXT, "txt"):
                    if self.information_page.check_current_page_activity(self.information_page.PAGE_ACTIVITY_SOURCE):
                        self.information_page.scroll_down()


                if str(use_shepherd) == "2" and engines_from_device["serverMatch"] != None:
                    server_match_to_check = "ServerMatch(" + str(samplingPlan) + "|" + str(
                        signatureUploadPlan) + "|" + str(use_shepherd) + ")"

                    if server_match_to_check != engines_from_device["serverMatch"]:
                        assert False
                    else:
                        print_pass("Server match in DB {0} is equal to server match on the device".format(
                            server_match_to_check))

                elif str(use_shepherd) == "99" and engines_from_device["serverMatch"] == None:
                    print_pass("server match is OFF in the device and OFF on the DB")

                elif str(use_shepherd) == "2" and engines_from_device["serverMatch"] == None:
                    print_failed("for DB use serverMatch is ON from the device is OFF")
                    assert False

                if str(use_spotter) == "1" and engines_from_device["onDeckMatch"] != None:
                    count_of_ads_on_deck = db.get_count_of_ads_on_engine(self.information_page.CUSTOMER_ID,
                                                                         self.information_page.device["projectid"])
                    # on_deck_from_device = splited[0]

                    p = '[\d]+'

                    if re.search(p, engines_from_device["onDeckMatch"]) is not None:
                        for catch in re.finditer(p, engines_from_device["onDeckMatch"]):
                            if str(catch[0]) < str(count_of_ads_on_deck):
                                print_warning("device download {0}/{1} ads".format(catch[0], count_of_ads_on_deck))

                            elif str(catch[0]) == str(count_of_ads_on_deck):
                                print_pass("device download all ads {0}/{1}".format(catch[0], count_of_ads_on_deck))

                            else:
                                print_failed("device didnt download ads")
                                assert False

                if str(use_watermark) == "1" and engines_from_device["watermark"] != None:
                    count_of_ads_watermark = db.get_count_of_ads_on_engine(self.information_page.CUSTOMER_ID,
                                                                           self.information_page.device["projectid"],
                                                                           check_watermark=True)

                    p = '[\d]+'

                    if re.search(p, engines_from_device["watermark"]) is not None:
                        for catch in re.finditer(p, engines_from_device["watermark"]):
                            if str(catch[0]) < str(count_of_ads_watermark):
                                print_warning("device download {0}/{1} wm ads".format(catch[0], count_of_ads_watermark))

                            elif str(catch[0]) == str(count_of_ads_watermark):
                                print_pass(
                                    "device download all wm ads {0}/{1}".format(catch[0], count_of_ads_watermark))

                            else:
                                print_failed("device didnt download wm ads")
                                assert False
        else:
            assert False

    @pytest.mark.order(3)
    def test_email_us(self):
        if not self.information_page.click_by(self.information_page.INFORMATION_BUTTON_TEXT, "txt"):
            assert False
        if not self.information_page.run_send_email_us():
            assert False
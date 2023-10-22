import unittest
from Pages.HomePage import *
from Tests.conftest import *
from DataBase.DataBase import *
from Config.Helper import *


class HomePageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.homePage = HomePage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1])
        if not self.homePage.run_set_allow_all_permissions_by_device():
            assert False


    @pytest.mark.order(1)
    def test_dB_value(self):

        res = self.homePage.check_text_by_res_id(res_id=self.homePage.DB_VALUE_ID_RES,
                                                 val_to_check=True)
        assert res > "0" or res != self.homePage.OFF_TEXT

    @pytest.mark.order(2)
    def test_dB_bubble_msg(self):

        res_bubble_title_msg = self.homePage.check_text_by_res_id(res_id=self.homePage.DB_TITLE_ID_RES,
                                                                  val_to_check=True)


        res_bubble_msg = self.homePage.check_text_by_res_id(res_id=self.homePage.DB_BUBBLE_MSG_ID,
                                                 val_to_check=True)


        if res_bubble_title_msg != self.homePage.DB_BUBBLE_MSG_TITLE_SAFE:
            print_warning("checking not safe title text")
            if res_bubble_title_msg != self.homePage.DB_BUBBLE_MSG_TITLE_NOT_SAFE:
                assert False

        if res_bubble_msg != self.homePage.DB_BUBBLE_MSG_SAFE:
            print_warning("checking not safe text")
            if res_bubble_msg != self.homePage.DB_BUBBLE_MSG_NOT_SAFE:
                assert False


    @pytest.mark.order(3)
    def test_dB_bubble_loud_msg(self):


        self.homePage.click_back_to_home_page()
        self.homePage.click_by("EXTREMELY_Painful_Sound.mp3","txt")
        sleep_time_for(2)
        self.homePage.click_back_to_home_page()
        if self.homePage.open_asound_from_background():

            for _ in range(10):
                self.homePage.volume_up()

            sleep_time_for(7)

            res_bubble_title_msg = self.homePage.check_text_by_res_id(res_id=self.homePage.DB_TITLE_ID_RES,
                                                                      val_to_check=True)


            res_bubble_msg = self.homePage.check_text_by_res_id(res_id=self.homePage.DB_BUBBLE_MSG_ID,
                                                     val_to_check=True)

            #pause music from notifation center

            self.homePage.open_notification_center()
            self.homePage.click_by("Pause","cd")
            self.homePage.click_back()

            if res_bubble_title_msg != self.homePage.DB_BUBBLE_MSG_TITLE_NOT_SAFE:
                assert False

            if res_bubble_msg != self.homePage.DB_BUBBLE_MSG_NOT_SAFE:
                assert False

            res_db_val = self.homePage.check_text_by_res_id(res_id=self.homePage.DB_VALUE_ID_RES,
                                                     val_to_check=True)
            print_title("db value ="+res_db_val)


            assert True



    @pytest.mark.order(4)
    def test_home_page_texts(self):
        print_title("Home page")
        texts_to_check = [self.homePage.SOUND_LEVEL_TEXT,
                          self.homePage.HOME_BUTTON_TEXT,
                          self.homePage.HISTORY_BUTTON_TEXT,
                          self.homePage.INFORMATION_BUTTON_TEXT
                          ]
        for text in texts_to_check:
            if not self.homePage.check_text(text):
                assert False


    @pytest.mark.order(5)
    def test_mute_texts(self):
        print_title("Home Page")
        if not self.homePage.click_by(self.homePage.MUTE_BUTTON_RES_ID, "id"):
            assert False

        mute_list_to_check, result_for_after_mute = self.homePage.get_mute_list()
        if mute_list_to_check == False:
            assert False

        texts_to_check = [self.homePage.MUTE_TITLE_TEXT, self.homePage.MUTE_SUB_TITLE_TEXT]

        for text in texts_to_check:
            if not self.homePage.check_text(text):
                assert False

        for mute_text in mute_list_to_check:
            if not self.homePage.check_text(mute_text):
                assert False


    @pytest.mark.order(6)
    def test_mute_until(self):
        print_title("Home Page")
        if not self.homePage.click_by(self.homePage.MUTE_BUTTON_RES_ID, "id"):
            assert False

        mute_list_to_check, result_for_after_mute = self.homePage.get_mute_list()
        if not mute_list_to_check:
            assert False

        for mute in mute_list_to_check:
            if "Until" in mute:

                if not self.homePage.click_by(mute, "txt"):
                    assert False

                time.sleep(2)
                if not self.homePage.check_text(self.homePage.OFF_TEXT):
                    assert False

        count_success = 0
        for check_after_mute in result_for_after_mute:
            if type(check_after_mute) == str:
                txt_to_check = self.homePage.MUTE_MSG + check_after_mute + self.homePage.MUTE_MSG_PART_2
                if not self.homePage.check_text(txt_to_check):
                    continue

                else:
                    count_success += 1

        if count_success == 0:
            assert False

    @pytest.mark.order(7)
    def test_mute_for(self):

        print_title("Home Page")
        if not self.homePage.click_by(self.homePage.MUTE_BUTTON_RES_ID, "id"):
            assert False

        mute_list_to_check, result_for_after_mute = self.homePage.get_mute_list()
        if not mute_list_to_check:
            assert False

        for mute in mute_list_to_check:
            if "For" in mute:
                if not self.homePage.click_by(mute, "txt"):
                    assert False

                time.sleep(2)

                if not self.homePage.check_text(self.homePage.OFF_TEXT):
                    assert False

        count_success = 0
        for check_after_mute in result_for_after_mute:
            if type(check_after_mute) == int:
                corrent_time = datetime.datetime.now()
                time_delta = datetime.timedelta(minutes=check_after_mute)
                after_delta = corrent_time + time_delta
                after_delta = after_delta.strftime("%H:%M")

                txt_to_check = self.homePage.MUTE_MSG + after_delta + self.homePage.MUTE_MSG_PART_2
                if not self.homePage.check_text(txt_to_check):
                    continue

            else:
                count_success += 1

        if count_success == 0:
            assert False

    @pytest.mark.order(8)
    def test_back_from_mute(self):
        count_mute = 0
        print_title("Home Page")
        if not self.homePage.click_by(self.homePage.MUTE_BUTTON_RES_ID, "id"):
            assert False

        mute_list_to_check, result_for_after_mute = self.homePage.get_mute_list()
        print(mute_list_to_check)
        if not mute_list_to_check:
            assert False
        print(mute_list_to_check)
        for mute_to_do in mute_list_to_check:
            print(mute_to_do)
            if self.homePage.click_by(mute_to_do, "txt"):
                count_mute +=1
                break

        if count_mute == 0:
            assert False

        time.sleep(10)

        if not self.homePage.click_by(self.homePage.MUTE_BUTTON_RES_ID, "id"):
            assert False

        if not self.homePage.check_text(self.homePage.DB_VALUE_TEXT):
            assert False






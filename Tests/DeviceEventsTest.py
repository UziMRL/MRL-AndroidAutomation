import time
import unittest
from Pages.InformationPage import  *
from Tests.conftest import *
from DataBase.DataBase import *
from Config.Helper import *


class DeviceEventsTest(unittest.TestCase):


    @pytest.mark.skip()
    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.infoPage = InformationPage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1])
        if not self.infoPage.run_set_allow_all_permissions_by_device():
            assert False

    def test_foreground_device_event(self):

        test_time = 600

        if not self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            assert False


        for time_ in range(0,test_time):
            print_title(str(time_))
            self.infoPage.click_back_to_home_page()
            sleep_time_for(5)
            self.infoPage.open_asound_from_background()
            self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt")

        print_title("done waiting to send email")
        sleep_time_for(300)
        if  self.infoPage.click_by(self.infoPage.INFORMATION_BUTTON_TEXT, "txt"):
            self.infoPage.run_send_email_us()












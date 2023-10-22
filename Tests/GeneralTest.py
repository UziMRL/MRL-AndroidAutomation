import time
import unittest
from Pages.InformationPage import  *
from Tests.conftest import *
from DataBase.DataBase import *
from Config.Helper import *
import re

class GeneralTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.infoPage = InformationPage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1])
        # if not self.infoPage.run_set_allow_all_permissions_by_device():
        #     assert False



    def test_check_MRL_dir_and_PCMS(self):
        if self.infoPage.IS_QA:
            if not get_if_MRL_dir_exist_or_PCMs(self.infoPage.device["device_id"]):
                assert False
        else:
            if get_if_MRL_dir_exist_or_PCMs(self.infoPage.device["device_id"]):
                print_failed("Found MRL dir in prod version!")
                assert False
            else:
                print_pass("MRL dir not found in prod version")







import time
import unittest
from Pages.InformationPage import  *
from Tests.conftest import *
from DataBase.DataBase import *

class MapTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.infoPage = InformationPage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1])
        if not self.infoPage.run_set_allow_all_permissions_by_device():
            assert False

    @pytest.mark.skip()
    def test_mock_hod_hasharon_city(self):

        coocoordinates = [{"lat":32.135997,"long":34.891779},
                          {"lat": 32.135686, "long": 34.892021},
                          {"lat": 32.135309, "long": 34.892318},
                          {"lat": 32.134734, "long": 34.892755},
                          {"lat": 32.134007, "long": 34.893349},
                          {"lat": 32.133253, "long": 34.893903},
                          {"lat": 32.132359, "long": 34.893709},
                          {"lat": 32.131328, "long": 34.893497},
                          {"lat": 32.130765, "long": 34.893369},
                          {"lat": 32.130248, "long": 34.892886}
                        ]


        for coo in coocoordinates:


            self.infoPage.set_location(coo["lat"],coo["long"],90)
            time.sleep(60)
            self.infoPage.take_screenshots_and_send_by_mail()

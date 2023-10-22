import unittest
from Pages.HomePage import *
from Tests.conftest import *
from DataBase.DataBase import *
from Config.Helper import *


class HistoryPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.homePage = HomePage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1])
        if not self.homePage.run_set_allow_all_permissions_by_device():
            assert False


    @pytest.mark.order(1)
    def test_History_page(self):
        assert True



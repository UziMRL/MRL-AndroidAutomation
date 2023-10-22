import unittest
from Pages.PermissionsPage import *
from Pages.InformationPage import *
from Tests.conftest import *
from DataBase.DataBase import *
from Config.Helper import *
from Pages.Devices.Sony import *
from Pages.Devices.Pixel_5A import *



class FreeSoundMeterTest(unittest.TestCase):
    JOIN_COMMUNITY = "Join a Community"

    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self, device_name=sys.argv[len(sys.argv) - 1])
        self.permissionsPage = PermissionsPage(driver=self.driver, device_name=sys.argv[len(sys.argv) - 1],run_begin=False)
       # self.infoPage = InformationPage(driver=self.driver,device_name=sys.argv[len(sys.argv) - 1])
        if not self.permissionsPage.run_free_sound_meter_until_permission_page():
            assert False

    #@pytest.mark.skip()
    def test_free_meter(self):
       # self.permissionsPage.run_free_sound_meter_until_permission_page()

        if self.permissionsPage.DEVICE_NAME == "sony":
            if not Sony(self.permissionsPage).set_all_permissions_to_allow_v2():
                assert False

        if self.permissionsPage.DEVICE_NAME == "pixel_5a":
            if not Pixel_5A(self.permissionsPage).set_all_permissions_to_allow_v2():
                assert False

        if not self.permissionsPage.click_by(self.permissionsPage.INFORMATION_BUTTON_TEXT,"txt"):
            assert False
        if not self.permissionsPage.check_text(self.JOIN_COMMUNITY):
            assert False

    #@pytest.mark.skip()
    def test_free_meter_wrong_activation_code(self):
        if self.permissionsPage.DEVICE_NAME == "sony":
            if not Sony(self.permissionsPage).set_all_permissions_to_allow_v2():
                assert False

        if self.permissionsPage.DEVICE_NAME == "pixel_5a":
            if not Pixel_5A(self.permissionsPage).set_all_permissions_to_allow_v2():
                assert False

        if not self.permissionsPage.click_by(self.permissionsPage.INFORMATION_BUTTON_TEXT, "txt"):
            assert False
        if not self.permissionsPage.click_by(self.JOIN_COMMUNITY, "txt"):
            assert False
        if not self.permissionsPage.fill_textfield(self.permissionsPage.INCORRECT_PASSWORD):
            assert False
        if not self.permissionsPage.click_by(self.permissionsPage.ACTIVE_BUTTON_TEXT,"txt"):
            assert False

        time.sleep(2)

        if not self.permissionsPage.check_text(self.permissionsPage.ACTIVE_ERROR_TEXT):
            assert False
        if not self.permissionsPage.click_by(self.permissionsPage.OK_TEXT_CAP,"txt"):
            assert False

    #@pytest.mark.skip()
    def test_free_meter_correct_activation_code(self):

        if self.permissionsPage.DEVICE_NAME == "sony":
            if not Sony(self.permissionsPage).set_all_permissions_to_allow_v2():
                assert False

        if self.permissionsPage.DEVICE_NAME == "pixel_5a":
            if not Pixel_5A(self.permissionsPage).set_all_permissions_to_allow_v2():
                assert False



        if not self.permissionsPage.click_by(self.permissionsPage.INFORMATION_BUTTON_TEXT, "txt"):
            assert False
        if not self.permissionsPage.click_by(self.JOIN_COMMUNITY, "txt"):
            assert False
        if not self.permissionsPage.fill_textfield(self.permissionsPage.ACTIVATION_CODE):
            assert False
        if not self.permissionsPage.click_by(self.permissionsPage.ACTIVE_BUTTON_TEXT,"txt"):
            assert False

        time.sleep(60)




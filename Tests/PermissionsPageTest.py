import unittest
from Pages.PermissionsPage import  *
from Tests.conftest import *
from Config.Helper import *

class PermissionsPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self,device_name = sys.argv[len(sys.argv)-1])
        self.permissionsPage = PermissionsPage(driver=self.driver,device_name=sys.argv[len(sys.argv)-1])

    @pytest.mark.skip()
    def test_set_all_permissions_to_allow_by_device(self):
        if not self.permissionsPage.run_set_allow_all_permissions_by_device():
            assert False

    #@pytest.mark.skip()
    @pytest.mark.order(1)
    def test_set_audio_record_deny(self):
        if not self.permissionsPage.run_set_permission_record_audio_deny_by_device():
            assert False

   # @pytest.mark.skip()
    @pytest.mark.order(2)
    def test_set_location_deny(self):
        if not self.permissionsPage.run_set_permissions_location_deny_by_device():
            assert False

    #@pytest.mark.skip()
    @pytest.mark.order(3)
    def test_set_physical_activity_deny(self):
        if not self.permissionsPage.run_set_permissions_physical_activity_deny_by_device():
            assert False

    @pytest.mark.order(4)
    def test_set_appear_on_top_deny(self):
        if not self.permissionsPage.run_set_permission_appear_on_top_deny_by_device():
            assert False

    def test_set_usage_deny(self):
        if not self.permissionsPage.run_set_permission_usage_deny_by_device():
            assert False

    def test_set_notification_deny(self):
        if not self.permissionsPage.run_set_permission_notification_deny_by_device():
            assert False
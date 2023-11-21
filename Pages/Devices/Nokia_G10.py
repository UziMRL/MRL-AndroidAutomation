from Pages.Devices.BaseDevices import *
import time
from Config.Helper import *

from Pages.Devices.Sony import *
class Nokia_G10(Sony):

    def __init__(self, permission_page):
        self.permission_page = permission_page
        self.Base_devices = BaseDevices(permission_page)
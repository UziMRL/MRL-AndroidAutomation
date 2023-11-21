import time

from Config.Helper import *
from Pages.Devices.BaseDevices import *

from Pages.Devices.Pixel_5A import *
class Pixel_3A(Pixel_5A):

    def __init__(self, permission_page):
        self.permission_page = permission_page
        self.Base_devices = BaseDevices(permission_page)

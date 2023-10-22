from appium import webdriver

from Config.configuration import *

from Config.Helper import *
import pytest
#import allure


def pytest_report_header(config):
     return "Asound"

def pytest_addoption(parser):
    parser.addoption("--input1", action="store", default="default input1")


@pytest.fixture
def input1(request):
    return request.config.getoption("--input1")


@pytest.fixture(scope='session')
def serial_port(request):
    port = request.config.option.serial_port
    if port is None:
        pytest.skip()
    return port


def init_driver(self, device_name):
    print_title("\ndevice name: " + device_name)
    device = device_to_run(device_name=device_name)
    print_warning(str(device))

    desired_caps = dict(
        deviceName=device["device_name"],
        platformName='Android',
        platformVersion=device["android_version"],
        automationName='UiAutomator2',
        deviceid=device['device_id'],
        app=device["app_dir"],
        appPackage=device["app_package"],
        appActivity=device["app_activity"],
        #systemPort = device["systemPort"],
        #adbPort = device["adbPort"],
        newCommandTimeout=100 * 600,
        fullReset=True,
        noReset = False,
        enforceAppInstall=True,
        adbExecTimeout=20000,
        ignoreHiddenApiPolicyError=True,
        clearSystemFiles = True
        # deviceName='Android Emulator',
        # autoGrantPermissions='true'
        # skipServerInstallation = True
    )

    web = 'http://localhost:' + device["local_port"] + '/wd/hub'

    self.driver = webdriver.Remote(web, desired_caps)


    #yield self.driver.close()

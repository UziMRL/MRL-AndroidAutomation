import subprocess
import time

from Config.configuration import *
from Config.Helper import *



def run_main(argv):
    # run main - running all the tests
    l_argv = argv

    if "ios" not in argv:
        # #get devices ids to run
        devices_ids = get_devices_ids()
        appium_process = []
        # get config of devices
        if devices_ids != None:
            for device_id in devices_ids:
                device_config = devices_by_ids[device_id]
                run_pytest(device_id, device_config,l_argv)
                time.sleep(10)


        else:
            print_failed("No found device")




if __name__ == '__main__':
    run_main(sys.argv)

from Config.configuration import *
from Config.Helper import *

def clear_prev_appium_sessions():
    cmd = "killall node"
    p = subprocess.Popen(cmd.split(" "))
    time.sleep(5)
    poll = p.poll()
    if poll is None:
        print_warning("clear_prev_appium_sessions still alive")
        return False
    else:
        print_title("done clear_prev_appium_sessions")
        return True

def start_appium_sessions():
    #get devices ids to run
    devices_ids = get_devices_ids()
    appium_process = []
    # get config of devices

    if devices_ids != [] and devices_ids != None:
        for device_id in devices_ids:
            device_config = devices_by_ids[device_id]
            # for every device open connection with appium
            p1 = connect_device_to_appium(device_id, device_config)
    else:
        print_warning("there is no devices to connect")
if __name__ == '__main__':

    #create appium session to all devices that connected to the computre

    if clear_prev_appium_sessions():
        start_appium_sessions()
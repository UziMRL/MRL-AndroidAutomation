import datetime
import os

import playsound
import sox

import base64
import time
from datetime import timedelta
import subprocess
from Config.configuration import devices_by_ids
from  Config.thread_handler import *
import csv
#import  allure
import threading
import concurrent.futures
from subprocess import PIPE,STDOUT

home_dir = str(os.getcwd())

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# color functions
# ----------------------------------------------------#
using_allure = False

def print_pass(text):
    if not using_allure:
        print(color.GREEN + text +" ---> PASSED"+ color.END)
    else:
        print(text + " => PASSED")


def print_failed(text):
    if not using_allure:
        print(color.RED + text +" ---> FAILED"+color.END)
    else:
        print(text + " => FAILED")


def print_warning(text):
    if not using_allure:
        print(color.YELLOW + text + color.END)
    else:
        print("\n ! " +text+" ! " )


def print_title(text):
    if not using_allure:
        print(color.BLUE + color.BOLD + text + color.END)
    else:
        print("\n ----- " +text+" ----- " )


#convert functions

def convert_base64_to_pic(base64_file,file_name="screenshoot"):
    home_dir = str(os.getcwd())
    print_warning("convert_base64_to_pic")
    image_64_decode= base64.b64decode(base64_file)
    image_result = open(home_dir+'/screenshots/'+file_name+str(datetime.datetime.now())+".png", 'wb')  # create a writable image and write the decoding result
    image_result.write(image_64_decode)


def parser_config_mute(mute_value,device_name):

    print_title("mute value from config table  = "+str(mute_value))

    result_for_after_mute = []
    result = []
    try:
        splited = mute_value.split(";")
        print(splited)

        for text in splited:
            if 'f' in text:
                text_splited = text.split('f')
                value = int(text_splited[1])
                result_for_after_mute.append(value)
                if value < 60:
                    result.append("For {0} minutes".format(value))

                elif value >= 60:
                    hour = int(value) / 60
                    if hour == 1:
                        result.append("For an hour")
                    else:
                        result.append("For {0} hours".format(hour))


            if 'u' in text:
                text_splited = text.split('u')
                value = text_splited[1]
                try:
                    hour = datetime.datetime.strptime(value, "%H")
                except ValueError as e:
                    print("Error to parse mute Until")
                if int(value) == 24:
                    result_for_after_mute.append("12:00")

                if int(value) < 10:
                    result_for_after_mute.append("0{0}:00".format(value))
                else:
                    result_for_after_mute.append("{0}:00".format(value))


                hour = hour.strftime("%-I:%M %p")

                if device_name == "google_Pixel_5a":
                    hour = hour.upper()
                else:
                    hour = hour.lower()
                result.append("Until {0}".format(hour))






        return result,result_for_after_mute

    except ValueError as ve:
        print_failed(str(ve))
        return False,False

def parser_time_to_mute_msg(time_str):
    splited = time_str.splited (" ")

    hour = datetime.datetime.strptime(time_str, "%H")
    hour = hour.strftime("%-I:%M %p")
    print(hour)

def parser_engines_from_device(engines_from_device):


    result = {}
    splited = engines_from_device.split("\n")


    for engine in splited:
        engine_splited=engine.split("(")
        if engine_splited[0] == "OnDeckMatch":
            result["onDeckMatch"] = engine

        if engine_splited[0] == "Watermark":
            result["watermark"] = engine

        elif engine_splited[0] == "ServerMatch":
            result["serverMatch"] = engine

    if "onDeckMatch" not in result.keys():
        result["onDeckMatch"] = None
    if "watermark" not in result.keys():
        result["watermark"] = None
    if "serverMatch" not in result.keys():
        result["serverMatch"] = None




    return  result


def analyes_event(self, event_type, all_data):

    # get info from all data
    eventTS = all_data[0]
    eventMinorType = all_data[1]
    data = all_data[2]

    key_list = list(self.deviceEvents.keys())
    val_list = list(self.deviceEvents.values())
    position = val_list.index(event_type)

    event_date = eventTS.strftime("%Y %m %d")

    current_date = datetime.datetime.today().strftime("%Y %m %d")

    if event_date == current_date:
        print_pass("Event type ({0}) {1} - Minor type = {2}, Data = {3}, eventTS = {4}".format(event_type,
                                                                                               key_list[position],
                                                                                               eventMinorType,
                                                                                               data if data != None or data != "" or data != " " else "None",
                                                                                               eventTS))

    else:
        print_warning("Event type ({0}) {1} - Minor type = {2}, Data = {3}, eventTS = {4}".format(event_type,
                                                                                                  key_list[
                                                                                                      position],
                                                                                                  eventMinorType,
                                                                                                  data if data != None or data != "" else "None",
                                                                                          eventTS))



#Time functions
# ----------------------------------------------------#
import sys
def sleep_time_for(sec=60,need_to_print = False):

    if need_to_print:
        for remaining in range(sec, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)

        sys.stdout.flush()
        sys.stdout.write("\rComplete!\n")
    else:
        print_title("sleep for - "+ str(sec) +" sec")
        time.sleep(sec)
        print_pass("done sleep")


def get_time_mute_for(minutes_=5):

    time_d = datetime.datetime.now() + datetime.timedelta(minutes=minutes_)
    time_d = time_d.strftime("%H:%M")
    return time_d

def check_detction_time(detectionTS):
    print_warning("check detection time")
    limit = datetime.timedelta(minutes=5)  # global

    now_ts = datetime.datetime.utcnow()
    diff = now_ts - detectionTS

    if diff < limit:
        print_title('detection, diff det_ts: ' + str(diff))
        return True

    print_failed('no in limit, diff det_ts: ' + str(diff))
    return False

def get_current_year():
    return datetime.date.today().year

#ads functions
# ----------------------------------------------------#
def play_ad(ad_name_and_format,dir_to_play = ""):

    home_dir =str(os.getcwd())
    if dir_to_play == "":
        path_ =home_dir+'/Ads/' + ad_name_and_format
    else:
        path_ = home_dir + "/Ads/"+ dir_to_play + "/" + ad_name_and_format


    if not os.path.exists(path_):
        print_failed(path_ + " not exists")
        return False

    length = sox.file_info.duration(path_)
    length_ =str(int(length / 60)) + ':' + str(int(length % 60))
    start_to_play = str(datetime.datetime.utcnow().replace(microsecond=0))
    print_title("Start to play ad {0} at {1} UTC time".format(ad_name_and_format,start_to_play))
    print_title("Ad duration: {0} ".format(length_))
    playsound.playsound(path_)

    return start_to_play,length

def play_large_ads_file(dir_name):
    home_dir =str(os.getcwd())
    path_ = home_dir + '/Ads/' + dir_name +"/"

    if not os.path.exists(path_):
        print_failed(path_ + " not exists")
        return False,False,False

    list_dir = os.listdir(path_)

    for item in list_dir:
        if item.endswith(".mp3"):
            length = sox.file_info.duration(path_+item)
            length_ = str(int(length / 60)) + ':' + str(int(length % 60))
            start_to_play = datetime.datetime.utcnow().replace(microsecond=0)
            end_play = start_to_play + timedelta(seconds= length)
            end_play = end_play.replace(microsecond=0)
            print_title("End_play = "+str(end_play) )
            print_title("Start to play ad {0} at {1} UTC time".format(item, start_to_play))
            print_title("Ad duration: {0} ".format(length_))
            playsound.playsound(path_+item)

            return str(start_to_play),str(end_play), length


def read_indexes_ads_from_csv(fileName):
    ads = []
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ads.append(row['Ads'])
    csvfile.close()
    return ads


def compare_result_with_indexes(dir_files,results):
    home_dir = str(os.getcwd())
    path_ = home_dir + '/Ads/' + dir_files + "/"


    list_dir = os.listdir(path_)

    for file in list_dir:
        if file.endswith(".csv"):
            ads_to_compare=read_indexes_ads_from_csv(path_+"/"+file)

    for result in results:
        ad_id = result[0]
        ad_name = result[1]
        detectionTS = result[2]
        exposure_duration = result[3]
        if ad_name in ads_to_compare:
            print_pass(ad_name + " detected")
            continue
        else:
            print_failed(ad_name + "not  detected")


def get_ad_len(ad_name_and_format):
    path_ = "/Users/qa_mrl/Desktop/Appium_Asound_Android/Ads" + '/' + ad_name_and_format
    length = sox.file_info.duration(path_)
    return length


def play_not_exist_ad(ad_name_and_format):
    print_title("Start to play ad " + ad_name_and_format)

    path_ = "/Users/qa_mrl/Desktop/Appium_Asound_Android/NegativeAds" + '/' + ad_name_and_format
    length = sox.file_info.duration(path_)
    length_ = str(int(length / 60)) + ':' + str(int(length % 60))
    print_title("Ad duration:{0}".format(length_))

    playsound.playsound(path_)

def get_ads_to_play_from_dir(path_name=""):
    to_play = []
    if path_name == "":
        path_ = home_dir + "/Ads/"
        list_ = os.listdir(path_)
        for item in list_:
            if item.endswith(".mp3"):
                to_play.append(item)
    else:
        path_ = home_dir + "/Ads/" + path_name +"/"
        list_ = os.listdir(path_)
        for item in list_:
            if item.endswith(".mp3"):
                to_play.append(item)
    return to_play

def get_ads_list_from_csv(path_name):
    print_title("get_ads_list_from_csv : "+path_name)
    to_check = []
    path_ = home_dir + "/Ads/" + path_name + "/"
    list_ = os.listdir(path_)

    for item in list_:
        if item.endswith(".csv"):
            with open(path_+item) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    to_check.append((row["Ads"],row["duration"]))

    return to_check





    # ----------------------------------------------------#

def get_devices_ids():
    devices = []
    try:
        res = subprocess.check_output(["adb", "devices"]).decode("utf-8")

        res = res.split(" ")

        res = res[len(res) - 1]

        res = res.split("\n")



        for item in res:

            if ('device' in item):
                res = item
                res = res.split("\tdevice")
                deviceid = res[0]
                devices.append(deviceid)
        print_warning("device to connect appium service:")
        print(devices)
        return devices
    except Exception as e:
        print_failed(str(e))
        return None

def connect_device_to_appium(device_id,device_config):

    to_run = "appium -p {0} -U {1}".format(device_config["systemPort"],device_id)
    to_run = "appium -p {0} --default-capabilities '{, 'udid':'{1}'}'".format(device_config["local_port"],device_id)
    print_title(to_run)
    proccess = subprocess.Popen(to_run.split(),shell=False)
    print_title(str(proccess))

    return proccess

def get_device_using_headphone(device_id):
    print_title("checking if using cable headphone")
    to_run = "adb -s {0} shell dumpsys activity broadcasts | grep microphone".format(device_id)
    proccess = subprocess.check_output(to_run.split(),shell=False)
    proccess = str(proccess)
    proccess = proccess.split(",")
    for pr in proccess:
        if "state" in pr:
            temp=pr.split("=")
            res = temp[1]

            if res == "1":
                print_pass("using headphone")
                return True

            elif res == "0":
                print_failed("not using cable headphone!")
                return False

def get_device_using_bluetooth_headphone(device_id):
    print_title("checking bluetooth headphone")
    to_run = "adb -s {0} shell dumpsys bluetooth_manager | grep state  ".format(device_id)
    proccess = subprocess.check_output(to_run.split(),shell=False)
    proccess = str(proccess)

    proccess = proccess.split(" ")

    for pr in proccess:
        if "Connected" in pr:
            print_pass("bluetooth headphone connected")
            return True
    else:
        print_failed("not using bluetooth headphone!")
        return False



def get_device_name_and_model_adb(device_id):

    print_title("get_device_name_and_model_adb")
    to_run = "adb -s {0} shell getprop  ro.product.model".format(device_id)
    proccess_device_model = subprocess.check_output(to_run.split(),shell=False)
    proccess_device_model = str(proccess_device_model,'UTF-8')
    proccess_device_model = proccess_device_model.replace('\n',"")

    to_run = "adb -s {0} shell getprop ro.product.brand".format(device_id)
    proccess_device_brand = subprocess.check_output(to_run.split(), shell=False)
    proccess_device_brand = str(proccess_device_brand,'UTF-8')
    proccess_device_brand = proccess_device_brand.replace('\n',"")

    if " " in proccess_device_model:
        proccess_device_model=proccess_device_model.replace(" ","_")

    return proccess_device_brand +"_"+ proccess_device_model



def get_if_MRL_dir_exist_or_PCMs(device_id):
    to_run_1 = "adb -s {0} shell".format(device_id)
    to_run_2 = "if [ -d /sdcard/Download/MRL ]; then echo 'Exists'; else echo 'Not found'; fi"

    to_run = to_run_1 +"  "+to_run_2
    process_1 = subprocess.check_output(to_run.split(), shell=False)

    res = process_1.decode('utf-8')

    if res == 'Exists' or 'Exists' in res:
        print_title("Found MRL folder with PCMs in this device")
        return True
    else:
        print_failed("MRL dir not found on this device")
        return False


def get_if_KotlinRecord_dir_exist(device_id):
    to_run_1 = "adb -s {0} shell".format(device_id)
    to_run_2 = "if [ -d sdcard/Android/data/com.mobileresearchlabs.asound.q/files/kotlinRecords/ ]; then echo 'Exists'; else echo 'Not found'; fi"

    to_run = to_run_1 +"  "+to_run_2
    process_1 = subprocess.check_output(to_run.split(), shell=False)

    res = process_1.decode('utf-8')

    if res == 'Exists' or 'Exists' in res:
        print_title("Found kotlinRecords folder with PCMs in this device")
        return True
    else:
        print_failed("kotlinRecords dir not found on this device")
        return False

def copy_PCMs(device_id,test_name=""):

    device_model = get_device_name_and_model_adb(device_id)

    date_time = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")

    path_ = home_dir + "/PCMs/"
    if test_name == "":
        dir_to_create = device_model+"_"+date_time
    else:
        dir_to_create = device_model + "_" +test_name+ "_" + date_time
    path_+=dir_to_create
    if not os.path.exists(path_):
        os.mkdir(path_)

    to_run_1 = "adb -s {0} pull sdcard/Android/data/com.mobileresearchlabs.asound.q/files/kotlinRecords/ {1}".format(
            device_id,path_)
    to_run_1 = to_run_1.split()

    try:
        process_1 = subprocess.check_output(to_run_1, shell=False)
        print_pass("copied PCMs files + logs")
    except Exception as e:
        print_failed("Error to pull PCMS")
        print_failed(str(e))





def run_pytest(device_id,device_config,l_argv):
    # run_py test - create to_run.txt, file can copy commands and run them manually
    home_dir =str(os.getcwd())
    report_dir = home_dir + "/Reports"
    test_to_run = []
    try:
        test_dir = os.listdir("/Users/qa_mrl/Desktop/Asound_Appium_Automation_v2/Tests")
        #test_dir = os.listdir(home_dir+"/Tests/")
        dir_to_create = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        dir_to_create += "_"+device_config["device_name"]
        # dir_to_create += "_"+get_device_name_and_model_adb(device_id)
        os.mkdir(report_dir+"/"+dir_to_create)
        # os.mkdir(report_dir+dir_to_create+"/allure_results/")


        for test in test_dir:
            if test.endswith("Test.py"):
                name_for_html_res=test.split(".py")
                if len(l_argv) >1:
                    #--alluredir=Reports/"+dir_to_create+"/Allure_Results
                    #--alluredir=Reports/"+dir_to_create+"/allure_results
                    #if l_argv[1] == "-s":
                    #--template=html1/index.html  --report=Reports/"+dir_to_create+"/"+str(name_for_html_res[0])+".html

                        test_to_run.append("pytest  Tests/"+str(test)+" -v -s -l  --template=html/index.html --alluredir=Reports/"+dir_to_create+"/allure_results  --input1 "+get_device_name_and_model_adb(device_id))

                else:

                    #test_to_run.append("pytest  Tests/"+str(test)+" -v -l --capture=tee-sys  --color=yes --alluredir=Reports/"+dir_to_create+"/allure_results   --input1 "+get_device_name_and_model_adb(device_id))
                    #test_to_run.append("pytest  Tests/"+str(test)+" -v -l --capture=tee-sys  --color=yes --html-report=./Reports/"+dir_to_create+"/ --title='"+str(test)+"'  --input1 "+get_device_name_and_model_adb(device_id))
                    test_to_run.append("pytest  Tests/" + str(
                        test) + " -v -l --capture=tee-sys  --color=yes  --template=html/index.html --report=./Reports/" + dir_to_create + "/report_"+str(name_for_html_res[0])+".html --input1 " + get_device_name_and_model_adb(device_id))



        print_title("done to init pytest")
        print_title("pytest tests to run =>")
        test_to_run = sorted(test_to_run)
        print_warning(str(test_to_run))

        file = open(report_dir+"/"+dir_to_create+"/to_run.txt","w")
        file.writelines(str(test_to_run))
        file.close()

        for test in test_to_run:
            subprocess.run(test.split(" "))
            time.sleep(10)



    except Exception as e:
        print_failed(str(e))

def device_to_run(device_name=""):


    devices = get_devices_ids()

    for deviceid in devices:
            devices_by_ids[deviceid]["device_name"] =get_device_name_and_model_adb(device_id=deviceid)
            if device_name ==  devices_by_ids[deviceid]["device_name"]:

                return devices_by_ids[deviceid]



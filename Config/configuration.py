import sys

use_qa = True
USING_PROD_OR_QA_VERSION = 'QA'

APP_DIR_NO_QA = '/Users/qa_mrl/Downloads/Asound 6.11.64.190_useQA.apk'
APP_PACKAGE_NO_QA = 'com.mobileresearchlabs.asound'
APP_ACTIVITY_NO_QA = 'com.mobileresearchlabs.asound.HomeActivity'


APP_DIR_QA = '/Users/qa_mrl/Downloads/Asound 6.11.64.190_useQA.apk'
APP_PACKAGE_QA = 'com.mobileresearchlabs.asound.q'
APP_ACTIVITY_QA = 'com.mobileresearchlabs.asound.HomeActivity'



APP_DIR_QA_KOTLIN = '/Users/qa_mrl/Desktop/Asound_Appium_Automation_v2/APKs/Asound 6.11.64.190_useQA.apk'
APP_PACKAGE_QA_KOTLIN = 'com.mobileresearchlabs.asound.q'
APP_ACTIVITY_QA_KOTLIN = 'com.mobileresearchlabs.asound.ui.HomeActivity'

sql_data_prod = {
    "user": "prod",
    "password": "Prod-mrl-1234",
    "host": 'database-1.c0afvkhvzdxy.us-east-1.rds.amazonaws.com',
    'database': 'ad_db'
}

sql_data_qa = {

    "user": 'admin',
    "password": "Mrl-mrl-1234",
    "host": 'database-1.c0afvkhvzdxy.us-east-1.rds.amazonaws.com',
    "database": 'staging_ad_db'
}


# runnable devices
devices_by_ids = {
## Sony device, running android 12
    'QV725RY83A': {
        "panelistid": "1191005",
        "customerid": "119",
        "projectid":"429",
        "activation_code": "119_1005",
        "android_version": "12",
        "device_name":"Sony_XQ-AU52",
        "device_id":"QV725RY83A",
        "systemPort":"8200",
        "local_port":"10000",
        "app_dir": APP_DIR_QA_KOTLIN,
        "app_package": APP_PACKAGE_QA_KOTLIN,
        "app_activity": APP_ACTIVITY_QA_KOTLIN,
        "iskotlin": True,
        "isQA": True
    }


    ,
    '16211JECB07681':{
        "panelistid":"1191001",
        "customerid":"119",
        "projectid":"429",
        "activation_code": "119_1001",
        "android_version": "14",
        "device_name": "google_Pixel_5a",
        "device_id":"16211JECB07681",
        "systemPort": "8200",
        "local_port": "10000",
        "app_dir": APP_DIR_QA_KOTLIN,
        "app_package": APP_PACKAGE_QA_KOTLIN,
        "app_activity": APP_ACTIVITY_QA_KOTLIN,
        "iskotlin": True,
        "isQA": True
    },


    'MVT0219A11000107':{
        "panelistid":"11901",
        "customerid":"1",
        "projectid":"34",
        "activation_code": "MRLtest11901",
        "android_version": "11",
        "device_name": "mi_poco",
        "device_id":"MVT0219A11000107",
        "systemPort": "8203",
        "local_port": "10006",
        "app_dir": APP_DIR_QA_KOTLIN,
        "app_package": APP_PACKAGE_QA_KOTLIN,
        "app_activity": APP_ACTIVITY_QA_KOTLIN,
        "iskotlin": False,
        "isQA": False
    },
    'c022ca61':{
        "panelistid": "11902",
        "customerid": "1",
        "projectid": "34",
        "activation_code": "MRLtest11902",
        "android_version": "8.1",
        "device_name": "oppo_r11t",
        "device_id": "93VAY0GR73",
        "systemPort": "8204",
        "local_port": "10009",
        "app_dir": APP_DIR_QA_KOTLIN,
        "app_package": APP_PACKAGE_QA_KOTLIN,
        "app_activity": APP_ACTIVITY_QA_KOTLIN,
        "iskotlin": True,
        "isQA": True
    },
    'ce0317133b1b191b04':{
        "panelistid": "1191012",
        "customerid": "119",
        "projectid": "429",
        "activation_code": "119_429_1191012",
        "android_version": "9.0",
        "device_name": "samsung_SM-G950F",
        "deviceid": "ce0317133b1b191b04",
        "device_id":"ce0317133b1b191b04",
        "local_port":"10003",
        "systemPort":"10003",
        "app_dir": APP_DIR_QA_KOTLIN,
        "app_package": APP_PACKAGE_QA_KOTLIN,
        "app_activity":"com.mobileresearchlabs.asound.ui.HomeActivity",
        "iskotlin": True,
        "isQA": True
    },
    'PT99652IA1160900143':{
        "panelistid": "1191008",
        "customerid": "119",
        "projectid": "429",
        "activation_code": "119_429_1191008",
        "android_version": "11",
        "device_name": "nokia_g10",
        "device_id": "PT99652IA1160900143",
        "local_port":"10004",
        "app_dir": APP_DIR_QA_KOTLIN,
        "app_package": APP_PACKAGE_QA_KOTLIN,
        "app_activity": APP_ACTIVITY_QA_KOTLIN,
        "iskotlin": True,
        "isQA": True
    },
    'MVT0219A11000107':{
        "panelistid": "1191025",
        "customerid": "119",
        "projectid": "429",
        "activation_code": "119_429_1025",
        "android_version": "10",
        "device_name": "huawei_mate_30",
        "device_id": "VQM0218302001696",
        "local_port": "10005",
        "app_dir": APP_DIR_QA_KOTLIN,
        "app_package": APP_PACKAGE_QA_KOTLIN,
        "app_activity": APP_ACTIVITY_QA_KOTLIN,
        "iskotlin": True,
        "isQA": True
    }


}



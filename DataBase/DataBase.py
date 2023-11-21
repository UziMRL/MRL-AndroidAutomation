import mysql.connector
from Config.Helper import *
from Config.configuration import *

COUNT_TRY = 5



class DataBase:

    def __init__(self,isQA):
            if isQA:
                self.cnx = mysql.connector.connect(user=sql_data_qa["user"], password=sql_data_qa["password"],
                                               host=sql_data_qa["host"],
                                               database=sql_data_qa["database"])
            else:
                self.cnx = mysql.connector.connect(user=sql_data_prod["user"], password=sql_data_prod["password"],
                                                   host=sql_data_prod["host"],
                                                   database=sql_data_prod["database"])

    def get_ad_detection(self, customerid, panelistid, ad_name, detectionTS,ad_len):
        """Form get_ad_detection.
           @param: detectionTS Data+Time
           @param: ad_len seconds
           """
        ads_ids=self.get_ads_ids_by_customer_id(customerid)

        if ad_name in ads_ids:
            adID = ads_ids[ad_name]
        else:
            print_failed("Ad id Not found for {0} ".format(ad_name))
            return False


        qurey = "select panelistid,detectionTS,addetections.AdID,ads.Name,addetections.watermarkid,addetections.ad_exposure_duration" \
                " from addetections " \
                "join ads using (adid) " \
                "join content using (contentid) " \
                "where addetections.customerid={0} and ads.adid = '{1}' " \
                " and addetections.DetectionTS between '{2}' - interval 2 second and '{2}' + interval {3} second " \
                "and addetections.panelistid = {4}  order by addetections.DetectionTS desc;".format(customerid, adID,
                                                                                                    detectionTS,ad_len,
                                                                                                    panelistid)

        try:
            print_warning(qurey)
            curA = self.cnx.cursor(buffered=True)
            curA.execute(qurey)
            one = curA.fetchone()

            panelistid = one[0]
            detectionTS = one[1]
            adID = one[2]
            ad_name = one[3]
            wm_id = one[4]
            ad_exposure_duration = one[5]

            if wm_id == 0:
                print_pass(
                    "Ad name = " + ad_name + " Ad ID =  "+ str(adID) + " Detected at " + str(detectionTS) +" Exposure duration = "+ str(ad_exposure_duration)+" for panelistid = " + str(panelistid))
            else:
                print_pass(
                    "Ad name = " + ad_name + ", Ad ID =  " + str(adID) + ", WM id = "+str(wm_id)+ ", Detected at " + str(
                        detectionTS) + " for panelistid = " + str(panelistid) )

            return True
        except Exception as e:
            print_failed(str(e))
            print_failed("ad name = "+ ad_name)
            return False

    def get_config_by_customerID(self,customer_id,panelist_id):
        print_title("get config by customerID = {0}".format(customer_id))
        query = "select UseShepherd,UseSpotter,UseWaterMark,Mute  from v1_app_config where customerid = {0} and panelistid = {1};".format(customer_id,panelist_id)


        try:
            print_warning(query)
            curA = self.cnx.cursor(buffered=True)
            curA.execute(query)
            one = curA.fetchone()

            use_shepherd = one[0]
            use_onDeck = one[1]
            use_waterMark = one[2]
            default_mute = one[3]

            return {"use_shepherd":use_shepherd,"use_onDeck":use_onDeck,"use_waterMark":use_waterMark,"default_mute":default_mute}

        except Exception as e:
            print_failed(str(e))
            return False

    def get_engine_config(self,customerid,panelistid):
        query = "select signatureUploadPlan,SamplingPlan,UseSpotter,UseWaterMark,UseShepherd FROM v1_app_config " \
                " where customerid={0} and panelistid={1} limit 1;".format(customerid,panelistid)

        try:
            print_warning(query)
            curA = self.cnx.cursor(buffered=True)
            curA.execute(query)
            one = curA.fetchone()
            if one == None:
                assert False
            else:
                signatureUploadPlan = one[0]
                samplingPlan = one[1]
                use_spotter = one[2]
                use_watermark = one[3]
                use_shepherd = one[4]
                return signatureUploadPlan,samplingPlan,use_shepherd,use_spotter,use_watermark

        except Exception as e:
            print_failed(str(e))
            return False

    def get_count_of_ads_on_engine(self,customerid,projectid,check_watermark=False):

        if check_watermark:
            query = "select distinct count(*) from v1_ads_metadata" \
                    " where customerid = {0} and projectid = {1} and watermarkid!=0;".format(customerid,projectid)
        else:
            query = "select distinct count(*) from v1_ads_metadata" \
                    " where customerid = {0} and projectid = {1} and watermarkid=0;".format(customerid,projectid)

        try:
            print_warning(query)
            curA = self.cnx.cursor(buffered=True)
            curA.execute(query)
            one = curA.fetchone()

            if one == None:
                assert False
            return one[0]

        except Exception as e:
            print_failed(str(e))
            return False

    def get_all_ads_detections_between_times(self,customerid,panelistid,startTime,endTime):

        query = "select addetections.AdID,content.Name,addetections.DetectionTS,addetections.ad_exposure_duration from addetections" \
                " join ads using (adid)" \
                " join content using (contentid)" \
                " where addetections.customerid={0} and panelistid ={1} " \
                " and addetections.DetectionTS between '{2}' and '{3}' + interval 2 minute " \
                " order by detectionTS;".format(customerid,panelistid,startTime,endTime)

        try:
            print_warning(query)
            curA = self.cnx.cursor(buffered=True)
            curA.execute(query)
            all = curA.fetchall()

            if all == [] or all == None:
                print_failed("not found")
                assert False


            else:
                return all

        except Exception as e:
            return False

    def get_device_events(self, panelist_id, customer_id):

        deviceEvents = {1: 'foreground', 2: 'unlocked', 7: 'battery_connection', 10: 'signal_strength',
                        11: 'app_close_by_user', 12: 'battery_charge_level', 13: 'device_startup',
                        14: 'app_force_close', 15: 'wifi_ssid_change', 18: 'device_shutdown',
                        19: 'internet_connectivity', 26: 'clock_diff', 28: 'upload_size', 31: 'sim_swap',
                        34: 'airplane_mode',
                        35: 'roaming_end', 36: 'roaming_end', 40: 'airplane_mode_end', 49: 'screen_off', 52: 'earphone',
                        53: 'significant_motion', 54: 'user_declined_notifications',
                        57: 'timezone_changed', 60: 'is_music_active', 64: 'ip_changed', 65: 'memory',
                        66: 'UNHANDLED_EXCEPTION', 67: 'VISUALIZER_BUFFER'}

        try:
            for event_type in sorted(deviceEvents.keys()):

                quary = "select eventTS,EventMinorType,data from deviceevents where panelistid={0} and customerid={1} and eventType={2} order by eventTS desc limit 10;".format(
                    panelist_id, customer_id, event_type)

                curA = self.cnx.cursor(buffered=True)
                curA.execute(quary)
                all_data = curA.fetchone()

                if all_data == [] or all_data == None:

                    print_failed("cannot find event type ({0}) - {1}".format(event_type, self.deviceEvents[event_type]))


                else:
                    analyes_event(self.deviceEvents[event_type], all_data)

        except Exception as e:
            print_failed(str(e))

    def get_ads_ids_by_customer_id(self,customerid):

        query = "select Name,AdID from ads where customerid={0};".format(customerid)


        temp_results = []

        try:
            curA = self.cnx.cursor(buffered=True)
            curA.execute(query)
            all_results = curA.fetchall()


            if all_results == [] or all_results == None:
                return False
            else:


                temp_dict= {}
                for result in all_results:
                    temp_dict[result[0]] = result[1]

                return temp_dict

        except AttributeError as e:
            print(str(e))
            return False

    def update_mute_values_by_customer_and_project(self,customerid,projectid,mute_values_str):
        query = "update projects set Mute = '{0}' where CustomerID = {1} and projectid={2};".format(mute_values_str,customerid,projectid)

        try:
            curA = self.cnx.cursor(buffered=True)
            curA.execute(query)
            self.cnx.commit()
            if curA.rowcount > 0:
                print(curA.rowcount, "record(s) affected")
                return True
        except mysql.connector.Error as err:
            print_failed(str(err))
            return False



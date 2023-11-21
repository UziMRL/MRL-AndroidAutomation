
from Pages.BasePage import *
from Config.configuration import *
from  Config.Helper import *
import pytest
class StartPage(BasePage):

    # Start page before activation
    TITLE_TEXT = "Quick Question"
    BODY_TEXT = "Hey there, thanks for downloading. We have a quick question before we start…\n\nHave you been invited to join a community panel and were assigned an activation code?"
    ACTIVATE_TEXT = "Yes, I would like to Activate"
    FREE_USER_TEXT = "No, I will use the free sound meter"
    PHOTO_TEXT = "Photo by Priscilla Du Preez on Unsplash"
    Copyright_TEXT = "©{0} Mobile Research Labs Ltd.".format(get_current_year())


    ACTIVE_BUTTON_TEXT ="ACTIVATE"
    ACTIVE_ERROR_TEXT = "Activation Code Error"
    NO_INTERNET_CONNECTION = "No Internet Connection"
    ACTIVE_OK_BUTTON = "OK"
    ACTIVE_CANCEL_BUTTON = "CANCEL"
    INCORRECT_PASSWORD = "1A2B3C4D5E6"


    # Start after activation
    WELCOME_TO_ASOUND_TEXT = "Welcome to Asound"
    GET_START_TEXT = "Get Started"
    BODY_TEXT_AFTER_ACTIVATION ="Congratulations!\n\nYou have been chosen to participate in a special content survey.\n\nAsound measures this device's exposure to audio content playing from any audio source.\n\nThe app runs in the background and should not interfere with the mobile device's regular operation."
    EULA_PRIVACY_TEXT = "By continuing, you agree to our\nEULA and Privacy Policy"

    # Before Start Page
    BEFORE_TITLE_TEXT = "Before we start"
    BODY_TEXT_BEFORE_START = "For the successful operation of this app and in order to be able to create your daily Sound Map, Asound will require certain access permissions.\n\nWe respect your privacy and would like to assure you that none of your personal information is saved and any other information is encrypted immediately.\n\nBy continuing you agree to allow Asound all requested permissions"


    # Permission Page
    PERMISSION_TITLE_TEXT = "Permission"
    MIC_TITLE_TEXT = "Access your Microphone - To Measure the sound around you"
    PHONE_TITLE_TEXT = "Access you Phone state - To allow you privacy during a phone call"
    LOCATION_TITLE_TEXT = "Access your Location - To be able to show the reading on a map.\nFor better coverage please allow the location to be 'Always on'"
    PHYSICAL_TITLE_TEXT = "Access your Physical Activity - To help improve the display on the map and reduce battery consumption"
    NEAR_BY_TITLE_TEXT = "Access nearby devices - To allow checking the audio while using headphones."
    COMMUNICATION_ERROR = "Communication Error"

    def __init__(self, driver,device_name):
        super().__init__(driver,device_name)

    def run_correct_activation(self):

        try:
           if not self.click_by(self.ACTIVATE_TEXT, "txt"):
               assert False

           print_title("fill activation code")

           if not self.fill_textfield(self.ACTIVATION_CODE):
               assert False

           if not self.click_by(self.ACTIVE_BUTTON_TEXT,"txt"):
               assert False


           if not self.check_text(self.WELCOME_TO_ASOUND_TEXT):
               if self.check_text(self.COMMUNICATION_ERROR):
                   assert False

           return True

        except AssertionError as e:

            print_failed("function "+ self.run_correct_activation.__name__)
            return False

    def run_incorrect_activation(self):
        try:

            self.click_by(self.ACTIVATE_TEXT, "txt")

            print_title("fill wrong activation code")

            self.fill_textfield(self.INCORRECT_PASSWORD)

            self.click_by(self.ACTIVE_BUTTON_TEXT, "txt")

            if not self.check_text(self.ACTIVE_ERROR_TEXT):
                assert False

            return True

        except AssertionError as e:
            print_failed("function " + self.run_incorrect_activation.__name__)
            return False

    def run_beginning_until_permission_page(self):

       if not self.run_correct_activation():
           return False
       if not self.click_by(self.GET_START_TEXT, "txt"):
           return False
       if not self.click_by(self.AGREE_AND_CONTINUE_TEXT, "txt"):
           return False
       if not self.click_by(self.AGREE_AND_CONTINUE_TEXT, "txt"):
           return False

       return True

    def run_free_sound_meter_until_permission_page(self):

        list_to_click = [self.FREE_USER_TEXT,
                    self.GET_START_TEXT,
                    self.AGREE_AND_CONTINUE_TEXT,
                    self.AGREE_AND_CONTINUE_TEXT]

        for to_click in list_to_click:
            if not self.click_by(to_click,"txt"):
                return False
        return True

    #checking pages texts
    def start_page_texts_check(self):
        self.run_correct_activation()

        try:

            text_to_check = [self.WELCOME_TO_ASOUND_TEXT,
                            # self.BODY_TEXT_AFTER_ACTIVATION,
                             self.EULA_PRIVACY_TEXT,
                             self.GET_START_TEXT,
                             self.Copyright_TEXT,
                             self.PHOTO_TEXT]

            for text in text_to_check:
               if not self.check_text(text):
                   assert False

            return True
        except AssertionError as e:
            print_failed("function "+self.start_page_texts_check.__name__)
            return False

    def before_start_page_texts_check(self):
        self.run_correct_activation()

        try:

            self.click_by(self.GET_START_TEXT, "txt")
            text_to_check = [self.BEFORE_TITLE_TEXT,
                             self.BODY_TEXT_BEFORE_START,
                             self.AGREE_AND_CONTINUE_TEXT,
                             self.PHOTO_TEXT]

            for text in text_to_check:
               if not self.check_text(text):
                   assert False
            return True
        except AssertionError as e:
            print_failed("function "+self.before_start_page_texts_check.__name__)
            return False

    def permission_page_texts_check(self):
        self.run_correct_activation()
        self.click_by(self.GET_START_TEXT, "txt")
        self.click_by(self.AGREE_AND_CONTINUE_TEXT, "txt")


        try:

            text_to_check = [self.PERMISSION_TITLE_TEXT,
                             self.MIC_TITLE_TEXT,
                             self.PHYSICAL_TITLE_TEXT,
                             self.NEAR_BY_TITLE_TEXT,
                            # self.LOCATION_TITLE_TEXT,
                             self.AGREE_AND_CONTINUE_TEXT,
                             self.PHOTO_TEXT]

            for text in text_to_check:
                if not self.check_text(text):
                    assert False

            return True
        except AssertionError as e:
            print_failed("function " + self.permission_page_texts_check.__name__)
            return False









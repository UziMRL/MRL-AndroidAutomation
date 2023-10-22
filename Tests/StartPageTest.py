import unittest
from Pages.StartPage import  *
from Tests.conftest import *
from Config.Helper import *

class StartPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup_modulo(self):
        init_driver(self,device_name = sys.argv[len(sys.argv)-1])
        self.firstPage = StartPage(driver=self.driver,device_name=sys.argv[len(sys.argv)-1])





    # ------ Tests functions  -----
    # to unskip comment this line -> @pytest.mark.skip()

   #@pytest.mark.skip()
    def test_first_page_texts(self):

        text_to_check = [self.firstPage.TITLE_TEXT,
                    self.firstPage.BODY_TEXT,
                    self.firstPage.ACTIVATE_TEXT,
                    self.firstPage.FREE_USER_TEXT,
                    self.firstPage.Copyright_TEXT,
                    self.firstPage.PHOTO_TEXT
                    ]


        try:
            for text in text_to_check:
                if not self.firstPage.check_text(text):
                    assert False

        except AssertionError as e:
                print_failed("function " + self.test_first_page_texts.__name__)

    #@pytest.mark.skip()
    def test_correct_activation_code(self):
       if not self.firstPage.run_correct_activation():
           assert False

    #@pytest.mark.skip()
    def test_incorrect_activation_code(self):
        if not self.firstPage.run_incorrect_activation():
            assert False

    #@pytest.mark.skip()
    def test_start_page_texts_after_activation(self):
       if not self.firstPage.start_page_texts_check():
           assert False

    #@pytest.mark.skip()
    def test_before_start_page_texts(self):
        if not self.firstPage.before_start_page_texts_check():
            assert False

    #@pytest.mark.skip()
    def test_permission_page_texts(self):
        if not self.firstPage.permission_page_texts_check():
            assert False





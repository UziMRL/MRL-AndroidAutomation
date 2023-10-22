import allure


class AllureHelper:

    def test_attach_body_with_default_kwargs(txt):
         allure.attach(txt)

from page_object.data import BASE_URL
from page_object.pages.dostavka_page import DostavkaPage
import allure


@allure.epic("QAP 19")
@allure.feature("Lesson 22")
@allure.story("Doctavka")
class TestDostavka():

    @allure.title("User open page Dostavka")
    @allure.link(BASE_URL, name="WB")
    @allure.issue("Lesson 22")
    @allure.testcase("TMS-1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_dostavka_page(self, driver):
        dostavka = DostavkaPage(driver)

        dostavka.open()
        dostavka.assert_that_page_is_open()

    @allure.title("User open page Dostavka")
    @allure.link(BASE_URL, name="WB")
    @allure.issue("Lesson 22")
    @allure.testcase("TMS-1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_dostavka_page(self, driver):
        dostavka = DostavkaPage(driver)

        dostavka.open().assert_that_page_is_open()
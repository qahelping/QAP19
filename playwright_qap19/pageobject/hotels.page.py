from playwright.sync_api import Locator

from data.urls import DOMAIN


class HotelsPage():

    def __init__(self, page):
        self.page = page

        self.HOTELS_PAGE: Locator = page.locator('[class="JGFbQ zNQ2x"]')
        self.IN_DATA_PICKER: Locator = page.locator('[aria-label="Дата заезда"]')
        self.OUT_DATA_PICKER: Locator = page.locator('[aria-label="Дата выезда"]')
        self.SUBMIT: Locator = page.locator('[type="submit"]')
        self.WHERE_INPUT: Locator = page.locator('[class="w_eHd input_center"]')

        self.path = f'{DOMAIN}hotels/'

    def open(self):
        self.page.goto(self.path)

    def open_select_data(self, city,  checkin_data, checkin_out_data):
        checkin = self.page.locator(f'[data-qa="calendar-day-{checkin_data}"]')
        checkout = self.page.locator(f'[data-qa="calendar-day-{checkin_out_data}"]')

        self.WHERE_INPUT.fill(city)
        checkin.click()
        checkout.click()
        self.SUBMIT.click()








import time
import random
from itertools import count

from generator.generator import generated_user
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        user_info = next(generated_user())
        full_name = user_info.full_name
        email = user_info.email
        current_address = user_info.current_address
        permanent_address = user_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return full_name, email, current_address, permanent_address

    def verify_filled_fields(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1].strip()
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1].strip()
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]  #.strip().replace('\n', ' ')
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        # for item in item_list:
        #     self.go_to_element(item)
        #     item.click()
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_of_item = box.find_element(*self.locators.TITLE_ITEM).text.strip().lower()
            data.append(title_of_item)
        return str(sorted(data)).replace(' ', '').replace('doc', '').replace('.', '')

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(sorted(data)).replace(' ', '').lower()

class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()
    def click_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_BUTTON,
            'impressive': self.locators.IMPRESSIVE_BUTTON,
            'no': self.locators.NO_BUTTON,
                  }
        radio = self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text

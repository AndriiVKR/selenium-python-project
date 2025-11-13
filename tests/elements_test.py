import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:

    class TestTextBox:
        def test_text_boxes(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.verify_filled_fields()
            assert input_data == output_data, 'data are not equal'

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox, 'check boxes have not been checked'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            assert output_yes == 'Yes', 'data are not equal'
            assert output_no == 'No', 'data are not equal'
            assert output_impressive == 'Impressive', 'data are not equal'

    class TestWebTable:
        def test_web_table_add_person(self, driver):
           web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
           web_table_page.open()
           new_person = web_table_page.add_new_person()
           all_table_persons = web_table_page.check_new_added_person()
           print(new_person)
           print(all_table_persons)
           assert new_person in all_table_persons, 'data are not equal'

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_added_person(key_word)
            table_result = web_table_page.verify_searched_person()
            assert key_word in table_result, 'data are not equal'
























import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class Bot:
    def __init__(self):
        self.driver = None
        self.initialize_driver()
        self.last_message = ""

    def initialize_driver(self):
        self.driver = webdriver.Firefox(
            firefox_profile="C:\\Users\\User\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\szju00ws.selenium",
            executable_path="D:\\programming\\selenium\\geckodriver.exe")

    def enter_whatsapp(self):
        self.driver.get("https://web.whatsapp.com")

    def enter_chat(self, contact):
        inp_xpath_search = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"
        input_box_search = WebDriverWait(self.driver, 50).until(
            lambda driver: driver.find_element_by_xpath(inp_xpath_search))
        input_box_search.click()
        time.sleep(2)
        input_box_search.send_keys(contact + Keys.ENTER)
        time.sleep(2)

    def send_message(self, message):
        inp_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
        input_box = self.driver.find_element_by_xpath(inp_xpath)
        time.sleep(2)
        input_box.send_keys(message + Keys.ENTER)

    def get_last_message(self):
        messages = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]")
        in_messages = messages.find_elements_by_css_selector('div[class="_1RAno message-in focusable-list-item"]')
        if len(in_messages) == 0:
            print("couldn't find messages")
            return
        message = in_messages[-1]
        message_elements = message.find_elements_by_css_selector(
            'span[class="_1VzZY selectable-text copyable-text"]')
        for value in message_elements:
            value.find_elements_by_class_name("span")
            try:
                return value.text
            except selenium.common.exceptions.StaleElementReferenceException:
                return

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

contact = "Laniel"
text = "yeet"


def send_message(driver, message):
    inp_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    time.sleep(2)
    input_box.send_keys(message + Keys.ENTER)


def initialize_firefox():
    return webdriver.Firefox(
        firefox_profile="C:\\Users\\User\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\szju00ws.selenium",
        executable_path="D:\\programming\\selenium\\geckodriver.exe")


def enter_whatsapp(driver):
    driver.get("https://web.whatsapp.com")


def enter_chat(driver, contact):
    inp_xpath_search = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"
    input_box_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    input_box_search.click()
    time.sleep(2)
    input_box_search.send_keys(contact + Keys.ENTER)
    time.sleep(2)


def get_last_message(driver):
    messages = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]")
    in_messages = messages.find_elements_by_css_selector('div[class="_1RAno message-in focusable-list-item"]')
    if len(in_messages) == 0:
        print("couldn't find messages")
        return
    message = in_messages[-1]
    message_elements = message.find_elements_by_tag_name('span')
    for value in message_elements:
        if value.get_attribute("class") == "_1Oy25":
            return value.text


def main():
    driver = initialize_firefox()
    enter_whatsapp(driver)
    enter_chat(driver, contact)
    last_message = ""
    while True:
        message = get_last_message(driver)
        if message != last_message:
            print(message)
            last_message = message
        time.sleep(0.1)
    # driver.quit()


if __name__ == '__main__':
    main()

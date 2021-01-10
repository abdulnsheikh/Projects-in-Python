from selenium import webdriver
from time import sleep


class instagramBot(object):
    """docstring for instagramBot"""
    def __init__(self, username, password):

        self.opts = webdriver.ChromeOptions()
        self.opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.opts,executable_path='chromedriver.exe')

        self.username = username
        self.password = password

        self.driver.get("https://instagram.com")
        sleep(2)

        # send the username to the input box
        self.driver.find_element_by_xpath("//input[@name = 'username']").send_keys(username)

        # send the password to the input box
        self.driver.find_element_by_xpath("//input[@name = 'password']").send_keys(password)

        # click the log in
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
        sleep(2)

        # click the not now button
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(2)

        # dismiss the last notifacation
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()


user_name = ""
password = ""

instagramBot(user_name, password) 


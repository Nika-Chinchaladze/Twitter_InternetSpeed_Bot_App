from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class TwitterPost:
    def __init__(self):
        self.my_service = Service("C:/Zoo_Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.my_service)
        self.gmail = "chincho2022chincho@gmail.com"
        self.user_name = "@Chincharito123"
        self.password = "PeackyBlinders888"

    def into_twitter(self):
        try:
            self.driver.get("https://twitter.com/i/flow/login")
            sleep(5)
            # ------------------ enter gmail ----------------------------:
            enter_gmail = self.driver.find_element(By.TAG_NAME, "input")
            enter_gmail.click()
            sleep(1)
            enter_gmail.send_keys(self.gmail)
            sleep(1)
            enter_gmail.send_keys(Keys.ENTER)
            sleep(5)
            # ------------------ enter username ----------------------------:
            enter_name = self.driver.find_element(By.TAG_NAME, "input")
            enter_name.click()
            sleep(1)
            enter_name.send_keys(self.user_name)
            sleep(1)
            enter_name.send_keys(Keys.ENTER)
            sleep(5)
            # ------------------ enter password ----------------------------:
            enter_password = self.driver.find_element(By.NAME, "password")
            enter_password.click()
            sleep(1)
            enter_password.send_keys(self.password)
            sleep(1)
            enter_password.send_keys(Keys.ENTER)
            sleep(10)
        except NoSuchElementException:
            print("element was not found")

    def twitter_post(self, letter):
        try:
            # ----------------- find text box ------------------- #
            text_place_1 = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            text_place_1.click()
            sleep(2)
            text_place_2 = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            text_place_2.send_keys(f"{letter}")
            sleep(2)
            # ----------------- find twitter button again ------------------- #
            post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            post_button.click()
            sleep(20)
        except NoSuchElementException:
            print("element not found")
        self.driver.quit()

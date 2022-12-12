from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


class InternetSpeed:
    def __init__(self):
        self.my_service = Service("C:/Zoo_Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.my_service)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        sleep(60)
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        speed_down = download_speed.text
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        speed_up = upload_speed.text
        self.driver.quit()
        return {"download": f"{speed_down} Mbps", "upload": f"{speed_up} Mbps"}

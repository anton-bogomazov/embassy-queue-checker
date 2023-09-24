from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.window import WindowTypes


class Driver:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)

    def __get_element(self, id):
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.ID, id)))
        return self.driver.find_element(By.ID, id)

    def fill_field(self, id, content):
        self.__get_element(id).send_keys(content)

    def click_button(self, id):
        try:
            self.__get_element(id).click()
        except:
            pass

    def run(self, uri):
        self.driver.get(uri)

    def new_tab(self):
        self.driver.switch_to.new_window(WindowTypes.TAB)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()
        
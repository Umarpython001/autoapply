from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #EC stands for Expected Condition
import backend.logic.constants as const



class Logic(webdriver.Chrome):
    def __init__(self, should_close = True):
        self.should_close = should_close
        super().__init__(service=Service(r"C:\seleniumDrivers\chromedriver.exe"))

        ...

    def __exit__(self, exc_type, exc, traceback):

        if self.should_close:
            self.quit()

        return super().__exit__(exc_type, exc, traceback)

    def load_page(self):
        self.get(const.BASE_URL)

    def change_currency(self):
        try:
            curr_btn = self.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
        except Exception as e:
            print(e)
        else:
            print(curr_btn.get_attribute("aria-haspopup"))
        ...
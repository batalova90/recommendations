import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager



class Application:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def teardown_method(self):
        self.driver.quit()
    
    def open_admin_panel(self):
        self.driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        self.driver.set_window_size(1022, 745)

    def open_homepage(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1022, 745)

    def login_admin(self, username, password):
        self.open_homepage()
        self.open_admin_panel()
        self.driver.find_element(By.ID, "id_password").send_keys(password)
        self.driver.find_element(By.ID, "id_username").send_keys(username)
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").click()
        element = self.driver.find_element(By.ID, "id_password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()

    def logout_admin(self):
        self.driver.get("http://127.0.0.1:8000/admin/logout/")
        self.open_homepage()

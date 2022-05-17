from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_admin(self, username, password):
        self.app.open_homepage()
        self.app.open_admin_panel()
        self.app.driver.find_element(
                By.ID,
                "id_password"
        ).send_keys(password)
        self.app.driver.find_element(
                By.ID,
                "id_username"
        ).send_keys(username)
        self.app.driver.find_element(
                By.ID,
                "id_password"
        ).click()
        self.app.driver.find_element(
                By.ID,
                "id_password"
        ).click()
        element = self.app.driver.find_element(
                By.ID,
                "id_password"
        )
        actions = ActionChains(self.app.driver)
        actions.double_click(element).perform()
        self.app.driver.find_element(
                By.CSS_SELECTOR,
                ".submit-row > input"
        ).click()

    def logout_admin(self):
        self.app.driver.get(
                "http://127.0.0.1:8000/admin/logout/"
        )
        self.app.open_homepage()

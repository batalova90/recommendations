from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_admin(self, username, password):
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

    def is_logged_in_as(self, username):
        return self.app.driver.find_element(
                By.CSS_SELECTOR,
                "strong"
        ).text.lower() == username

    def is_login(self):
        try:
            self.app.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4)")
            return True
        except:
            return False

    def ensure_login_admin(self, username, password):
        if self.is_login():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout_admin()
        self.login_admin(username, password)

    def ensure_logout_admin(self):
        if self.is_login():
            self.logout_admin()

    def logout_admin(self):
        self.app.open_logoutpage()
        self.app.open_homepage()

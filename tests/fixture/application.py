import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from .session import SessionHelper
from enum_urls import EnumURL


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install()
        )
        self.session = SessionHelper(self)

    def teardown_method(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False
    
    def open_admin_panel(self):
        self.driver.get(
                EnumURL.ADMIN_LOGIN.value
        )

    def open_homepage(self):
        self.driver.get(
                EnumURL.HOMEPAGE.value
        )
        self.driver.set_window_size(1022, 745)

    def open_logoutpage(self):
        self.driver.get(
                EnumURL.ADMIN_LOGOUT.value
        )

    def open_groups_page(self):
        if self.driver.current_url != EnumURL.GROUPS_PAGE.value:
            self.driver.get(
                    EnumURL.GROUPS_PAGE.value
            )

    def open_categories_page(self):
        if self.driver.current_url != EnumURL.CATEGORIES_PAGE.value:
            self.driver.get(
                    EnumURL.CATEGORIES_PAGE.value
            )

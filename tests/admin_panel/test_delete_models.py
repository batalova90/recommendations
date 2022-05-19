import pytest
from selenium.webdriver.common.by import By


def test_delete_group(app):
    app.session.login_admin(
            username="admin",
            password="admin"
    )
    app.driver.find_element(
            By.LINK_TEXT,
            "Groups"
    ).click()
    app.driver.find_elements(
            By.NAME,
            "_selected_action"
    )[-1].click()
    app.driver.find_element(
            By.NAME,
            "action"
    ).find_element(
            By.XPATH,
            "//option[. = 'Delete selected groups']"
    ).click()
    app.driver.find_element(
            By.CSS_SELECTOR,
            "option:nth-child(2)"
    ).click()
    app.driver.find_element(
            By.NAME,
            "index"
    ).click()
    app.driver.find_element(
            By.CSS_SELECTOR,
            "input:nth-child(4)"
    ).click()
    app.session.logout_admin()


def test_delete_category(app):
    app.session.login_admin(
            username="admin",
            password="admin"
    )
    app.driver.find_element(
            By.LINK_TEXT,
            "Categories"
    ).click()
    app.driver.find_elements(
            By.NAME,
            "_selected_action"
    )[-1].click()
    app.driver.find_element(
            By.NAME,
            "action"
    ).find_element(
            By.XPATH,
            "//option[. = 'Delete selected Categories']"
    ).click()
    app.driver.find_element(
            By.CSS_SELECTOR,
            "option:nth-child(2)"
    ).click()
    app.driver.find_element(
            By.NAME,
            "index"
    ).click()
    app.driver.find_element(
            By.CSS_SELECTOR,
            "input:nth-child(4)"
    ).click()
    app.session.logout_admin()

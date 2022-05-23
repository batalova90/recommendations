import pytest
from selenium.webdriver.common.by import By


def count_elements(app, elements):
    elements += app.driver.find_elements(
            By.NAME,
            "_selected_action")
    return len(elements) > 0


def test_delete_group(app):
    app.open_admin_panel()
    app.driver.find_element(
            By.LINK_TEXT,
            "Groups"
    ).click()
    list_elements = []
    if count_elements(app, list_elements):
        list_elements[-1].click()
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


def test_delete_category(app):
    app.open_admin_panel()
    app.driver.find_element(
            By.LINK_TEXT,
            "Categories"
    ).click()
    list_elements = []
    if count_elements(app, list_elements):
        list_elements[-1].click()
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

import pytest
from selenium.webdriver.common.by import By


def get_list_selected(app):
    list_elements = app.driver.find_elements(
            By.NAME,
            "_selected_action"
    )
    return len(list_elements)

def test_create_group(app):
    app.open_admin_panel()
    app.driver.find_element(
            By.LINK_TEXT,
            "Groups"
    ).click()
    old_count_groups = get_list_selected(app)
    app.driver.find_element(
            By.CSS_SELECTOR,
            ".addlink"
    ).click()
    app.driver.find_element(
            By.ID,
            "id_name"
    ).send_keys("test_create_group5")
    app.driver.find_element(
            By.NAME,
            "_save"
    ).click()
    app.open_groups_page()
    new_count_groups = get_list_selected(app)
    assert old_count_groups + 1 == new_count_groups, "The group hasn't been created"


def test_create_category(app):
    app.open_admin_panel()
    app.driver.find_element(
            By.LINK_TEXT,
            "Categories"
    ).click()
    old_count_categories = get_list_selected(app)
    app.driver.find_element(
            By.CSS_SELECTOR,
            ".addlink"
    ).click()
    app.driver.find_element(
            By.ID,
            "id_name"
    ).send_keys("test_create_category")
    app.driver.find_element(
            By.ID,
            "id_slug"
    ).send_keys("test")
    app.driver.find_element(
            By.NAME,
            "_save"
    ).click()
    app.open_categories_page()
    new_count_categories = get_list_selected(app)
    assert old_count_categories + 1 == new_count_categories, "The category hasn't been created"

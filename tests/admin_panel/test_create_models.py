import pytest
from selenium.webdriver.common.by import By

from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.teardown_method)
    return fixture


def test_create_group(app):
    app.login_admin(
            username="admin",
            password="admin"
    )
    app.driver.find_element(
            By.LINK_TEXT,
            "Groups"
    ).click()
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
    app.logout_admin()


def test_create_category(app):
    app.login_admin(
            username="admin",
            password="admin"
    )
    app.driver.find_element(
            By.LINK_TEXT,
            "Categories"
    ).click()
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
    app.logout_admin()

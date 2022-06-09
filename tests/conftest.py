import pytest
import json
import os
from dotenv import load_dotenv

from fixture.application import Application
from fixture.db import DbFixture


load_dotenv()

fixture = None
target = None


def load_config(file_name):
    global target
    if target is None:
        with open(file_name) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(
            request.config.getoption("--target")
    )["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)
    username = web_config["username"]
    password = web_config["password"]
    fixture.session.ensure_login_admin(
            username=username,
            password=password
    )
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(
            request.config.getoption("--target")
    )["db"]
    dbfixture = DbFixture(
            host=db_config['host'],
            database=os.getenv('NAME_DB'),
            user=os.getenv('USERNAME'),
            password=os.getenv('PASSWORD')
    )
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def destroy(request):
    def fin():
        fixture.session.ensure_logout_admin()
        fixture.teardown_method()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

import pytest
import json

from fixture.application import Application


fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    username = target["username"]
    password = target["password"]
    fixture.session.ensure_login_admin(
            username=username,
            password=password
    )
    return fixture


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

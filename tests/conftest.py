import pytest
from fixture.application import Application


fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None:
        fixture = Application(browser=browser)
    elif not fixture.is_valid():
        fixture = Application(browser=browser)
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
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
    parser.addoption("--password", action="store", default="admin")
    parser.addoption("--username", action="store", default="admin")

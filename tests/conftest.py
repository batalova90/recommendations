import pytest
from fixture.application import Application


fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    elif not fixture.is_valid():
        fixture = Application()
    fixture.session.ensure_login_admin(
            username="admin",
            password="admin"
    )
    return fixture


@pytest.fixture(scope="session", autouse=True)
def destroy(request):
    def fin():
        fixture.session.ensure_logout_admin()
        fixture.teardown_method()
    request.addfinalizer(fin)
    return fixture

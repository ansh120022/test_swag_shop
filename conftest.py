import pytest

from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    headless = request.config.getoption("--headless")
    app = Application(headless, url)
    yield app
    app.browser_close()


@pytest.fixture(scope="class")
def login(request, app):
    login = request.config.getoption("--username")
    passwd = request.config.getoption("--password")
    app.open_main_page()
    if app.login.logout_button() == 0:
        app.login.auth(login, passwd)


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://www.saucedemo.com/",
        help="enter base_url",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default=False,
        help="launching browser without gui",
    )

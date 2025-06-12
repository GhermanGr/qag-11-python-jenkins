import pytest
from selene import browser

@pytest.fixture
def setup_formpage_chrome():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.close()

@pytest.fixture()
def fill_out_form(setup_formpage_chrome):
    pass
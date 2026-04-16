from app import app
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('h1', timeout=10)
    assert 'Pink Morsel' in dash_duo.find_element('h1').text


def test_chart_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#sales-chart', timeout=10)
    assert dash_duo.find_element('#sales-chart')


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#region-picker', timeout=10)
    assert dash_duo.find_element('#region-picker')
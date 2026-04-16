import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def pytest_configure(config):
    driver_path = ChromeDriverManager().install()
    driver_dir = os.path.dirname(driver_path)
    os.environ["PATH"] = driver_dir + os.pathsep + os.environ.get("PATH", "")


def pytest_setup_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options
import pytest
import logging
import os
import sys
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium import webdriver
from _pytest.runner import runtestprotocol
from utils.common.logger import configure_log

python_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0,os.path.dirname(__file__))

LOG = configure_log(logging.DEBUG, __name__, "test")

@pytest.fixture(scope='function')
def driver(request):
	"""
	Conftest to Initialize Selenium Webdriver tests.
	1. Opens the browser.
	2. Opens URL.
	3. Maximizes browser window.
	Args:
	request (object): gives access to the requesting test context.
	Raises: NA
	Returns: selenium webdriver instance
	"""
	LOGGER.setLevel(logging.WARNING)
	display = Display(visible=0, size=(1680, 1050))
	display.start()
	if os.getenv("browser") is None or os.getenv("browser") == "chrome":
		chrome_options = Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument("--no-sandbox")
		chrome_options.add_argument("--disable-extensions")
		chrome_options.add_argument("disable-infobars")
		chrome_options.add_argument("enable-automation")
		if os.getenv("CHROME_PATH") is None:
			wdriver = webdriver.Chrome(chrome_options=chrome_options)
		else:
			wdriver = webdriver.Chrome(os.getenv("CHROME_PATH"), chrome_options=chrome_options)
		wdriver.set_window_size(1680, 1050)
	else:
		fp = webdriver.FirefoxProfile()
		fp.set_preference("dom.max_chrome_script_run_time", 60)
		fp.set_preference("dom.max_script_run_time", 60)
		wdriver = webdriver.Firefox(firefox_profile=fp)

	# wdriver.maximize_window()
	wdriver.set_page_load_timeout(50)
	wdriver.implicitly_wait(10)
	wdriver.set_script_timeout(10)
	def end():
		wdriver.quit()
		display.stop()
	request.addfinalizer(end)
	return wdriver


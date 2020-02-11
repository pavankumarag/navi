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

	global TESTNAME_G
	global wdriver
	global display
	testname = request.node.name
	index = testname.find("_")
	TESTNAME_G = testname[index + 1:]
	LOGGER.setLevel(logging.WARNING)
	script_dir = os.path.abspath(sys.path[0])
	"""try:
		display = Display(visible=0, size=(1680, 1050))
		display.start()
	except:
		pass"""
	if os.environ["browser"] == "chrome":
		chrome_options = Options()
		# chrome_options.add_argument('--headless')
		chrome_options.add_argument("--no-sandbox")
		chrome_options.add_argument("--disable-extensions")
		chrome_options.add_argument("disable-infobars")
		chrome_options.add_argument("enable-automation")
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

	return wdriver


def pytest_runtest_protocol(item, nextitem):
	"""
	This method takes snapshot upon test case failure
	Args:
			item (object) : pytest run call object
			nextitem (object) : pytest run call next object
	Returns:
			bool
	"""
	reports = runtestprotocol(item, nextitem=nextitem)
	for report in reports:
		if report.when == 'call':
			if report.outcome == "failed":
				LOG.info("Test has failed")
	LOG.info("Stop display and Quite the browser")
	wdriver.quit()
	#display.stop()
	return True

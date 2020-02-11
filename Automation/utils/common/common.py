# -*- coding: utf-8 -*-
"""Common multi class helpers"""

# pylint: disable=broad-except, bare-except
import logging

import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

from utils.common.logger import configure_log

LOG = configure_log(logging.DEBUG, __name__, "test")


class WaitHelper(object):
    """Helper for different waits"""

    def __init__(self, wdriver, timeout=300):
        """
        Initializes the Web driver wait
        Args:
            wdriver (object): Selenium webdriver object.
            timeout (int) : Timeout value for a wait
        """
        self.wait = ui.WebDriverWait(wdriver, timeout)
        self.driver = wdriver

    def wait_until_element_present(self, element):
        """
        Waits until element is present
        Args:
            element (tuple): Element locator
        """
        try:
            self.wait.until(EC.presence_of_element_located(element))
        except TimeoutException:
            raise NoSuchElementException("UI Element %s not found" % element[1])
        except Exception as exce:
            raise exce

    def wait_until_element_not_present(self, element):
        """
        Waits until element is not present
        Args:
            element (tuple): Element locator
        """
        try:
            self.wait.until_not(EC.presence_of_element_located(element))
        except:
            pass

    def wait_until_page_loads(self, page_start):
        """
        Waits until page is loaded , page is identified by starts with string method
        Args:
            element (tuple): Element locator
            page_start (string): Page start string
        """
        try:
            self.wait.until(lambda driver: driver.title.lower().startswith(page_start))
        except Exception as exce:
            raise exce

    def wait_until_element_visible(self, element):
        """
        Waits until element is visible in timeout secs, if not throws exception
        Args:
            element (tuple): Element locator
        """
        LOG.info("Waiting for '%s' element to get visible" % element[1])
        try:
            self.wait.until(EC.visibility_of_element_located(element))
        except TimeoutException:
            raise NoSuchElementException("UI Element %s not found" % element[1])
        except Exception as exce:
            raise exce

    def wait_until_element_not_visible(self, element):
        """
        Waits until element is not visible in timeout secs, if not throws exception
        Args:
            element (tuple): Element locator
        """
        LOG.info("Waiting for '%s' element to get dis-appear" % element[1])
        try:
            self.wait.until_not(EC.visibility_of_element_located(element))
        except Exception as exce:
            raise exce

    def wait_until_element_is_clickable(self, element):
        """
        Waits until element becomes clickable until timeout secs
        Args:
            element (tuple): Element locator
        """
        try:
            self.wait.until(EC.element_to_be_clickable(element))
        except TimeoutException:
            raise NoSuchElementException("UI Element %s not found" % element[1])
        except Exception as exce:
            raise exce

    def wait_for_text(self, element, text):
        """
        Waits until text to be present in the element
        Args:
            element (tuple): Element locator
            text (string): Text to be present
        """
        try:
            self.wait.until(EC.text_to_be_present_in_element(element, text))
        except TimeoutException:
            raise NoSuchElementException("UI Element %s not found" % element[1])
        except Exception as exce:
            raise exce


class Browser(object):
    """
    This module contains WebElement Related helper methods
    """
    def __init__(self, driver):
        """
        Constructor for Browser class
        Args:
            driver(object): Web driver object
        """
        self.driver = driver

    def is_element_present(self, locator):
        """
        This routines returns True if locator element param <locator> is present on UI else False.
        Args:
            locator(tuple): Web element locator
        Returns:
             boolean: True  if param <locator> element is present on UI else False.
        """
        try:
            self.driver.find_element(*locator)
        except Exception:
            return False
        return True

    def is_element_absent(self, locator):
        """
        This routines returns True if locator element param <locator> is absent on UI else False.
        Args:
            locator(tuple): Web element locator
        Returns:
            boolean: True  if param <locator> element is absent on UI else False.
        """
        try:
            self.driver.find_element(*locator)
        except Exception:
            return True
        return False

    def is_visible(self, element, timeout=2):
        """
        Return True if element is visible within 2 seconds, otherwise False
        Args:
            element (tuple): Element locator
            timeout (int) : Timeout secs for webdriver wait
        Returns:
            True if element is visible within 2 seconds, otherwise False
        """
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element))
            return True
        except TimeoutException:
            return False

    def is_not_visible(self, element, timeout=2):
        """
        Return True if element is not visible within 2 seconds, otherwise False
        Args:
            element (tuple): Element locator
            timeout (int) : Timeout secs for webdriver wait
        Returns:
            True if element is not visible within 2 seconds, otherwise False
        """
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(element))
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        """
        This routine returns current url of the browser
        Returns:
            str : Current url of the browser
        """
        return self.driver.current_url


def scroll_into_view(driver, element):
    """
    This routine scrolls the view to the <element>.
    Args:
        driver(object): web driver object
        element(tuple): web element locator to which you want to scroll
    """
    element = driver.find_element(*element)
    driver.execute_script("return arguments[0].scrollIntoView();", element)

# -*- coding: utf-8 -*-
"""Helper for Clicking WebElement"""

# pylint: disable=broad-except

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class Click(object):
    """
    Contains webelement click related methods.
    """
    def __init__(self, driver):
        """
        Constructor for Click class
        Args:
            driver(object): web driver object
        """
        self.driver = driver

    def button(self, locator):
        """
        Clicks on a button
        Args:
            locator (webelement): Web element to click.
        Raises:
            NoSuchElementException
        Returns: None
        """
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(locator))
            element = self.driver.find_element(*locator)
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()
        except TimeoutException:
            raise NoSuchElementException("UI Element %s not found" % locator[1])
        except Exception:
            try:
                element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(3)
                element.click()
            except Exception as exp:
                raise exp

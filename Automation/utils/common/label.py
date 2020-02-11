# -*- coding: utf-8 -*-
# pylint: disable=no-self-use
"""This module contains methods which helpers in getting data from UI page"""
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Label(object):
    """This module contains methods which helps in getting data from UI page"""
    def __init__(self, driver):
        """
        Constructor for input class
        Args:
            driver(obj): web driver object
        """
        self.driver = driver

    def get_text(self, locator, timeout=30):
        """
        This routine returns text from the label
        Args:
            locator(tuple):  Tuple of two elements containing locator and locator type
            timeout(int): timeout in seconds
        Returns:
            str: text of the web element.
        """
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return element.text
        except TimeoutException:
            raise NoSuchElementException("UI Element %s not found" % locator[1])
        except Exception as exp:
            raise exp

    def get_attribute(self, attribute, locator, is_multiple_attributes=False):
        """This routine gets particular attribute's value of an web element
        Args:
            attribute(str): Name of the attribute whose value you want to egt
            locator(str): Locator of the web element
            is_multiple_attributes(boolean): Set to True if there a are multiple attributes value you want to get
                                             else False.
        Returns:
            str: value of the param <attribute> of the param <locator>
        """
        try:
            if is_multiple_attributes:
                WebDriverWait(self.driver, 30).until(ec.presence_of_all_elements_located(locator))
                attributes = []
                elements = self.driver.find_elements(*locator)
                for element in elements:
                    attributes.append(element.get_attribute(attribute))
                return attributes
            else:
                WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(locator))
                element = self.driver.find_element(*locator)
                return element.get_attribute(attribute)
        except TimeoutException:
            raise NoSuchElementException("UI Element %s not found" % locator[1])
        except Exception as exp:
            raise exp

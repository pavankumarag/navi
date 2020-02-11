import logging
from page_locators.letterboxd import Letterboxd
from utils.common.click import Click
from utils.common.input import Input
from utils.common.label import Label
from utils.common.logger import configure_log
from utils.common.common import WaitHelper
from selenium.webdriver.common.keys import Keys

LOG = configure_log(logging.DEBUG, __name__, "test")

class LetterboxdHelper:
	"""
	Letterboxd relatd helper methods
	"""
	def __init__(self, driver):
		self.driver = driver
		self.input = Input(self.driver)
		self.click = Click(self.driver)
		self.label = Label(self.driver)
		self.wait = WaitHelper(self.driver, timeout=30)

	def search_for_director(self, director):
		"""
		Searches for director in the search field
		:param director:
		"""
		self.input.textbox(director + Keys.ENTER, Letterboxd.SEARCH)

	def go_to_directed_movies_page(self):
		"""
		Takes to directed movies page among others
		"""
		self.click.button(Letterboxd.DIRECTOR_SELECT_PAGE)

	def get_all_movies_of_director(self):
		"""
		Gets all movie names in director movies page
		"""
		movies = []
		i = 1
		try:
			while True:
				ele = list(Letterboxd.EVERY_MOVIE_NAME)
				ele[1] %= i
				self.wait.wait_until_element_present(tuple(ele))
				movie_name = self.label.get_text(tuple(ele))
				movies.append(movie_name)
				i += 1
		except Exception as e:
			LOG.info("Found all movies %s" % str(e))
		return movies
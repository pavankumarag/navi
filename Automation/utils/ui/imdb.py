import logging
from page_locators.imdb import Imdb
from utils.common.click import Click
from utils.common.input import Input
from utils.common.label import Label
from utils.common.logger import configure_log

LOG = configure_log(logging.DEBUG, __name__, "test")

class ImdbHelper:
	def __init__(self, driver):
		self.driver = driver
		self.input = Input(self.driver)
		self.click = Click(self.driver)
		self.label = Label(self.driver)

	def search_for_director(self, director):
		self.input.textbox(director, Imdb.IMDB_SEARCH)
		self.click.button(Imdb.SELECT_DIRECTOR)

	def go_to_directed_movies(self):
		self.click.button(Imdb.GET_DIRECTION_DETAILS)

	def get_all_movies_of_director(self):
		i = 1
		movies = []
		try:
			while True:
				ele = list(Imdb.EVERY_MOVIE_NAME)
				ele[1] %= i
				movie_name = self.label.get_text(tuple(ele))
				if len(movie_name) == 0:
					break
				movies.append(movie_name)
				i += 1
		except Exception as e:
			LOG.info("Found all movies %s" % str(e))
		return movies






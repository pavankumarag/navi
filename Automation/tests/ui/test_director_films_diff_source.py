import pytest
import re
import logging
import json
from utils.ui.imdb import ImdbHelper
from utils.ui.letterboxd import LetterboxdHelper
from utils.common.logger import configure_log

LOG = configure_log(logging.DEBUG, __name__, "test")



imdb_list = []
letterboxd_list = []
test_params = ["Steven Spielberg"]

class TestDifference(object):

	@pytest.mark.parametrize("director", test_params)
	def test_imdb_director_details(self, driver, director):
		"""
		Tests fetcing movies directed by given director from IMDB
		:param driver:
		:param director:
		"""
		global imdb_list
		# director = "Steven Spielberg"
		driver.get("https://www.imdb.com/")
		imdb = ImdbHelper(driver)
		imdb.search_for_director(director)
		imdb.go_to_directed_movies()
		imdb_list = imdb.get_all_movies_of_director()
		assert len(imdb_list) > 0, "Getting movies from imdb failed"

	@pytest.mark.parametrize("director", test_params)
	def test_letterboxd_director_details(self, driver, director):
		"""
		Tests fetcing movies directed by given director from letterboxd
		:param driver:
		:param director:
		"""
		global letterboxd_list
		# director = "Steven Spielberg"
		driver.get("https://letterboxd.com/")
		letterboxd = LetterboxdHelper(driver)
		letterboxd.search_for_director(director)
		letterboxd.go_to_directed_movies_page()
		letterboxd_list = letterboxd.get_all_movies_of_director()
		assert len(letterboxd_list) > 0, "Getting movies from letterboxd failed"

	def test_compare_imdb_letterboxd_result(self):
		"""
		Tests whether movies recieved from imdb and letterboxd are same or not
		"""
		global imdb_list
		global letterboxd_list
		assert len(imdb_list) == len(letterboxd_list), "mismatch between imdb and letterboxd movie list"

	def test_stats_between_imdb_letterboxd(self):
		"""
		Prints various stats like
		1. common movies in IMDB and letterbox
		2. movies which are in imdb but not in letterbox
		3. movies which are in letterbox but not in imdb
		"""
		global imdb_list
		global letterboxd_list
		dict = {}
		dict["number_of_movies_imdb"] = len(imdb_list)
		dict["numbe_of_movies_letterboxd"] = len(letterboxd_list)
		for i in range(len(letterboxd_list)):
			letterboxd_list[i] = re.sub("\d", "", letterboxd_list[i]).strip("()").strip().lower()
		for i in range(len(imdb_list)):
			imdb_list[i] = imdb_list[i].lower()
		imdb_set = set(imdb_list)
		letterboxd_set = set(letterboxd_list)
		#print(imdb_set)
		#print(letterboxd_set)
		#print(imdb_set.intersection(letterboxd_set))
		#print(imdb_set.difference(letterboxd_set))
		#print(letterboxd_set.difference(imdb_set))
		dict["Common_movies"] = list(imdb_set.intersection(letterboxd_set))
		dict["movies_in_imdb_not_in_letterbox"] = list(imdb_set.difference(letterboxd_set))
		dict["movies_in_letterbox_not_in_imdb"] = list(letterboxd_set.difference(imdb_set))
		fp = open("report.json", "w")
		json.dump(dict, fp, indent=4, sort_keys=True)
		fp.close()
		LOG.info("Movies present in both imdb and letterbox %r" % list(imdb_set.intersection(letterboxd_set)))
		LOG.info("Movies present in imdb but not in letterbox %r" % list(imdb_set.difference(letterboxd_set)))
		LOG.info("Movies present in letterbox but not in imdb %r" % list(letterboxd_set.difference(imdb_set)))








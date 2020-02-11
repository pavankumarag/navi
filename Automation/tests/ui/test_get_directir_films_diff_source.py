from utils.ui.imdb import ImdbHelper

imdb_list = []
class TestDifference(object):
	def test_imdb_director_details(self, driver):
		director = "Steven Spielberg"
		driver.get("https://www.imdb.com/")
		imdb = ImdbHelper(driver)
		imdb.search_for_director(director)
		imdb.go_to_directed_movies()
		imdb_list = imdb.get_all_movies_of_director()
		assert len(imdb_list) > 0, "Getting movies from imdb failed"






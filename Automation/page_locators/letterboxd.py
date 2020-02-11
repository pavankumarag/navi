from selenium.webdriver.common.by import By

class Letterboxd:
	SEARCH = By.XPATH, "//input[contains(@id,'search')]"
	DIRECTOR_SELECT_PAGE = By.XPATH, "//a[contains(@href, 'director')]"
	EVERY_MOVIE_NAME = By.XPATH, "//div[@id='content-nav']//following-sibling::ul/li[%d]//span[@class='frame-title']"

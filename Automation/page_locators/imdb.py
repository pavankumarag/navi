from selenium.webdriver.common.by import By

class Imdb:
	IMDB_SEARCH = By.XPATH, "//input[@placeholder='Search IMDb']"
	SELECT_DIRECTOR = By.XPATH, "//li//div[text()='Steven Spielberg']"
	GET_DIRECTION_DETAILS = By.XPATH, "//td[contains(@class, 'name-overview')]//a[@href='#director']"
	ALL_MOVIES = By.XPATH, "//div[@data-category='director']//following-sibling::div"
	EVERY_MOVIE_NAME =By.XPATH, "//div[@data-category='director']//following-sibling::div/div[contains(@class,'filmo-row')][%d]/b/a"
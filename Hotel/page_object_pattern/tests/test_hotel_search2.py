import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from search_hotel import SearchHotelPage
from search_results import SearchResultsPage


@pytest.mark.usefixtures('setup')
class TestHotelSearch:

#   @pytest.fixture()
#   def setup(self):
#       self.driver = webdriver.Chrome(ChromeDriverManager().install())
#       self.driver.implicitly_wait(10)
#       self.driver.maximize_window()
#       yield
#       self.driver.quit()
# drugi test - setup będzie w oddizelnym pliku test_base.py - class rozszerzona o TestBase         

    def test_hotel_search(self, setup):
        self.driver.get('http://www.kurs-selenium.pl/demo/')
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city('Dubai')
        search_hotel_page.set_date_range('23/08/2022', '25/08/2022')
        search_hotel_page.set_travellers('2', '4')
        search_hotel_page.perform_search()
        
        result_page = SearchResultsPage(self.driver)
        hotel_names = result_page.get_hotel_names()
        price_values = result_page.get_hotel_prices()
        
        assert hotel_names[0] == 'Jumeirah Beach Hotel', 'To jest inna nazwa hotelu'
        assert hotel_names[1] == 'Oasis Beach Tower', 'To jest inna nazwa hotelu'
        assert hotel_names[2] == 'Rose Rayhaan Rotana', 'To jest inna nazwa hotelu'
        assert hotel_names[3] == 'Hyatt Regency Perth', 'To jest inna nazwa hotelu'
        
        assert price_values[0] == '$22', 'To jest inna cena'
        assert price_values[1] == '$50', 'To jest inna cena'
        assert price_values[2] == '$80', 'To jest inna cena'
        assert price_values[3] == '$150', 'To jest inna cena'

from selenium.webdriver.common.by import By 
from locators.locators import SearchResultsLocators
import logging
class SearchResultsPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)        
        # self.hotel_names_xpath = SearchResultsLocators.hotel_names_xpath
        # self.hotel_prices_xpath = SearchResultsLocators.hotel_prices_xpath
    
    def get_hotel_names(self):
        
        hotels = self.driver.find_elements(By.XPATH, SearchResultsLocators.hotel_names_xpath)
        names = [hotel.get_attribute('textContent') for hotel in hotels]
        self.logger.info('Available hotels are: ')
        for name in names:
            self.logger.info(name)
        return names            
           
    def get_hotel_prices(self):
        prices = self.driver.find_elements(By.XPATH, SearchResultsLocators.hotel_prices_xpath)
        self.logger.info('Prices are: ')
        hotel_prices = [price.get_attribute('textContent') for price in prices]        
        for price in hotel_prices:
            self.logger.info(price)
        return hotel_prices            
    

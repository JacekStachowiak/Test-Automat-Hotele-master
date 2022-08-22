from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://www.kurs-selenium.pl/demo/')

driver.find_element(By.XPATH, '//span[text()="Search by Hotel or City Name"]').click()
driver.find_element(By.XPATH, '//div[@id="select2-drop"]//input').send_keys('Dubai')
driver.find_element(By.XPATH, '//span[text()="Dubai"]').click()
driver.find_element(By.NAME, 'checkin').send_keys('23/08/2022')
driver.find_element(By.NAME, 'checkout').send_keys('31/08/2022')
driver.find_element(By.ID, 'travellersInput').click()
driver.find_element(By.ID, 'adultInput').clear()
driver.find_element(By.ID, 'adultInput').send_keys('2')
driver.find_element(By.ID, 'childInput').clear()
driver.find_element(By.ID, 'childInput').send_keys('3')
driver.find_element(By.XPATH, '//button[text()=" Search"]').click()

# //h4[contains(@class, 'list_title')]//b
hotels = driver.find_elements(By.XPATH, '//h4[contains(@class, "list_title")]//b') # przypisujemy listę do zmiennej
hotel_names = [hotel.get_attribute('textContent') for hotel in hotels]
for name in hotel_names:
    print('Hotel name: ' + name)
print()    
prices = driver.find_elements(By.XPATH, '//div[contains(@class, "price_tab")]//b') # przypisujemy listę do zmiennej
price_values = [price.get_attribute('textContent') for price in prices]
for price in price_values:
    print('Hotel price:' + price)

assert hotel_names[0] == 'Jumeirah Beach Hotel'
assert hotel_names[1] == 'Oasis Beach Tower'
assert hotel_names[2] == 'Rose Rayhaan Rotana'
assert hotel_names[3] == 'Hyatt Regency Perth'

assert price_values[0] == '$22'
assert price_values[1] == '$50'
assert price_values[2] == '$80'
assert price_values[3] == '$150'

driver.quit()





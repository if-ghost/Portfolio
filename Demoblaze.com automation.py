from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='C:\\Users\IT Productivity Hub\PycharmProjects\pythonProject\chromedriver.exe')
driver = webdriver.Chrome(service = s)
###
import datetime
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Moodle app website
    driver.get('https://www.demoblaze.com/')

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == 'https://www.demoblaze.com/' and driver.title == 'STORE':
        print(f'We\'re at the Demoblaze homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "STORE"')
        # sleep(5)
        # driver.close()
    else:
        print(f'We\'re not at the Demoblaze homepage. Check your code!')
        driver.close()
        driver.quit()

def nexus_6_addtocart():
    driver.find_element(By.XPATH, '//a[contains(., "Nexus 6")]').click()
    assert driver.find_element(By.XPATH, '//h2[contains(., "Nexus 6")]').is_displayed
    driver.find_element(By.XPATH, '//a[contains(., "Add to cart")]').click()
    sleep(0.5)
    driver.switch_to.alert.accept()
    sleep(0.25)
    driver.find_element(By.ID, 'cartur').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[contains(., "Delete")]').click()

def tearDown():
    if driver is not None:
        print(f'---------------')
        print(f'Test completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


setUp()
nexus_6_addtocart()
tearDown()

import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='C:\\Users\IT Productivity Hub\PycharmProjects\pythonProject\chromedriver.exe')

driver = webdriver.Chrome(service = s)

def setUp():
    # Make window full screen
    driver.maximize_window()

    # Let's wait for browser response in general
    driver.implicitly_wait(20)

    # Navigating to the desired website
    url = 'https://en.wikipedia.org/'
    driver.get(url)

    # Checking that we're on the correct URL address and that we're seeing the correct title
    if driver.current_url == 'https://en.wikipedia.org/wiki/Main_Page' and driver.title == 'Wikipedia, the free encyclopedia':
        print(f'We\'re on the wikipedia homepage -- {driver.current_url}')
        print(f'We\'re seeing the following in the title: "Wikipedia, the free encyclopedia"')
    else:
        print(f'Error. Please check your code and try again.')


def search_python():
    driver.find_element(By.ID, 'searchInput').send_keys('Python (programming language')
    sleep(0.25)

    # By using XPATH, we can directly click on the highlighted suggestion
    driver.find_element(By.XPATH, '/html/body/div[6]/div/a/div/span').click()
    sleep(0.25)

    # If we use the following, we will get a list of results:
    # driver.find_element(By.ID, 'searchButton').click()

    if driver.title == 'Python (programming language) - Wikipedia':
        print('We\'re on the Python(programming language) page')
    else:
        print('This is not the Python(programming language) page. Please try again.')


def tearDown():
    if driver is not None:
        print(f'---------------')
        print(f'Test completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

setUp()
search_python()

# Click on Wikipedia logo to navigate to homepage
driver.find_element(By.ID, 'p-logo').click()

tearDown()
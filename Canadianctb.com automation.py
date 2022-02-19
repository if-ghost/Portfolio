import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='C:\\Users\IT Productivity Hub\PycharmProjects\pythonProject\chromedriver.exe')

driver = webdriver.Chrome(service = s)

# Fixture method to open web browser

def setUp():
    # Make window full screen
    driver.maximize_window()

    # Let's wait for browser response in general
    driver.implicitly_wait(30)

    # Navigating to the desired website
    url = 'https://www.canadianctb.ca/'
    driver.get(url)

    # Checking that we're on the correct URL address and we're seeing the correct title
    if driver.current_url == 'https://www.canadianctb.ca/' and driver.title == 'CCTB | Canadian College of Technology and Business':
        print(f'We\'re on the CCTB homepage -- {driver.current_url}')
        print(f'(We\'re seeing the following in the title: "CCTB | Canadian College of Technology and Business"')
    else:
        print(f'Error. Please check your code and try again.')

def virtual_student_lounge():
    if driver.current_url ==  'https://www.canadianctb.ca/':
        driver.find_element(By.LINK_TEXT, 'Virtual Student Lounge').click()
    if driver.current_url == 'https://www.canadianctb.ca/virtual-student-lounge' and driver.title == 'Virtual Student Lounge | CCTB':
        print(f'We are at the Virtual Student Lounge')
    else:
        print(f'We\'re not at the Virtual Student Lounge. Please try again')
    sleep(5)

def tearDown():
    if driver is not None:
        print(f'---------------')
        print(f'Test completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

setUp()
virtual_student_lounge()
tearDown()
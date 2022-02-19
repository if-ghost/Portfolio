import sys
import datetime
import Lab17_Locators_MaxOtis as locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service(executable_path= 'C:\\Users\IT Productivity Hub\PycharmProjects\pythonProject\chromedriver.exe')
driver = webdriver.Chrome(service=s)
###
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def logger():
    old_instance = sys.stdout
    log_file = open('opencart_data.log', 'a')
    sys.stdout = log_file
    print(f'Email: {locators.email} \nUsername: {locators.username} \nPassword: {locators.password}')
    print('--------------')
    sys.stdout = old_instance
    log_file.close()


def setUp():
    # make full screen
    driver.maximize_window()

    # driver wait
    driver.implicitly_wait(10)

    # Navigate to the open cart homepage
    driver.get(locators.opencart_homepage_url)

    # Confirm we are on the right page
    if driver.current_url == 'https://www.opencart.com/' and driver.title == 'OpenCart - Open Source Shopping Cart Solution':
        print(f'We are the Opencart homepage: {driver.current_url}')
        print('We are seeing "OpenCart - Open Source Shopping Cart Solution" in the title')
    else:
        print('We are not at the opencart homepage. Please check the code and try again.')

def register_newuser():
    driver.find_element(By.XPATH, '//div/a[contains(., "Register")]').click()
    # or
    # driver.find_element(By.XPATH, '//div/a[text() = "Register"]').click()
    driver.find_element(By.ID, 'input-username').send_keys(locators.username)
    print(f'Username: {locators.username}')
    driver.find_element(By.ID, 'input-firstname').send_keys(locators.first_name)
    driver.find_element(By.ID, 'input-lastname').send_keys(locators.last_name)
    driver.find_element(By.NAME, 'email').send_keys(locators.email)
    sleep(0.25)
    print(f'Email: {locators.email}')
    # Select country from drop down list
    Select(driver.find_element(By.ID, 'input-country')).select_by_visible_text('Canada')

    driver.find_element(By.ID, 'input-password').send_keys(locators.password)
    print(f'Password: {locators.password}')

    # You have to manually choose and click on the requested image. This is a security feature and cannot be automated. Complete registration manually.

    # Capture generated data
    logger()

    # Check that registration was successful
    # if driver.title == 'OpenCart - Account Register Success':
    #     print('Registration was successful')
    # else:
    #     print('Registration failed')


def log_in():
    # make full screen
    driver.maximize_window()

    # driver wait
    driver.implicitly_wait(10)

    # Navigate to the open cart homepage
    driver.get(locators.opencart_homepage_url)

    driver.find_element(By.XPATH, '//div/a[contains(., "Login")]').click()
    driver.find_element(By.CSS_SELECTOR, "input#input-email").send_keys(locators.opencart_email)
    driver.find_element(By.ID, 'input-password').send_keys(locators.opencart_password)

    driver.find_element(By.XPATH, '//button[contains(., "Login")]').click()

    # one time pin setup- not needed for subsequent login
    # assert driver.title = 'Account PIN'
    # driver.find_element(By.ID, 'input-pin').send_keys('1122')
    # driver.find_element(By.XPATH, '//button[contains(., "Submit")]').click()

    # Enter PIN if prompted
    if driver.find_element(By.XPATH, '//h1[text() = "PIN Security Check"]').is_displayed():
        driver.find_element(By.ID, 'input-pin').send_keys('1122')
        driver.find_element(By.XPATH, '//button[contains(., "Continue")]').click()


    # Confirm that you are logged in
    if driver.title == 'OpenCart - Your Account' and driver.find_element(By.XPATH, '//p[text() = "Welcome to OpenCart!"]').is_displayed():
        print('Login Successful. We are at the user account page.')

def topmenu_navigation():
    # Navigate to "showcase" page
    driver.find_element(By.XPATH, '//a[contains(., "Resources")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[contains(., "Showcase")]').click()
    if driver.title == 'OpenCart - Showcase':
        print('Successfully navigated to "Showcase" page.')
    sleep(0.25)
    # Navigate to "Download page
    driver.find_element(By.XPATH, '//a[text() = "Download"]').click()
    if driver.title == 'OpenCart - Downloads' and driver.find_element(By.XPATH, '//h4[text() = "Download & host your own"]').is_displayed():
        print('Successfully navigated to "Download" page.')

def log_out():
    driver.find_element(By.XPATH, '//div/a[contains(., "Logout")]').click()
    # Note: This will not work when trying to immediately log out after registration, as the webdriver is interrupted, due to manual registration. (see notes in register_newuser() step.)
    sleep(0.25)
    assert driver.title == 'OpenCart - Open Source Shopping Cart Solution'

def tearDown():
    if driver is not None:
        print(f'---------------')
        print(f'Test completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

###
# Call the functions
setUp()
register_newuser()
sleep(1)
log_in()
topmenu_navigation()
log_out()
tearDown()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 

URL= 'https://www.saucedemo.com/'
USERNAME= 'standard_user'
PASSWORD= 'secret_sauce'

def get_driver():
    #instalacion del driver
    service = Service(ChromeDriverManager().install())
    driver= webdriver.Chrome(service=service)

    time.sleep(5)
    return driver


def login_saucedemo(driver):
    driver.get(URL) #ingresamos a la URL

    #ingresamos credenciales
    driver.find_element(By.NAME, 'user-name').send_keys(USERNAME)
    driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
    time.sleep(5)
    driver.find_element(By.ID, 'login-button').click() #clickeamos el boton
    time.sleep(5)

    






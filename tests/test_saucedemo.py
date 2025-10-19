import pytest   # en este archivo usamos el framewor pytest
import sys
import os
#hacer una ruta relativa, absoluta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from selenium.webdriver.common.by import By
from utils.helpers import login_saucedemo, get_driver  #importamos las funciones 
import time






@pytest.fixture

def driver():
    #para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()


def test_login(driver):
    login_saucedemo(driver)                         # iniciamos secion
    assert "inventory.html" in driver.current_url   # verificamos la url del catalogo sea correcto
    titulo = driver.find_element(By.CSS_SELECTOR, 'Div.header_secondary_container .title').text
    assert titulo == 'Products'


def test_catalogo(driver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0


def test_carrito(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    products[0].find_element(By.TAG_NAME, 'button').click()
    products[1].find_element(By.TAG_NAME, 'button').click()

    time.sleep(3)

    total = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert total =='2'

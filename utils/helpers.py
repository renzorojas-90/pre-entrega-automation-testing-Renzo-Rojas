from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 
from selenium.webdriver.support.ui import WebDriverWait # modulo de espera
from selenium.webdriver.support import expected_conditions as EC # modulo para condicionar, 

URL= 'https://www.saucedemo.com/'
USERNAME= 'standard_user'
PASSWORD= 'secret_sauce'

def get_driver():
    #instalacion del driver
    service = Service(ChromeDriverManager().install())
    driver= webdriver.Chrome(service=service)

    #time.sleep(5) espera siempre los seundos
    driver.implicitly_wait(5)  #un limite de tiempo para resolver 
    return driver


def login_saucedemo(driver):
    driver.get(URL) #ingresamos a la URL

    #ingresamos credenciales

    # atacamos un tema puntual, esperamos 10 segundos, sino encuentra el elemento, lanza error de time
    WebDriverWait(driver, 10).until(    
        EC.element_to_be_clickable((By.NAME, 'user-name'))
    ).send_keys(USERNAME)  
    
    #driver.find_element(By.NAME, 'user-name').send_keys(USERNAME)

    driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
    time.sleep(5)
    driver.find_element(By.ID, 'login-button').click() #clickeamos el boton
    time.sleep(5)

    






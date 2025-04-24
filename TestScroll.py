import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_opciones = Options()
chrome_opciones.add_argument("--start-maximized")

localizador = webdriver.Chrome(options=chrome_opciones)

localizador.get("https://landing-page-tesla.vercel.app/")
time.sleep(3)

try:
    espera = WebDriverWait(localizador,10)
    Buscar = espera.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='modelS']//a[@class='hero-footer-a'][normalize-space()='Pedido Personalizado']")))
    Buscar = localizador.find_element(By.XPATH,"//div[@id='modelS']//a[@class='hero-footer-a'][normalize-space()='Pedido Personalizado']")
    ir = localizador.execute_script("arguments[0].scrollIntoView()", Buscar)
    time.sleep(4)

except TimeoutError as ex:
    print("Elemento no disponible")
time.sleep(2)
localizador.close()
from selenium import webdriver
import time 
import os
from datetime import datetime 

file_path = 'file:///' + os.path.abspath('banner.html')


# Configuración de Selenium con ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ejecutar en modo headless (sin abrir el navegador)  # Establecer el tamaño de la ventana

# Ruta del ChromeDriver (asegúrate de que esté en tu PATH o proporciona la ruta completa)
driver = webdriver.Chrome(options=options)

def get_banner():
    try:
        # Cargar el archivo HTML
        driver.get(file_path)

        # Esperar un momento para asegurarse de que todo el contenido esté cargado
        time.sleep(2)

        banner_width = 1592
        banner_height = 543

        driver.set_window_size(banner_width, banner_height)

        # Tomar la captura de pantalla
        name_screenshot = f"banner-linkedin-{datetime.now().time().strftime("%H:%M")}.png"
        driver.save_screenshot(f"../banners/{name_screenshot}")

        print(f"Imagen PNG generada: {name_screenshot}")
    finally:
        # Cerrar el navegador
        driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def buscar_links_promocoes(driver):
    driver.get('https://www.kabum.com.br/ofertas/ofertasdodia')
    wait = WebDriverWait(driver, 25)
    
    # Espera carregar os produtos (pode variar, ajustamos conforme necessário)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/produto/']")))
    except:
        time.sleep(5)  # fallback
    
    # Pega links de produtos (padrão KaBuM: /produto/ID/nome)
    elementos = driver.find_elements(By.CSS_SELECTOR, "a[href*='/produto/']")
    
    urls = []
    for elemento in elementos:
        try:
            href = elemento.get_attribute("href")
            if "/produto/" in href and href not in urls:
                # Limpa parâmetros extras
                clean_url = href.split("?")[0].split("#")[0]
                urls.append(clean_url)
        except:
            pass
    
    return list(set(urls))[:30]  # limita para não sobrecarregar
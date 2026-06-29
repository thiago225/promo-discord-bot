from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def buscar_produto(driver, url):

    driver.get(url)

    wait = WebDriverWait(driver, 20)
    try:
        preco_inteiro = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole")))
        preco_decimal = driver.find_element(By.CLASS_NAME, "a-price-fraction")
        preco = f"{preco_inteiro.text},{preco_decimal.text}"
    except TimeoutException:
        try:
            preco = driver.find_element(By.ID, "priceblock_ourprice").text.strip()
        except Exception:
            try:
                preco = driver.find_element(By.ID, "priceblock_dealprice").text.strip()
            except Exception:
                return None

    try:
        foto = driver.find_element(By.ID, "landingImage").get_attribute("src")
    except Exception:
        foto = ""

    # esse elemento é um span que contém o desconto, mas pode não estar presente em todos os produtos. Então, vamos usar um try-except para lidar com isso.
    try:
        desconto = driver.find_element(By.CLASS_NAME, "savingsPercentage").text.strip()
    except Exception:
        desconto = "Desconto não disponível"

    try:
        preco_total = driver.find_element(By.CSS_SELECTOR, ".a-price.a-text-price .a-offscreen").text.strip()
    except Exception:
        preco_total = "Preço total não disponível"

    try:
        titulo = driver.find_element(By.ID, "productTitle").text.strip()
    except Exception:
        titulo = "Título não disponível"

    return {
        "titulo": titulo,
        "preco": preco,
        "url": url,
        "foto": foto,
        "desconto": desconto,
        "preco_total": preco_total,
        "store": "amazon"
    }
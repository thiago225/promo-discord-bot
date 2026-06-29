from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def buscar_produto(driver, url):

    driver.get(url)

    wait = WebDriverWait(driver, 20)
    preco_inteiro = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole")))

    preco_decimal = driver.find_element(By.CLASS_NAME, "a-price-fraction")
    preco_desconto = f"{preco_inteiro.text},{preco_decimal.text}"
    foto = driver.find_element(By.ID, "landingImage").get_attribute("src")

    # esse elemento é um span que contém o desconto, mas pode não estar presente em todos os produtos. Então, vamos usar um try-except para lidar com isso.
    try:
        desconto = driver.find_element(By.CLASS_NAME, "savingsPercentage").text.strip()
    except:
        desconto = "Desconto não disponível"

    try:
        preco_total = driver.find_element(By.CSS_SELECTOR, ".a-price.a-text-price .a-offscreen").text.strip()
    except:
        preco_total = "Preço total não disponível"

    titulo = driver.find_element( By.ID, "productTitle").text.strip()

    return {
        "titulo": titulo,
        "preco": preco_desconto,
        "url": url,
        "foto": foto,
        "desconto": desconto,
        "preco_total": preco_total
    }
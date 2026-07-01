from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def buscar_produto(driver, url):
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    time.sleep(5)  # mais tempo para JS carregar

    # Título
    try:
        titulo = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text.strip()
    except:
        titulo = "Título não disponível"

    # === PREÇO - Versão mais forte ===
    preco = "Preço não encontrado"
    
    # 1. Seletores comuns
    selectors = [
        ".preco_normal", ".preco_desconto", "span[class*='price']", 
        ".final-price", ".product-price", "[data-testid*='price']",
        "strong[class*='price']", ".offer-price"
    ]
    
    for selector in selectors:
        try:
            elems = driver.find_elements(By.CSS_SELECTOR, selector)
            for elem in elems:
                text = elem.text.strip()
                if any(c.isdigit() for c in text):
                    preco = re.sub(r'[^\d.,]', '', text)
                    print(f"   → Preço encontrado com: {selector}")
                    break
            if preco != "Preço não encontrado":
                break
        except:
            continue

    # 2. Fallback com regex no body inteiro
    if preco == "Preço não encontrado":
        try:
            body_text = driver.find_element(By.TAG_NAME, "body").text
            match = re.search(r'R\$\s*(\d{1,3}(?:\.\d{3})*,\d{2})', body_text)
            if match:
                preco = match.group(1)
                print("   → Preço encontrado via regex")
        except:
            pass

    # Foto
    try:
        foto = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img, img[src*='produtos/fotos']").get_attribute("src")
    except:
        try:
            fotos = driver.find_elements(By.TAG_NAME, "img")
            for img in fotos:
                src = img.get_attribute("src") or ""
                if "kabum.com.br" in src and ("produtos" in src or "fotos" in src) and "logo" not in src.lower():
                    foto = src
                    break
            else:
                foto = ""
        except:
            foto = ""

    # Desconto
    try:
        desconto = driver.find_element(By.CSS_SELECTOR, "[class*='discount'], .desconto, .economy").text.strip()
    except:
        desconto = "Desconto não disponível"

    return {
        "titulo": titulo,
        "preco": preco,
        "url": url,
        "foto": foto,
        "desconto": desconto,
        "preco_total": preco,
        "store": "kabum"
    }
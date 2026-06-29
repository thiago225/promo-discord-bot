from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def buscar_links_promocoes(driver):

    driver.get("https://www.amazon.com.br/gp/goldbox/")
    wait = WebDriverWait(driver, 20)

    wait.until(EC.presence_of_element_located((By.ID, "DealsGridScrollAnchor")))
    elementos = driver.find_elements(By.CSS_SELECTOR,"a[href*='/dp/']" )

    urls = []

    for elemento in elementos:
        try:
            href = elemento.get_attribute("href")

            if "/dp/" in href:
                urls.append(href.split("?")[0])

        except:
            pass

    return list(set(urls))
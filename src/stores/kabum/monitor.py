from stores.kabum.discover import buscar_links_promocoes
from stores.kabum.product import buscar_produto
from database.comandos.sql import *
import traceback

def monitorar_kabum(driver):
    novos = []
    urls = buscar_links_promocoes(driver)

    for url in urls:
        try:
            produto = buscar_produto(driver, url)
            if produto is None or not produto["preco"] or produto["preco"] == "Preço não encontrado":
                continue

            existente = get_product_by_url(url)

            if existente:
                if existente["last_price"] != produto["preco"]:
                    update_product_price(url, produto["preco"])
                    novos.append(produto)
            else:
                insert_product(produto)
                novos.append(produto)

        except Exception as erro:
            print(f"ERRO Kabum {url}: {erro}")
            traceback.print_exc()
            continue  # continua com próximo em vez de parar tudo
        finally:
            # Pequena pausa para não ser bloqueado
            driver.refresh()
            # time.sleep(1)  # opcional

    return novos
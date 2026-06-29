from stores.amazon.discover import buscar_links_promocoes
from stores.amazon.product import buscar_produto
from database.comandos.sql import *
import traceback

def monitorar_mercadolivre(driver):

    novos = []

    urls = buscar_links_promocoes(driver)

    for url in urls:
        try:

            produto = buscar_produto(driver)
            # print(f"Produto encontrado: {produto['titulo']} - R$ {produto['preco']} - {produto['url']} - {produto['desconto']}  - {produto['foto']} - {produto['preco_total']}")
            existente = get_product_by_url(url)

            if existente:

                if existente["last_price"] != produto["preco"]:
                    update_product_price( url, produto["preco"])
                    novos.append(produto)

            else:
                insert_product(  produto["url"],  produto["titulo"], produto["preco"] )
                novos.append(produto)

        except Exception as erro:
            print(erro)
            print("ERRO:")
            print(type(erro).__name__)
            print(erro)
            traceback.print_exc()

            return []
        finally:
            driver.refresh()


    return novos
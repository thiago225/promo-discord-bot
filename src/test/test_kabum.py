import sys
import os
# Adiciona o diretório atual e o pai no path (importante!)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.utils.browser import criar_driver  # ajuste o caminho se necessário
except ImportError:
    from utils.browser import criar_driver
    
from stores.kabum.discover import buscar_links_promocoes
from stores.kabum.product import buscar_produto
import traceback

def test_kabum():
    print("🚀 Iniciando teste da KaBuM...")
    driver = criar_driver()
    try:
        print("\n=== 1. Discover (Ofertas do Dia) ===")
        urls = buscar_links_promocoes(driver)
        print(f"✅ Encontradas {len(urls)} URLs de produtos.")

        for i, url in enumerate(urls[:6]):
            print(f"   {i+1}: {url}")

        if urls:
            print("\n=== 2. Produto (primeiro link) ===")
            produto = buscar_produto(driver, urls[0])
            
            print(f"Título: {produto['titulo']}")
            print(f"Preço:   R$ {produto['preco']}")
            print(f"Desconto: {produto['desconto']}")
            print(f"Foto: {produto['foto']}..." if produto['foto'] else "Foto: Sem imagem")
            print(f"URL: {produto['url']}")

    except Exception as e:
        print("❌ ERRO durante o teste:")
        traceback.print_exc()
    finally:
        driver.quit()
        print("\n✅ Teste finalizado. Driver fechado.")

if __name__ == "__main__":
    test_kabum()
import asyncio
from utils.browser import criar_driver
from stores.amazon.monitor import monitorar_amazon
from stores.kabum.monitor import monitorar_kabum
from stores.mercado_livre.monitor import monitorar_mercadolivre
from stores.shopee.monitor import monitorar_shopee

from discord_bot import (iniciar,enviar_promocao,client)
import sys
from config import STORES

sys.dont_write_bytecode = True

MONITOR_FUNCTIONS = {
    "monitorar_amazon": monitorar_amazon,
    "monitorar_kabum": monitorar_kabum,
    "monitorar_mercadolivre": monitorar_mercadolivre,
    "monitorar_shopee": monitorar_shopee,
}


async def verificar():

    while True:

        print("Verificando promoções...")

        driver = criar_driver()

        try:
            for store in STORES: 

                monitor_fn = MONITOR_FUNCTIONS.get(store["monitor"])
                if monitor_fn is None:
                    raise ValueError(f"Monitor não encontrado: {store['monitor']}")

                produtos = await asyncio.to_thread(monitor_fn, driver)

                # envia no discord
                for produto in produtos:
                    print("Enviando promoção... Titulo:" + produto["titulo"])
                    await enviar_promocao(produto, store['channel']) #enviar_promocao(produto, channel_id)

        except Exception as erro:
            print(erro)
        finally:
            driver.quit()

        await asyncio.sleep(1800)


@client.event
async def on_ready():
    print(f"Conectado: {client.user}")

    await verificar()


iniciar()
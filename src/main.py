import asyncio
from stores.amazon.browser import criar_driver
from stores.amazon.monitor import monitorar
from discord_bot import (iniciar,enviar_promocao,client)
import sys

sys.dont_write_bytecode = True


async def verificar():

    while True:

        print("Verificando promoções...")

        driver = criar_driver()

        try:
            produtos = await asyncio.to_thread(monitorar, driver )

            # envia no discord
            for produto in produtos:
                print("Enviando promoção... Titulo:" + produto["titulo"])
                await enviar_promocao(produto)

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
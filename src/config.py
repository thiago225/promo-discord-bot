from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

STORES = [
    {'name': 'AMAZON', 'channel': int(os.getenv("CHANNEL_ID_AMAZON")), "monitor": "monitorar_amazon"},
    {'name': 'KABUM', 'channel': int(os.getenv("CHANNEL_ID_KABUM")), "monitor": "monitorar_kabum"},
    # {'name': 'MERCADO LIVRE', 'channel': int(os.getenv("CHANNEL_ID_MECARDO_LIVRE")), "monitor": "monitorar_mercadolivre"},
    # {'name': 'SHOPEE', 'channel': int(os.getenv("CHANNEL_ID_SHOPEE")), "monitor": "monitorar_shopee"},
]

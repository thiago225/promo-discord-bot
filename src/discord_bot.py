import discord
import asyncio

from config import DISCORD_TOKEN, CHANNEL_ID

intents = discord.Intents.default()

client = discord.Client(intents=intents)


async def enviar_promocao(produto):

    canal = client.get_channel(CHANNEL_ID)

    if canal:

        embed = discord.Embed(
            title=produto["titulo"],
            url=produto["url"],
            description="🔥 Promoção encontrada na Amazon",
            color=0xff9900
        )

        embed.set_image(url=produto["foto"])

        embed.add_field(
            name="💰 Preço atual",
            value=f"**R$ {produto['preco']}**",
            inline=True
        )

        embed.add_field(
            name="🏷️ Desconto",
            value=produto["desconto"],
            inline=True
        )

        embed.add_field(
            name="📉 Preço anterior",
            value=produto["preco_total"],
            inline=False
        )

        embed.set_footer(
            text="Monitor de promoções Amazon"
        )
        await canal.send(embed=embed)


@client.event
async def on_ready():
    print(f"Conectado como {client.user}")


def iniciar():
    client.run(DISCORD_TOKEN)
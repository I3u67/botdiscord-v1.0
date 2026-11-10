import discord
from discord.ext import commands
from discord import app_commands

class Math(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client: commands.Bot = client

#SOMA
#porque eu ja importei o app_commands
    @app_commands.command(
        name="soma", description="some dois numeros"
    )
    @app_commands.describe(
        numero1="Escolha o primeiro número",
        numero2="Escolha o segundo número"
    )
    async def soma(self, interaction:discord.Integration, numero1:int, numero2:int):
        numero_somado = numero1 + numero2
        await interaction.response.send_message(f"O resultado da soma é {numero_somado}", ephemeral=True)

#SUBSTRAÇÃO
    @app_commands.command(
        name="substração", description="subtraia dois numeros"
    )
    @app_commands.describe(
        numero1="Escolha o primeiro número",
        numero2="Escolha o primeiro número"
    )
    async def subtracao(self, interaction:discord.Interaction, numero1:int, numero2:int):
        numero_subtraido = numero1 - numero2
        await interaction.response.send_message(f"O resultado da substração é {numero_subtraido}", ephemeral=True)

#praticando...
    # DIVISÃO
    @app_commands.command(
        name="divisão",
        description="Divida dois números"
    )
    @app_commands.describe(
        numero1="Escolha o primeiro número",
        numero2="Escolha o segundo número"
    )
    async def divisao(self, interaction:discord.Interaction, numero1:int, numero2:int):
        numero_dividido = numero1 / numero2
        sobra = numero1 % numero2
        await interaction.response.send_message(f"{numero1} dividido por {numero2} é {numero_dividido} , e sobra {sobra}", ephemeral=True)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Math(client))



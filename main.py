import discord
from discord import app_commands

from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

#head
class Klient(commands.Bot):
    #(discord.Client) -> se eu quiser que os comandos funcionem tudo aqui, sem extensões e outros py com comandos organizados
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="!",
            intents=intents
        )
        #self.tree = app_commands.CommandTree(self) -> para o uso do (discord.Client) somente em main
    async def setup_hook(self):

        diretorio = "cogs"
        for root,dirs,files in os.walk(diretorio):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    caminho = os.path.join(root,file).replace("\\","/").replace("/",".")[:-3]
                    await self.load_extension(caminho)
                    print(f"cog carregado {caminho}")

        #ver uma por uma
        #await self.load_extension("cogs.commands.math")
        #await self.load_extension("cogs.logs.on_message")

        print("extensão conectada com o main.py")

        await self.tree.sync() #sincronizar comandos em um servidor só, dentro do ()

    async def on_ready(self): #sempre que o bot ligar, algo dentro dessa def será feito
        print(f"BOT {self.user} ATIVADO")

bot = Klient()

#comandos principais
@bot.tree.command(name="saudacao", description="Fale com o sonic")
async def saudacao(interaction:discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.mention}!", ephemeral=(True)) #ephemeral ativado quer dizer que somente o usuario que usou o commando pode ver o resto do comando

@bot.tree.command(name="amor", description="mensagem secreta")
async def amor(interaction:discord.Interaction):
    await interaction.response.send_message("te amo! <3", ephemeral=(True))

bot.run(DISCORD_TOKEN) #token do bot



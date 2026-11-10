import discord
from discord.ext import commands
from discord import app_commands

class OnMessage(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client: commands.Bot = client
    # no console é exibido as mesagens dos usuarios
    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        print(message.content)

async def setup(client:commands.Bot) -> None:
    await client.add_cog(OnMessage(client))
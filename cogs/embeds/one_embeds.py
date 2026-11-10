import discord
from discord.ext import commands
from discord import app_commands

class emb(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client: commands.Bot = client

@commands.command()
async def enviar_msg(ctx: commands.Context):
    embed = discord.Embed(
        title="sonic do zap",
        description="atendimento do sonic"
    )
    await ctx.send(embed=embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(emb(client))
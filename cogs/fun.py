import discord
from discord.ext import commands
 
class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def nigga(self, ctx):
    await ctx.send('nigga')

def setup(bot):
    bot.add_cog(fun(bot))
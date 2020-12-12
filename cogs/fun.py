import discord
from discord.ext import commands
import random
 
class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nigga(self, ctx):
        await ctx.send('nigga')

    @commands.command()
    async def swag(self, ctx):
        await ctx.send('(random.randint(1, 100))')

def setup(bot):
    bot.add_cog(fun(bot))
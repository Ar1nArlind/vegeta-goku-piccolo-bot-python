import discord
from discord.ext import commands
import random
 
class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nigga(self, ctx):
        await ctx.send('nigga')

    @commands.command(pass_context = True)
    async def swag(ctx):
        embed = discord.Embed(Title = "Random Number", description  = (random.randint(1, 100)), color = (OxF85252))
        embed)
        title await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(fun(bot))
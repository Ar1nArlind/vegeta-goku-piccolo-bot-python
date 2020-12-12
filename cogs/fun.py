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
    async def swag(self, ctx):
        text = str(random.randint(1, 100)) 
        text += '%'
        embed = discord.Embed(title = "Swag Meter", description  = (text), color = (0xa11cff))
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(fun(bot))
import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def swag(self, ctx):
        text = str(random.randint(0, 100)) 
        text += '%'
        embed = discord.Embed(title = "Swag Meter", description  = (text), color = (0xa11cff))
        await ctx.send(embed = embed)

    @commands.command()
    async def avatar(self, ctx, user: discord.Member):
        mbed = discord.Embed(
            color=discord.Color(0xa11cff),
            title=f"{user}"
        )
        mbed.set_image(url=f"{user.avatar_url}")
        await ctx.send(embed=mbed)

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            mbed = discord.Embed(
                color=discord.Color(0xa11cff),
                title=f"{ctx.author}"
            )
            mbed.set_image(url=f"{ctx.author.avatar_url}")
            await ctx.send(embed=mbed)

def setup(bot):
    bot.add_cog(Fun(bot))

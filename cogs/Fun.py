import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '$')

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.Cog.listener()
async def on_ready(self):
    print(f'Logged in as: {bot.user.name}')
    print(f"User ID: {bot.user.id}")
    print('-----')

@commands.command()
async def ping(self, ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(Fun(bot))
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f"User ID: {bot.user.id}")
    print('-----')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

bot.run(os.environ['DISCORD_TOKEN'])

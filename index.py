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

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog Loaded')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog Unloaded')    

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ['DISCORD_TOKEN'])
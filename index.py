import os
import discord
import json
import asyncio
import random
import datetime
from discord.ext import commands
from discord.ext.commands import CommandNotFound

def get_prefix(bot,message):
    with open('src/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f"User ID: {bot.user.id}")
    print('-----')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        pass

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

@bot.event
async def on_guild_join(guild):
    with open('src/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '$'

    with open('src/prefixes.json', 'w') as f:
        json.dump(prefixes,f,indent=4)

@bot.command()
@commands.has_permissions(administrator = True)
async def prefix(ctx, prefix):
    with open('src/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('src/prefixes.json', 'w') as f:
        json.dump(prefixes,f,indent=4)

    await ctx.send(f'The prefix was changed to {prefix}')

bot.run('TOKEN')

import os
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = '$')
client = discord.Client()

@client.event
@asyncio.coroutine
 def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f"User ID: {client.user.id}")
    print('-----')

@client.command()
    @asyncio.coroutine
    def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
    @asyncio.coroutine
    def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filemame in os.listdir(./cogs):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('os.environ['DISCORD_TOKEN']')

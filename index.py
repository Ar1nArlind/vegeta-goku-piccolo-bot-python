import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f"User ID: {client.user.id}")
    print('-----')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

    @client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filemame in os.listdir(./cogs):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('os.environ['DISCORD_TOKEN']')
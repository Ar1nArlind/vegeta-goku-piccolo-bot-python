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
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

client.run(os.environ['DISCORD_TOKEN'])

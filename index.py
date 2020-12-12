import os
import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f"User ID: {client.user.id}")
    print('-----')

client.run(os.environ['DISCORD_TOKEN'])

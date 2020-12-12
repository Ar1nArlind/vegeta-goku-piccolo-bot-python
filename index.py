import os

import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f"User ID: {client.user.id}")
    print('-----')

client.run('Njc2ODUyMDg1OTY2NTAzOTY4.XkLtoA.pvmrvJ0GE9NIo6DPimX8JezNkJk')
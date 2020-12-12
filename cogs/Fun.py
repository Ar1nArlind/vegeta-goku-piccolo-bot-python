import os
import discord
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
    #events 
@client.Cog.listener()
async def on_ready(self):
    print(f'Logged in as: {client.user.name}')
    print(f"User ID: {client.user.id}")
    print('-----')

    #commands
@commands.command()
 async def ping(self, ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Fun(client))
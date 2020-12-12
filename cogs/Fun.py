import discord
from discord.ext import commands
import os
import asyncio 

client = discord.Client()

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

@commands.command()
@asyncio.coroutine
    def ping(self, ctx):
        yield ctx.send(f'pong!\n{round(client.latency * 1000)}ms') 
        return

def setup(client):
    client.add_cog(Fun(client))

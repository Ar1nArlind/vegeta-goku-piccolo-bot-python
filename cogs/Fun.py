import discord
from discord.ext import commands
import os

client = discord.Client()

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self, ctx): # This was inside '__init__' before
        await ctx.send(f'pong!\n{round(client.latency * 1000)}ms') 
        return

def setup(client):
    client.add_cog(Fun(client))

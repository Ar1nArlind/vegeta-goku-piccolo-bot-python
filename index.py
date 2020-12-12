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

@bot.command
async def load(ctx, extension):
    try:
        bot.load_extension(f'''cogs.{extension}''')
        await ctx.channel.send(f'''Successfully loaded {extension}''')
    except Exception as e:
        print(f'''Error! We could not load the extension {extension} because {e}''')

@bot.command
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'''cogs.{extension}''')
        await ctx.channel.send(f'''Successfully loaded {extension}''')
    except Exception as e:
        print(f'''Error! We could not load the extension {extension} because {e}''')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ['DISCORD_TOKEN'])

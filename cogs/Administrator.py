import discord
from discord.ext import commands
 
class Administrator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User):
        guild = ctx.guild
        mbed = discord.Embed(
            title = 'Success',
            descrition = f"{user} has been banned."
        )
        await ctx.send(embed=mbed)
        await guild.ban(user=user)
         
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.User):
        guild = ctx.guild
        mbed = discord.Embed(
            title = 'Success',
            descrition = f'{user} has been kicked.'
        )
        await ctx.send(embed=mbed)
        await guild.kick(user=user)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"ok")
        
        

def setup(bot):
    bot.add_cog(Administrator(bot))
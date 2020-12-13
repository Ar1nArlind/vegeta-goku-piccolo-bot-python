import discord
from discord.ext import commands
 
class Administrator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, user: discord.User):
        guild = ctx.guild
        embed = discord.Embed(
                title = 'Success',
                descrition = f"{user} has been banned."
        )
        if ctx.author.guild_permission.ban_members:
            await ctx.send(embed=embed)
            await guild.ban(user=user)
         

    @commands.command()
    async def kick(self, ctx, user: discord.User):
        guild = ctx.guild
        embed = discord.Embed(
                title = 'Success',
                descrition = f"{user} has been kicked."
        )
        if ctx.author.guild_permission.kick_members:
            await ctx.send(embed=embed)
            await guild.kick(user=user)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"ok")
        
        

def setup(bot):
    bot.add_cog(Administrator(bot))
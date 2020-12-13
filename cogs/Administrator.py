import discord
from discord.ext import commands
 
class Administrator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command() 
    @commands.has_permissions(ban_members=True) 
    async def ban(self, ctx, user: discord.Member, *, reason):
        await ctx.guild.ban(user, reason=reason) 
        await user.send(f"You have been banned in {ctx.guild} for {reason}")
        await ctx.send(f"{user} has been successfully banned.") 

def setup(bot):
    bot.add_cog(Administrator(bot))
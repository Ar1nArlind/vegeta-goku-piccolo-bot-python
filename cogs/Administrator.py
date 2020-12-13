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

    @commands.command() 
    @commands.has_permissions(kick_members=True) 
    async def kick(self, ctx, user: discord.Member, *, reason):
        await ctx.guild.kick(user, reason=reason) 
        await user.send(f"You have been kicked in {ctx.guild} for {reason}")
        await ctx.send(f"{user} has been successfully kicked.") 

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"ok")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(id)
                await ctx.send(f'Unbanned {user.mention}')
                return

def setup(bot):
    bot.add_cog(Administrator(bot))
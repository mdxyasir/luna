import discord, json, ctypes, asyncio, colorama, os

from discord.ext import commands
from colorama import Fore, Back, Style

with open("config.json","r") as f:
    config = json.load(f)

prefix = config.get("prefix")

class Moderation(commands.Cog, name="Mod Commands", description="Commands to moderate your server"):

    def __init__(self, Luna):
        self.Luna = Luna

    @commands.command(brief="Kick a member", description="Kick a member")
    async def kick(self, ctx, member:discord.Member):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=f"Kicked by {ctx.author}")
            embed=discord.Embed(description=f'**{member}** has been kicked')
            embed.set_footer(text="github.com/mdxyasir/Luna-DiscordBot")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Permission Denied.", description=f"You don't have permission to use this command.")
            await ctx.send(embed=embed)
        
    @commands.command(brief="Ban a member", description="Ban a member")
    async def ban(self, ctx, member:discord.Member):
        if ctx.author.guild_permissions.ban_members:
            await member.ban(reason=f"Banned by {ctx.author}")
            embed=discord.Embed(description=f'**{member}** has been banned')
            embed.set_footer(text="github.com/mdxyasir/Luna-DiscordBot")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Permission Denied.", description=f"You don't have permission to use this command.")
            await ctx.send(embed=embed)

    @commands.command(brief="Unban a user", description="Unban a user")
    async def unban(self, ctx, member:discord.User):
        if ctx.author.guild_permissions.ban_members:
            await ctx.guild.unban(member)
            await ctx.send(f"**{member}** has been unbanned")
        else:
            embed=discord.Embed(title="Permission Denied.", description=f"You don't have permission to use this command.")
            await ctx.send(embed=embed)


def setup(Luna):
    Luna.add_cog(Moderation(Luna))
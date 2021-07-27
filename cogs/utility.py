import discord, json, ctypes, asyncio, colorama, os

from discord.ext import commands
from colorama import Fore, Back, Style

with open("config.json","r") as f:
    config = json.load(f)

prefix = config.get("prefix")

class Utility(commands.Cog, name="Utility Commands", description="Commands to help staff members"):

    def __init__(self, Luna):
        self.Luna = Luna

    @commands.command(description="Get the bot's latency", brief="Bot's latency")
    async def ping(self, ctx):
        embed = discord.Embed(description=f"{self.Luna.user.name}'s latency: `{round(self.Luna.latency*1000)}`ms")
        embed.set_footer(text="github.com/mdxyasir/Luna-DiscordBot")
        await ctx.send(embed=embed)

    @commands.command(description="Purge messages in a channel", brief="Purge messages")
    async def purge(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        msg = await ctx.send(f"Purged {amount} messages")
        await asyncio.sleep(3)
        await msg.delete()

    @commands.command(description="Get info on a user", brief="Info on any user")
    async def userinfo(self, ctx, user:discord.Member = None):
        if user == None:
            user = ctx.author

            embed = discord.Embed()
            embed.set_image(url=user.avatar_url)
            embed.add_field(name="Username:", value=user, inline=False)
            embed.add_field(name="User ID:", value=user.id, inline=False)
            embed.add_field(name="Avatar URL:", value=f"[Click Here]({user.avatar_url})")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed()
            embed.set_image(url=user.avatar_url)
            embed.add_field(name="Username:", value=user, inline=False)
            embed.add_field(name="User ID:", value=user.id, inline=False)
            embed.add_field(name="Avatar URL:", value=f"[Click Here]({user.avatar_url})")
            await ctx.send(embed=embed)  

    

def setup(Luna):
    Luna.add_cog(Utility(Luna))
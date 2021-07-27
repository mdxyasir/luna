import discord, json, ctypes, asyncio, colorama, os

from discord.ext import commands
from colorama import Fore, Back, Style

with open("config.json","r") as f:
    config = json.load(f)

prefix = config.get("prefix")
token = config.get("token")
status = config.get("status")

class Events(commands.Cog):

    def __init__(self, Luna):
        self.Luna = Luna

    @commands.Cog.listener()
    async def on_ready(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f'Luna | Logged in as {self.Luna.user}')
        os.system("cls")
        intro = f"""{Fore.RESET}                 

                            █░░ █░█ █▄░█ ▄▀█   █▀▄ █ █▀ █▀▀ █▀█ █▀█ █▀▄
                            █▄▄ █▄█ █░▀█ █▀█   █▄▀ █ ▄█ █▄▄ █▄█ █▀▄ █▄▀

                            {Fore.CYAN}User | {Fore.GREEN}{self.Luna.user}
                            {Fore.CYAN}ID | {Fore.GREEN}{self.Luna.user.id}
                            {Fore.CYAN}Prefix | {Fore.GREEN}{prefix}
                            {Fore.CYAN}Token | {Fore.GREEN}{token}
                            {Fore.CYAN}Code | {Fore.GREEN}github.com/mdxyasir/luna
                {Fore.RESET}
                """
        print(intro)
        await self.Luna.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/mdxyasir"))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.add_reaction("⏳")
        else:
            raise error

def setup(Luna):
    Luna.add_cog(Events(Luna))

import discord, json, ctypes, asyncio, colorama, os

from discord.ext import commands
from discord.ext.commands import Bot
from pretty_help import PrettyHelp
from colorama import Fore, Back, Style
from colorama import init

init()
ctypes.windll.kernel32.SetConsoleTitleW(f'Luna | Loading...')

with open("config.json","r") as f:
    config = json.load(f)

token = config.get("token")
prefix = config.get("prefix")

Luna = commands.Bot(command_prefix=prefix, case_insensitive=True, help_command=PrettyHelp())

def Clear():
    os.system('cls')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        Luna.load_extension(f'cogs.{filename[:-3]}')

if token == "your-token-here":
    Clear()
    print(f"{Fore.RED}Error: {Fore.YELLOW}You need to open config.json and add your bot's token" + Fore.RESET)
    os.system("pause >NUL")
else:
    try:
        Luna.run(token)
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}Error: {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')
import discord, json, ctypes, asyncio, colorama, os, random, aiohttp

from discord.ext import commands
from colorama import Fore, Back, Style

with open("config.json","r") as f:
    config = json.load(f)

prefix = config.get("prefix")

class Fun(commands.Cog, name="Fun Commands", description="Commands to keep users entertained"):

    def __init__(self, Luna):
        self.Luna = Luna

    @commands.command(aliases=["coin","cf"], description="Flip a coin", brief="Flip a coin")
    async def coinflip(self, ctx):
        coin = ["Heads", "Tails"]
        embed=discord.Embed(description=f"{random.choice(coin)}")
        await ctx.send(embed=embed)

    @commands.command(aliases = ["8ball"], description="Ask the 8ball a question", brief="Ask the 8ball a question")
    async def ball(self, ctx):
        phrases = [
            "As I see it, yes.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Don't count on it.",
            "It is certain.",
            "Very doubtful.",
            "My reply is no.",
            "Without a doubt.",
            "You may rely on it.",
            "No.",
            "Yes.",
            "Signs point to yes.",
            "Get a life, I'm busy right now."]
            
        embed=discord.Embed(description=f"🎱 {random.choice(phrases)}")
        await ctx.send(embed=embed)

    @commands.command(description="Create a fake tweet", brief="Create a fake tweet")
    async def tweet(self, ctx, *, message: str):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={ctx.author.name}&text={message}") as r:
                res = await r.json()
                em = discord.Embed()
                em.set_image(url=res["message"])
                await ctx.send(embed=em)

    @commands.command(aliases=["say"], description="Make the bot say anything", brief="Make the bot say anything")
    async def repeat(self, ctx, *, message):
        await ctx.send(f"{message} - **{ctx.author}**")

    @commands.command(aliases=["spoil"], description="Send a message as a spoiler", brief="Send a message as a spoiler")
    async def spoiler(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(f"||{message}|| \n\n - {ctx.author}")

    @commands.command(aliases=["message"], description="Send messages to other users", brief="Send messages to other users")
    async def send(self, ctx, user:discord.Member=None, *,message=None):
        if user == None:
            await ctx.send(f"Format: `ar send <@user> <message>`")
        elif message == None:
            await ctx.send(f"Format: `ar send <@user> <message>`")
        await user.send(f"{message}\n\n- **{ctx.author}** from **{ctx.guild}**")
        
        await ctx.send("Message Sent!")

    @commands.command(aliases=['meow', 'catimage', 'meowimage'], description="Get a random cat image", brief="Random cat image")
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://aws.random.cat/meow') as r:
                data = await r.json()
                embed = discord.Embed(title='Here\'s a cat')
                embed.set_image(url=data['file'])
                await ctx.send(embed=embed)

    @commands.command(aliases=['woof', 'bark', 'dogimage', 'woofimage', 'barkimage'], description="Get a random dog image", brief="Random dog iamge")
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://random.dog/woof.json') as r:
                data = await r.json()
                embed = discord.Embed(title='Here\'s a dog')
                embed.set_image(url=data['url'])
                await ctx.send(embed=embed)
    
    @commands.command(aliases = ['badjoke', 'popjoke'], description="Get a random dad joke", brief="Random dad joke")
    async def dadjoke(self, ctx):

        url = "https://dad-jokes.p.rapidapi.com/random/jokes"

        headers = {
            'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
            'x-rapidapi-key': "acc48b4a54msh434788231f8058ap1e19e3jsnc36d72d7bb79"
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r = await response.json()
                r = r["body"][0]
                embed = discord.Embed(title = 'Dad Joke', description = f"**{r['setup']}**\n\n||{r['punchline']}||")
                await ctx.send(embed=embed)

    @commands.command(aliases=['dumbfacts', 'uselessknowledge'], description="Get a random useless fact", brief="Random useless fact")
    async def uselessfact(self, ctx):
        URL = 'https://uselessfacts.jsph.pl/random.json?language=en'
        async with aiohttp.request("GET", URL, headers = {}) as response:
            if response.status  == 200:
                data = await response.json()
                embed = discord.Embed(title = 'Useless Fact', description = data["text"])
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description = f'API returned a {response.status} status')
                await ctx.send(embed=embed)


def setup(Luna):
    Luna.add_cog(Fun(Luna))
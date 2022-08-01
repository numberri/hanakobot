from random import choice
from random import randint
import asyncio

import discord
from discord.ext import commands
from discord.ext.commands import bot

from __main__ import HanakoBot

class Utility(commands.Cog):
    def __init__(self, bot: HanakoBot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(
            title=member.name + "'s Avatar", 
            url= member.avatar_url,
            colour = discord.Colour.from_rgb(55, 34, 77)
            )
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def choose(self, ctx, *args):
        """
        Give HanakoBot a list of options divided by "|", and it will return an option for you!
        """
        user = ctx.author.mention
        choices = ' '.join(args)
        if choices == "":
            await ctx.send('To use this command, send a list of options seperated with `|`')
        else:
            choicelist = choices.split("|")
            if len(choicelist) == 1:
                await ctx.send(f"*{user}, I'll need more than one option to choose from...*")
            else:
                chosen = choice(choicelist).strip()
                await ctx.send(f"{user}, my choice is **{chosen}**!")
    
    @commands.command()
    async def diceroll(self, ctx, sides = None):
        """
        Roll a die with a given amount of sides.
        """
        if sides == None:
            dsides = 6
        else:
            try:
                dsides = int(sides)
            except:
                await ctx.send("I'll need to know the number of sides for your diceroll...")
        result = randint(1, dsides)
        await ctx.send(f"**You rolled a die with {sides} sides and got a {str(result)}!**")

    @commands.command()
    async def coinflip(self, ctx, coins = None):
        """
        Flip a given amount of coins.
        """
        if coins == None:
            c = 1
        else:
            try:
                c = int(coins)
            except:
                await ctx.send("I'll need to know the number of coins for your coinflip...")
        heads = 0
        tails = 0
        for coin in range(c):
            n = randint(0, 1)
            if n == 0:
                heads += 1
            elif n == 1:
                tails += 1
        await ctx.send(f"**You flipped {coins} coins!**\nHeads: **{heads}**\nTails: **{tails}**")

    @commands.command()
    async def remind(self, ctx, time, unit, *args):
        """
Hanako gives you a reminder in a given amount of time.
        """
        user = ctx.author.mention
        req = ""
        for item in args:
            req = req + item + " "
        req = req.strip()
        try:
            x = int(time)
        except:
            await ctx.send("Please enter a time for me to remind you in! Make sure to enter a number for time as well as a unit.")
        unit = unit.lower()
        if unit == "s" or unit == "second" or unit == "seconds" or unit == "sec" or unit == "secs":
            secs = x
        elif unit == "m" or unit == "minutes" or unit == "minute" or unit == "min" or unit == "mins":
            secs = x * 60
        elif unit == "h" or unit == "hour" or unit == "hours":
            secs = x * 3600
        elif unit == "d" or unit == "day" or unit == "days":
            secs = x * 86400
        else:
            raise NotImplementedError
        await ctx.send(f"**Reminding you to {req} in {time} {unit}!**")
        await asyncio.sleep(secs)
        await ctx.send(f"**{user} {req} ({time} {unit} ago)**")    

    @remind.error
    async def remind_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandInvokeError):
            await ctx.send("Please enter a time for me to remind you in! Make sure to enter a number for time as well as a unit.")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")
        
def setup(bot: HanakoBot):
    cog = Utility(bot)
    bot.add_cog(cog)
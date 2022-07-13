from random import choice
from random import randint

from discord.ext import commands
from discord.ext.commands import bot

from __main__ import HanakoBot

class Utility(commands.Cog):
    def __init__(self, bot: HanakoBot):
        self.bot = bot

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
        
def setup(bot: HanakoBot):
    cog = Utility(bot)
    bot.add_cog(cog)
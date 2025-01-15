import discord
import numpy
from discord import option
from discord.ext import commands
from random import choice
from random import randint

class Utility(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    @option(
        "member",
        discord.Member,
        description="Who's avatar do you want to see?"
    )
    async def avatar(self, ctx, member: discord.Member):
        """
        Sends an image of someone's server avatar - or their regular avatar if they don't have one set.
        """
        embed = discord.Embed(
            title=member.name + "'s Avatar", 
            url= member.display_avatar,
            colour = discord.Colour.dark_red()
            )
        embed.set_image(url=member.display_avatar)
        await ctx.respond(embed=embed)

    @discord.slash_command()
    @option(
        "choices",
        str,
        description="Seperate choices by |, or use commas or spaces."
    )
    async def choose(self, ctx, choices):
        """
        Choose from a list of options seperated by |, commas, or spaces.
        """
        user = ctx.author.mention
        if "|" in choices:
            choicelist = choices.split("|")
        elif "," in choices:
            choicelist = choices.split(",")
        else:
            choicelist = choices.split(" ")

        if len(choicelist) == 1:
            await ctx.respond("*I'll need more than one option to choose from...*")
        else:
            chosen = choice(choicelist).strip()
            await ctx.respond(f"{user}, my choice is **{chosen}**!")
        
    @discord.slash_command()
    @option(
        "sides",
        str,
        description="The number of sides your dice have. Defaults to 6."
    )
    @option(
        "dice",
        str,
        description="The number of dice you're rolling. Defaults to 1."
    )
    async def dice(self, ctx, sides: str = "6", dice: str = "1"):
        """
        Roll the dice and test your luck...
        """
        user = ctx.author.mention
        if not sides.isdigit() or not dice.isdigit() or int(sides) < 2 or int(dice) == 0:
            await ctx.respond(f"<:hk_mocking:964913418165424218> **Roll {dice} dice with {sides} sides...? Now that's just silly!**")
        elif int(dice) > 100:
            await ctx.respond("<:hk_shocked:964913449350070272> **Do you *expect* me to have that many dice laying around?**")
        else:
            total = 0
            sides = int(sides)
            dice = int(dice)
            roll_list = []
            if dice == 1:
                await ctx.respond(f"**{user} rolls a D{sides} and it lands on a {randint(1, sides)}.**")
            else:
                for i in range(dice):
                    roll = randint(1, sides)
                    total += roll
                    roll_list.append(roll)
                roll_list.sort()
                rolls = ', '.join(map(str, roll_list))
                await ctx.respond(f"**{user} rolls {dice} dice with {sides} sides. They land on:**\n`{rolls}`\n**Adding up the sides results in a total of {total}.**")

    @discord.slash_command()
    @option(
        "coins",
        str,
        description="The number of coins to flip. Defaults to 1."
    )
    async def coinflip(self, ctx, coins: str = "1"):
        """
        Flip a coin! Or two. Or twenty.
        """
        # note that this command used to manually flip all the coins asked for
        # this was fine until the bot got asked to flip 10 billion coins
        # RIP hanakobot you will be missed
        if not coins.isdigit() or coins == "0":
            await ctx.respond("<:hk_face:964931042584702996> **Coin, please.**")
        else:
            coins = int(coins)
            if coins == 1:
                flip = randint(0, 1)
                if flip == 1:
                    result = "heads"
                else:
                    result = "tails"
                await ctx.respond(f"**You flipped a coin! It landed on {result}.**")
            else:
                # remember to import numpy
                rng = numpy.random.default_rng()
                heads = round(rng.normal(coins/2, (coins ** 0.5)/2))
                tails = coins - heads
                await ctx.respond(f"**You flipped {coins} coins!**\nHeads: **{heads}**\nTails: **{tails}**")

def setup(bot):
    cog = Utility(bot)
    bot.add_cog(cog)
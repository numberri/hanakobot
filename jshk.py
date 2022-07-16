import discord
import datetime
import pytz
#from random import choice ... since it's not used in this, do I need it?

from discord.ext import commands

from __main__ import HanakoBot
#vsc I sure hope you know what you're doing

class JSHK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chapter(self, ctx):
        """
        Tells the time until the next TBHK chapter release. (For reference, this \
is on the 18th of every month at midnight in Japan.)
        """
        japan = pytz.timezone('Japan')
        jp_time = datetime.datetime.now(japan)
        # await ctx.send(f'{jshk_release()}')
        x = jp_time.strftime('%Y %m %d %H %M %S').split()
        days = 17 - int(x[2])
        if days < 0:
            if int(x[1]) == 2:
                if int(x[0])%400 == 0:
                    days = days + 28
                elif int(x[0])%100 == 0:
                    days = days + 27
                elif int(x[0])%4 == 0:
                    days = days + 28
                else:
                    days = days + 27
            elif int(x[1]) == 4 or int(x[1]) == 6 or int(x[1]) == 9\
                or int(x[1]) == 11:
                #re-format line above
                days = days + 29
            else:
                days = days + 30
        hours = 23 - int(x[3])
        minutes = 60 - int(x[4])
        if days == 0 and hours == 0 and minutes == 0:
            await ctx.send("The newest Toilet Bound Hanako Kun chapter has \
just been released! <:hk_yay:964912514179674203>")
        elif days == 0 and hours == 0:
            await ctx.send(f"There are {minutes} minutes until the next \
Toilet Bound Hanako Kun chapter.")
        elif days == 0:
            await ctx.send(f"There are {hours} hours and {minutes} minutes \
until the next Toilet Bound Hanako Kun chapter.")
        else:
            await ctx.send(f"There are {days} days, {hours} hours, and \
{minutes} minutes until the next Toilet Bound Hanako Kun chapter.")

def setup(bot: HanakoBot):
    cog = JSHK(bot)
    bot.add_cog(cog)

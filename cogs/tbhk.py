import discord
from discord import option
from discord.ext import commands
import datetime
import pytz

def datetime_list(date):
    strings = date.strftime('%Y %m %d %H %M %S').split()
    dt = []
    for s in strings:
        dt.append(int(s))
    return dt

def release_date(year: int, month: int):
    normal_release = datetime.datetime(year, month, 18, 0, 0, 0)
    if normal_release.weekday() == 6:
        return datetime.datetime(year, month, 17, 0, 0, 0)
    elif month in [7, 9]:
        if normal_release.weekday() == 0:
            return datetime.datetime(year, month, 15, 0, 0, 0)
    else:
        return normal_release

def odd_release(year: int, month: int):
    """
    Takes in a given year and month.
    Returns 1 if the normal release is on a Saturday.
    Returns 2 if the normal release is on a Sunday.
    Returns 2 if the normal release is on a Monday public holiday.
    Returns 0 otherwise.
    Can be used as a bool or to give different cases for weekends and public holidays.
    """
    normal_release = datetime.datetime(year, month, 18, 0, 0, 0)
    if normal_release.weekday() == 5: #Saturday release
        return 1
    elif normal_release.weekday() == 6: #Sunday release
        return 2
    elif month in [7, 9]:
        if normal_release.weekday() == 0: # Public holiday release
            return 3
    return 0

def next_manga_release():
    japan = pytz.timezone('Japan')
    jp_time = datetime.datetime.now(japan)
    now = datetime_list(jp_time)
    if release_date(now[0], now[1]) > jp_time.replace(tzinfo=None):
        return japan.localize(release_date(now[0], now[1]))
    #safe to assume if == they'd want the next chapter date
    if now[1] == 12:
        return japan.localize(release_date(now[0]+1, 1))
    return japan.localize(release_date(now[0], now[1]+1))

def next_anime_release():
    japan = pytz.timezone('Japan')
    jp_time = datetime.datetime.now(japan)
    now = datetime_list(jp_time)
    weekday = jp_time.weekday()
    if weekday == 6: #it's a sunday, is it before 4:30?
        if datetime.datetime(now[0], now[1], now[2], 16, 30, 0) > jp_time:
            days_till_sunday = 0
        else:
            days_till_sunday = 7
    else:
        days_till_sunday = 6 - weekday
    return japan.localize(datetime.datetime(now[0], now[1], now[2], 16, 30, 0)) + datetime.timedelta(days=days_till_sunday)

def release_countdown(release):
    diff = release - datetime.datetime.now(pytz.timezone('Japan'))
    days = diff.days
    hours, seconds = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return [days, hours, minutes, seconds]

class Tbhk(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def chapter(self, ctx):
        """
        Tells the time until the next TBHK chapter release.
        """
        next_release = next_manga_release()
        countdown = release_countdown(next_manga_release())
        japan = pytz.timezone('Japan')
        jp_time = datetime.datetime.now(japan)
        now = datetime_list(jp_time)
        if countdown[0] == 0: #less than 24 hours
            if countdown[1] == 0: #less than 1 hour
                if countdown[2] == 0: #less than a minute
                    if countdown[3] == 0: #they've managed to get it in the milliseconds
                        response = "The newest Toilet Bound Hanako Kun chapter has just been released! <:hk_yay:964912514179674203>"
                    else: #at least 1 second left
                        response = f"There are {countdown[3]} seconds until the next Toilet Bound Hanako Kun chapter! <:hk_happy:964911972275593256> Get hyped!"
                else: #at least a minute left
                    response = f"There are {countdown[2]} minutes and {countdown[3]} until the next Toilet Bound Hanako Kun chapter!"
            else: # at least an hour left
                response = f"There are {countdown[1]} hours, and {countdown[2]} minutes, and {countdown[3]} seconds until the next Toilet Bound Hanako Kun chapter."
        else: #over a day
            response = f"There are {countdown[0]} days, {countdown[1]} hours, and {countdown[2]} minutes until the next Toilet Bound Hanako Kun chapter."
        next_month = datetime_list(next_manga_release())
        odd_check = odd_release(next_month[0], next_month[1])
        if odd_check:
            if odd_check == 1:
                response += "\n-# Note that the regular release date is on a Saturday, and may be a day earlier than HanakoBot says."
            elif odd_check == 2:
                response += "\n-# Note that the regular release date is on a Sunday, and is probably on the 17th - but may be a day earlier (or later) than HanakoBot says."
            else:
                response += "\n-# Note that the regular release date is on a Japanese public holiday, and the release is most likely on the 15th this month."
        await ctx.respond(response)

    @discord.slash_command()
    async def anime(self, ctx):
        """
        Tells the time until the next TBHK episode airs in Japan.
        """
        # MAKE SURE TO UPDATE THIS WHEN WE KNOW THE END DATE
        countdown = release_countdown(next_anime_release())
        japan = pytz.timezone('Japan')
        jp_time = datetime.datetime.now(japan)
        now = datetime_list(jp_time)
        if countdown[0] == 0: #less than 24 hours
            if countdown[1] == 0: #less than 1 hour
                if countdown[2] == 0: #less than a minute
                    if countdown[3] == 0: #they've managed to get it in the milliseconds
                        response = "The newest Toilet Bound Hanako Kun episode is airing now in Japan! <:hk_yay:964912514179674203>"
                    else: #at least 1 second left
                        response = f"There are {countdown[3]} seconds until the next TBHK episode airs in Japan! <:hk_happy:964911972275593256> Get hyped!"
                else: #at least a minute left
                    response = f"There are {countdown[2]} minutes and {countdown[3]} until the next TBHK episode airs in Japan!"
            else: # at least an hour left
                response = f"There are {countdown[1]} hours, and {countdown[2]} minutes, and {countdown[3]} seconds until the next TBHK episode airs in Japan."
        else: #over a day
            response = f"There are {countdown[0]} days, {countdown[1]} hours, and {countdown[2]} minutes until the next TBHK episode airs in Japan."
        await ctx.respond(response)

def setup(bot):
    cog = Tbhk(bot)
    bot.add_cog(cog)
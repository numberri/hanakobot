import discord
import time
import datetime
import pytz
from random import choice

from discord.ext import commands
from discord.ext.commands import bot
import discord.ext.commands.errors

class HanakoBot(commands.Bot):
    #I have no idea what I am writing.
    async def on_ready(self):
        await bot.change_presence(activity=discord.Game(name="+help | hanako-bot.carrd.co"))
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

def __init__(self, bot: HanakoBot):
    self.bot = bot

intents = discord.Intents.default()
allowed_mentions = discord.AllowedMentions(everyone=True, users=True, roles=False)
allowed_mentions.replied_user = True
#discord.AllowedMentions(everyone=False, users=True, roles=False)
#discord.AllowedMentions.none()
description = 'Seventh of the school\'s seven mysteries. "Hanako-san of the toilet."'
bot = HanakoBot(command_prefix = "+", intents=intents, allowed_mentions=discord.AllowedMentions(everyone=True, users=True, roles=False))

def japantime():
    japan = pytz.timezone('Japan')
    jp_time = datetime.datetime.now(japan)
    return jp_time.strftime('%Y %m %d %H %M %S').split()

def jshk_release():
    tuplex = japantime()
    days = 17 - int(tuplex[2])
    if days < 0:
        if int(tuplex[1]) == 2:
            if int(tuplex[0])%400 == 0:
                days = days + 28
            elif int(tuplex[0])%100 == 0:
                days = days + 27
            elif int(tuplex[0])%4 == 0:
                days = days + 28
            else:
                days = days + 27
        elif int(tuplex[1]) == 4 or int(tuplex[1]) == 6 or int(tuplex[1]) == 9 or int(tuplex[1]) == 11:
            #re-format line above
            days = days + 29
        else:
            days = days + 30
    hours = 23 - int(tuplex[3])
    minutes = 60 - int(tuplex[4])
    if days == 0 and hours == 0 and minutes == 0:
        return "The newest Toilet Bound Hanako Kun chapter has just been released! <:hk_yay:964912514179674203>"
    elif days == 0 and hours == 0:
        return f"There are {minutes} minutes until the next Toilet Bound Hanako Kun chapter."
    elif days == 0:
        return f"There are {hours} hours and {minutes} minutes until the next Toilet Bound Hanako Kun chapter."
    else:
        return f"There are {days} days, {hours} hours, and {minutes} minutes until the next Toilet Bound Hanako Kun chapter."
    #make that return look pretty PLEASE. it works but damn its ugly

#/home/averyarmstrong/hanakobot/bot_main.py

@bot.command()
async def chapter(ctx):
    """
    Tells the time until the next TBHK chapter release. (For reference, this is on the 18th of every month at midnight in Japan.)
    """
    await ctx.send(f'{jshk_release()}')

@bot.command()
async def todo(ctx):
    await ctx.send("""**TO DO**
- make other interaction commands (e.g. +kill)
- add lines to +kiss and +hug
- rework the +help command
- rewatch tbhk and make hug GIFs
- split bot commands into cogs""")

@bot.command()
async def test(ctx):
    image = [
        r"/home/averyarmstrong/hanakobot/physical_labor.jpg",
        r"/home/averyarmstrong/hanakobot/peaceout.jpg"
        ]
    chosen_image = choice(image)
    await ctx.send("Huh? What? I'm awake, hello!", file=discord.File(chosen_image))

@test.error
async def test_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandError):
        await ctx.send("Snzz... Let me go back to sleep. (" + str(error) + ")")

@bot.command()
async def choose(ctx, *args):
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

@bot.command()
async def kiss(ctx, member: discord.Member=None):
    """
    Mention a user to give them a kiss!
    """
    user = ctx.author.mention
    if member == None:
        await ctx.send("**You must mention a user to use this command! Or perhaps you want me to kiss you instead...?**")
    elif member.id == 955611964560777236:
        kiss_choice = [
            "<:hk_blush:964948035371163688>",
            "<:hk_kiss:964947590259032109> **Huh? You want me to kiss you?**"
            ]
        kiss = choice(kiss_choice)
        await ctx.send(f'{kiss}')
    elif member.id == ctx.author.id:
        kiss_choice = [
            f"**{user} leans forward to lovingly kiss... their reflection in the mirror in front of them.**",
            f"**{user} has decided that self love is important! They give themselves a kiss.**",
            f"**{user} kisses one of the many pictures of themselves on their wall. Why do you have all of those, anyways...?**",
            f"**{user} wants to kiss themself? I could kiss you instead... <:hk_kiss:964947590259032109>**"
            ]
        kiss = choice(kiss_choice)
        await ctx.send(f'{kiss}')
    else:
        receiver = f"<@{member.id}>"
        kiss_choice = [
            f"**{user} places a spell of protection on {receiver} by kissing their cheek.**",
            f"**{user} gently kisses {receiver} on the forehead.**",
            f"**{user} tries to wake up {receiver} with a good-morning kiss, but accidentally startles them and gets headbutted.**",
            f'**"There are many different kinds of threats, Honorable Number 7!" {user} leans in to kiss {receiver} in order to threaten Hanako into helping them. (That was unfair! <:hk_dissapoint:964931557456482404>)**',
            f"**{receiver} has finally gotten the kiss from {user} they've been dreaming of... or at least they think, until they wake up.**",
            f"**{user} and {receiver} share a sweet, sappy reunion kiss. Aww... <:yn_love:964940266844856340>**",
            f"**Month ⬤, day X... the weather is bright and sunny! Today's big event... {receiver} shares their first kiss with {user}!**",
            f"**{user} is about to share a kiss with {receiver}, when... <:teru_small:973999293398663279> \"Uhh... Did I... interrupt something?\"**",
            ]
        kiss = choice(kiss_choice)
        await ctx.send(f'{kiss}')
#(That's not working. kind of sucks but oh well)
#UPDATE ITS WORKING!!! FUCK YES!!

@kiss.error
async def kiss_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MemberNotFound):
        await ctx.send("Uhh... sorry, who are you talking about?")
    elif isinstance(error, discord.ext.commands.CommandError):
        await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) + ")")

@bot.command()
async def comfort(ctx, member: discord.Member=None):
    """
    Send a TBHK character to cheer somebody up! Mention the user in the command, or mention nobody to have the bot comfort you instead.
    """
    user = ctx.author.mention
    #if member == "@everyone":
    #    await ctx.send("**<:hk_yay:964912514179674203> Hanako calls a meeting with all the school mysteries... to organize the school supernaturals to cheer everybody up! (Please use \"everyone\" without the mention to avoid pinging too mant people.)**")
    #    member = ctx.author
    #elif member == "everyone" or member == "here" or member == "@here" or member == "everybody":
    #    await ctx.send("**<:hk_yay:964912514179674203> Hanako calls a meeting with all the school mysteries... to organize the school supernaturals to cheer everybody up!**")
    #    member = ctx.author
    if member == None or member.id == ctx.author.id:
        receiver = f"<@{ctx.author.id}>"
    else:
        receiver = f"<@{member.id}>"
    general_comforts = [
        f"**<:mt_star:964954713705545827> Tiara gives {receiver} a bouquet of flowers! :bouquet:**",
        f"**<:ty_hug:964958594195927041> Tsukasa hugs {receiver} so tight, he squishes out all sadness!**",
        f"**<:mk_hehe:964948970147282986> {receiver} is feeling down. Kou made them some donuts to cheer them up and tightly hugs them.**",
        f"**<:mokke1:965249524346024036> the Mokke bring {receiver} candy (and things they stole from students) to cheer them up.**",
        f"**<:m_happy:964932907548430397> Mei draws a reality where {receiver} is never sad.**",
        f"**<:aa_point:964952748799950879> \"I'm not exactly a fan of scary stories... but I'll tell you as many as you want, {receiver}, if it will help you feel better!\"**",
        f"**<:yn_love:964940266844856340> Yashiro hugs {receiver} to cheer them up. The sweet aroma of strawberries fills the air!**",
        f"**<:mk_fluster:973890909529862144> Kou is on {receiver}'s side! \"If there's anything getting you down... or anything... I hope you'll remember that I'm here for you.\"**",
        f"**<:yn_love:964940266844856340> Nene has hired the Mokke delivery service to deliver {receiver} some homemade muffins to cheer them up!**"
        ]
    other_comforts = [
        f"**<:sn_tired:964940862540877864> Sakura and {user} bring out tea for {receiver} to cheer them up.**"
        ]
    self_comforts = [
        f"**<:sn_tired:964940862540877864> Sakura brings out tea for {receiver} to cheer them up.**"
        ]
    #japantimex = japantime()
    # ^^^^^ MAKE THIS WORK
    #add in an "if member = hanakobot" thing
    #if japantimex[2] == 18 and japantimex[3] == 0:
    #    comforts = ["**<:hn_hug:964907449515647057> Aww, was the new chapter that painful...?**"]
    if member == None or member.id == ctx.author.id:
        comforts = general_comforts + self_comforts
    else:
        comforts = general_comforts + other_comforts
    chosen_comfort = choice(comforts)
    await ctx.send(f'{chosen_comfort}')

@comfort.error #comfort.error
async def comfort_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MemberNotFound):
        await ctx.send("Uhh... sorry, who are you talking about?")
    elif isinstance(error, discord.ext.commands.CommandError):
        await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) + ")")

@bot.command()
async def hug(ctx, member: discord.Member=None):
    """
    Mention a user to give them a hug!
    """
    user = ctx.author.mention
    if member == None:
        await ctx.send("**You must mention a user to use this command! Or maybe you want a hug from me...?**")
    elif member.id == 955611964560777236:
        hugs = [
            f"**{user}, you can't hug me! I'm a ghost after all.**",
            f"**{user} tries to hug Hanako... they pass right through him, but feel a chill pass through them.**"
            ]
        hug = choice(hugs)
        await ctx.send(hug)
    elif member.id == ctx.author.id:
        hugs = [
            f"**Aww... {user}, do you need a hug?**",
            f"**{user} wraps their arms around themselves to give themselves a big hug. (Self-love is important!)**",
            f"**{user} hugs a life-size plush of themselves. It's kind of cute... maybe?**"
            ]
        hug = choice(hugs)
        await ctx.send(hug)
    else:
        receiver = f"<@{member.id}>"
        hugs = [
            f"**{user} wraps their arms around {receiver} in a big bear hug.**",
            f"**{user} just sent a hug request! Do you accept, {receiver}?**",
            f"**{receiver} nearly falls over after being suprised by a tackle hug from {user}.**",
            f"**{user} offers warm hugs to comfort {receiver}, gently patting their back. There, there...**",
            f"**{receiver}, there is no escape from {user}'s hugs!**",
            f"**{user} thinks that it's {receiver} they're hugging, but it's actually just a life-size plush of them.**",
            f"**Surprise hug! {user} gives {receiver} a hug from behind them suddenly, startling them a little bit.**"
            ]
        hug = choice(hugs)
        await ctx.send(hug)

@hug.error
async def hug_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MemberNotFound):
        await ctx.send("Uhh... sorry, who are you talking about?")
    elif isinstance(error, discord.ext.commands.CommandError):
        await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) + ")")

#Sakura: <:sn_tired:964940862540877864>
#Hanako hug: <:hn_hug:964907449515647057>
#Hanako happy: <:hk_yay:964912514179674203>
#Aoi: <:aa_happy:964952748628009060>
#Yashiro: <:yn_hm:964907321241260042>
#Tsukasa: <:ty_hug:964958594195927041>
#Kou: <:mk_hehe:964948970147282986>
#Tiara: <:mt_star:964954713705545827>
#Natsuhiko: <:n_cheer:964950239922515979>
#Mei happy: <:m_happy:964932907548430397>
#Mei drawing: <:m_drawing:964938095491428382>
#Mei heart: <:m_heart:964932907527471184>
#Mokke: <:mokke1:965249524346024036>

@bot.command()
async def mokke(ctx, member: discord.Member=None):
    """
    Send the Mokke to give the user you mentioned a candy. However, the Mokke may not always listen to what you want them to do...
    """
    user = ctx.author.mention
    if member == None:
        await ctx.send("**You must mention a user to use this command!**")
    elif member.id == 955611964560777236:
        image_list = [
            r"/home/averyarmstrong/hanakobot/mokke/MD_2.jpg",
            r"/home/averyarmstrong/hanakobot/mokke/MD_3.jpg",
            r"/home/averyarmstrong/hanakobot/mokke/MD_16.jpg"
            ]
        image = choice(image_list)
        await ctx.send("**You don't need to send Mokke to give me candy. I am Mokke.**", file=discord.File(image))
    elif member.id == ctx.author.id:
        image = r"/home/averyarmstrong/hanakobot/mokke/mokke_horde.jpg"
        await ctx.send("**You shall become one with the Mokke.**", file=discord.File(image))
    else:
        receiver = f"<@{member.id}>"
        image_list = [
            r"/home/averyarmstrong/hanakobot/mokke/mokkecandy.gif",
            r"/home/averyarmstrong/hanakobot/mokke/mokke_candy.png",
            r"/home/averyarmstrong/hanakobot/mokke/mokkelounge.gif",
            r"/home/averyarmstrong/hanakobot/mokke/many_mokke.png",
            r"/home/averyarmstrong/hanakobot/mokke/mokke_delivery.png",
            r"/home/averyarmstrong/hanakobot/mokke/mokke_milkshake.png",
            r"/home/averyarmstrong/hanakobot/mokke/mokke_hunting.png",
            ]
        image = choice(image_list)
        if image == image_list[0] or image == image_list[1]:
            message = [
                f'**"Want a candy?" A mokke offers a candy to {receiver}.**',
                f"**The Mokke are hesitant to share their candy with {receiver}, but decide to be generous.**",
                f"**{receiver} is handed one lemon-flavored piece of candy. Reject candy is better than nothing...**",
                f"**The Mokke are willing to give {receiver} as much candy as they want... as long as it's all lemon flavored.**"
                ]
            message_choice = choice(message)
            await ctx.send(message_choice, file=discord.File(image))
        elif image == image_list[2] or image == image_list[3]:
            message = [
                f"**{user} calls for a Mokke to give {receiver} a candy, but the Mokke do as they want.**",
                f"**The Mokke would give {receiver} candy, but they have already eaten it all themselves...**",
                f"**{user}'s request to give {receiver} candy somehow isn't heard by the Mokke's disproportionately large ears. (Or maybe it was just ignored...)**"
                ]
            message_choice = choice(message)
            await ctx.send(message_choice, file=discord.File(image))
        elif image == image_list[4]:
            message = [
                f"**Delivery from {user}! It's a package for {receiver} full of candy (and Mokke).**",
                f"**{receiver} receives a delivery of candy- wait, but the delivery fee needs to be paid in candy? This isn't fair! <:hk_shocked:964913449350070272>**"
                ]
            message_choice = choice(message)
            await ctx.send(message_choice, file=discord.File(image))
        elif image == image_list[5]:
            await ctx.send(f"**The Mokke are out of candy (because they ate it all). However, they still have a milkshake for {receiver} to enjoy.**", file=discord.File(image))
        elif image == image_list[6]:
            await ctx.send(f"**{user} calls for a Mokke to give {receiver} a candy, but Yako decided to go Mokke hunting.**", file=discord.File(image))
        else:
            await ctx.send(f"**A Mokke gives a candy to {receiver}!**")

@mokke.error
async def mokke_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MemberNotFound):
        await ctx.send("Uhh... sorry, who are you talking about?")
    elif isinstance(error, discord.ext.commands.CommandError):
        await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) + ")")
            
bot.run('OTU1NjExOTY0NTYwNzc3MjM2.YjkM_g.4OMkshGrC0Ml-YflykuVvo4T1Io')
#version: 1.0.3

import discord
from discord.ext import commands
import discord.ext.commands.errors
from random import choice

from __main__ import HanakoBot

"""
interaction base:
@commands.command()
async def command(self, ctx, member: discord.Member=None):
    user = ctx.author.mention
    if member == None:
        await ctx.send([needs a user])
    elif member.id == 955611964560777236: #if user is hanakobot
        options = []
        chosen = choice(options)
        await ctx.send(chosen)
    elif member.id == ctx.author.id: #if mentioned user is self
        options = []
        chosen = choice(options)
        await ctx.send(chosen)
    else:
        options = []
        chosen = choice(options)
        await ctx.send(chosen)

error base:
@command.error
async def kiss_error(self, ctx, error):
    if isinstance(error, discord.ext.commands.errors.MemberNotFound):
        await ctx.send("Uhh... sorry, who are you talking about?")
    (if needed)
    elif isinstance(error, discord.ext.commands.CommandError):
        await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
            + ")\nYou can report this error in the HanakoBot test " +
            "server! https://discord.com/invite/ANb3v6bHvx")
"""

class Interactions(commands.Cog):
    def __init__(self, bot: HanakoBot):
        self.bot = bot

    @commands.command()
    async def kiss(self, ctx, member: discord.Member=None):
        """
        Mention a user to give them a kiss.
        """
        user = ctx.author.mention
        if member == None:
            await ctx.send("**You must mention a user to use this command! Or \
perhaps you want me to kiss you instead...?**")
        elif member.id == 955611964560777236:
            kiss_choice = [
                "<:hk_blush:964948035371163688>",
                "<:hk_kiss:964947590259032109> **Huh? You want me to kiss you?**",
                "<:hk_nothanks:964930571178475520> **I don't think Yashiro would \
be happy with you kissing me like that...**"
                ]
            kiss = choice(kiss_choice)
            await ctx.send(f'{kiss}')
        elif member.id == ctx.author.id:
            kiss_choice = [
                f"**{user} leans forward to lovingly kiss... their reflection in \
the mirror in front of them.**",
                f"**{user} has decided that self love is important! They give \
themselves a kiss.**",
                f"**{user} kisses one of the many pictures of themselves on their \
wall. Why do you have all of those, anyways...?**",
                f"**{user} wants to kiss themself? I could kiss you instead... \
<:hk_kiss:964947590259032109>**"
                ]
            kiss = choice(kiss_choice)
            await ctx.send(f'{kiss}')
        else:
            receiver = f"<@{member.id}>"
            kiss_choice = [
                f"**{user} places a spell of protection on {receiver} by kissing \
their cheek.**",
                f"**{user} gently kisses {receiver} on the forehead.**",
                f"**{user} tries to wake up {receiver} with a good-morning kiss, \
but accidentally startles them and gets headbutted.**",
                f'**"There are many different kinds of threats, Honorable Number \
7!" {user} leans in to kiss {receiver} in order to threaten Hanako into \
helping them. (That was unfair! <:hk_dissapoint:964931557456482404>)**',
                f"**{receiver} has finally gotten the kiss from {user} they've \
been dreaming of... or at least they think, until they wake up.**",
                f"**{user} and {receiver} share a sweet, sappy reunion kiss. \
Aww... <:yn_love:964940266844856340>**",
                f"**Month ⬤, day X... the weather is bright and sunny! Today's \
big event... {receiver} shares their first kiss with {user}!**",
                f"**{user} is about to share a kiss with {receiver}, when... \
<:teru_small:973999293398663279> \"Uhh... Did I... interrupt something?\"**",
                f"**{receiver} had a rough day, but {user}'s kiss works like a \
potion and makes everything better.",
                f"**Oh, look - somebody is under the confession tree... it's \
{user} and {receiver}! Such a cute couple. <:yn_love:964940266844856340>**",
                f"**{user} kisses {receiver}. After the sweet, gentle kiss, \
{receiver} decides to rest on the shoulder of {user} as the sun goes down.**",
                f"**{user} kisses {receiver} in the middle of the school garden, \
while Nene jealously looks at them form the bush. <:yn_ehh:964907409502003211>",
                f"**After 5 years of missing each other, {user} runs towards \
{receiver} and gives them a big kiss.",
                f"**{user} gives {receiver} a kiss sweeter than Kou's donuts.**",
                f"**🌙 {user} and {receiver} kiss as the moon shines brightly. \
Their kiss lasts forever...**",
                f"**Whenever {receiver} feels sad, they think of the day they \
received a kiss from {user}. The memory always puts a smile on their face.**",
                f"**{user} and {receiver} almost kissed each other... when \
suddenly, {user} turns into a Mokke.**",
                f"**{user} and {receiver} are kissing under the poring rain, when \
lightning flashes outside! ⛈️ {receiver} suddenly gets scared and faints \
unexpectedly...**",
                f"**Somebody pushes {receiver} into {user}, causing them to \
accidentally kiss.**",
                f"**After so long, {user} gets an oppertunity and kisses \
{receiver}. But they're only *very close friends,* right? Right...?**",
                f"**{receiver} receives a kiss from {user}. Hey, look - these two \
got together faster than Hanako and Nene!**",
                f"**{user} shares a secret kiss with {receiver}. Shh - Nobody \
knows about this!**"
                
                ]
            kiss = choice(kiss_choice)
            await ctx.send(f'{kiss}')

    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

    @commands.command()
    async def comfort(self, ctx, member: discord.Member=None):
        """
        Sends a TBHK character to cheer somebody up.
        """
        user = ctx.author.mention
        if member == None or member.id == ctx.author.id:
            receiver = f"<@{ctx.author.id}>"
        else:
            receiver = f"<@{member.id}>"
        general_comforts = [
            f"**<:mt_star:964954713705545827> Tiara gives {receiver} a bouquet of \
flowers! :bouquet:**",
            f"**<:ty_hug:964958594195927041> Tsukasa hugs {receiver} so tight, he \
squishes out all sadness!**",
            f"**<:mk_hehe:964948970147282986> {receiver} is feeling down. Kou \
made them some donuts to cheer them up and tightly hugs them.**",
            f"**<:mokke1:965249524346024036> the Mokke bring {receiver} candy \
(and things they stole from students) to cheer them up.**",
            f"**<:m_happy:964932907548430397> Mei draws a reality where \
{receiver} is never sad.**",
            f"**<:aa_point:964952748799950879> \"I'm not exactly a fan of scary \
stories... but I'll tell you as many as you want, {receiver}, if it will help \
you feel better!\"**",
            f"**<:yn_love:964940266844856340> Yashiro hugs {receiver} to cheer \
them up. The sweet aroma of strawberries fills the air!**",
            f"**<:mk_fluster:973890909529862144> Kou is on {receiver}'s side! \
\"If there's anything getting you down... or anything... I hope you'll \
remember that I'm here for you.\"**",
            f"**<:yn_love:964940266844856340> Nene has hired the Mokke delivery \
service to deliver {receiver} some homemade muffins to cheer them up!**"
            ]
        other_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura and {user} bring out tea \
for {receiver} to cheer them up.**"
            ]
        self_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura brings out tea for \
{receiver} to cheer them up.**"
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

    @comfort.error
    async def comfort_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

    @commands.command()
    async def hug(self, ctx, member: discord.Member=None):
        """
        Mention a user to give them a hug.
        """
        user = ctx.author.mention
        if member == None:
            await ctx.send("**You must mention a user to use this command! Or \
maybe you want a hug from me...?**")
        elif member.id == 955611964560777236:
            hugs = [
                f"**{user}, you can't hug me! I'm a ghost after all.**",
                f"**{user} tries to hug Hanako... they pass right through him, \
but feel a chill pass through them.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        elif member.id == ctx.author.id:
            hugs = [
                f"**Aww... {user}, do you need a hug?**",
                f"**{user} wraps their arms around themselves to give themselves \
a big hug. (Self-love is important!)**",
                f"**{user} hugs a life-size plush of themselves. It's kind of \
cute... maybe?**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        else:
            receiver = f"<@{member.id}>"
            hugs = [
                f"**{user} wraps their arms around {receiver} in a big bear hug.**",
                f"**{user} just sent a hug request! Do you accept, {receiver}?**",
                f"**{receiver} nearly falls over after being suprised by a tackle \
hug from {user}.**",
                f"**{user} offers warm hugs to comfort {receiver}, gently patting \
their back. There, there...**",
                f"**{receiver}, there is no escape from {user}'s hugs!**",
                f"**{user} thinks that it's {receiver} they're hugging, but it's \
actually just a life-size plush of them.**",
                f"**Surprise hug! {user} gives {receiver} a hug from behind them \
suddenly, startling them a little bit.**",
                f"**{user} hugs {receiver} forever and eternally, until the end \
of time.**",
                f"**Even though {user} doesn't like hugs, they make an exception \
and tightly hug {receiver}.**",
                f"**A gift pops up in front of {receiver}! Let's open it and see \
what it is... it's {user}! They jump out and tightly hug {receiver}.**",
                f"**{user} tries to get {receiver}'s attention, but ends up being \
ignored. Because of that, {user} tries to slap {receiver}. However, they \
realise that they are too cute to be slapped, and so they hug them very \
tightly instead.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

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

    @commands.command()
    async def mokke(self, ctx, member: discord.Member=None):
        """
        Ask the Mokke to give a user some candy.
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
            await ctx.send("**You don't need to send Mokke to give me candy. I am \
Mokke.**", file=discord.File(image))
        elif member.id == ctx.author.id:
            image = r"/home/averyarmstrong/hanakobot/mokke/mokke_horde.jpg"
            await ctx.send("**You shall become one with the Mokke.**", 
                        file=discord.File(image))
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
                    f"**The Mokke are hesitant to share their candy with \
{receiver}, but decide to be generous.**",
                    f"**{receiver} is handed one lemon-flavored piece of candy. \
Reject candy is better than nothing...**",
                    f"**The Mokke are willing to give {receiver} as much candy as \
they want... as long as it's all lemon flavored.**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[2] or image == image_list[3]:
                message = [
                    f"**{user} calls for a Mokke to give {receiver} a candy, but \
the Mokke do as they want.**",
                    f"**The Mokke would give {receiver} candy, but they have \
already eaten it all themselves...**",
                    f"**{user}'s request to give {receiver} candy somehow isn't \
heard by the Mokke's disproportionately large ears. (Or maybe it was just ignored...)**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[4]:
                message = [
                    f"**Delivery from {user}! It's a package for {receiver} full \
of candy (and Mokke).**",
                    f"**{receiver} receives a delivery of candy- wait, but the \
delivery fee needs to be paid in candy? This isn't fair! \
<:hk_shocked:964913449350070272>**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[5]:
                await ctx.send(f"**The Mokke are out of candy (because they ate " +
                    "it all). However, they still have a milkshake for " 
                    + f"{receiver} to enjoy.**",
    file=discord.File(image))
            elif image == image_list[6]:
                await ctx.send(f"**{user} calls for a Mokke to give {receiver} a " +
                    "candy, but Yako decided to go Mokke hunting.**",
                    file=discord.File(image))
            else:
                await ctx.send(f"**A Mokke gives a candy to {receiver}!**")

    @mokke.error
    async def mokke_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                        + ")\nYou can report this error in the HanakoBot " +
                        "test server! https://discord.com/invite/ANb3v6bHvx")


        if member == None or member.id == ctx.author.id:
            receiver = f"<@{ctx.author.id}>"
        else:
            receiver = f"<@{member.id}>"
        general_comforts = [
            f"**<:mt_star:964954713705545827> Tiara gives {receiver} a bouquet of \
flowers! :bouquet:**",
            f"**<:ty_hug:964958594195927041> Tsukasa hugs {receiver} so tight, he \
squishes out all sadness!**",
            f"**<:mk_hehe:964948970147282986> {receiver} is feeling down. Kou \
made them some donuts to cheer them up and tightly hugs them.**",
            f"**<:mokke1:965249524346024036> the Mokke bring {receiver} candy \
(and things they stole from students) to cheer them up.**",
            f"**<:m_happy:964932907548430397> Mei draws a reality where \
{receiver} is never sad.**",
            f"**<:aa_point:964952748799950879> \"I'm not exactly a fan of scary \
stories... but I'll tell you as many as you want, {receiver}, if it will help \
you feel better!\"**",
            f"**<:yn_love:964940266844856340> Yashiro hugs {receiver} to cheer \
them up. The sweet aroma of strawberries fills the air!**",
            f"**<:mk_fluster:973890909529862144> Kou is on {receiver}'s side! \
\"If there's anything getting you down... or anything... I hope you'll \
remember that I'm here for you.\"**",
            f"**<:yn_love:964940266844856340> Nene has hired the Mokke delivery \
service to deliver {receiver} some homemade muffins to cheer them up!**"
            ]
        other_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura and {user} bring out tea \
for {receiver} to cheer them up.**"
            ]
        self_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura brings out tea for \
{receiver} to cheer them up.**"
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

    @comfort.error
    async def comfort_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

    @commands.command()
    async def hug(self, ctx, member: discord.Member=None):
        """
        Mention a user to give them a hug.
        """
        user = ctx.author.mention
        if member == None:
            await ctx.send("**You must mention a user to use this command! Or \
maybe you want a hug from me...?**")
        elif member.id == 955611964560777236:
            hugs = [
                f"**{user}, you can't hug me! I'm a ghost after all.**",
                f"**{user} tries to hug Hanako... they pass right through him, \
but feel a chill pass through them.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        elif member.id == ctx.author.id:
            hugs = [
                f"**Aww... {user}, do you need a hug?**",
                f"**{user} wraps their arms around themselves to give themselves \
a big hug. (Self-love is important!)**",
                f"**{user} hugs a life-size plush of themselves. It's kind of \
cute... maybe?**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        else:
            receiver = f"<@{member.id}>"
            hugs = [
                f"**{user} wraps their arms around {receiver} in a big bear hug.**",
                f"**{user} just sent a hug request! Do you accept, {receiver}?**",
                f"**{receiver} nearly falls over after being suprised by a tackle \
hug from {user}.**",
                f"**{user} offers warm hugs to comfort {receiver}, gently patting \
their back. There, there...**",
                f"**{receiver}, there is no escape from {user}'s hugs!**",
                f"**{user} thinks that it's {receiver} they're hugging, but it's \
actually just a life-size plush of them.**",
                f"**Surprise hug! {user} gives {receiver} a hug from behind them \
suddenly, startling them a little bit.**",
                f"**{user} hugs {receiver} forever and eternally, until the end \
of time.**",
                f"**Even though {user} doesn't like hugs, they make an exception \
and tightly hug {receiver}.**",
                f"**A gift pops up in front of {receiver}! Let's open it and see \
what it is... it's {user}! They jump out and tightly hug {receiver}.**",
                f"**{user} tries to get {receiver}'s attention, but ends up being \
ignored. Because of that, {user} tries to slap {receiver}. However, they \
realise that they are too cute to be slapped, and so they hug them very \
tightly instead.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

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

    @commands.command()
    async def mokke(self, ctx, member: discord.Member=None):
        """
        Ask the Mokke to give a user some candy.
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
            await ctx.send("**You don't need to send Mokke to give me candy. I am \
Mokke.**", file=discord.File(image))
        elif member.id == ctx.author.id:
            image = r"/home/averyarmstrong/hanakobot/mokke/mokke_horde.jpg"
            await ctx.send("**You shall become one with the Mokke.**", 
                        file=discord.File(image))
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
                    f"**The Mokke are hesitant to share their candy with \
{receiver}, but decide to be generous.**",
                    f"**{receiver} is handed one lemon-flavored piece of candy. \
Reject candy is better than nothing...**",
                    f"**The Mokke are willing to give {receiver} as much candy as \
they want... as long as it's all lemon flavored.**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[2] or image == image_list[3]:
                message = [
                    f"**{user} calls for a Mokke to give {receiver} a candy, but \
the Mokke do as they want.**",
                    f"**The Mokke would give {receiver} candy, but they have \
already eaten it all themselves...**",
                    f"**{user}'s request to give {receiver} candy somehow isn't \
heard by the Mokke's disproportionately large ears. (Or maybe it was just ignored...)**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[4]:
                message = [
                    f"**Delivery from {user}! It's a package for {receiver} full \
of candy (and Mokke).**",
                    f"**{receiver} receives a delivery of candy- wait, but the \
delivery fee needs to be paid in candy? This isn't fair! \
<:hk_shocked:964913449350070272>**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[5]:
                await ctx.send(f"**The Mokke are out of candy (because they ate " +
                    "it all). However, they still have a milkshake for " 
                    + f"{receiver} to enjoy.**",
    file=discord.File(image))
            elif image == image_list[6]:
                await ctx.send(f"**{user} calls for a Mokke to give {receiver} a " +
                    "candy, but Yako decided to go Mokke hunting.**",
                    file=discord.File(image))
            else:
                await ctx.send(f"**A Mokke gives a candy to {receiver}!**")

    @mokke.error
    async def mokke_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                        + ")\nYou can report this error in the HanakoBot " +
                        "test server! https://discord.com/invite/ANb3v6bHvx")


        if member == None or member.id == ctx.author.id:
            receiver = f"<@{ctx.author.id}>"
        else:
            receiver = f"<@{member.id}>"
        general_comforts = [
            f"**<:mt_star:964954713705545827> Tiara gives {receiver} a bouquet of \
flowers! :bouquet:**",
            f"**<:ty_hug:964958594195927041> Tsukasa hugs {receiver} so tight, he \
squishes out all sadness!**",
            f"**<:mk_hehe:964948970147282986> {receiver} is feeling down. Kou \
made them some donuts to cheer them up and tightly hugs them.**",
            f"**<:mokke1:965249524346024036> the Mokke bring {receiver} candy \
(and things they stole from students) to cheer them up.**",
            f"**<:m_happy:964932907548430397> Mei draws a reality where \
{receiver} is never sad.**",
            f"**<:aa_point:964952748799950879> \"I'm not exactly a fan of scary \
stories... but I'll tell you as many as you want, {receiver}, if it will help \
you feel better!\"**",
            f"**<:yn_love:964940266844856340> Yashiro hugs {receiver} to cheer \
them up. The sweet aroma of strawberries fills the air!**",
            f"**<:mk_fluster:973890909529862144> Kou is on {receiver}'s side! \
\"If there's anything getting you down... or anything... I hope you'll \
remember that I'm here for you.\"**",
            f"**<:yn_love:964940266844856340> Nene has hired the Mokke delivery \
service to deliver {receiver} some homemade muffins to cheer them up!**"
            ]
        other_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura and {user} bring out tea \
for {receiver} to cheer them up.**"
            ]
        self_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura brings out tea for \
{receiver} to cheer them up.**"
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

    @comfort.error
    async def comfort_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

    @commands.command()
    async def hug(self, ctx, member: discord.Member=None):
        """
        Mention a user to give them a hug.
        """
        user = ctx.author.mention
        if member == None:
            await ctx.send("**You must mention a user to use this command! Or \
maybe you want a hug from me...?**")
        elif member.id == 955611964560777236:
            hugs = [
                f"**{user}, you can't hug me! I'm a ghost after all.**",
                f"**{user} tries to hug Hanako... they pass right through him, \
but feel a chill pass through them.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        elif member.id == ctx.author.id:
            hugs = [
                f"**Aww... {user}, do you need a hug?**",
                f"**{user} wraps their arms around themselves to give themselves \
a big hug. (Self-love is important!)**",
                f"**{user} hugs a life-size plush of themselves. It's kind of \
cute... maybe?**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        else:
            receiver = f"<@{member.id}>"
            hugs = [
                f"**{user} wraps their arms around {receiver} in a big bear hug.**",
                f"**{user} just sent a hug request! Do you accept, {receiver}?**",
                f"**{receiver} nearly falls over after being suprised by a tackle \
hug from {user}.**",
                f"**{user} offers warm hugs to comfort {receiver}, gently patting \
their back. There, there...**",
                f"**{receiver}, there is no escape from {user}'s hugs!**",
                f"**{user} thinks that it's {receiver} they're hugging, but it's \
actually just a life-size plush of them.**",
                f"**Surprise hug! {user} gives {receiver} a hug from behind them \
suddenly, startling them a little bit.**",
                f"**{user} hugs {receiver} forever and eternally, until the end \
of time.**",
                f"**Even though {user} doesn't like hugs, they make an exception \
and tightly hug {receiver}.**",
                f"**A gift pops up in front of {receiver}! Let's open it and see \
what it is... it's {user}! They jump out and tightly hug {receiver}.**",
                f"**{user} tries to get {receiver}'s attention, but ends up being \
ignored. Because of that, {user} tries to slap {receiver}. However, they \
realise that they are too cute to be slapped, and so they hug them very \
tightly instead.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

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

    @commands.command()
    async def mokke(self, ctx, member: discord.Member=None):
        """
        Ask the Mokke to give a user some candy.
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
            await ctx.send("**You don't need to send Mokke to give me candy. I am \
Mokke.**", file=discord.File(image))
        elif member.id == ctx.author.id:
            image = r"/home/averyarmstrong/hanakobot/mokke/mokke_horde.jpg"
            await ctx.send("**You shall become one with the Mokke.**", 
                        file=discord.File(image))
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
                    f"**The Mokke are hesitant to share their candy with \
{receiver}, but decide to be generous.**",
                    f"**{receiver} is handed one lemon-flavored piece of candy. \
Reject candy is better than nothing...**",
                    f"**The Mokke are willing to give {receiver} as much candy as \
they want... as long as it's all lemon flavored.**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[2] or image == image_list[3]:
                message = [
                    f"**{user} calls for a Mokke to give {receiver} a candy, but \
the Mokke do as they want.**",
                    f"**The Mokke would give {receiver} candy, but they have \
already eaten it all themselves...**",
                    f"**{user}'s request to give {receiver} candy somehow isn't \
heard by the Mokke's disproportionately large ears. (Or maybe it was just ignored...)**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[4]:
                message = [
                    f"**Delivery from {user}! It's a package for {receiver} full \
of candy (and Mokke).**",
                    f"**{receiver} receives a delivery of candy- wait, but the \
delivery fee needs to be paid in candy? This isn't fair! \
<:hk_shocked:964913449350070272>**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[5]:
                await ctx.send(f"**The Mokke are out of candy (because they ate " +
                    "it all). However, they still have a milkshake for " 
                    + f"{receiver} to enjoy.**",
    file=discord.File(image))
            elif image == image_list[6]:
                await ctx.send(f"**{user} calls for a Mokke to give {receiver} a " +
                    "candy, but Yako decided to go Mokke hunting.**",
                    file=discord.File(image))
            else:
                await ctx.send(f"**A Mokke gives a candy to {receiver}!**")

    @mokke.error
    async def mokke_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                        + ")\nYou can report this error in the HanakoBot " +
                        "test server! https://discord.com/invite/ANb3v6bHvx")


        if member == None or member.id == ctx.author.id:
            receiver = f"<@{ctx.author.id}>"
        else:
            receiver = f"<@{member.id}>"
        general_comforts = [
            f"**<:mt_star:964954713705545827> Tiara gives {receiver} a bouquet of \
flowers! :bouquet:**",
            f"**<:ty_hug:964958594195927041> Tsukasa hugs {receiver} so tight, he \
squishes out all sadness!**",
            f"**<:mk_hehe:964948970147282986> {receiver} is feeling down. Kou \
made them some donuts to cheer them up and tightly hugs them.**",
            f"**<:mokke1:965249524346024036> the Mokke bring {receiver} candy \
(and things they stole from students) to cheer them up.**",
            f"**<:m_happy:964932907548430397> Mei draws a reality where \
{receiver} is never sad.**",
            f"**<:aa_point:964952748799950879> \"I'm not exactly a fan of scary \
stories... but I'll tell you as many as you want, {receiver}, if it will help \
you feel better!\"**",
            f"**<:yn_love:964940266844856340> Yashiro hugs {receiver} to cheer \
them up. The sweet aroma of strawberries fills the air!**",
            f"**<:mk_fluster:973890909529862144> Kou is on {receiver}'s side! \
\"If there's anything getting you down... or anything... I hope you'll \
remember that I'm here for you.\"**",
            f"**<:yn_love:964940266844856340> Nene has hired the Mokke delivery \
service to deliver {receiver} some homemade muffins to cheer them up!**"
            ]
        other_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura and {user} bring out tea \
for {receiver} to cheer them up.**"
            ]
        self_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura brings out tea for \
{receiver} to cheer them up.**"
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

    @comfort.error
    async def comfort_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

    @commands.command()
    async def hug(self, ctx, member: discord.Member=None):
        """
        Mention a user to give them a hug.
        """
        user = ctx.author.mention
        if member == None:
            await ctx.send("**You must mention a user to use this command! Or \
maybe you want a hug from me...?**")
        elif member.id == 955611964560777236:
            hugs = [
                f"**{user}, you can't hug me! I'm a ghost after all.**",
                f"**{user} tries to hug Hanako... they pass right through him, \
but feel a chill pass through them.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        elif member.id == ctx.author.id:
            hugs = [
                f"**Aww... {user}, do you need a hug?**",
                f"**{user} wraps their arms around themselves to give themselves \
a big hug. (Self-love is important!)**",
                f"**{user} hugs a life-size plush of themselves. It's kind of \
cute... maybe?**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        else:
            receiver = f"<@{member.id}>"
            hugs = [
                f"**{user} wraps their arms around {receiver} in a big bear hug.**",
                f"**{user} just sent a hug request! Do you accept, {receiver}?**",
                f"**{receiver} nearly falls over after being suprised by a tackle \
hug from {user}.**",
                f"**{user} offers warm hugs to comfort {receiver}, gently patting \
their back. There, there...**",
                f"**{receiver}, there is no escape from {user}'s hugs!**",
                f"**{user} thinks that it's {receiver} they're hugging, but it's \
actually just a life-size plush of them.**",
                f"**Surprise hug! {user} gives {receiver} a hug from behind them \
suddenly, startling them a little bit.**",
                f"**{user} hugs {receiver} forever and eternally, until the end \
of time.**",
                f"**Even though {user} doesn't like hugs, they make an exception \
and tightly hug {receiver}.**",
                f"**A gift pops up in front of {receiver}! Let's open it and see \
what it is... it's {user}! They jump out and tightly hug {receiver}.**",
                f"**{user} tries to get {receiver}'s attention, but ends up being \
ignored. Because of that, {user} tries to slap {receiver}. However, they \
realise that they are too cute to be slapped, and so they hug them very \
tightly instead.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

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

    @commands.command()
    async def mokke(self, ctx, member: discord.Member=None):
        """
        Ask the Mokke to give a user some candy.
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
            await ctx.send("**You don't need to send Mokke to give me candy. I am \
Mokke.**", file=discord.File(image))
        elif member.id == ctx.author.id:
            image = r"/home/averyarmstrong/hanakobot/mokke/mokke_horde.jpg"
            await ctx.send("**You shall become one with the Mokke.**", 
                        file=discord.File(image))
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
                    f"**The Mokke are hesitant to share their candy with \
{receiver}, but decide to be generous.**",
                    f"**{receiver} is handed one lemon-flavored piece of candy. \
Reject candy is better than nothing...**",
                    f"**The Mokke are willing to give {receiver} as much candy as \
they want... as long as it's all lemon flavored.**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[2] or image == image_list[3]:
                message = [
                    f"**{user} calls for a Mokke to give {receiver} a candy, but \
the Mokke do as they want.**",
                    f"**The Mokke would give {receiver} candy, but they have \
already eaten it all themselves...**",
                    f"**{user}'s request to give {receiver} candy somehow isn't \
heard by the Mokke's disproportionately large ears. (Or maybe it was just ignored...)**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[4]:
                message = [
                    f"**Delivery from {user}! It's a package for {receiver} full \
of candy (and Mokke).**",
                    f"**{receiver} receives a delivery of candy- wait, but the \
delivery fee needs to be paid in candy? This isn't fair! \
<:hk_shocked:964913449350070272>**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[5]:
                await ctx.send(f"**The Mokke are out of candy (because they ate " +
                    "it all). However, they still have a milkshake for " 
                    + f"{receiver} to enjoy.**",
    file=discord.File(image))
            elif image == image_list[6]:
                await ctx.send(f"**{user} calls for a Mokke to give {receiver} a " +
                    "candy, but Yako decided to go Mokke hunting.**",
                    file=discord.File(image))
            else:
                await ctx.send(f"**A Mokke gives a candy to {receiver}!**")

    @mokke.error
    async def mokke_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                        + ")\nYou can report this error in the HanakoBot " +
                        "test server! https://discord.com/invite/ANb3v6bHvx")


        if member == None or member.id == ctx.author.id:
            receiver = f"<@{ctx.author.id}>"
        else:
            receiver = f"<@{member.id}>"
        general_comforts = [
            f"**<:mt_star:964954713705545827> Tiara gives {receiver} a bouquet of \
flowers! :bouquet:**",
            f"**<:ty_hug:964958594195927041> Tsukasa hugs {receiver} so tight, he \
squishes out all sadness!**",
            f"**<:mk_hehe:964948970147282986> {receiver} is feeling down. Kou \
made them some donuts to cheer them up and tightly hugs them.**",
            f"**<:mokke1:965249524346024036> the Mokke bring {receiver} candy \
(and things they stole from students) to cheer them up.**",
            f"**<:m_happy:964932907548430397> Mei draws a reality where \
{receiver} is never sad.**",
            f"**<:aa_point:964952748799950879> \"I'm not exactly a fan of scary \
stories... but I'll tell you as many as you want, {receiver}, if it will help \
you feel better!\"**",
            f"**<:yn_love:964940266844856340> Yashiro hugs {receiver} to cheer \
them up. The sweet aroma of strawberries fills the air!**",
            f"**<:mk_fluster:973890909529862144> Kou is on {receiver}'s side! \
\"If there's anything getting you down... or anything... I hope you'll \
remember that I'm here for you.\"**",
            f"**<:yn_love:964940266844856340> Nene has hired the Mokke delivery \
service to deliver {receiver} some homemade muffins to cheer them up!**"
            ]
        other_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura and {user} bring out tea \
for {receiver} to cheer them up.**"
            ]
        self_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura brings out tea for \
{receiver} to cheer them up.**"
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

    @comfort.error
    async def comfort_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

    @commands.command()
    async def hug(self, ctx, member: discord.Member=None):
        """
        Mention a user to give them a hug.
        """
        user = ctx.author.mention
        if member == None:
            await ctx.send("**You must mention a user to use this command! Or \
maybe you want a hug from me...?**")
        elif member.id == 955611964560777236:
            hugs = [
                f"**{user}, you can't hug me! I'm a ghost after all.**",
                f"**{user} tries to hug Hanako... they pass right through him, \
but feel a chill pass through them.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        elif member.id == ctx.author.id:
            hugs = [
                f"**Aww... {user}, do you need a hug?**",
                f"**{user} wraps their arms around themselves to give themselves \
a big hug. (Self-love is important!)**",
                f"**{user} hugs a life-size plush of themselves. It's kind of \
cute... maybe?**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        else:
            receiver = f"<@{member.id}>"
            hugs = [
                f"**{user} wraps their arms around {receiver} in a big bear hug.**",
                f"**{user} just sent a hug request! Do you accept, {receiver}?**",
                f"**{receiver} nearly falls over after being suprised by a tackle \
hug from {user}.**",
                f"**{user} offers warm hugs to comfort {receiver}, gently patting \
their back. There, there...**",
                f"**{receiver}, there is no escape from {user}'s hugs!**",
                f"**{user} thinks that it's {receiver} they're hugging, but it's \
actually just a life-size plush of them.**",
                f"**Surprise hug! {user} gives {receiver} a hug from behind them \
suddenly, startling them a little bit.**",
                f"**{user} hugs {receiver} forever and eternally, until the end \
of time.**",
                f"**Even though {user} doesn't like hugs, they make an exception \
and tightly hug {receiver}.**",
                f"**A gift pops up in front of {receiver}! Let's open it and see \
what it is... it's {user}! They jump out and tightly hug {receiver}.**",
                f"**{user} tries to get {receiver}'s attention, but ends up being \
ignored. Because of that, {user} tries to slap {receiver}. However, they \
realise that they are too cute to be slapped, and so they hug them very \
tightly instead.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

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

    @commands.command()
    async def mokke(self, ctx, member: discord.Member=None):
        """
        Ask the Mokke to give a user some candy.
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
            await ctx.send("**You don't need to send Mokke to give me candy. I am \
Mokke.**", file=discord.File(image))
        elif member.id == ctx.author.id:
            image = r"/home/averyarmstrong/hanakobot/mokke/mokke_horde.jpg"
            await ctx.send("**You shall become one with the Mokke.**", 
                        file=discord.File(image))
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
                    f"**The Mokke are hesitant to share their candy with \
{receiver}, but decide to be generous.**",
                    f"**{receiver} is handed one lemon-flavored piece of candy. \
Reject candy is better than nothing...**",
                    f"**The Mokke are willing to give {receiver} as much candy as \
they want... as long as it's all lemon flavored.**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[2] or image == image_list[3]:
                message = [
                    f"**{user} calls for a Mokke to give {receiver} a candy, but \
the Mokke do as they want.**",
                    f"**The Mokke would give {receiver} candy, but they have \
already eaten it all themselves...**",
                    f"**{user}'s request to give {receiver} candy somehow isn't \
heard by the Mokke's disproportionately large ears. (Or maybe it was just ignored...)**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[4]:
                message = [
                    f"**Delivery from {user}! It's a package for {receiver} full \
of candy (and Mokke).**",
                    f"**{receiver} receives a delivery of candy- wait, but the \
delivery fee needs to be paid in candy? This isn't fair! \
<:hk_shocked:964913449350070272>**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[5]:
                await ctx.send(f"**The Mokke are out of candy (because they ate " +
                    "it all). However, they still have a milkshake for " 
                    + f"{receiver} to enjoy.**",
    file=discord.File(image))
            elif image == image_list[6]:
                await ctx.send(f"**{user} calls for a Mokke to give {receiver} a " +
                    "candy, but Yako decided to go Mokke hunting.**",
                    file=discord.File(image))
            else:
                await ctx.send(f"**A Mokke gives a candy to {receiver}!**")

    @mokke.error
    async def mokke_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                        + ")\nYou can report this error in the HanakoBot " +
                        "test server! https://discord.com/invite/ANb3v6bHvx")


        if member == None or member.id == ctx.author.id:
            receiver = f"<@{ctx.author.id}>"
        else:
            receiver = f"<@{member.id}>"
        general_comforts = [
            f"**<:mt_star:964954713705545827> Tiara gives {receiver} a bouquet of \
flowers! :bouquet:**",
            f"**<:ty_hug:964958594195927041> Tsukasa hugs {receiver} so tight, he \
squishes out all sadness!**",
            f"**<:mk_hehe:964948970147282986> {receiver} is feeling down. Kou \
made them some donuts to cheer them up and tightly hugs them.**",
            f"**<:mokke1:965249524346024036> the Mokke bring {receiver} candy \
(and things they stole from students) to cheer them up.**",
            f"**<:m_happy:964932907548430397> Mei draws a reality where \
{receiver} is never sad.**",
            f"**<:aa_point:964952748799950879> \"I'm not exactly a fan of scary \
stories... but I'll tell you as many as you want, {receiver}, if it will help \
you feel better!\"**",
            f"**<:yn_love:964940266844856340> Yashiro hugs {receiver} to cheer \
them up. The sweet aroma of strawberries fills the air!**",
            f"**<:mk_fluster:973890909529862144> Kou is on {receiver}'s side! \
\"If there's anything getting you down... or anything... I hope you'll \
remember that I'm here for you.\"**",
            f"**<:yn_love:964940266844856340> Nene has hired the Mokke delivery \
service to deliver {receiver} some homemade muffins to cheer them up!**"
            ]
        other_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura and {user} bring out tea \
for {receiver} to cheer them up.**"
            ]
        self_comforts = [
            f"**<:sn_tired:964940862540877864> Sakura brings out tea for \
{receiver} to cheer them up.**"
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

    @comfort.error
    async def comfort_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

    @commands.command()
    async def hug(self, ctx, member: discord.Member=None):
        """
        Mention a user to give them a hug.
        """
        user = ctx.author.mention
        if member == None:
            await ctx.send("**You must mention a user to use this command! Or \
maybe you want a hug from me...?**")
        elif member.id == 955611964560777236:
            hugs = [
                f"**{user}, you can't hug me! I'm a ghost after all.**",
                f"**{user} tries to hug Hanako... they pass right through him, \
but feel a chill pass through them.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        elif member.id == ctx.author.id:
            hugs = [
                f"**Aww... {user}, do you need a hug?**",
                f"**{user} wraps their arms around themselves to give themselves \
a big hug. (Self-love is important!)**",
                f"**{user} hugs a life-size plush of themselves. It's kind of \
cute... maybe?**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)
        else:
            receiver = f"<@{member.id}>"
            hugs = [
                f"**{user} wraps their arms around {receiver} in a big bear hug.**",
                f"**{user} just sent a hug request! Do you accept, {receiver}?**",
                f"**{receiver} nearly falls over after being suprised by a tackle \
hug from {user}.**",
                f"**{user} offers warm hugs to comfort {receiver}, gently patting \
their back. There, there...**",
                f"**{receiver}, there is no escape from {user}'s hugs!**",
                f"**{user} thinks that it's {receiver} they're hugging, but it's \
actually just a life-size plush of them.**",
                f"**Surprise hug! {user} gives {receiver} a hug from behind them \
suddenly, startling them a little bit.**",
                f"**{user} hugs {receiver} forever and eternally, until the end \
of time.**",
                f"**Even though {user} doesn't like hugs, they make an exception \
and tightly hug {receiver}.**",
                f"**A gift pops up in front of {receiver}! Let's open it and see \
what it is... it's {user}! They jump out and tightly hug {receiver}.**",
                f"**{user} tries to get {receiver}'s attention, but ends up being \
ignored. Because of that, {user} tries to slap {receiver}. However, they \
realise that they are too cute to be slapped, and so they hug them very \
tightly instead.**"
                ]
            hug = choice(hugs)
            await ctx.send(hug)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                + ")\nYou can report this error in the HanakoBot test " +
                "server! https://discord.com/invite/ANb3v6bHvx")

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

    @commands.command()
    async def mokke(self, ctx, member: discord.Member=None):
        """
        Ask the Mokke to give a user some candy.
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
            await ctx.send("**You don't need to send Mokke to give me candy. I am \
Mokke.**", file=discord.File(image))
        elif member.id == ctx.author.id:
            image = r"/home/averyarmstrong/hanakobot/mokke/mokke_horde.jpg"
            await ctx.send("**You shall become one with the Mokke.**", 
                        file=discord.File(image))
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
                    f"**The Mokke are hesitant to share their candy with \
{receiver}, but decide to be generous.**",
                    f"**{receiver} is handed one lemon-flavored piece of candy. \
Reject candy is better than nothing...**",
                    f"**The Mokke are willing to give {receiver} as much candy as \
they want... as long as it's all lemon flavored.**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[2] or image == image_list[3]:
                message = [
                    f"**{user} calls for a Mokke to give {receiver} a candy, but \
the Mokke do as they want.**",
                    f"**The Mokke would give {receiver} candy, but they have \
already eaten it all themselves...**",
                    f"**{user}'s request to give {receiver} candy somehow isn't \
heard by the Mokke's disproportionately large ears. (Or maybe it was just ignored...)**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[4]:
                message = [
                    f"**Delivery from {user}! It's a package for {receiver} full \
of candy (and Mokke).**",
                    f"**{receiver} receives a delivery of candy- wait, but the \
delivery fee needs to be paid in candy? This isn't fair! \
<:hk_shocked:964913449350070272>**"
                    ]
                message_choice = choice(message)
                await ctx.send(message_choice, file=discord.File(image))
            elif image == image_list[5]:
                await ctx.send(f"**The Mokke are out of candy (because they ate " +
                    "it all). However, they still have a milkshake for " 
                    + f"{receiver} to enjoy.**",
    file=discord.File(image))
            elif image == image_list[6]:
                await ctx.send(f"**{user} calls for a Mokke to give {receiver} a " +
                    "candy, but Yako decided to go Mokke hunting.**",
                    file=discord.File(image))
            else:
                await ctx.send(f"**A Mokke gives a candy to {receiver}!**")

    @mokke.error
    async def mokke_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MemberNotFound):
            await ctx.send("Uhh... sorry, who are you talking about?")
        elif isinstance(error, discord.ext.commands.CommandError):
            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
                        + ")\nYou can report this error in the HanakoBot " +
                        "test server! https://discord.com/invite/ANb3v6bHvx")

    @commands.command()
    async def kill(self, ctx, member: discord.Member=None):
        user = ctx.author.mention
        if member == None:
            await ctx.send("**You need to mention your target to use this command...**")
        elif member.id == 955611964560777236: #if user is hanakobot
            options = [
                "**You can't kill me, I'm already dead!**",
                "**I think I'm dying... That was a joke. I'm already dead.**",
                "**WOW, that was scary! I thought I was going to die... Oh, \
yeah. I died already..."
            ]
            chosen = choice(options)
            await ctx.send(chosen)
        elif member.id == member.id: #if user is self
            options = [
                "<:hk_stare:964958157673750650> **Are you okay...? Do you need a hug?**",
                "<:hk_shocked:964913449350070272> **Wait - no, you can't do that. That's illegal!**",
                "<:hn_hug:964907449515647057> **I'm here to listen if you need it...**",
                "<:hk_blush3:964912865746231356> **Don't tell me that it's okay if you die...**"
            ]
            #come up with more options
            chosen = choice(options)
            await ctx.send(chosen)
        else:
            receiver = f"<@{member.id}>"
            options = [
                f "**{receiver} gets turned into a donut by {user}.**",
                f"**It seems that {receiver} has gotten killed yet another time... Just like a certain \
someone else we k- Oh... too soon? <:ms_stand:1065241097242161213>**",
                f"<:teru_small:973999293398663279> **{receiver} gets exorcised by Teru and {user}. To the Far Shore with you!**",
                f"<:aa_think:964952749181636628> **It seems that {receiver} was chosen as the next kannagi, and is thrown off a cliff.**",
                f"**<:aa_shock:1065244522252091412> Looks like Aoi has a new crush... on {receiver}, who ends up on the wrong end \
of Akane's bat.**",
                f"**{receiver} stepped on the fourth step of Misaki stairs... You know what happens next!**",
                f"**{receiver} gets made into a tasty meal and is eaten by {user}. Yum...?**",
                f"**<:sn_blank:964943466620657694> Sakura and {user} invite {receiver} to a very deadly tea party.**"
            ]
            chosen = choice(options)
            await ctx.send(chosen)

def setup(bot: HanakoBot):
    cog = Interactions(bot)
    bot.add_cog(cog)


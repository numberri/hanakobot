import discord
from discord import option
from discord.ext import commands
from random import choice

def response(target_id, user_id, 
            hanako_response, 
            self_response, 
            regular_response):
    #user = ctx.author.mention
    if target_id == 955611964560777236: #if target is hanakobot
        return choice(hanako_response)
    elif target_id == user_id: #if mentioned user is self
        return choice(self_response)
    else:
        return choice(regular_response)

class Interactions(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot
        #bot_id = self.bot.user.id
    
    interactions = discord.SlashCommandGroup("interactions", description="Interact with people - and yourself - the TBHK way!")

    @interactions.command()
    @option(
        "member",
        discord.Member,
        description="You and this person, sitting in a tree..."
    )
    async def kiss(self, ctx, member: discord.Member):
        """
        Mention a user to give them a kiss <3
        """
        #if member == None:
        #    await ctx.respond(
        #        "**You must mention a user to use this command! Or perhaps you want me to kiss you instead...?**"
        #        )
        user_id = ctx.author.id
        hanako_kiss = [
            "<:hk_blush:964948035371163688>",
            "<:hk_kiss:964947590259032109> **Huh? You want me to kiss you?**",
            "<:hk_nothanks:964930571178475520> **I don't think Yashiro would be happy with you kissing me like that...**"
        ]
        self_kiss = [
            f"**<@{user_id}> leans forward to lovingly kiss... their reflection in the mirror in front of them.**",
            f"**<@{user_id}> has decided that self love is important! They give themselves a kiss.**",
            f"**<@{user_id}> kisses one of the many pictures of themselves on their wall. Why do you have all of those, anyways...?**",
            f"**<@{user_id}> wants to kiss themself? I could kiss you instead... <:hk_kiss:964947590259032109>**"
        ]
        kiss_choice = [
            f"**<@{user_id}> places a spell of protection on <@{member.id}> by kissing their cheek.**",
            f"**<@{user_id}> gently kisses <@{member.id}> on the forehead.**",
            f"**<@{user_id}> tries to wake up <@{member.id}> with a good-morning kiss, but accidentally startles them and gets headbutted.**",
            f'**"There are many different kinds of threats, Honorable Number 7!" <@{user_id}> leans in to kiss <@{member.id}> in order to threaten Hanako into helping them. (That was unfair! <:hk_dissapoint:964931557456482404>)**',
            f"**<@{member.id}> has finally gotten the kiss from <@{user_id}> they've been dreaming of... or at least they think, until they wake up.**",
            f"**<@{user_id}> and <@{member.id}> share a sweet, sappy reunion kiss. Aww... <:yn_love:964940266844856340>**",
            f"**Month ⬤, day X... the weather is bright and sunny! Today's big event... <@{member.id}> shares their first kiss with <@{user_id}>!**",
            f"**<@{user_id}> is about to share a kiss with <@{member.id}>, when... <:teru_small:973999293398663279> \"Uhh... Did I... interrupt something?\"**",
            f"**<@{member.id}> had a rough day, but <@{user_id}>'s kiss works like a potion and makes everything better.",
            f"**Oh, look - somebody is under the confession tree... it's <@{user_id}> and <@{member.id}>! Such a cute couple. <:yn_love:964940266844856340>**",
            f"**<@{user_id}> kisses <@{member.id}>. After the sweet, gentle kiss, <@{member.id}> decides to rest on the shoulder of <@{user_id}> as the sun goes down.**",
            f"**<@{user_id}> kisses <@{member.id}> in the middle of the school garden, while Nene jealously looks at them form the bush. <:yn_ehh:964907409502003211>",
            f"**After 5 years of missing each other, <@{user_id}> runs towards <@{member.id}> and gives them a big kiss.",
            f"**<@{user_id}> gives <@{member.id}> a kiss sweeter than Kou's donuts.**",
            f"**🌙 <@{user_id}> and <@{member.id}> kiss as the moon shines brightly. Their kiss lasts forever...**",
            f"**Whenever <@{member.id}> feels sad, they think of the day they received a kiss from <@{user_id}>. The memory always puts a smile on their face.**",
            f"**<@{user_id}> and <@{member.id}> almost kissed each other... when suddenly, <@{user_id}> turns into a Mokke.**",
            f"**<@{user_id}> and <@{member.id}> are kissing under the poring rain, when lightning flashes outside! ⛈️ <@{member.id}> suddenly gets scared and faints unexpectedly...**",
            f"**Somebody pushes <@{member.id}> into <@{user_id}>, causing them to accidentally kiss.**",
            f"**After so long, <@{user_id}> gets an oppertunity and kisses <@{member.id}>. But they're only *very close friends,* right? Right...?**",
            f"**<@{member.id}> receives a kiss from <@{user_id}>. Hey, look - these two got together faster than Hanako and Nene!**",
            f"**<@{user_id}> shares a secret kiss with <@{member.id}>. Shh - Nobody knows about this!**"
        ]
        msg = response(member.id, user_id, hanako_kiss, self_kiss, kiss_choice)
        await ctx.respond(msg)

    @interactions.command()
    @option(
        "member",
        discord.Member,
        description="Leave blank to send a character to cheer you up"
    )
    async def comfort(self, ctx, member: discord.Member=None):
        """
        Send a TBHK character to cheer someone - or you - up!
        """
        if member == None:
            member = ctx.author
        user_id = ctx.author.id

        general_comforts = [
            f"**<:mt_star:964954713705545827> Tiara gives <@{member.id}> a bouquet of flowers! :bouquet:**",
            f"**<:ty_hug:964958594195927041> Tsukasa hugs <@{member.id}> so tight, he squishes out all sadness!**",
            f"**<:mk_hehe:964948970147282986> <@{member.id}> is feeling down. Kou made them some donuts to cheer them up and tightly hugs them.**",
            f"**<:mokke1:965249524346024036> the Mokke bring <@{member.id}> candy (and things they stole from students) to cheer them up.**",
            f"**<:m_happy:964932907548430397> Mei draws a reality where <@{member.id}> is never sad.**",
            f"**<:aa_point:964952748799950879> \"I'm not exactly a fan of scary stories... but I'll tell you as many as you want, <@{member.id}>, if it will help you feel better!\"**",
            f"**<:yn_love:964940266844856340> Yashiro hugs <@{member.id}> to cheer them up. The sweet aroma of strawberries fills the air!**",
            f"**<:mk_fluster:973890909529862144> Kou is on <@{member.id}>'s side! \"If there's anything getting you down... or anything... I hope you'll remember that I'm here for you.\"**",
            f"**<:yn_love:964940266844856340> Nene has hired the Mokke delivery service to deliver <@{member.id}> some homemade muffins to cheer them up!**"
            ]
        other_comforts = general_comforts
        other_comforts.append(f"**<:sn_tired:964940862540877864> Sakura and <@{user_id}> bring out tea for <@{member.id}> to cheer them up.**")
        self_comforts = general_comforts
        self_comforts.append(f"**<:sn_tired:964940862540877864> Sakura brings out tea for <@{member.id}> to cheer them up.**")

        msg = response(member.id, user_id, other_comforts, self_comforts, other_comforts)
        # note to self write specific hanako comforts
        await ctx.respond(msg)

    @interactions.command()
    @option(
        "member",
        discord.Member,
        description="Who are you giving a hug?"
    )
    async def hug(self, ctx, member: discord.Member):
        """
        Give someone a biiiig hug.
        """
        user_id = ctx.author.id
        hanako_hug = [
            f"**<@{user_id}>, you can't hug me! I'm a ghost after all.**",
            f"**<@{user_id}> tries to hug Hanako... they pass right through him, but feel a chill pass through them.**"
        ]
        self_hug = [
            f"**Aww... <@{user_id}>, do you need a hug?**",
            f"**<@{user_id}> wraps their arms around themselves to give themselves a big hug. (Self-love is important!)**",
            f"**<@{user_id}> hugs a life-size plush of themselves. It's kind of cute... maybe?**"
        ]
        hug_choice = [
            f"**<@{user_id}> wraps their arms around <@{member.id}> in a big bear hug.**",
            f"**<@{user_id}> just sent a hug request! Do you accept, <@{member.id}>?**",
            f"**<@{member.id}> nearly falls over after being suprised by a tackle hug from <@{user_id}>.**",
            f"**<@{user_id}> offers warm hugs to comfort <@{member.id}>, gently patting their back. There, there...**",
            f"**<@{member.id}>, there is no escape from <@{user_id}>'s hugs!**",
            f"**<@{user_id}> thinks that it's <@{member.id}> they're hugging, but it's actually just a life-size plush of them.**",
            f"**Surprise hug! <@{user_id}> gives <@{member.id}> a hug from behind them suddenly, startling them a little bit.**",
            f"**<@{user_id}> hugs <@{member.id}> forever and eternally, until the end of time.**",
            f"**Even though <@{user_id}> doesn't like hugs, they make an exception and tightly hug <@{member.id}>.**",
            f"**A gift pops up in front of <@{member.id}>! Let's open it and see what it is... it's <@{user_id}>! They jump out and tightly hug <@{member.id}>.**",
            f"**<@{user_id}> tries to get <@{member.id}>'s attention, but ends up being ignored. Because of that, <@{user_id}> tries to slap <@{member.id}>. However, they realise that they are too cute to be slapped, and so they hug them very tightly instead.**"
        ]
        msg = response(member.id, user_id, hanako_hug, self_hug, hug_choice)
        await ctx.respond(msg)

    @interactions.command()
    @option(
        "member",
        discord.Member,
        description="Your target is..."
    )
    async def kill(self, ctx, member: discord.Member):
        """
        Who are you sending to the far shore?
        """
        user_id = ctx.author.id
        hanako_kill = [
            "**You can't kill me, I'm already dead!**",
            "**I think I'm dying... That was a joke. I'm already dead.**",
            "**WOW, that was scary! I thought I was going to die... Oh, yeah. I died already...**"
        ]
        self_kill = [
            "<:hk_stare:964958157673750650> **Are you okay...? Do you need a hug?**",
            "<:hk_shocked:964913449350070272> **Wait - no, you can't do that. That's illegal!**",
            "<:hn_hug:964907449515647057> **I'm here to listen if you need it...**",
            "<:hk_blush3:964912865746231356> **Don't tell me that it's okay if you die...**"
        ]
        kill_choice = [
            f"**<@{member.id}> gets turned into a donut by <@{user_id}>.**",
            f"**It seems that <@{member.id}> has gotten killed yet another time... Just like a certain someone else we k- Oh... too soon? <:ms_stand:1065241097242161213>**",
            f"<:teru_small:973999293398663279> **<@{member.id}> gets exorcised by Teru and <@{user_id}>. To the Far Shore with you!**",
            f"<:aa_think:964952749181636628> **It seems that <@{member.id}> was chosen as the next kannagi, and is thrown off a cliff.**",
            f"**<:aa_shock:1065244522252091412> Looks like Aoi has a new crush... on <@{member.id}>, who ends up on the wrong end of Akane's bat.**",
            f"**<@{member.id}> stepped on the fourth step of Misaki stairs... You know what happens next!**",
            f"**<@{member.id}> gets made into a tasty meal and is eaten by <@{user_id}>. Yum...?**",
            f"**<:sn_blank:964943466620657694> Sakura and <@{user_id}> invite <@{member.id}> to a very deadly tea party.**"
        ]
        msg = response(member.id, user_id, hanako_kill, self_kill, kill_choice)
        await ctx.respond(msg)

    @interactions.command()
    @option(
        "member",
        discord.Member,
        description="Let's hope the Mokke give this user some candy..."
    )
    async def mokke(self, ctx, member: discord.Member):
        """
        Ask the Mokke to give a user some candy.
        """
        user = ctx.author.mention
        receiver = member.mention

        if member.id == 955611964560777236:
            image_list = [
                "https://i.ibb.co/G9QpQ9X/MD-16.jpg",
                "https://i.ibb.co/MRbz6hz/MD-2.jpg",
                "https://i.ibb.co/VtwgKzj/MD-3.jpg"
                ]
            image = choice(image_list)
            message = "**You don't need to send Mokke to give me candy. I am Mokke.**"

        elif member.id == ctx.author.id:
            image = "https://i.ibb.co/k9VYPh0/mokke-horde.jpg"
            message = "**You shall become one with the Mokke.**"

        else:
            receiver = f"<@{member.id}>"
            image_list = [
                "https://i.ibb.co/nztmgmp/mokkecandy.gif",
                "https://i.ibb.co/D8s2xj6/mokke-candy.png",
                "https://i.ibb.co/1Rdmn3w/mokkelounge.gif",
                "https://i.ibb.co/341QzY0/many-mokke.png", 
                "https://i.ibb.co/8Y7CZTy/mokke-delivery.png",
                "https://i.ibb.co/D49PgZc/mokke-milkshake.png",
                "https://i.ibb.co/wW9xWFv/mokke-hunting.png"
            ]
            image = choice(image_list)
            if image == image_list[0] or image == image_list[1]:
                message_choices = [
                    f'**"Want a candy?" A mokke offers a candy to {receiver}.**',
                    f"**The Mokke are hesitant to share their candy with {receiver}, but decide to be generous.**",
                    f"**{receiver} is handed one lemon-flavored piece of candy. Reject candy is better than nothing...**",
                    f"**The Mokke are willing to give {receiver} as much candy as they want... as long as it's all lemon flavored.**"
                    ]
                message = choice(message_choices)
            elif image == image_list[2] or image == image_list[3]:
                message_choices = [
                    f"**{user} calls for a Mokke to give {receiver} a candy, but the Mokke do as they want.**",
                    f"**The Mokke would give {receiver} candy, but they have already eaten it all themselves...**",
                    f"**{user}'s request to give {receiver} candy somehow isn't heard by the Mokke's disproportionately large ears. (Or maybe it was just ignored...)**"
                    ]
                message = choice(message_choices)
            elif image == image_list[4]:
                message_choices = [
                    f"**Delivery from {user}! It's a package for {receiver} full of candy (and Mokke).**",
                    f"**{receiver} receives a delivery of candy- wait, but the delivery fee needs to be paid in candy? This isn't fair! <:hk_shocked:964913449350070272>**"
                    ]
                message = choice(message_choices)
            elif image == image_list[5]:
                message = f"**The Mokke are out of candy (because they ate it all). However, they still have a milkshake for {receiver} to enjoy.**"
            elif image == image_list[6]:
                message = f"**{user} calls for a Mokke to give {receiver} a candy, but Yako decided to go Mokke hunting.**"
            else:
                message = f"**A Mokke gives a candy to {receiver}!**"
        
        embed = discord.Embed(
            description=message,
            color=discord.Colour.fuchsia(), # Pycord provides a class with default colors you can choose from
        )
        embed.set_image(url=image)
        await ctx.respond(embed=embed)

def setup(bot):
    cog = Interactions(bot)
    bot.add_cog(cog)


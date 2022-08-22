################ THIS CODE IS ARCHIVED. ################
# I do not need this to be in the bot at the moment,   #
# however it is staying in the code in case I need to  #
# use it again.                                        #
########################################################

#import discord
#from random import choice
#from discord.ext import commands
#from discord.ext.commands import bot
#import discord.ext.commands.errors

#from __main__ import HanakoBot

#class Testing(commands.Cog):
#    def __init__(self, bot: HanakoBot):
#        self.bot = bot

#    @commands.command()
#    async def todo(self, ctx):
#        await ctx.send("""**TO DO**
#- make other interaction commands (e.g. +kill)
#- rewatch tbhk and make hug GIFs

#    @commands.command()
#    async def test(self, ctx):
#        image = [
#            r"/home/averyarmstrong/hanakobot/physical_labor.jpg",
#            r"/home/averyarmstrong/hanakobot/peaceout.jpg"
#            ]
#        chosen_image = choice(image)
#        await ctx.send("Huh? What? I'm awake, hello!",
#                    file=discord.File(chosen_image))

#    @test.error
#    async def test_error(self, ctx, error):
#        if isinstance(error, discord.ext.commands.CommandError):
#            await ctx.send("Snzz... Let me go back to sleep. (" 
#            + str(error) + ")")
#
#    @commands.command()
#    async def throwerror(self, ctx):
#        raise NotImplementedError

#    @throwerror.error
#    async def kiss_error(self, ctx, error):
#        if isinstance(error, discord.ext.commands.CommandError):
#            await ctx.send("Uh-oh, Avery made a mistake... (" + str(error) 
#                + ")\nYou can report this error in the HanakoBot test " +
#                "server! https://discord.com/invite/ANb3v6bHvx")

#def setup(bot: HanakoBot):
#    cog = Testing(bot)
#    bot.add_cog(cog)
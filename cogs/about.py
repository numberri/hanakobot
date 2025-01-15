import discord
from discord import option
from discord.ext import commands
from random import choice

class About(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def about(self, ctx):
        """
        More information about the bot!
        """
        gifs = [
            "https://media1.tenor.com/m/Ur9fgrjvYygAAAAC/hanako-kun-hes-spitting-facts.gif",
            "https://media1.tenor.com/m/iL7ztJAxpBAAAAAC/toilet-bound-hanako-kun-spirits.gif",
            "https://media1.tenor.com/m/iL7ztJAxpBAAAAAC/toilet-bound-hanako-kun-spirits.gif",
            "https://media1.tenor.com/m/OBzWJTvRsHsAAAAC/toilet-bound-hanako-kun-hanako-kun.gif",
            "https://media1.tenor.com/m/o_KuULVq01oAAAAC/hanako-kun.gif",
            "https://media1.tenor.com/m/3J1TEeh0gYAAAAAC/jshk-jibaku-shounen-hanako-kun.gif"
        ]
        embed_gif = choice(gifs)
        embed = discord.Embed(
            title="HanakoBot - Pleased to meet you!",
            description="Seventh of Discord's seven mysteries.",
            color=discord.Colour.dark_red(), # Pycord provides a class with default colors you can choose from
        )
        embed.add_field(name="About", value="HanakoBot was created by numberri. If you enjoy the bot, consider adding it to your server, donating on Kofi, or just popping by the support server to say hi!", inline=False)

        embed.add_field(name="Source Code", value="[Github](https://github.com/numberri/hanakobot)", inline=True)
        embed.add_field(name="Kofi", value="[numberri on Kofi](https://ko-fi.com/numberri)", inline=True)
        embed.add_field(name="More info", value="[HanakoBot's Website](https://hanako-bot.carrd.co)", inline=True)
        embed.set_image(url=embed_gif)
        await ctx.respond(embed=embed)

def setup(bot):
    cog = About(bot)
    bot.add_cog(cog)
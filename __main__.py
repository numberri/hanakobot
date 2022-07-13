import discord
from discord.ext import commands
from discord.ext.commands import bot
import discord.ext.commands.errors

class HanakoBot(commands.Bot):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

def __init__(self, bot: HanakoBot):
    self.bot = bot

def main():
    intents = discord.Intents.default()
    allowed_mentions = discord.AllowedMentions(everyone=True, users=True,
                                           roles=False)
    allowed_mentions.replied_user = True
    bot = HanakoBot(
        command_prefix = "+", 
        intents=intents,
        allowed_mentions = discord.AllowedMentions(everyone = False, users = True, 
            roles = False),
        status = discord.Status.online,
        activity = discord.Game(name = "+help | hanako-bot.carrd.co")
        )
    cogs = [
        "interactions",
        "jshk",
        "testing",
        "utility"
    ]
    for cog in cogs:
        bot.load_extension(f"{cog}")
    
    bot.run('OTU1NjExOTY0NTYwNzc3MjM2.YjkM_g.4OMkshGrC0Ml-YflykuVvo4T1Io')
    #todo: change this to use an .env file

main()
#version: 1.0.3

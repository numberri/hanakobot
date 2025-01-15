import discord
import os
from dotenv import load_dotenv


load_dotenv()
bot = discord.Bot(
    activity = discord.Game(name = "New update: now with slash commands!"),
    allowed_mentions = discord.AllowedMentions(everyone=False, users=True, roles=False)
)

token = str(os.getenv("TOKEN"))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

cogs = [
    "about",
    "interactions",
    "tbhk",
    "utility"
]
for cog in cogs:
    bot.load_extension(f"cogs.{cog}")

bot.run(os.getenv('TOKEN'))
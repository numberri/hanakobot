import discord
from discord.ext import commands
from discord.ext.commands import bot
import discord.ext.commands.errors
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = "HanakoKey"
KVUri = f"https://{keyVaultName}.vault.azure.net"
keyname = "hanakobotkey2"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
botkey = client.get_secret(keyname).value

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
        "utility"
    ]
    for cog in cogs:
        bot.load_extension(f"{cog}")
    
    bot.run(botkey)

main()
#version: 1.3.0

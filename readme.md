# HanakoBot: A bot for all things TBHK (and more!)
HanakoBot was made for the Discord server Kamone Garden to provide wholesome, TBHK related interaction commands and to count down to when the next chapter is. From here, it's grown to have more general-purpose commands, and is open for anybody to add to their server!
## Adding the bot to a server
If you want to add the official bot to your server, you can do so [here](https://discord.com/oauth2/authorize?client_id=955611964560777236&permissions=414464724032&scope=bot). I also have a support server where you can check out what the bot does before you add it to a server which can be accessed [here](https://discord.com/invite/ANb3v6bHvx).
## Self hosting the bot
The bot has no offical support for self hosting, but as it has no interactions with databases it is pretty easy! You need to go to the Discord Developer Portal to make an application and bot, and generate a bot token, then make a .env file with the line ```TOKEN = your token here```.

The bot also has these external dependencies, which you will need to install beforehand:
- py-cord
- python-dotenv
- numpy
- datetime
- pytz

## Other information
You can find update history at update_history.md, and information about all commands [on the bot's website](https://hanako-bot.carrd.co/#commands).

This bot is something that I run in my spare time, so if you want to support my work you can [donate through Kofi](https://ko-fi.com/numberri)!
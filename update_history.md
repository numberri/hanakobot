# Update History
## 2.0
- Moves __all commands__ to slash commands, and changes the library from discord.py to py-cord
- Fixes edge cases in /chapter where the release is on a Japanese public holiday or Sunday, and adds a disclaimer that the release date may be irregular on these days and Saturdays
- Optimizes /coinflip - I was unaware that flipping billions of coins was a use case for the bot, but it caused several crashes. Hanako now uses numpy to flip coins, so this won't happen again.
- Adds an option to roll multiple dice with /diceroll, and limited this to 100 dice.
- Fixes parsing errors in /choose
- Removes /remind. This is due to the fact that the command was poorly implemented, and it may come back in the future
- Changes bot token implementation - now uses .env files instead of Azure key vault
- Changes /avatar to provide the user's server-specific avatar if they have one
- Changes /interactions mokke to embed the response
- Adds /anime to track time until Toilet Bound Hanako Kun season 2 episodes air
- Adds /about to provide information about the bot and relevant links

## 1.3
- Adds interaction command +kill
- Small changes to +coin, +diceroll, +remind, +kiss, and +choose

## 1.2
- Adds +avatar
- Small bug fixes in +coinflip and +kiss
- Removed all testing commands - +test, +todo, and +throwerror
- Security fixes in regards to bot token implementation

## 1.1
- Adds more responses to +hug and +kiss
- Adds utility commands +coinflip, +diceroll, and +remind, and the debug command +throwerror
- Splits the bot commands into cogs to improve code readability and categorize commands in +help

## 1.0.3
- Small bug fix in +mokke command
- Adds error handling, when a command goes wrong HanakoBot will send error information

## 1.0.2
- Adds a "playing" status to the bot, showing the +help command and linking to https://hanako-bot.carrd.co
- Adds more responses to +kiss, +comfort, +hug, and +mokke
- Changes formatting for +chapter when the time until the next chapter is less than 1 day

## 1.0.1
- Fixes a small error in bolding to the hug command

## 1.0
- Public release of HanakoBot
- Beginning of tracking updates for HanakoBot
- Released with +chapter, +choose, +comfort, +help, +hug, +kiss, and +mokke, +test, and +todo
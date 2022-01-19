from os import getenv
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

prefixes = ['!j ']
cogs = ['cogs.spaces.spaces', 'cogs.quotes.quotes', 'cogs.stocks.stocks']

bot = commands.Bot(command_prefix=prefixes, description='JarvisBot hurr durr description needed still.')

if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)

@bot.event
async def on_ready():
    """On ready description"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    await bot.register_application_commands()
    
bot.run(TOKEN, reconnect=True)
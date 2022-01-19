import discord
from discord.ext import commands
import json
from random import choice

json_file = 'quotes.json'

class QuotesCog(commands.Cog):
    """Display random quotes from TV shows"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='quote')
    async def quote_lookup(self, ctx, show='', char=''):
        """ : Display a quote from a show
        This command takes 2 arguments. The first is a show, 2nd is a character from that show.
        If you omit the character or show, a random one will be chosen.
        
        Available shows:
            The Office
        Sample usage:
            !j quote "The Office" "Creed Bratton"
            !j quote "The Office"
            !j quote
        """

        quotes = self.open_json_read("cogs/quotes/" + json_file)
        show = show.strip().title()
        char = char.strip().title()
        quote = self.lookup_quote(quotes, show, char)

        embed=discord.Embed(title=quote[1])
        embed.set_author(name=quote[0])
        embed.add_field(name="Season", value=quote[2]["Season"], inline=True)
        embed.add_field(name="Episode", value=quote[2]["Episode"], inline=True)
        embed.set_footer(text=quote[2]["Quote"])

        await ctx.send(embed=embed)



    def open_json_read(self, in_file):

        try:
            with open(in_file, 'r') as read_file:
                quotes = json.load(read_file)
            return quotes
        except FileNotFoundError:
            print("Unable to locate quotes.json.")
            return


    def lookup_quote(self, quotes, show, char):

        # If user didn't specify a show and character
        if show == '':
            show = choice(list(quotes))
            char = choice(list(quotes[show]))
        # Show was specified, but not the character
        elif char == '':
            char = choice(list(quotes[show]))

        quote = choice(list(quotes[show][char]["Quotes"]))
        result = [show, char, quote]

        return result

            


def setup(bot):
    bot.add_cog(QuotesCog(bot))
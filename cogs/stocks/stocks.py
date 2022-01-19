import discord
from discord.ext import commands
from yahoofinancials import YahooFinancials

class Stocks(commands.Cog):
    """Looks up stock tickers"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stock')
    async def print_stock_ticker(self, ctx, ticker, option=''):
        """ : Show a stock ticker
        This command takes 2 arguments. The first is a stock ticker, and 2nd is one of the available arguments below.
        If you omit the 2nd, it will default to current price. The stock ticker is required.
        
        Avaiable arguments:
            []      - Current price
            [ch]    - Change since opening
            [low]   - Daily low
            [high]  - Daily high
        Sample usage:
            !j stock AMD low
            !j stock AMD
        """

        in_ticker = ticker
        ticker = YahooFinancials(ticker)

        if option == "":
            title = "Current Price"
            option = "Current"
            price = ticker.get_current_price()
        elif option == "ch":
            title = "Change Since Opening"
            option = "Change since opening"
            price = f"{round(ticker.get_current_change(), 2)} / {round(ticker.get_current_percent_change() * 100, 2)}%"
        elif option == "low":
            title = "Daily Low"
            option = "Daily low"
            price = ticker.get_daily_low()
        elif option == "high":
            title = "Daily High"
            option = "Daily high"
            price = ticker.get_daily_high()
        else:
            result = "Invalid option. Ticker lookup canceled. Use '!j stock help for assistance."
            await ctx.send(result)
            return

        embed_result = discord.Embed(title=title, description=' ', color=0x00ff00)
        embed_result.add_field(name="Company", value=in_ticker.upper(), inline=True)
        embed_result.add_field(name="Value", value='$' + str(price), inline=True)

        await ctx.send(embed=embed_result)


def setup(bot):
    bot.add_cog(Stocks(bot))
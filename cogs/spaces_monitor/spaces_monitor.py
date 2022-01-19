from os import getenv
from dotenv import load_dotenv
import boto3
import discord
from discord.ext import commands, tasks

class SpacesMonitor(commands.Cog):
    """ Management of lostsons files """

    def __init__(self, bot):
        self.bot = bot
        self.channel = 378001361796857858
        load_dotenv()
        self.SPACES_KEY = getenv('SPACES_KEY')
        self.SPACES_SECRET = getenv('SPACES_SECRET')
        #self.query_spaces.start(bot)

        # Initialize DO-Space connection
        self.spaces_session = boto3.session.Session()
        self.spaces_client = self.spaces_session.client('s3',
                                region_name = 'sfo3',
                                endpoint_url = 'https://sfo3.digitaloceanspaces.com',
                                aws_access_key_id = self.SPACES_KEY,
                                aws_secret_access_key = self.SPACES_SECRET
        )

    @commands.command(name='files')
    async def manual_query_space(self, ctx):
        """ Manual query of lostsons files """
        response = self.spaces_client.list_objects(Bucket='lostsons')
        files = {}
        for obj in response['Contents']:
            files[obj['Key']] = obj['LastModified']

        

        

        await ctx.send(files)

"""
    @tasks.loop(minutes=5.0)
    # TODO: Change query_spaces to only report to channel if it finds a new or missing file.
    # TODO: Add function to manually query space.
    # TODO: Add function to upload/delete?
    async def query_spaces(self, bot):

        response = self.spaces_client.list_objects(Bucket='lostsons')
        files = []
        for obj in response['Contents']:
            files.append(obj['Key'])

        # Get the channel to report changes too
        channel = self.bot.get_channel(self.channel)

        await channel.send(files)


    # Wait for Discord connection before running task
    @query_spaces.before_loop  
    async def before_send(self):
        await self.bot.wait_until_ready()

        return
"""
def setup(bot):
    bot.add_cog(SpacesMonitor(bot))
from redbot.core import commands
import aiohttp


class Quotes(commands.Cog):
    """Random Quotes"""

    async def red_delete_data_for_user(self, **kwargs):
        """ Nothing to delete """
        return

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quotes(self, ctx):
        """Random Qutoes"""
        api = "https://zenquotes.io/api/random"
        async with aiohttp.request("GET", api, headers={"Accept": "application/json"}) as r:
            result = await r.json(content_type=None)
            await ctx.send(f" `{result[0]['q']} - {result[0]['a']}`")
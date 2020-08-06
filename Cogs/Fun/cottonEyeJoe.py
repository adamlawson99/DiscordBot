from discord.ext import commands
import discord
import json
from pathlib import Path
from Bot import constants


class CottonEyeJoe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gif_url = None

    @commands.command(
        name="CottonEyeJoe",
        help="$CottonEyeJoe",
        brief="Summons Cotton Eye Joe to the channel"
    )
    async def cotton_eye_joe(self, ctx: discord.ext.commands.Context):
        if self.gif_url is None:
            path = Path(__file__).parent / "../../Resources/Config.JSON"
            print(path)
            with open(path) as json_file:
                data = json.load(json_file)
                self.gif_url = data['links']['cottonEyeJoe']
        await ctx.send(self.gif_url)
        await ctx.message.delete(delay=1)

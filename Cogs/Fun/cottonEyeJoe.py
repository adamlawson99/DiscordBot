from discord.ext import commands
import discord
from Bot import constants


class CottonEyeJoe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="CottonEyeJoe",
        help="$CottonEyeJoe",
        brief="Summons Cotton Eye Joe to the channel"
    )
    async def cotton_eye_joe(self, ctx: discord.ext.commands.Context):
        await ctx.send(constants.Links.cotton_eye_joe_gif)
        await ctx.message.delete(delay=1)

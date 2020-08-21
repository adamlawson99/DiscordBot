from discord.ext import commands
import discord
import json
from pathlib import Path
from Bot import constants


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="Poll",
        help="$Poll \"poll question\"",
        brief="Creates a poll with 2 choices"
    )
    async def poll(self, ctx : discord.ext.commands.context, question):
        embed = discord.Embed(
            title="{} has created a poll:".format(ctx.message.author),
            description=question,
            color=discord.Color.orange()

        )
        sent = await ctx.message.channel.send(embed=embed)
        await sent.add_reaction('👍')
        await sent.add_reaction('👎')
        await ctx.message.delete(delay=1)



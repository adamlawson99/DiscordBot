import discord
from discord.ext import commands
import re


class DirectMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Enter a user mention followed by a URL pointing an image for the bot to DM "
             "the mentioned user the picture found at the URL",
        brief="Mention a user followed by a URL",
        name="SendImageDM"

    )
    async def send_image_dm(self, ctx, member: discord.Member, url):
        regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\." \
                r"[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)\.(jpg|png|svg)"
        match = re.search(regex, url)
        if match:
            await member.send(url)
            await ctx.message.delete()
        else:
            await ctx.message.channel.send("Please enter a valid url")

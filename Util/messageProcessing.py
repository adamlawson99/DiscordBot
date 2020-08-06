from discord.ext import commands
import re


class MessageProcessing:
    def __init__(self, msg, bot: commands.Bot):
        self.msg = msg
        self.bot = bot

    async def process_message(self):
        match = self.eligible_for_joke()
        if match:
            match_as_list = match.group(0).split()
            word_for_joke = match_as_list[len(match_as_list) - 1]
            response = f"Hi {word_for_joke} I'm dad!"
            await self.msg.channel.send(response)

    def eligible_for_joke(self):
        return re.search(r"I'm \w*|I am \w*", self.msg.content)


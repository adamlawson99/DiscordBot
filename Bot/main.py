import os
import re
import logging

import discord
from discord.ext import commands

from Cogs.Fun import greetings
from Cogs.Messaging import directMessaging
from Cogs.Fun import cottonEyeJoe


from Bot.constants import Config, MODERATION_ROLES
from Bot.bot import Bot

allowed_roles = [discord.Object(id_) for id_ in MODERATION_ROLES]

bot = Bot(
    command_prefix=discord.ext.commands.when_mentioned_or(Config.PREFIX),
    #allowed_mentions=discord.AllowedMentions(everyone=False, roles=allowed_roles)
)

logging.basicConfig(level=logging.DEBUG)


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=Config.GUILD)
    print(
        f'{bot.user} is connected to the guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Night time blue!'
    )


@bot.event
async def on_message(message: discord.message):
    if message.author == bot.user:
        return
    if message.content.startswith("$"):
        await bot.process_commands(message)
    else:
        match = eligible_for_joke(message)
        if match:
            match_as_list = match.group(0).split()
            word_for_joke = match_as_list[len(match_as_list) - 1]
            response = f"Hi {word_for_joke} I'm dad!"
            await message.channel.send(response)


def eligible_for_joke(message):
    return re.search(r"I'm \w*|I am \w*", message.content)


bot.add_cog(greetings.Greetings(bot))
bot.add_cog(directMessaging.DirectMessage(bot))
bot.add_cog(cottonEyeJoe.CottonEyeJoe(bot))

bot.run(Config.TOKEN)

import os
import sys
import re
import logging

import discord
from discord.ext import commands

from Cogs.Fun import greetings
from Cogs.Messaging import directMessaging
from Cogs.Fun import cottonEyeJoe
from Cogs.Fun import poll

from Bot.constants import Config, MODERATION_ROLES
from Bot.bot import Bot

from Util.messageProcessing import MessageProcessing

sys.path.insert(0, '/the/folder/path/name-package/')

allowed_roles = [discord.Object(id_) for id_ in MODERATION_ROLES]

bot = Bot(
    command_prefix=discord.ext.commands.when_mentioned_or(Config.PREFIX),
    # allowed_mentions=discord.AllowedMentions(everyone=False, roles=allowed_roles)
)

logging.basicConfig(level=logging.DEBUG)


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=Config.GUILD)
    print(
        f'{bot.user} is connected to the guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print(bot.get_guild(guild.id).roles)


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
        msg_processor = MessageProcessing(message, bot)
        await msg_processor.process_message()


bot.add_cog(greetings.Greetings(bot))
bot.add_cog(directMessaging.DirectMessage(bot))
bot.add_cog(cottonEyeJoe.CottonEyeJoe(bot))
bot.add_cog(poll.Poll(bot))

bot.run(Config.TOKEN)

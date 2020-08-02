import os
import re
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv
from Cogs import Greetings

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot('$')

logging.basicConfig(level=logging.DEBUG)

client.add_cog(Greetings.Greetings(client))

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    match = eligible_for_joke(message)
    if match:
        match_as_list = match.group(0).split()
        word_for_joke = match_as_list[len(match_as_list) - 1]
        response = f"Hi {word_for_joke} I'm dad!"
        await message.channel.send(response)
    else:
        await client.process_commands(message)


@client.command(
    help="Enter a user mention followed by a URL pointing an image for the bot to DM "
    "the mentioned user the picture found at the URL",
    brief="Mention a user followed by a URL"

)
async def send_image_dm(ctx, member: discord.Member, url):
    regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\." \
            r"[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)\.(jpg|png|svg)"
    match = re.search(regex, url)
    if match:
        await member.send(url)
    else:
        await ctx.message.channel.send("Please enter a valid url")


def eligible_for_joke(message):
    return re.search(r"I'm \w*|I am \w*", message.content)


client.run(TOKEN)

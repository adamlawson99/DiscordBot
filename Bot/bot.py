import discord
import logging
from discord.ext import commands
from Bot.constants import Config


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

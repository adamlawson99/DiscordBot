from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    PREFIX = os.getenv('PREFIX')


class Links:
    cotton_eye_joe_gif = "https://raw.githubusercontent.com/adamlawson99/" \
                         "DiscordBot/master/Resources/Gifs/CottonEyeJoe.gif"


MODERATION_ROLES = [664915698300092436, 402974652843950090]

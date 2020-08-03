from discord.ext import commands
import discord

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.user_count = 0

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member : discord.member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            self.user_count = 0
            await ctx.send("Hello {0.name}~".format(member))
        else:
            if self.user_count <= 5:
                await ctx.send("Hello {0.name}... This feels familiar.".format(member))
            elif self.user_count <= 10:
                await ctx.send("Hello {0.name}... This is getting to be a bit much".format(member))
            else:
                await ctx.send("Hello {0.name}... *Sweats nervously*".format(member))
            self.user_count += 1

        self._last_member = member

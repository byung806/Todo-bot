'''
Get bot latency & ping
'''

import discord
from discord.ext import commands

from util.send_embed import send_embed


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx, *, content=None):
        await send_embed(ctx, 'Pong!', f'**Ping:** {round(self.bot.latency, 2)}ms')

def setup(bot):
    bot.add_cog(Ping(bot))
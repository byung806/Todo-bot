'''
Display the todo-list.
'''

import discord
import json
from discord.ext import commands

from util.get_embed_color import get_embed_color
from data.prefix import PREFIX


class Display(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['list'])
    async def display(self, ctx, *, content=None):
        data = json.load(open('data\\tasks.json', 'r'))
        description = ''
        if str(ctx.message.author.id) in data:
            for task in data[str(ctx.message.author.id)]:
                if data[str(ctx.message.author.id)][task] == True:
                    description += f'<:check:867760636980756500> ~~{task}~~'
                else:
                    description += f'<:cross:868291477808226354> {task}'
                description += '\n'
            if description.rstrip() == '':
                description = 'You have no tasks!'
        else:
            description += 'You have no tasks!'
        embed = discord.Embed(
            description=description.rstrip(),
            color = get_embed_color(ctx.message.author.id)
        ).set_author(name=f'{ctx.message.author.name}\'s todo-list', icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=f'Add a task with `{PREFIX} add <task>`')
        await ctx.message.channel.send(embed=embed)

    @display.error
    async def display_error(self, ctx, error):
        raise error

def setup(bot):
    bot.add_cog(Display(bot))
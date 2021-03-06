'''
Clear all your tasks in your todo-list.
'''

import json

import discord
from discord.ext import commands

from util.generate_embed import generate_embed


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['empty', 'wipe'])
    async def clear(self, ctx, *, content=None):
        data = json.load(open('data\\tasks.json', 'r'))
        if str(ctx.message.author.id) in data:
            await ctx.send(embed=await generate_embed(ctx.message.author, 'Confirmation',
                                                      'Are you sure you want to clear your todo-list? This is **irreversible**.'))
            if (await self.bot.wait_for('message', check=lambda msg: msg.author == ctx.author)).content.lower() in [
                'yes', 'y', 'yup', 'sure', 'ok', 'okay', 'yeah', 'ofc', 'of course']:
                data[str(ctx.message.author.id)] = {}
                json_data = json.dumps(data)
                f = open('data\\tasks.json', 'w')
                f.write(json_data)
                f.close()
                await ctx.send(
                    embed=await generate_embed(ctx.message.author, 'Todo-list cleared', 'Cleared your todo-list!',
                                               color=discord.Color.green()))
            else:
                await ctx.send(
                    embed=await generate_embed(ctx.message.author, 'Not cleared', 'Okay, didn\'t clear your todo-list.',
                                               color=discord.Color.red()))
        else:
            await ctx.send(embed=await generate_embed(ctx.message.author, 'No todo-list',
                                                      'You don\'t have a todo-list! Create one with the `add` command.',
                                                      color=discord.Color.red()))


def setup(bot):
    bot.add_cog(Clear(bot))

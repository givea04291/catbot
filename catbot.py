import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='냥이야')

@bot.event
async def on_ready():
    print('complete')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(os.environ["BOT_TOKEN"])

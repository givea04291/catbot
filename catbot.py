import discord
from discord.ext import commands

client = discord.Bot(command_prefix="냥이야 ")


@client.event
async def on_ready():
    print("ready")

@client.command()
async def 안녕(ctx):
    await ctx.send("nice to meet you")


client.run(os.environ["BOT_TOKEN"])

import discord
import os

from discord import Client

client = discord.Client()
prefix = "냥"


@client.event
async def on_ready():
    print("후아아암~ 잘 잤다냥!")
    game = discord.Game("내가 놀아주러 왔다냥!")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.endswith(f'{prefix} 안녕'):
        await message.channel.send('그래 안녕')

    if message.content.endswith(f'{prefix} 안녕하세요'):
        await message.channel.send('그래 안녕허허허')


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

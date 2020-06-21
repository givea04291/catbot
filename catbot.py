import discord
import os

from discord import Client

client: Client = discord.Client()
prefix = "냥"


@client.event
async def on_ready():
    print("후아아암~ 잘 잤다냥!")
    game = discord.Game("내가 놀아주러 왔다냥!")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content == "냥이야":
        await message.channel.send("")

    if message.content == "f'{prefix}안녕'":
        await message.channel.send("반가워")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

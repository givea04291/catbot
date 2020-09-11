import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('complete')
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await message.channel.send('pong')

client.run(os.environ["BOT_TOKEN"])

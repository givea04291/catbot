import discord

client = discord.Client()


@client.event
async def on_ready():
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("냥이야"):
        await message.channel.send('냥?')


client.run(os.environ["BOT_TOKEN"])

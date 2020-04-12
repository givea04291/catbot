import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("준비 완료다냥!")
    game = discord.Game("인간들 놀아주기")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith(".안녕"):
        await message.channel.send("다음부턴 고양이말로 인사해달라냥")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

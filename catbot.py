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
#인사 and 일상대화
    if message.content.startswith("냥이야 안녕"):
        await message.channel.send("다음부턴 고양이말로 인사해라냥")

    if message.content.startswith("냥이야 안냥"):
        await message.channel.send("반갑다냥!")

    if message.content.startswith("냥이야 반가워"):
        await message.channel.send("나도 반갑다냥")

    if message.content.startswith("냥이야 뭐해"):
        await message.channel.send("할게 없어서 아무것도 안하고있다냥 심심하다냥")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

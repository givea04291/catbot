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
# 목록
    if message.content.startswith("냥이야 목록"):
        await message.channel.send("어떤 목록을 찾는거냥?")
        await message.channel.send("'냥이야 목록이름'으로 알려달라냥")
        await message.channel.send("어떤 목록이 있는지 모르겠다면 '냥이야 목록 명령어목록'을 입력해라냥")
# 인사 및 대화
    if message.content.startswith("냥이야 안녕"):
        await message.channel.send("반갑다냥")
        await message.channel.send("하지만 다음부턴 고양이말로 인사해라냥")

    if message.content.startswith("냥이야 안냥"):
        await message.channel.send("반갑다냥!")

    if message.content.startswith("냥이야 반가워"):
        await message.channel.send("나도 반갑다냥")

    if message.content == "냥이야":
        await message.channel.send("왜부르냥?")
        await message.channel.send("나한테 하고싶은 말이나 물어보고 싶은게 있으면 '냥이야 "할말"'로 입력하라냥")
        await message.channel.send("뭐라고 해야 할지 모르겠다면 '냥이야 목록 명령어목록'를 입력해라냥")




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

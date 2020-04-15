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
# 중1 - 1단원
    if message.content.startswith("냥이야 거듭제곱"):
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/698905428008108073/2e951eacfe5b6cfc.png")
        await message.channel.send("같은 수나 문자를 거듭하여 곱한 것이다냥", embed=embed)

    if message.content.startswith("냥이야 소수"):
        await message.channel.send("소수(素數)는 약수의 개수가 2개인 자연수다냥")
        await message.channel.send("소수(小數)는 0보다 크고 1보다 작은 실수다냥")

    if message.content.startswith("냥이야 합성수"):
        await message.channel.send("약수의 개수가 3개 이상인 자연수, 즉 1보다 큰 자연수 중 소수가 아닌 자연수다냥")

    if message.content.startswith("냥이야 인수"):
        await message.channel.send("어떤 수나 식을 곱하기만으로 표현했을 때 곱해지는 각각의 것들이다냥")

    if message.content.startswith("냥이야 소인수"):
        await message.channel.send("인수 중에서 소수인 것들이다냥")

    if message.content.startswith("냥이야 소인수분해"):
        await message.channel.send("자연수를 소인수들의 곱으로 표현하는 것이다냥")

    if message.content.startswith("냥이야 공약수"):
        await message.channel.send("두 개 이상의 자연수의 공통된 약수다냥")

    if message.content.startswith("냥이야 최대공약수"):
        await message.channel.send("공약수 중 가장 큰 공약수다냥")

    if message.content.startswith("냥이야 서로소"):
        await message.channel.send("공약수가 1뿐인 2개 이상의 자연수, 즉 최대공약수가 1인 자연수들이다냥")

    if message.content.startswith("냥이야 공배수"):
        await message.channel.send("두 개 이상의 자연수의 공통된 배수다냥")

    if message.content.startswith("냥이야 최소공배수"):
        await message.channel.send("공배수 중 가장 작은 공배수다냥")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

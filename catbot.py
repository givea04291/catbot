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
# 중1 - 2단원
    if message.content.startswith("냥이야 양수"):
        await message.channel.send("0보다 큰 실수다냥")

    if message.content.startswith("냥이야 음수"):
        await message.channel.send("0보다 작은 실수다냥")

    if message.content.startswith("냥이야 정수"):
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/699102744669323274/8338200a5fe87fd4.png")
        await message.channel.send("양의 정수, 0, 음의 정수를 통튼 것을 말한다냥", embed=embed)
        
    if message.content.startswith("냥이야 수직선"):
        await message.channel.send("직선에 점을 찍어서 숫자(실수)와 대응시킨 선이다냥")

    if message.content.startswith("냥이야 절댓값"):
        await message.channel.send("수직선 위의 점에 대해 원점으로부터의 거리다냥")
        await message.channel.send("절댓값의 기호는 '||'이다냥")

    if message.content.startswith("냥이야 부등호"):
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/699104938277601381/77ecd8578444a73b.png")
        await message.channel.send("두 수 또는 식의 크기 비교를 할 때 사용하는 수학기호다냥", embed=embed)

    if message.content.startswith("냥이야 덧셈의 교환법칙"):
        await message.channel.send("덧셈의 순서를 바꿔도 결과가 변하지 않는다는 법칙이다냥")

    if message.content.startswith("냥이야 덧셈의 결합법칙"):
        await message.channel.send("덧셈에서 먼저 계산을 하는 순서를 바꿔도 결과가 변하지 않는다는 법칙이다냥")
        
    if message.content.startswith("냥이야 곱셈의 교환법칙"):
        await message.channel.send("곱셈의 순서를 바꿔도 결과가 변하지 않는다는 법칙이다냥")
        
    if message.content.startswith("냥이야 곱셈의 결합법칙"):
        await message.channel.send("곱셈에서 먼저 계산을 하는 순서를 바꿔도 결과가 변하지 않는다는 법칙이다냥")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

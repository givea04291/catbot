import discord
import os

from discord import Client

client: Client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("준비 완료다냥!")
    game = discord.Game("인간들 놀아주기")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    # 기타
    if message.content.startswith("냥이야 원론"):
        await message.channel.send("《유클리드의 원론》(Στοιχεῖα)은 고대 그리스의 수학자 유클리드가 집필한, '세계 최초의 수학 교과서'로 일컬어지는 책이다냥")
        await message.channel.send("원론을 인터넷에서 볼 수 있다냥(영어다냥) : https://mathcs.clarku.edu/~djoyce/java/elements/")
        await message.channel.send("원론을 pdf파일로 다운로드해서 볼 수 있다냥(영어다냥) : "
                                   "https://cdn.discordapp.com/attachments/698830342458703912/699591726549041182"
                                   "/031db884f6b92cdb.pdf")

    # 목록
    if message.content.startswith("냥이야 목록"):
        await message.channel.send("어떤 목록을 찾는거냥?")
        await message.channel.send("'냥이야 목록이름'으로 알려달라냥")
        await message.channel.send("어떤 목록이 있는지 모르겠다면 '냥이야 목록 명령어목록'을 입력해라냥")

    # 공식 - 중1 - 3단원
    if message.content.startswith("냥이야 공식 거리"):
        await message.channel.send("거리 = 속력 × 시간")

    if message.content.startswith("냥이야 공식 속력"):
        await message.channel.send("속력 = 거리 ÷ 시간")

    if message.content.startswith("냥이야 공식 시간"):
        await message.channel.send("시간 = 거리 ÷ 속력")

    if message.content.startswith("냥이야 공식 농도"):
        await message.channel.send("농도 = 용질(소금)의 양/용액(소금물)의 양 × 100(%)")

    if message.content.startswith("냥이야 공식 용질"):
        await message.channel.send("용질(소금) = 농도/100(%) × 용액(소금물)의 양")

    if message.content.startswith("냥이야 공식 소금"):
        await message.channel.send("용질(소금) = 농도/100(%) × 용액(소금물)의 양")

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
        await message.channel.send("나한테 하고싶은 말이나 물어보고 싶은게 있으면 '냥이야 할말'로 입력하라냥")
        await message.channel.send("뭐라고 해야 할지 모르겠다면 '냥이야 목록 명령어목록'을 입력해라냥")

    # 중1 - 1단원
    if message.content.startswith("냥이야 거듭제곱"):
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/698905428008108073/2e951eacfe5b6cfc.png")
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
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/699102744669323274/8338200a5fe87fd4.png")
        await message.channel.send("양의 정수, 0, 음의 정수를 통튼 것을 말한다냥", embed=embed)

    if message.content.startswith("냥이야 수직선"):
        await message.channel.send("직선에 점을 찍어서 숫자(실수)와 대응시킨 선이다냥")

    if message.content.startswith("냥이야 절댓값"):
        await message.channel.send("수직선 위의 점에 대해 원점으로부터의 거리다냥")
        await message.channel.send("절댓값의 기호는 '||'이다냥")

    if message.content.startswith("냥이야 부등호"):
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/699104938277601381/77ecd8578444a73b.png")
        await message.channel.send("두 수 또는 식의 크기 비교를 할 때 사용하는 수학기호다냥", embed=embed)

    if message.content.startswith("냥이야 덧셈의 교환법칙"):
        await message.channel.send("덧셈의 순서를 바꿔도 결과가 변하지 않는다는 법칙이다냥")

    if message.content.startswith("냥이야 덧셈의 결합법칙"):
        await message.channel.send("덧셈에서 먼저 계산을 하는 순서를 바꿔도 결과가 변하지 않는다는 법칙이다냥")

    if message.content.startswith("냥이야 곱셈의 교환법칙"):
        await message.channel.send("곱셈의 순서를 바꿔도 결과가 변하지 않는다는 법칙이다냥")

    if message.content.startswith("냥이야 곱셈의 결합법칙"):
        await message.channel.send("곱셈에서 먼저 계산을 하는 순서를 바꿔도 결과가 변하지 않는다는 법칙이다냥")

    if message.content.startswith("냥이야 분배법칙"):
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/699261160800911410/744c440fbb59e606.png")
        await message.channel.send("괄호 안의 식과 밖의 식을 곱할 때 사용하는 법칙이다냥", embed=embed)

    if message.content.startswith("냥이야 분배법칙"):
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/699261158510559372/a88252ce309c72a3.png")
        await message.channel.send("분배법칙을 직사각형의 넓이로 증명해 보았다냥", embed=embed)

    if message.content.startswith("냥이야 유리수"):
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/699483090866667551/4b8a15bf99fb7928.png")
        await message.channel.send("정수/정수 꼴로 나타낼 수 있는 수다냥", embed=embed)

    # 중1 - 3단원
    if message.content == "냥이야 항":
        await message.channel.send("숫자 또는 문자의 곱으로 이루어진 식이다냥")

    if message.content.startswith("냥이야 상수항"):
        await message.channel.send("항 중애서 숫자로만 이루어져 있는 항을 말한다냥")

    if message.content.startswith("냥이야 계수"):
        await message.channel.send("숫자와 문자의 곱에서 곱해져있는 숫자를 말한다냥")

    if message.content.startswith("냥이야 단항식"):
        await message.channel.send("항 1개로 이루어진 식이다냥")

    if message.content.startswith("냥이야 다항식"):
        await message.channel.send("항 2개 이상으로 이루어진 식이다냥")

    if message.content.startswith("냥이야 차수"):
        await message.channel.send("항에 문자가 곱해진 횟수다냥")
        await message.channel.send("다항식에서는 가장 높은 최고차수가 그 식의 차수가 된다냥")

    if message.content == "냥이야 등식":
        await message.channel.send("등호(=)의 양쪽이 서로 같음을 나타내는 식이다냥")
        await message.channel.send("등호를 기준으로 왼쪽을 좌변, 오른쪽을 우변이라 하고, 이 둘을 통틀어 양변이라 한다냥")

    if message.content.startswith("냥이야 방정식"):
        await message.channel.send("미지수에 따라 참이 되기도 하고 거짓이 되기도 하는 등식이다냥")
        await message.channel.send("방정식을 참으로 만드는 미지수를 그 방정식의 근 또는 해 라고 한다냥")

    if message.content.startswith("냥이야 항등식"):
        await message.channel.send("미지수에 어떤 수를 대입해도 참이 되는 등식이다냥")

    if message.content.startswith("냥이야 등식의 성질"):
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/699981792194592798/954799c69d5129d5.png")
        await message.channel.send("등식의 성질이다냥", embed=embed)

    if message.content.startswith("냥이야 이항"):
        await message.channel.send("항의 부호를 바꾸어 반대쪽 변으로 항을 이동시키는 것이다냥")

    # 중1 - 4단원
    if message.content == "냥이야 좌표":
        await message.channel.send("수직선 또는 좌표평면 위의 한 점에 대응하는 수 또는 순서쌍이다냥")

    if message.content.startswith("냥이야 사분면"):
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/699982808415731752/ca90b9bb665cac64.png")
        await message.channel.send("좌표평면이 좌표축으로 나누어진 네 영역이다냥", embe=embed)

    if message.content.startswith("냥이야 정비례"):
        await message.channel.send("두 변수 x와 y에 대해 x가 2배, 3배, 4배, ...로 변함에 따라 y도 2배, 3배, 4배, ...로 변하는 관계를 말한다냥")

    if message.content.startswith("냥이야 반비례"):
        await message.channel.send("두 변수 x와 y에 대해 x가 2배, 3배, 4배, ...로 변함에 따라 y가 1/2배, 1/3배, 1/4배, ...로 변하는 관계를 말한다냥")

    # 중1 - 5단원
    if message.content == "냥이야 점":
        embed = discord.Embed(title="유클리드의 원론(Στοιχεῖα)에 따르면", color=0x00D8FF)
        embed.add_field(name="제1권 정의 1", value="점은 위치를 갖지만 차원은 없다. 즉 쪼갤 수 없는 것이다.", inline=False)
        embed.add_field(name="제1권 공리 1", value="어떤 점에서 어떤 또다른 점으로 직선을 그릴 수 있다. 따라서, 유한한 직선의 양 끝은 점이다.", inline=False)
        await message.channel.send("크기(부피나 넓이 혹은 길이)가 없고 위치만 있는 도형이다냥", embed=embed)

    if message.content == "냥이야 선":
        await message.channel.send("점들이 연속적으로 움직인 자리를 말한다냥")

    if message.content == "냥이야 면":
        await message.channel.send("선들이 연속적으로 움직인 자리를 말한다냥")

    if message.content.startswith("냥이야 교점"):
        await message.channel.send("선과 선 또는 면과 선이 만나서 생기는 점이다냥")

    if message.content.startswith("냥이야 교선"):
        await message.channel.send("면과 면이 만나서 생기는 선이다냥")

    if message.content.startswith("냥이야 직선"):
        embed = discord.Embed(title="유클리드의 원론(Στοιχεῖα)에 따르면", color=0x00D8FF)
        embed.add_field(name="직선에 대한 공리", value="점이 서로 반대인 두 방향으로 휘지 않고 무한히 뻗어나가는 1차원 도형으로 해석된다", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/699579922745655356"
                            "/2987fd047a61ccfd.png")
        await message.channel.send("곧게 뻗은 선을 추상화한 개념이다냥", embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

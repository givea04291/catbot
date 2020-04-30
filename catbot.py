import discord
import os

from discord import Client

client: Client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("후아아암~ 잘 잤다냥!")
    game = discord.Game("인간들 놀아주기")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    # 기타
    if message.content == "냥이야 원론":
        await message.channel.send("《유클리드의 원론》(Στοιχεῖα)은 고대 그리스의 수학자 유클리드가 집필한, '세계 최초의 수학 교과서'로 일컬어지는 책이다냥")
        await message.channel.send("읽을 수 있다면 읽어봐라냥 : https://mathcs.clarku.edu/~djoyce/java/elements/")

    # 목록
    if message.content == "냥이야 목록":
        await message.channel.send("어떤 목록을 찾는거냥?")
        await message.channel.send("어떤 목록이 있는지 모르겠다면 '냥이야 목록 목록이름'을 입력해라냥")

    # 공식
    if message.content == "냥이야 공식 거리":
        await message.channel.send("거리 = 속력 × 시간")

    if message.content == "냥이야 공식 속력":
        await message.channel.send("속력 = 거리 ÷ 시간")

    if message.content == "냥이야 공식 시간":
        await message.channel.send("시간 = 거리 ÷ 속력")

    if message.content == "냥이야 공식 농도":
        await message.channel.send("농도 = 용질(소금)의 양/용액(소금물)의 양 × 100(%)")

    if message.content == "냥이야 공식 용질":
        await message.channel.send("용질(소금) = 농도/100(%) × 용액(소금물)의 양")

    if message.content == "냥이야 공식 소금":
        await message.channel.send("용질(소금) = 농도/100(%) × 용액(소금물)의 양")

    if message.content == "냥이야 교환법칙":
        await message.channel.send("두 대상의 덧셈과 곱셈의 값이 두 원소의 순서에 관계 없이 같다는 성질이다냥")
        await message.channel.send("집합 S에 대해 연산 ×가 정의되어 있을 때, S의 임의의 두 원소 a, b에 대해 a × b = b × "
                                   "a가 성립하면, 이 연산은 교환법칙을 만족한다냥")

    if message.content == "냥이야 결합법칙":
        await message.channel.send("한 식에서 덧셈 또는 곱셈이 두 번 이상 연속될 때, 앞쪽의 연산을 먼저 계산한 값과 뒤쪽의 연산을 먼저 계산한 결과가 항상 같다는 성질이다냥")
        await message.channel.send("집합 S에 대해 연산 ×가 정의되어 있을 때, S의 임의의 세 원소 a, b, c에 대해 (a × b) × c = "
                                   "a × (b × c)가 성립하면, 이 연산은 결합법칙을 만족한다냥")

    if message.content == "냥이야 분배법칙":
        embed = discord.Embed(description="주어진 집합 S와 S에 대한 두 연산 •와 +에 대해, 만약 연산 •이", color=0x00D8FF)
        embed.add_field(name="S의 임의의 원소 x, y, z에 대해", value="x • (y + z) = (x • y) + (x • z)가 성립하면 연산 •은 연산 +에 대해 "
                                                            "좌분배법칙이 성립한다", inline=False)
        embed.add_field(name="S의 임의의 원소 x, y, z에 대해", value="(y + z) • x = (y • x) + (z • x)가 성립하면 연산 •은 연산 +에 대해 "
                                                            "우분배법칙이 성립한다", inline=False)
        embed.add_field(name="분배법칙", value="연산 +에 대해 좌분배법칙과 우분배법칙이 모두 성립하면 연산 •는 연산 +에 대해 분배법칙이 성립한다", inline=False)
        await message.channel.send(embed=embed)
        await message.channel.send("만약 연산 •에 대해 교환법칙이 성립하면 위의 세 조건은 모두 같은 말이 된다냥")

    # 대화
    if message.content == "냥이야 안녕":
        await message.channel.send("반갑다냥")
        await message.channel.send("하지만 다음부턴 고양이말로 인사해라냥")

    if message.content == "냥이야 안냥":
        await message.channel.send("반갑다냥!")

    if message.content == "냥이야 반가워":
        await message.channel.send("나도 반갑다냥")

    if message.content == "냥이야":
        await message.channel.send("왜부르냥?")
        await message.channel.send("나한테 하고싶은 말이나 물어보고 싶은게 있으면 '냥이야 [할말]'로 입력하라냥")

    if message.content == "냥이야 [할말]":
        await message.channel.send("바보냥?")
        await message.channel.send("할말을 하라는거다냥")

    # 증명
    if message.content == "냥이야 증명 소수":
        embed = discord.Embed(title="소수의 무한함 증명", description="'유클리드의 정리'에 따르면", color=0x8041D9)
        embed.add_field(name="제9권 정리 20", value="유한 개의 소수가 존재한다고 가정하고, 이 유한 개의 소수들을 모두 곱한 값에 1을 더한다. 그 결과값은 다른 어떤 소수로 "
                                                "나누어도 나머지가 1이므로 어떤 소수로도 나누어떨어지지 않는 수가 된다. 따라서 이 수가 소수라면 기존의 최대소수보다 큰 "
                                                "소수가 있다는 것이 증명되고, 이 수가 소수가 아니라고 해도 또다른 소수가 있어야 한다는 것을 의미하기 때문에 소수가 "
                                                "유한하다는 애초 가정에 모순이 존재함을 알 수 있다.", inline=False)
        await message.channel.send(embed=embed)

    if message.content == "냥이야 증명 맞꼭지각":
        embed = discord.Embed(title="유클리드의 원론(Στοιχεῖα)에서", color=0x00D8FF)
        embed.add_field(name="제1권 명제 15", value="두 직선이 한 점에서 만나면 맞꼭지각은 서로 같다", inline=False)
        embed.add_field(name="증명", value="두 직선이 한 점에서 만날 때 생기는 네 개의 각을 각각 ∠A, ∠B, ∠C, ∠D라 할 때, ∠A + ∠D는 평각이므로 180º이고, "
                                         "같은 원리로 ∠A + ∠C = 180º이다. 그러므로 ∠D = 180º - ∠A = ∠C이고, 같은 원리로 ∠A = ∠ B이다",
                        inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/705255540410023978/705255709872226326"
                            "/7f89427ca928c8b7.png")
        await message.channel.send(embed=embed)

    if message.content == "냥이야 증명 평행 동위각":
        embed = discord.Embed(description="서로 다른 평행한 두 직선과 한 직선이 만나 생기는 동위각의 크기는 같으며 그 역도 성립한다", color=0x00D8FF)
        embed.add_field(name="증명", value="평행하는 두 직선 l, m과 만나는 직선이 직선 l과 만나는 점을 점 A, 직선 m과 만나는 점을 점 C라 하고, 점 A, "
                                         "C에서 내린 수선의 "
                                         "발을 각각 점 B, D라 하자. △ABC, △CDA에 대해, □ABCD가 직사각형이므로 선분 BC = 선분 DA, 선분 AB = 선분 "
                                         "CD, ∠ABC = ∠CDA이므로 △ABC ≡ △CDA (SAS합동)이다. 따라서 ∠ACD = ∠CAB이고, ∠CAB와 ∠A는 "
                                         "맞꼭지각이므로 ∠ACD = ∠A, 즉 평행하는 두 직선에 대한 동위각의 크기는 같다.", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/705255540410023978/705255746102755398"
                            "/d399ed151a47d713.png")
        await message.channel.send(embed=embed)

    if message.content == "냥이야 증명 평행 엇각":
        embed = discord.Embed(description="서로 다른 평행한 두 직선과 한 직선이 만나 생기는 엇각의 크기는 같으며 그 역도 성립한다", color=0x00D8FF)
        embed.add_field(name="증명", value="두 직선이 l//m일 때, ∠c = ∠a (동위각), ∠a = ∠b (맞꼭지각), 따라서 ∠c = ∠b이므로 평행하는 두 직선에 대한 엇각의 크기는 같다", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/705255540410023978/705259071766265876/b1767688faeda8b3.png")
        await message.channel.send(embed=embed)

    # 수학
    if message.content == "냥이야 거듭제곱":
        await message.channel.send("주어진 수나 문자를 주어진 횟수만큼 여러 번 곱하는 연산이다냥")

    if message.content == "냥이야 거듭제곱 정수":
        embed = discord.Embed(color=0x00D8FF)
        embed.add_field(name="지수가 0보다 클 때", value="실수 a와 양의 정수 n에 대하여, a의 n제곱은 다음과 같다", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/703903563331665931"
                            "/eca4b2eb71d75388.png")
        await message.channel.send(embed=embed)

        embed = discord.Embed(color=0x00D8FF)
        embed.add_field(name="지수가 0일 때", value="0이 아닌 실수 a에 대하여, a의 0제곱은 다음과 같다 (0의 0제곱은 정의하지 않는다)", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/703904503266541629/0.png")
        await message.channel.send(embed=embed)

        embed = discord.Embed(color=0x00D8FF)
        embed.add_field(name="지수가 0보다 작을 때", value="0이 아닌 실수 a와 음의 정수 -n에 대하여, a의 -n제곱은 다음과 같다", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/703908467630669844"
                            "/9d771c0db725b4c4.png")
        await message.channel.send(embed=embed)

    if message.content == "냥이야 거듭제곱 유리수":
        embed = discord.Embed(description="유리수 지수를 다음과 같다고 한다면", color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/704137292817891348"
                            "/165238191020198b.png")
        embed.set_footer(text="두 정수 m,n은 서로소이고, n은 0보다 크다")
        await message.channel.send(embed=embed)

        embed = discord.Embed(description="음이 아닌 실수 a에 대하여, 이 거듭제곱은 다음과 같이 정의된다냥", color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/704137860139188346"
                            "/2c1c2773a43f9e08.png")
        await message.channel.send(embed=embed)

    if message.content == "냥이야 거듭제곱 실수":
        embed = discord.Embed(description="양의 실수 a와 x에 대하여, a의 x제곱을 다음과 같이 정의한다", color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/704138739210911814"
                            "/4118614901cf5ceb.png")
        embed.set_footer(text="유리수 q가 x에 한없이 가깝다(근사)")
        await message.channel.send(embed=embed)

    if message.content == "냥이야 거듭제곱 복소수":
        await message.channel.send("아...알려주기 싫다냥")
        await message.channel.send("절대 모르는거 아니다냥!")

    if message.content == "냥이야 소수":
        await message.channel.send("소수(素數)는 약수의 개수가 2개인 자연수다냥")
        await message.channel.send("소수(小數)는 0보다 크고 1보다 작은 실수다냥")

    if message.content == "냥이야 합성수":
        await message.channel.send("약수의 개수가 3개 이상인 자연수, 즉 1보다 큰 자연수 중 소수가 아닌 자연수다냥")

    if message.content == "냥이야 인수":
        await message.channel.send("정수 또는 정식을 몇 개의 곱의 꼴로 나타낼 때, 그것의 각 구성요소다냥")

    if message.content == "냥이야 정식":
        await message.channel.send("단항식과 다항식을 총칭해서 정식(整式)이라고 한다냥")

    if message.content == "냥이야 소인수":
        await message.channel.send("인수 중에서 소수인 것들이다냥")

    if message.content == "냥이야 소인수분해":
        await message.channel.send("합성수를 소수의 곱으로 나타내는 방법이다냥")

    if message.content == "냥이야 공약수":
        await message.channel.send("두 개 이상의 자연수의 공통된 약수다냥")

    if message.content == "냥이야 최대공약수":
        await message.channel.send("공약수 중 가장 큰 공약수다냥")

    if message.content == "냥이야 서로소":
        await message.channel.send("공약수가 1뿐인 2개 이상의 자연수, 즉 최대공약수가 1인 자연수들이다냥")

    if message.content == "냥이야 공배수":
        await message.channel.send("두 개 이상의 자연수의 공통된 배수다냥")

    if message.content == "냥이야 최소공배수":
        await message.channel.send("공배수 중 가장 작은 공배수다냥")

    if message.content == "냥이야 양수":
        await message.channel.send("0보다 큰 실수다냥")

    if message.content == "냥이야 음수":
        await message.channel.send("0보다 작은 실수다냥")

    if message.content == "냥이야 정수":
        embed = discord.Embed(description="양의 정수, 0, 음의 정수로 이루어진 수의 체계이다냥", color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/699102744669323274/8338200a5fe87fd4.png")
        await message.channel.send(embed=embed)
        await message.channel.send("정수 전체의 집합은 기호 ℤ를 사용한다냥")

    if message.content == "냥이야 자연수":
        await message.channel.send("수를 셀 때나 순서를 매길 때 사용되는 수를 말하고, 양의 정수라고도 할 수 있다냥")
        await message.channel.send("자연수 전체의 집합은 기호 ℕ을 사용하고, 가장 작은 크기의 무한 집합이다냥")

    if message.content == "냥이야 수직선":
        await message.channel.send("수직선[수ː직썬]은 실수 하나 하나를 점으로 하여 무한히 수평으로 뻗혀있는 직선이다냥")

    if message.content == "냥이야 실직선":
        await message.channel.send("실직선(또는 실수 직선)은 그 위의 점들이 모두 실수인 직선이다냥")
        await message.channel.send("1차원의 유클리드 공간이라고도 할 수 있다냥")

    if message.content == "냥이야 절댓값":
        await message.channel.send("실수가 실직선의 원점과, 복소수가 복소평면의 원점과 떨어진 거리를 나타내는 음이 아닌 실수다냥")
        await message.channel.send("절댓값의 기호는 '||'이다냥")

    if message.content == "냥이야 절댓값 실수":
        embed = discord.Embed(description="실수의 절댓값은 그 실수의 숫자 부분만 남겨두고 부호를 버려 얻는 음이 아닌 실수이다.", color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/704264816461742170"
                            "/4f30a516cb52ec81.png")
        await message.channel.send("실수 x의 절댓값은 다음과 같이 정의된다냥", embed=embed)

        embed = discord.Embed(description="실수에서 절댓값 함수의 그래프다냥", color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/704264223013863474"
                            "/ba76fc5565848a35.png")
        await message.channel.send(embed=embed)

    if message.content == "냥이야 절댓값 복소수":
        embed = discord.Embed(description="복소수 z의 절댓값은 다음과 같이 정의된다냥", color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/704266617470582784"
                            "/fcf3118a1f491733.png")
        embed.set_footer(text="Re z = z의 실수부, Im z = z의 허수부")
        await message.channel.send(embed=embed)

        embed = discord.Embed(description="복소평면 위에서 복소수 z의 절댓값 r", color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/704266646344433714"
                            "/3056f6038ee5dab2.png")
        await message.channel.send(embed=embed)

    if message.content == "냥이야 부등식":
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/704521854546870344/05d0fe05ff8d1061.png")
        await message.channel.send("두 수 및 두 식에 대한 크기 비교를 나타내는 식이다냥", embed=embed)

    if message.content == "냥이야 유리수":
        embed = discord.Embed(description="유리수는 다음과 같이 정의할 수 있다냥", color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/704580507735818290/87c4ec8b77e3523c.png")
        embed.set_footer(text="m, n은 정수이고, n은 0이 아니다")
        await message.channel.send(embed=embed)
        await message.channel.send("유리수체의 기호는 ℚ를 사용한다냥")

    if message.content == "냥이야 항":
        await message.channel.send("다항식을 이루는 각각의 단항식이다냥")

    if message.content == "냥이야 상수항":
        await message.channel.send("변수 또는 미지수를 포함하지 않은 항이다냥")

    if message.content == "냥이야 계수":
        await message.channel.send("변수에 일정하게 곱해진 상수이다냥")

    if message.content == "냥이야 단항식":
        await message.channel.send("하나의 항만으로 이루어진 다항식이다냥")

    if message.content == "냥이야 다항식":
        await message.channel.send("단항식들의 덧셈과 뺄셈으로 이루어진 식이다냥")

    if message.content == "냥이야 차수":
        await message.channel.send("다항식을 어떤 문자에 대해 정리했을 때, 그 문자의 가장 큰 거듭제곱 지수를 그 다항식의 차수라고 한다냥")

    if message.content == "냥이야 등식":
        await message.channel.send("등호 '='를 이용해 둘 이상의 식이 동일한 수학적 대상임을 나타내는 관계식이다냥")

    if message.content == "냥이야 방정식":
        await message.channel.send("미지수가 포함된 식에서, 그 미지수에 특정한 값을 주었을 때만 성립하는 등식이다냥")
        await message.channel.send("방정식을 참으로 만드는 미지수의 값을 그 방정식의 근 또는 해 라고 한다냥")

    if message.content == "냥이야 항등식":
        embed = discord.Embed(color=0x00D8FF)
        embed.add_field(name="1.", value="등식 내부의 특정한 변수가 복소수의 범위에서 어떤 값으로 변하든 항상 참을 만족하는 등식", inline=False)
        embed.add_field(name="2.", value="등식의 양변에서 특정한 문자의  차수에 따른 문자들의 계수가 각각 모두 같은 등식", inline=False)
        await message.channel.send("두가지의 정의가 있다냥", embed=embed)

    if message.content == "냥이야 부정방정식":
        await message.channel.send("항등식은 아니지만 해의 개수가 무한히 많은 방정식이다냥")

    if message.content == "냥이야 등식의 성질":
        await message.channel.send("등식의 양변에 같은 수를 더하거나, 빼거나, 곱하거나, 또는 0이 아닌 같은 수로 나누어도 그 등식은 성립한다는 성질이다냥")

    if message.content == "냥이야 이항":
        await message.channel.send("등식 또는 부등식의 한 변에 있는 항을 그 부호를 바꿔 다른 변으로 옮기는 것이다냥")

    if message.content == "냥이야 좌표":
        await message.channel.send("유클리드 공간에서 점이나 다른 요소를 고유하기 결정하기 위해 사용하는 하나 이상의 숫자이다냥")

    if message.content == "냥이야 사분면":
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/699982808415731752/ca90b9bb665cac64.png")
        await message.channel.send("x축, y축으로 나뉜 좌표평면의 네 부분이다냥", embed=embed)

    if message.content == "냥이야 정비례":
        await message.channel.send("변수 x, y와, 0이 아닌 상수 k에 대해 y = kx를 만족하는 관계")

    if message.content == "냥이야 반비례":
        await message.channel.send("변수 x, y와, 0이 아닌 상수 k에 대해 y = k/x를 만족하는 관계")

    if message.content == "냥이야 점":
        embed = discord.Embed(title="유클리드의 원론(Στοιχεῖα)에 따르면", color=0x00D8FF)
        embed.add_field(name="제1권 정의 1", value="점은 위치를 갖지만 차원은 없다. 즉 쪼갤 수 없는 것이다.", inline=False)
        embed.add_field(name="제1권 공리 1", value="어떤 점에서 어떤 또다른 점으로 직선을 그릴 수 있다. 따라서, 유한한 직선의 양 끝은 점이다.", inline=False)
        await message.channel.send("크기(부피나 넓이 혹은 길이)가 없고 위치만 있는 도형이다냥", embed=embed)

    if message.content == "냥이야 선":
        await message.channel.send("점이 움직여 이루어진 자취이다냥")

    if message.content == "냥이야 면":
        await message.channel.send("다면체를 이루는 평면을 말한다냥")

    if message.content == "냥이야 교점":
        await message.channel.send("선과 선 또는 면과 선이 만나서 생기는 점이다냥")

    if message.content == "냥이야 교선":
        await message.channel.send("면과 면이 만나서 생기는 선이다냥")

    if message.content == "냥이야 직선":
        embed = discord.Embed(title="유클리드의 원론(Στοιχεῖα)에 따르면", color=0x00D8FF)
        embed.add_field(name="직선에 대한 공리", value="점이 서로 반대인 두 방향으로 휘지 않고 무한히 뻗어나가는 1차원 도형으로 해석된다", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/699579922745655356"
                            "/2987fd047a61ccfd.png")
        await message.channel.send("곧게 뻗은 선을 추상화한 개념이다냥", embed=embed)

    if message.content == "냥이야 반직선":
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/699579918563934208/f8cb6a601e9905d8.png")
        await message.channel.send("점 하나에서 시작하여 한 방향으로 무한히 뻗어나가는 선이다냥", embed=embed)

    if message.content == "냥이야 선분":
        embed = discord.Embed(color=0x00D8FF)
        embed.set_image(
            url="https://media.discordapp.net/attachments/698830342458703912/699579920757817364/d609c097c16f1200.png")
        await message.channel.send("양쪽에 끝나는 점이 있는, 직선의 부분이다냥", embed=embed)

    if message.content == "냥이야 중점":
        await message.channel.send("주어진 선분을 같은 길이로 나누는 점을 일컫는다냥")

    if message.content == "냥이야 각":
        await message.channel.send("같은 끝점을 갖는 두 반직선이 이루는 도형이다냥")
        await message.channel.send("기호 ∠를 사용해서 나타내고, 보통 임의의 각을 ∠θ로 표현한다냥")

    if message.content == "냥이야 각도":
        await message.channel.send("각의 두 변이 벌어진 정도를 나타내는 양을 말한다냥")

    if message.content == "냥이야 맞꼭지각":
        await message.channel.send("교차하는 두 직선이 한 점에서 만날 때 생기는 한 쌍의 교각 중 서로 이웃하지 않는 것이다냥")

    if message.content == "냥이야 동위각":
        await message.channel.send("두 직선이 다른 한 직선과 만날 때 각 직선의 같은 쪽에서 이루는 각이다냥")

    if message.content == "냥이야 엇각":
        await message.channel.send("서로 다른 두 직선이 다른 한 직선과 만날 때 생기는 각 중에 두 직선 사이에 마주보고 있는 각에서 두 직선과 만나는 한 직선을 상대로 서로 "
                                   "반대편에 존재하는 각을 말한다냥")

    if message.content == "냥이야 직교":
        await message.channel.send("두 개의 직선(또는 반직선 또는 선분)이 만나 이루는 각이 직각일 때, 두 직선이 직교한다고 한다냥. 기호 ⊥를 사용하여 나타낸다냥. ⊥ㅎㅎ")

    if message.content == "냥이야 수선":
        await message.channel.send("두 개의 직선(또는 반직선 또는 선분)이 직교할 때, 한 직선을 다른 직선의 수선이라고 한다냥")

    if message.content == "냥이야 수선의 발":
        await message.channel.send("직선 위에 있지 않은 점을 지나는 직선이 먼저의 직선과 직교할 때 생기는 교점이다냥")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

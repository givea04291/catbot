import discord
import os

client = discord.Client()
prefix = "냥이야"
suf1 = "이다냥"
suf2 = "다냥"
suf3 = "을 말한다냥"
suf4 = "를 말한다냥"


@client.event
async def on_ready():
    print("후아아암~ 잘 잤다냥!")
    game = discord.Game("내가 놀아주러 왔다냥!")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    # 수학
    if message.content.endswith(f'{prefix} 가감'):
        await message.channel.send('**(1)** 더하거나 뺴는 일, 또는 그렇게 하여 알맞게 맞추는 일'f'{suf1}')
        await message.channel.send('**(2)** 덧셈과 뺄셈을 아울러 이르는 말'f'{suf1}')

    if message.content.endswith(f'{prefix} 가감법'):
        await message.channel.send('**(1)** 덧셈과 뺄셈을 하는 방법.')
        await message.channel.send('**(2)** 두 개 이상의 미지수를 가진 연립 방정식에서 한 미지수의 계수를 곱셈이나 나눗셈을 써서 같게 만든 후, 더하거나 빼어 그 미지수를 '
                                   '없애는 방법.')

    if message.content.endswith(f'{prefix} 가감산'):
        await message.channel.send('덧셈과 뺄셈을 아울러 이르는 말.')

    if message.content.endswith(f'{prefix} 가감소거법'):
        await message.channel.send('두 개 이상의 미지수를 가진 연립방정식에서 한 미지수의 계수를 곱셈이나 나눗셈을 써서 같게 만든 후, 더하거나 빼어 그 미지수를 없애는 방법.')

    if message.content.endswith(f'{prefix} 가감승제'):
        await message.channel.send('덧셈, 뺄셈, 곱셈, 나눗셈을 아울러 이르는 말.')

    if message.content.endswith(f'{prefix} 가감승합제'):
        await message.channel.send('덧셈과 뺄셈과 곱셈을 써서 풀게 되어 있는 문제.')

    if message.content.endswith(f'{prefix} 가감합제'):
        await message.channel.send('덧셈과 뺄셈을 써서 풀게 되어 있는 문제.')

    if message.content.endswith(f'{prefix} 가락꼴'):
        await message.channel.send('밑면이 정사각형인 각뿔.')

    if message.content.endswith(f'{prefix} 가로대'):
        await message.channel.send('좌표 평면에서 가로로 놓인 축.')

    if message.content.endswith(f'{prefix} 가로세로비'):
        await message.channel.send('가로와 세로의 비례.')

    if message.content.endswith(f'{prefix} 가로자리표'):
        await message.channel.send('좌표를 구성하는 수들 가운데에서 가로 방향으로 어떤 점의 위치를 지시하는 좌표.')

    if message.content.endswith(f'{prefix} 가로좌표'):
        await message.channel.send('좌표를 구성하는 수들 가운데에서 가로 방향으로 어떤 점의 위치를 지시하는 좌표.')

    if message.content.endswith(f'{prefix} 가로축'):
        await message.channel.send('좌표 평면에서 가로로 놓인 축.')

    if message.content.endswith(f'{prefix} 가법'):
        await message.channel.send('덧셈을 하는 방법.')

    if message.content.endswith(f'{prefix} 가법정리'):
        await message.channel.send('**(1)** 두 각의 합의 삼각 함수를 각각의 삼각 함수로 나타내는 방법.')
        await message.channel.send('**(2)** 몇 개의 배반 사건 가운데 어떤 사건이 일어날 확률은 각 사건이 일어날 확률의 합과 같다는 정리.')

    if message.content.endswith(f'{prefix} 가법함수'):
        await message.channel.send('등식 *a(x+y)=a(x)+a(y)*를 만족하는 함수.')

    if message.content.endswith(f'{prefix} 가부번개'):
        await message.channel.send('자연수 모임과 1대1로 대응되는 모임 원소의 개수.')

    if message.content.endswith(f'{prefix} 가부번집합'):
        await message.channel.send('자연수 전체의 집합과 일대잉 대응이 이루어지는 집합.')

    if message.content.endswith(f'{prefix} 가분수'):
        await message.channel.send('분자가 분모와 같거나 분모보다 큰 분수.')

    if message.content.endswith(f'{prefix} 가비원리'):
        await message.channel.send('두 개 이상의 비가 서로 같을 때, 각 비는 전항의 합과 후항의 합의 비와 같다는 정리. *a:b=c:d*라면 *(a+c):(b+d)=a:b*이다.')

    if message.content.endswith(f'{prefix} 가비의이'):
        await message.channel.send('두 개 이상의 비가 서로 같을 때, 각 비는 전항의 합과 후항의 합의 비와 같다는 정리. *a:b=c:d*라면 *(a+c):(b+d)=a:b*이다.')

    if message.content.endswith(f'{prefix} 가산'):
        await message.channel.send('**(1)** 덧셈.')
        await message.channel.send('**(2)** 자연수의 집합과 일대일의 대응을 만들 수 있음을 이르는 말.')

    if message.content.endswith(f'{prefix} 가산집합'):
        await message.channel.send('자연수 전체의 집합과 일대일 대응이 이루어지는 집합.')

    if message.content.endswith(f'{prefix} 가설검정'):
        await message.channel.send('가설의 옳고 그름을 통계적인 방법으로 따져 보는 일.')

    if message.content.endswith(f'{prefix} 가수'):
        await message.channel.send('**(1)** 어떤 수나 식에 다른 수나 식을 더할 때에, 더해지는 수나 식.')
        await message.channel.send('**(2)** 상용로그의 값에서 0과 같거나 0보다 크고 1보다 작은 소수.')

    if message.content.endswith(f'{prefix} 가수부'):
        await message.channel.send('상용로그값의 가수 부분.')

    if message.content.endswith(f'{prefix} 가약'):
        await message.channel.send('약분할 수 있음.')

    if message.content.endswith(f'{prefix} 가약분수'):
        await message.channel.send('약분할 수 있는 분수.')

    if message.content.endswith(f'{prefix} 가약분수식'):
        await message.channel.send('약분할 수 있는 분수식.')

    if message.content.endswith(f'{prefix} 가역행렬'):
        await message.channel.send('역행렬을 갖는 행렬. 행렬식의 값이 0이 아닌 행렬이다.')

    if message.content.endswith(f'{prefix} '):
        await message.channel.send('')

    if message.content.endswith(f'{prefix} '):
        await message.channel.send('')

    if message.content.endswith(f'{prefix} '):
        await message.channel.send('')

    if message.content.endswith(f'{prefix} '):
        await message.channel.send('')

    if message.content.endswith(f'{prefix} '):
        await message.channel.send('')

    if message.content.endswith(f'{prefix} '):
        await message.channel.send('')

    if message.content.endswith(f'{prefix} '):
        await message.channel.send('')

    if message.content.endswith(f'{prefix} '):
        await message.channel.send('')


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

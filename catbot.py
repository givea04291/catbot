import discord
import os
import datetime


client = discord.Client()
prefix = "냥이야 정의 "
prefix2 = "냥이야 "

suffix = "이다냥"
suffix2 = "을 말한다냥"
suffix3 = "를 말한다냥"
suffix4 = "냥"
# suffix : 이다. (이다냥) [.]
# suffix2 : 을 말한다. (을 말한다냥) [.]
# suffix3 : 를 말한다. (를 말한다냥) [.]
# suffix4 : . (냥) [.]

# 일상체, (냥체), [사전체]


@client.event
async def on_ready():
    print("후아아암~ 잘 잤다냥!")
    game = discord.Game("내가 놀아주러 왔다냥!")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    # ------------------------------ 필터 ------------------------------

    if message.content.startswith(f'{prefix}씨발'):
        await message.channel.send('라먹어 ㅎㅎ'f'{suffix}')

    if message.content.endswith(f'{prefix}시발'):
        await message.channel.send('[명] 맨 처음 떠나는 것'f'{suffix}')

    if message.content.startswith(f'{prefix}개새끼'):
        await message.channel.send('내가 개로 보여? ㅋ'f'{suffix}')

    if message.content.startswith(f'{prefix}섹스'):
        await message.channel.send('너가 못하는거?'f'{suffix}')

    if message.content.startswith(f'{prefix}벌려'):
        await message.channel.send('넣을게 없잖아...'f'{suffix}')

    if message.content.startswith(f'{prefix}좆까'):
        await message.channel.send('넌 깔 것마저 없잖아'f'{suffix}')

    if message.content.startswith(f'{prefix}애미'):
        await message.channel.send('있거든!'f'{suffix}')

    # ------------------------------ !필터 ------------------------------

    # ------------------------------ 시간 ------------------------------

    if message.content.endswith(f'{prefix2}시간'):
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        day = datetime.datetime.today().day
        hour = datetime.datetime.today().hour
        minute = datetime.datetime.today().minute
        second = datetime.datetime.today().second
        await message.channel.send('지금은 ' + str(year) + '년 ' + str(month) + '월 ' + str(day) + '일 '
                                   + str(hour) + '시 ' + str(minute) + '분 ' + str(second) + '초 이다냥')

    # ------------------------------ !시간 ------------------------------

    # ------------------------------ 기억 ------------------------------

    # ------------------------------ !기억 ------------------------------

    # ------------------------------ 수학 ------------------------------

    if message.content.endswith(f'{prefix}가감'):
        await message.channel.send('**(1)** 더하거나 뺴는 일, 또는 그렇게 하여 알맞게 맞추는 일'f'{suffix}')
        await message.channel.send('**(2)** 덧셈과 뺄셈을 아울러 이르는 말'f'{suffix}')

    if message.content.endswith(f'{prefix}가감법'):
        await message.channel.send('**(1)** 덧셈과 뺄셈을 하는 방법'f'{suffix}')
        await message.channel.send('**(2)** 두 개 이상의 미지수를 가진 연립 방정식에서 한 미지수의 계수를 곱셈이나 나눗셈을 써서 같게 만든 후, 더하거나 빼어 그 미지수를 '
                                   '없애는 방법'f'{suffix}')

    if message.content.endswith(f'{prefix}가감산'):
        await message.channel.send('덧셈과 뺄셈을 아울러 이르는 말'f'{suffix}')

    if message.content.endswith(f'{prefix}가감소거법'):
        await message.channel.send('두 개 이상의 미지수를 가진 연립방정식에서 한 미지수의 계수를 곱셈이나 나눗셈을 써서 같게 만든 후, 더하거나 빼어'
                                   ' 그 미지수를 없애는 방법'f'{suffix}')

    if message.content.endswith(f'{prefix}가감승제'):
        await message.channel.send('덧셈, 뺄셈, 곱셈, 나눗셈을 아울러 이르는 말'f'{suffix}')

    if message.content.endswith(f'{prefix}가감승합제'):
        await message.channel.send('덧셈과 뺄셈과 곱셈을 써서 풀게 되어 있는 문제'f'{suffix}')

    if message.content.endswith(f'{prefix}가감합제'):
        await message.channel.send('덧셈과 뺄셈을 써서 풀게 되어 있는 문제'f'{suffix}')

    if message.content.endswith(f'{prefix}가락꼴'):
        await message.channel.send('밑면이 정사각형인 각뿔'f'{suffix}')

    if message.content.endswith(f'{prefix}가로대'):
        await message.channel.send('좌표 평면에서 가로로 놓인 축'f'{suffix}')

    if message.content.endswith(f'{prefix}가로세로비'):
        await message.channel.send('가로와 세로의 비례'f'{suffix}')

    if message.content.endswith(f'{prefix}가로자리표'):
        await message.channel.send('좌표를 구성하는 수들 가운데에서 가로 방향으로 어떤 점의 위치를 지시하는 좌표'f'{suffix}')

    if message.content.endswith(f'{prefix}가로좌표'):
        await message.channel.send('좌표를 구성하는 수들 가운데에서 가로 방향으로 어떤 점의 위치를 지시하는 좌표'f'{suffix}')

    if message.content.endswith(f'{prefix}가로축'):
        await message.channel.send('좌표 평면에서 가로로 놓인 축'f'{suffix}')

    if message.content.endswith(f'{prefix}가법'):
        await message.channel.send('덧셈을 하는 방법'f'{suffix}')

    if message.content.endswith(f'{prefix}가법정리'):
        await message.channel.send('**(1)** 두 각의 합의 삼각 함수를 각각의 삼각 함수로 나타내는 방법'f'{suffix}')
        await message.channel.send('**(2)** 몇 개의 배반 사건 가운데 어떤 사건이 일어날 확률은 각 사건이 일어날 확률의 합과 같다는 정리'f'{suffix}')

    if message.content.endswith(f'{prefix}가법함수'):
        await message.channel.send('등식 *a(x+y)=a(x)+a(y)*를 만족하는 함수'f'{suffix}')

    if message.content.endswith(f'{prefix}가부번개'):
        await message.channel.send('자연수 모임과 1대1로 대응되는 모임 원소의 개수'f'{suffix}')

    if message.content.endswith(f'{prefix}가부번집합'):
        await message.channel.send('자연수 전체의 집합과 일대잉 대응이 이루어지는 집합'f'{suffix}')

    if message.content.endswith(f'{prefix}가분수'):
        await message.channel.send('분자가 분모와 같거나 분모보다 큰 분수'f'{suffix}')

    if message.content.endswith(f'{prefix}가비원리'):
        await message.channel.send('=가비의 이')

    if message.content.endswith(f'{prefix}가비의이'):
        await message.channel.send('두 개 이상의 비가 서로 같을 때, 각 비는 전항의 합과 후항의 합의 비와 같다는 정리, *a:b=c:d*라면 '
                                   '*(a+c):(b+d)=a:b*'f'{suffix}')

    if message.content.endswith(f'{prefix}가산'):
        await message.channel.send('**(1)** 덧셈'f'{suffix}')
        await message.channel.send('**(2)** 자연수의 집합과 일대일의 대응을 만들 수 있음을 이르는 말'f'{suffix}')

    if message.content.endswith(f'{prefix}가산집합'):
        await message.channel.send('자연수 전체의 집합과 일대일 대응이 이루어지는 집합'f'{suffix}')

    if message.content.endswith(f'{prefix}가설검정'):
        await message.channel.send('가설의 옳고 그름을 통계적인 방법으로 따져 보는 일'f'{suffix}')

    if message.content.endswith(f'{prefix}가수'):
        await message.channel.send('**(1)** 어떤 수나 식에 다른 수나 식을 더할 때에, 더해지는 수나 식'f'{suffix}')
        await message.channel.send('**(2)** 상용로그의 값에서 0과 같거나 0보다 크고 1보다 작은 소수'f'{suffix}')

    if message.content.endswith(f'{prefix}가수부'):
        await message.channel.send('상용로그값의 가수 부분'f'{suffix}')

    if message.content.endswith(f'{prefix}가약'):
        await message.channel.send('약분할 수 있음'f'{suffix2}')

    if message.content.endswith(f'{prefix}가약분수'):
        await message.channel.send('약분할 수 있는 분수'f'{suffix}')

    if message.content.endswith(f'{prefix}가약분수식'):
        await message.channel.send('약분할 수 있는 분수식'f'{suffix}')

    if message.content.endswith(f'{prefix}가역행렬'):
        await message.channel.send('역행렬을 갖는 행렬, 행렬식의 값이 0이 아닌 행렬'f'{suffix}')

    if message.content.endswith(f'{prefix}가우스곡선'):
        await message.channel.send('오차의 분포 상태를 나타낸다고 인정되는 곡선'f'{suffix}')

    if message.content.endswith(f'{prefix}가우스분포'):
        await message.channel.send('도수분포곡선이 평균값을 중앙으로 하여 좌우 대칭으로 종모양을 이루는 분포'f'{suffix3}')

    if message.content.endswith(f'{prefix}가우스기호'):
        await message.channel.send('실수 *x*에 대하여 *x*를 넘지 않는 최대의 정수를 뜻하는 기호로, []로 나타낸다'f'{suffix4}')

    if message.content.endswith(f'{prefix}가우스평면'):
        await message.channel.send('복소수를 평면에 나타낼 때 x축에 실숫값, y축에 허숫값을 나타낸 가상의 평면'f'{suffix}')

    if message.content.endswith(f'{prefix}가일배법'):
        await message.channel.send('1, 2, 4, 8, 16, ……과 같이 1에서 시작하여 차차 배로 늘려 가는 계산법'f'{suffix}')

    if message.content.endswith(f'{prefix}가정'):
        await message.channel.send('**(1)** 결론에 앞서 논리의 근거로 어떤 조건이나 전제를 내세움'f'{suffix2}')
        await message.channel.send('**(2)** 정리에서, 어떤 조건을 임시로 내세움, 또는 그 조건'f'{suffix2}')

    if message.content.endswith(f'{prefix}가제'):
        await message.channel.send('덧셈과 나눗셈을 아울러 이르는 말'f'{suffix}')

    if message.content.endswith(f'{prefix}가중산술평균'):
        await message.channel.send('=가중평균')

    if message.content.endswith(f'{prefix}가중평균'):
        await message.channel.send('각 항의 수치에 그 중요도에 비례하는 계수를 곱한 다음 산출한 평균'f'{suffix}')

    if message.content.endswith(f'{prefix}가측값'):
        await message.channel.send('일이 끝난 뒤에 실제로 헤아릴 수 있는 수치'f'{suffix3}')

    if message.content.endswith(f'{prefix}가측치'):
        await message.channel.send('=가측값'f'{suffix3}')

    if message.content.endswith(f'{prefix}가평균'):
        await message.channel.send('자료의 수가 많은 경우의 평균을 구할 때에, 간단하게 계산하기 위하여 임의로 정한 평균값'f'{suffix}')

    if message.content.endswith(f'{prefix}가환'):
        await message.channel.send('연산의 순서를 바꾸어도 그 결과가 변하지 않는 일'f'{suffix2}')

    if message.content.endswith(f'{prefix}가환군'):
        await message.channel.send('임의의 두 원소의 연산에서 자리를 바꾸어도 연산값이 변하지 않는 군'f'{suffix}')

    if message.content.endswith(f'{prefix}가환율'):
        await message.channel.send('덧셈이나 곱셈에서 그 수의 자리를 바꾸어도 결과가 변함이 없어 교환 관계가 성립하는 법칙'f'{suffix}')

    if message.content.endswith(f'{prefix}가환환'):
        await message.channel.send('곱셈에 관한 교환 법칙이 성립하는 환'f'{suffix}')

    if message.content.endswith(f'{prefix}각'):
        await message.channel.send('**(1)** =각도')
        await message.channel.send('**(2)** 한 점에서 나간 두 개의 반직선이 이루는 도형'f'{suffix}')

    if message.content.endswith(f'{prefix}각곁수'):
        await message.channel.send('직선의 방정식의 기울기'f'{suffix}')

    if message.content.endswith(f'{prefix}각기둥'):
        await message.channel.send('옆면은 한 직선에 평행하는 세 개 이상의 평면으로, 밑면은 이 직선과 만나는 두 개의 평행한 평면으로 둘러싸인 다면체'f'{suffix}')

    if message.content.endswith(f'{prefix}각대'):
        await message.channel.send('=각뿔대')

    if message.content.endswith(f'{prefix}각도'):
        await message.channel.send('한 점에서 갈리어 나간 두 직선의 벌어진 정도'f'{suffix3}')

    if message.content.endswith(f'{prefix}각변형'):
        await message.channel.send('도형의 두 선분이 이루는 각의 변화'f'{suffix}')

    if message.content.endswith(f'{prefix}각뿔'):
        await message.channel.send('다각형의 각 변을 밑변으로 하고, 다각형의 평면 밖의 한 점을 공통의 꼭짓점으로 하는 여러개의 삼각형으로 둘러싸인 다면체'f'{suffix}')

    if message.content.endswith(f'{prefix}각뿔대'):
        await message.channel.send('각뿔을 그 밑변에 평행하는 평면으로 잘라 꼭짓점이 있는 부분을 없애고 남은 부분으로 이루어진 입체'f'{suffix3}')

    if message.content.endswith(f'{prefix}각점'):
        await message.channel.send('특이점의 하나로, 곡선 위 각 점의 접선이 어떤 점에서 불연속적으로 방향을 바꿀 때의 그 점'f'{suffix2}')

    if message.content.endswith(f'{prefix}각형'):
        await message.channel.send('=사각형')

    if message.content.endswith(f'{prefix}간승법'):
        await message.channel.send('곱셈을 쉽게 하는 방법'f'{suffix2}')

    if message.content.endswith(f'{prefix}간약률'):
        await message.channel.send('공통 인자로 간단하게 약분하는 법칙'f'{suffix}')

    if message.content.endswith(f'{prefix}간접조사'):
        await message.channel.send('통계 조사에서, 다른 목적을 위하여 작성된 기존 자료를 이용하거나 전문가와의 인터뷰를 통하여 이루어지는 조사 방법'f'{suffix}')

    if message.content.endswith(f'{prefix}간접측정'):
        await message.channel.send('측정량과 일정한 관계가 있는 몇 개의 양을 측정함으로써 구하고자 하는 측정값을 간접적으로 유도해 내는 일'f'{suffix2}')

    if message.content.endswith(f'{prefix}간제법'):
        await message.channel.send('나눗셈을 쉽게 하는 방법'f'{suffix2}')

    if message.content.endswith(f'{prefix}간편셈'):
        await message.channel.send('계산을 쉽고 편하게 하는 방법'f'{suffix2}')

    if message.content.endswith(f'{prefix}감법'):
        await message.channel.send('=뺄셈법')

    if message.content.endswith(f'{prefix}감법기호'):
        await message.channel.send('=뺄셈 부호')

    if message.content.endswith(f'{prefix}감산'):
        await message.channel.send('=뺄셈')

    if message.content.endswith(f'{prefix}감산부호'):
        await message.channel.send('=뺄셈 부호')

    if message.content.endswith(f'{prefix}감소수열'):
        await message.channel.send('수열 *a1, a2, a3*, ……에서 항의 값이 점점 작아지는 수열. 항의 값이 커지지 않는 수열을 포함해서 이를 때도 있다'f'{suffix4}')

    if message.content.endswith(f'{prefix}감소함수'):
        await message.channel.send('독립 변수의 값이 커질수록 이에 대응하는 함숫값이 작아지는 함수'f'{suffix}')

    if message.content.endswith(f'{prefix}값'):
        await message.channel.send('하나의 글자나 식이 취하는 수, 또는 그런 수치'f'{suffix3}')

    if message.content.endswith(f'{prefix}'):
        await message.channel.send(''f'{suffix}')

    # ------------------------------ !수학 ------------------------------


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

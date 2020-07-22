import discord
import os
import datetime
import random


client = discord.Client()


@client.event
async def on_ready():
    print("후아아암~ 잘 잤다냥!")
    game = discord.Game("내가 놀아주러 왔다냥!")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    # ------------------------------ 랜덤 ------------------------------

    if message.content.startswith("냥이야 주사위"):
        roll = message.content.split(" ")
        rolld = roll[2]
        dice = random.randint(1, int(rolld))
        await message.channel.send('정' + str(rolld) + '면체 주사위를 굴려서 ' + str(dice) + '이(가) 나왔다냥')

    if message.content.startswith('냥이야 골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(2, len(choice)-1)
        choiceresult = choice[choicenumber]
        await message.channel.send(choiceresult)

    if message.content.endswith('냥이야 애니추천'):
        ani = "해피슈가라이프 코바야시네메이드드래곤 혈계전선 중2병이라도사랑하고싶어 데이트어라이브 지박소년하나코군 귀멸의칼날 소드아트온라인 너의이름은 목소리의형태 날씨의아이 진격의거인 늑대아이 " \
              "니세코이 역시내청춘러브코메디는잘못됐다 오버로드 방패용사성공담 아픈건싫으므로방어력에올인하려고합니다 기숙학교의줄리엣 전생했더니슬라임이었던건에대해여 이세계콰르텟 유녀전기 무장소녀베키알리즘 " \
              "살육의천사 노게임노라이프 케이온 나의히어로아카데미아 원펀맨 카구야님은고백받고싶어 여성향게임의파멸플래그밖에없는악역앵애로환생해버렸다 데스마치에서시작되는이세계광상곡 다윈즈게임 " \
              "악마에입문했습니다이루마군 이세계마왕과소환소녀 리제로부터시작하는이세계생활 도쿄구울 변변찮은마술강사와금기교전 이세계는스마트폰과함께 어서오세요실력지상주의교실에 토리코 " \
              "던전에서만남을추구하면안되는걸까 현자의손자 흔해빠진직업으로세계최강 기생수 낙제기사의영웅담 게이머즈 청춘돼지는바니걸선배의꿈을꾸지않는다 유라기장의유우나 시원찮은그녀를위한육성방법 5등분의신부 "\
              "어쌔신즈프라이드 알바뛰는마왕님 저능력은평균치로해달라고했잖아요 종말의세라프 마왕님리트라이 암살교실 우에노선배는서툴러 하울의움직이는성 센과치히로의행방불명 토토로 원피스 도우미여우센코씨 " \
              "노라가미 이과가사랑에빠졌기에증명해봤다 내여동생이이렇거귀여울리없어 나는친구가적다 러브라이브 4월은너의거짓말 월간순정노자키군 트리니티세븐 주문은토끼입니까 달링인더프랑키스 " \
              "스노하라장의관리인씨 뱅드림 벽람항로 카쿠시고토 경계의저편 듀라라라 길티크라운 골든타임 마탄의왕과바나디스 스트라이크더블러드 사이키쿠스오의재난 식극의소마 NEWGAME 그랑블루 " \
              "일반공격이전체공격에2회인엄마는좋아하세요 내옆에암흑파괴신이있습니다 무직전생이세계에갔으면최선을다한다 사이코패스"
        anichoice = ani.split(" ")
        aninumber = random.randint(1, len(anichoice))
        aniresult = anichoice[aninumber - 1]
        say = " 한 번 봐보라냥/ 추천한다냥"
        saychoice = say.split("/")
        saynumber = random.randint(1, 2)
        sayresult = saychoice[saynumber - 1]
        await message.channel.send(aniresult + sayresult)

    if message.content.endswith('냥이야 게임추천'):
        game = "오버워치 오수 배틀그라운드 마인크래프트 리그오브레전드 얼불춤 발로란트 테라리아 데스티니가디언즈 GTA 오리와눈먼숲 오리와도깨비불 레포데 데바데 서브노티카 스타크래프트 얼불춤" \
               "슬라임랜처 시티즈스카이라인"
        gamechoice = game.split(" ")
        gamenumber = random.randint(1, len(gamechoice))
        gameresult = gamechoice[gamenumber - 1]
        say = " 한 번 해보라냥/ 추천한다냥/ 같이 해보자냥"
        saychoice = say.split("/")
        saynumber = random.randint(1, 3)
        sayresult = saychoice[saynumber - 1]
        await message.channel.send(gameresult + sayresult)

    # ------------------------------ !랜덤 ------------------------------

    # ------------------------------ 시간 ------------------------------

    if message.content.endswith('냥이야 시간'):
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        day = datetime.datetime.today().day
        hour = datetime.datetime.today().hour
        minute = datetime.datetime.today().minute
        second = datetime.datetime.today().second
        await message.channel.send('지금은 ' + str(year) + '년 ' + str(month) + '월 ' + str(day) + '일 '
                                   + str(hour) + '시 ' + str(minute) + '분 ' + str(second) + '초다냥')

    if message.content.startswith('냥이야 몇년'):
        year = datetime.datetime.today().year
        await message.channel.send(str(year) + '년이다냥')

    if message.content.startswith('냥이야 몇월'):
        month = datetime.datetime.today().month
        await message.channel.send(str(month) + '월이다냥')

    if message.content.startswith('냥이야 몇일'):
        day = datetime.datetime.today().day
        await message.channel.send(str(day) + '일이다냥')

    if message.content.startswith('냥이야 몇시'):
        hour = datetime.datetime.today().hour
        await message.channel.send(str(hour) + '시다냥')

    if message.content.startswith('냥이야 몇분'):
        minute = datetime.datetime.today().minute
        await message.channel.send(str(minute) + '분이다냥')

    if message.content.startswith('냥이야 몇초'):
        second = datetime.datetime.today().second
        await message.channel.send(str(second) + '초... ' + str(second+1) + '초.. 지나가버렸다냥')

    # ------------------------------ !시간 ------------------------------

    # ------------------------------ 수학 ------------------------------

    if message.content.endswith('냥이야 가감'):
        await message.channel.send('**(1)** 더하거나 빼는 일, 또는 그렇게 하여 알맞게 맞추는 일이다냥')
        await message.channel.send('**(2)** 덧셈과 뺄셈을 아울러 이르는 말이다냥')

    if message.content.endswith('냥이야 가감법'):
        await message.channel.send('**(1)** 덧셈과 뺄셈을 하는 방법이다냥')
        await message.channel.send('**(2)** 두 개 이상의 미지수를 가진 연립 방정식에서 한 미지수의 계수를 곱셈이나 나눗셈을 써서 같게 만든 후, 더하거나 빼어 그 미지수를 '
                                   '없애는 방법이다냥')

    if message.content.endswith('냥이야 가감산'):
        await message.channel.send('덧셈과 뺄셈을 아울러 이르는 말이다냥')

    if message.content.endswith('냥이야 가감소거법'):
        await message.channel.send('두 개 이상의 미지수를 가진 연립방정식에서 한 미지수의 계수를 곱셈이나 나눗셈을 써서 같게 만든 후, 더하거나 빼어'
                                   ' 그 미지수를 없애는 방법이다냥')

    if message.content.endswith('냥이야 가감승제'):
        await message.channel.send('덧셈, 뺄셈, 곱셈, 나눗셈을 아울러 이르는 말이다냥')

    if message.content.endswith('냥이야 가감승합제'):
        await message.channel.send('덧셈과 뺄셈과 곱셈을 써서 풀게 되어 있는 문제이다냥')

    if message.content.endswith('냥이야 가감합제'):
        await message.channel.send('덧셈과 뺄셈을 써서 풀게 되어 있는 문제이다냥')

    if message.content.endswith('냥이야 가락꼴'):
        await message.channel.send('밑면이 정사각형인 각뿔이다냥')

    if message.content.endswith('냥이야 가로대'):
        await message.channel.send('좌표 평면에서 가로로 놓인 축이다냥')

    if message.content.endswith('냥이야 가로세로비'):
        await message.channel.send('가로와 세로의 비례이다냥')

    if message.content.endswith('냥이야 가로자리표'):
        await message.channel.send('좌표를 구성하는 수들 가운데에서 가로 방향으로 어떤 점의 위치를 지시하는 좌표이다냥')

    if message.content.endswith('냥이야 가로좌표'):
        await message.channel.send('좌표를 구성하는 수들 가운데에서 가로 방향으로 어떤 점의 위치를 지시하는 좌표이다냥')

    if message.content.endswith('냥이야 가로축'):
        await message.channel.send('좌표 평면에서 가로로 놓인 축이다냥')

    if message.content.endswith('냥이야 가법'):
        await message.channel.send('덧셈을 하는 방법이다냥')

    if message.content.endswith('냥이야 가법정리'):
        await message.channel.send('**(1)** 두 각의 합의 삼각 함수를 각각의 삼각 함수로 나타내는 방법이다냥')
        await message.channel.send('**(2)** 몇 개의 배반 사건 가운데 어떤 사건이 일어날 확률은 각 사건이 일어날 확률의 합과 같다는 정리이다냥')

    if message.content.endswith('냥이야 가법함수'):
        await message.channel.send('등식 *a(x+y)=a(x)+a(y)*를 만족하는 함수이다냥')

    if message.content.endswith('냥이야 가부번개'):
        await message.channel.send('자연수 모임과 1대1로 대응되는 모임 원소의 개수이다냥')

    if message.content.endswith('냥이야 가부번집합'):
        await message.channel.send('자연수 전체의 집합과 일대잉 대응이 이루어지는 집합이다냥')

    if message.content.endswith('냥이야 가분수'):
        await message.channel.send('분자가 분모와 같거나 분모보다 큰 분수이다냥')

    if message.content.endswith('냥이야 가비원리'):
        await message.channel.send('=가비의 이')

    if message.content.endswith('냥이야 가비의이'):
        await message.channel.send('두 개 이상의 비가 서로 같을 때, 각 비는 전항의 합과 후항의 합의 비와 같다는 정리, *a:b=c:d*라면 '
                                   '*(a+c):(b+d)=a:b*이다냥')

    if message.content.endswith('냥이야 가산'):
        await message.channel.send('**(1)** 덧셈이다냥')
        await message.channel.send('**(2)** 자연수의 집합과 일대일의 대응을 만들 수 있음을 이르는 말이다냥')

    if message.content.endswith('냥이야 가산집합'):
        await message.channel.send('자연수 전체의 집합과 일대일 대응이 이루어지는 집합이다냥')

    if message.content.endswith('냥이야 가설검정'):
        await message.channel.send('가설의 옳고 그름을 통계적인 방법으로 따져 보는 일이다냥')

    if message.content.endswith('냥이야 가수'):
        await message.channel.send('**(1)** 어떤 수나 식에 다른 수나 식을 더할 때에, 더해지는 수나 식이다냥')
        await message.channel.send('**(2)** 상용로그의 값에서 0과 같거나 0보다 크고 1보다 작은 소수이다냥')

    if message.content.endswith('냥이야 가수부'):
        await message.channel.send('상용로그값의 가수 부분이다냥')

    if message.content.endswith('냥이야 가약'):
        await message.channel.send('약분할 수 있음을 말한다냥')

    if message.content.endswith('냥이야 가약분수'):
        await message.channel.send('약분할 수 있는 분수이다냥')

    if message.content.endswith('냥이야 가약분수식'):
        await message.channel.send('약분할 수 있는 분수식이다냥')

    if message.content.endswith('냥이야 가역행렬'):
        await message.channel.send('역행렬을 갖는 행렬, 행렬식의 값이 0이 아닌 행렬이다냥')

    if message.content.endswith('냥이야 가우스곡선'):
        await message.channel.send('오차의 분포 상태를 나타낸다고 인정되는 곡선이다냥')

    if message.content.endswith('냥이야 가우스분포'):
        await message.channel.send('도수분포곡선이 평균값을 중앙으로 하여 좌우 대칭으로 종모양을 이루는 분포를 말한다냥')

    if message.content.endswith('냥이야 가우스기호'):
        await message.channel.send('실수 *x*에 대하여 *x*를 넘지 않는 최대의 정수를 뜻하는 기호로, []로 나타낸다냥')

    if message.content.endswith('냥이야 가우스평면'):
        await message.channel.send('복소수를 평면에 나타낼 때 x축에 실숫값, y축에 허숫값을 나타낸 가상의 평면이다냥')

    if message.content.endswith('냥이야 가일배법'):
        await message.channel.send('1, 2, 4, 8, 16, ……과 같이 1에서 시작하여 차차 배로 늘려 가는 계산법이다냥')

    if message.content.endswith('냥이야 가정'):
        await message.channel.send('**(1)** 결론에 앞서 논리의 근거로 어떤 조건이나 전제를 내세움을 말한다냥')
        await message.channel.send('**(2)** 정리에서, 어떤 조건을 임시로 내세움, 또는 그 조건을 말한다냥')

    if message.content.endswith('냥이야 가제'):
        await message.channel.send('덧셈과 나눗셈을 아울러 이르는 말이다냥')

    if message.content.endswith('냥이야 가중산술평균'):
        await message.channel.send('=가중평균')

    if message.content.endswith('냥이야 가중평균'):
        await message.channel.send('각 항의 수치에 그 중요도에 비례하는 계수를 곱한 다음 산출한 평균이다냥')

    if message.content.endswith('냥이야 가측값'):
        await message.channel.send('일이 끝난 뒤에 실제로 헤아릴 수 있는 수치를 말한다냥')

    if message.content.endswith('냥이야 가측치'):
        await message.channel.send('=가측값를 말한다냥')

    if message.content.endswith('냥이야 가평균'):
        await message.channel.send('자료의 수가 많은 경우의 평균을 구할 때에, 간단하게 계산하기 위하여 임의로 정한 평균값이다냥')

    if message.content.endswith('냥이야 가환'):
        await message.channel.send('연산의 순서를 바꾸어도 그 결과가 변하지 않는 일을 말한다냥')

    if message.content.endswith('냥이야 가환군'):
        await message.channel.send('임의의 두 원소의 연산에서 자리를 바꾸어도 연산값이 변하지 않는 군이다냥')

    if message.content.endswith('냥이야 가환율'):
        await message.channel.send('덧셈이나 곱셈에서 그 수의 자리를 바꾸어도 결과가 변함이 없어 교환 관계가 성립하는 법칙이다냥')

    if message.content.endswith('냥이야 가환환'):
        await message.channel.send('곱셈에 관한 교환 법칙이 성립하는 환이다냥')

    if message.content.endswith('냥이야 각'):
        await message.channel.send('**(1)** =각도')
        await message.channel.send('**(2)** 한 점에서 나간 두 개의 반직선이 이루는 도형이다냥')

    if message.content.endswith('냥이야 각곁수'):
        await message.channel.send('직선의 방정식의 기울기이다냥')

    if message.content.endswith('냥이야 각기둥'):
        await message.channel.send('옆면은 한 직선에 평행하는 세 개 이상의 평면으로, 밑면은 이 직선과 만나는 두 개의 평행한 평면으로 둘러싸인 다면체이다냥')

    if message.content.endswith('냥이야 각대'):
        await message.channel.send('=각뿔대')

    if message.content.endswith('냥이야 각도'):
        await message.channel.send('한 점에서 갈리어 나간 두 직선의 벌어진 정도를 말한다냥')

    if message.content.endswith('냥이야 각변형'):
        await message.channel.send('도형의 두 선분이 이루는 각의 변화이다냥')

    if message.content.endswith('냥이야 각뿔'):
        await message.channel.send('다각형의 각 변을 밑변으로 하고, 다각형의 평면 밖의 한 점을 공통의 꼭짓점으로 하는 여러개의 삼각형으로 둘러싸인 다면체이다냥')

    if message.content.endswith('냥이야 각뿔대'):
        await message.channel.send('각뿔을 그 밑변에 평행하는 평면으로 잘라 꼭짓점이 있는 부분을 없애고 남은 부분으로 이루어진 입체를 말한다냥')

    if message.content.endswith('냥이야 각점'):
        await message.channel.send('특이점의 하나로, 곡선 위 각 점의 접선이 어떤 점에서 불연속적으로 방향을 바꿀 때의 그 점을 말한다냥')

    if message.content.endswith('냥이야 각형'):
        await message.channel.send('=사각형')

    if message.content.endswith('냥이야 간승법'):
        await message.channel.send('곱셈을 쉽게 하는 방법을 말한다냥')

    if message.content.endswith('냥이야 간약률'):
        await message.channel.send('공통 인자로 간단하게 약분하는 법칙이다냥')

    if message.content.endswith('냥이야 간접조사'):
        await message.channel.send('통계 조사에서, 다른 목적을 위하여 작성된 기존 자료를 이용하거나 전문가와의 인터뷰를 통하여 이루어지는 조사 방법이다냥')

    if message.content.endswith('냥이야 간접측정'):
        await message.channel.send('측정량과 일정한 관계가 있는 몇 개의 양을 측정함으로써 구하고자 하는 측정값을 간접적으로 유도해 내는 일을 말한다냥')

    if message.content.endswith('냥이야 간제법'):
        await message.channel.send('나눗셈을 쉽게 하는 방법을 말한다냥')

    if message.content.endswith('냥이야 간편셈'):
        await message.channel.send('계산을 쉽고 편하게 하는 방법을 말한다냥')

    if message.content.endswith('냥이야 감법'):
        await message.channel.send('=뺄셈법')

    if message.content.endswith('냥이야 감법기호'):
        await message.channel.send('=뺄셈 부호')

    if message.content.endswith('냥이야 감산'):
        await message.channel.send('=뺄셈')

    if message.content.endswith('냥이야 감산부호'):
        await message.channel.send('=뺄셈 부호')

    if message.content.endswith('냥이야 감소수열'):
        await message.channel.send('수열 *a1, a2, a3*, ……에서 항의 값이 점점 작아지는 수열. 항의 값이 커지지 않는 수열을 포함해서 이를 때도 있다냥')

    if message.content.endswith('냥이야 감소함수'):
        await message.channel.send('독립 변수의 값이 커질수록 이에 대응하는 함숫값이 작아지는 함수이다냥')

    if message.content.endswith('냥이야 값'):
        await message.channel.send('하나의 글자나 식이 취하는 수, 또는 그런 수치를 말한다냥')

    if message.content.endswith('냥이야 '):
        await message.channel.send('냥')

    # ------------------------------ !수학 ------------------------------


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

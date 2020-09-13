import discord
import os
import datetime
import random


client = discord.Client()


@client.event
async def on_ready():
    print('후아아암~ 잘잤다냥!')
    game = discord.Game("인간들 놀아주기")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):

    # 목록

    if message.content.endswith('냥이야 목록'):
        await message.channel.send('아직 안만들었다냥 ㅇㅅㅇ')

    # !목록

    # 랜덤

    if message.content.startswith('냥이야 주사위'):
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

    # !랜덤

    # 시간

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
    
    # !시간

    # 대화

    if message.content.endswith('냥이야'):
        say = "왜부르냥?/냥?/무슨일로 날 불렀냥?"
        saychoice = say.split("/")
        saynumber = random.randint(1, 3)
        sayresult = saychoice[saynumber - 1]
        await message.channel.send(sayresult + '\n할말이 있다면 `냥이야 <할말>`로 말해달라냥')

    if message.content.endswith('냥이야 할말'):
        say = "너 바보냥?/어... 이걸 진짜로 쓸줄은 몰랐다냥/역시 인간들이란.."
        saychoice = say.split("/")
        saynumber = random.randint(1, 3)
        sayresult = saychoice[saynumber - 1]
        await message.channel.send(sayresult + '\n무슨 말을 해야할지 모르겠다면 `냥이야 목록`을 입력해라냥')

    if message.content.endswith('냥이야 <할말>'):
        say = "너 바보냥?/어... 이걸 진짜로 쓸줄은 몰랐다냥/역시 인간들이란.."
        saychoice = say.split("/")
        saynumber = random.randint(1, 3)
        sayresult = saychoice[saynumber - 1]
        await message.channel.send(sayresult + '\n무슨 말을 해야할지 모르겠다면 `냥이야 목록`을 입력해라냥')

    # !대화

    # 프로필

    if message.content.endswith('냥이야 프로필'):
        await message.channel.send('프로필을 보고싶으면 `냥이야 프로필 <이름>`을 적으라냥')

    if message.content.endswith('냥이야 프로필 종현'):
        embed=discord.Embed(title='차종현', description='[전사] Lv. 26', color=0x00D8FF)
        embed.set_thumbnail(url='https://post-phinf.pstatic.net/MjAxOTA2MjNfMTU4/MDAxNTYxMjYwNjMyNjUz.X1PHx3OkfkjK6coMGIjWgzdOx5yL_IS9HbjU_QnIGMMg.xhWi8ousZ3-gro3TvBmURsum0JGGHjmcOaBo-3PgLMsg.JPEG/1.jpg?type=w1200')
        embed.add_field(name='체력', value=':heart: 108', inline=True)
        embed.add_field(name='마나', value=':star2: 16', inline=True)
        embed.add_field(name='물리공격력', value=':dagger: 83', inline=True)
        embed.add_field(name='마법공격력', value=':dizzy: 35', inline=True)
        embed.add_field(name='힘', value=':muscle: 97', inline=True)
        embed.add_field(name='방어력', value=':shield: 74', inline=True)
        embed.add_field(name='지능', value=':books: 100000', inline=True)
        embed.add_field(name='민첩함', value=':athletic_shoe: 43', inline=True)
        embed.add_field(name='특성', value=':video_game: 뭐든 고였다. 피하는게 상책.', inline=False)
        await message.channel.send(embed=embed)

    # !프로필


client.run(os.environ["BOT_TOKEN"])

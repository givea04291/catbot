import discord
import os
import datetime
import random
import math
from sympy import factor, expand, symbols, solve


catmoney = {519751765080408074: 45, 645266885495226388: 5000}
client = discord.Client()


@client.event
async def on_ready():
    print('후아아암~ 잘잤다냥!')
    game = discord.Game("인간들 놀아주기")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):

# 주사위

    if message.content.endswith('냥이야 주사위'):
        embed=discord.Embed(title="'주사위' 사용법", color=0xABF200)
        embed.add_field(name='사용법', value='`냥이야 주사위 <면의 개수>`', inline=False)
        embed.add_field(name='면의 개수', value='주사위 면의 개수로는 0보다 큰 정수만 가능함\n0으로 시작되는 정수는 사용 불가능함', inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 주사위 '):
        try:
            roll = message.content.split(" ")
            rolld = roll[2]
            if rolld.startswith('0'):
                await message.channel.send('0으로 시작되는 정수는 사용할 수 없다냥')
            else:
                dice = random.randint(1, int(rolld))
                await message.channel.send('정' + str(rolld) + '면체 주사위를 굴려서 **' + str(dice) + '**이(가) 나왔다냥')
        except ValueError:
            await message.channel.send('주사위 면의 개수로는 0보다 큰 정수가 와야한다냥')

# 선택

    elif message.content.endswith('냥이야 골라'):
        embed=discord.Embed(title="'골라' 사용법", color=0xABF200)
        embed.add_field(name='사용법', value='`냥이야 골라 <옵션1> [옵션2] [옵션3] …`', inline=False)
        embed.add_field(name='옵션', value='`옵션` 자리에 공백이 오면 오류 발생', inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 골라 '):
        choice = message.content.split(" ")
        choicenumber = random.randint(2, len(choice)-1)
        choiceresult = choice[choicenumber]
        await message.channel.send(choiceresult)

# 추천

    elif message.content.endswith('냥이야 애니추천'):
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

    elif message.content.endswith('냥이야 게임추천'):
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

# 시간

    elif message.content.endswith('냥이야 시간'):
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        day = datetime.datetime.today().day
        hour = datetime.datetime.today().hour
        minute = datetime.datetime.today().minute
        second = datetime.datetime.today().second
        await message.channel.send('지금은 ' + str(year) + '년 ' + str(month) + '월 ' + str(day) + '일 '
                                   + str(hour) + '시 ' + str(minute) + '분 ' + str(second) + '초다냥')

    elif message.content.startswith('냥이야 몇년'):
        year = datetime.datetime.today().year
        await message.channel.send(str(year) + '년이다냥')

    elif message.content.startswith('냥이야 몇월'):
        month = datetime.datetime.today().month
        await message.channel.send(str(month) + '월이다냥')

    elif message.content.startswith('냥이야 몇일'):
        day = datetime.datetime.today().day
        await message.channel.send(str(day) + '일이다냥')

    elif message.content.startswith('냥이야 몇시'):
        hour = datetime.datetime.today().hour
        await message.channel.send(str(hour) + '시다냥')

    elif message.content.startswith('냥이야 몇분'):
        minute = datetime.datetime.today().minute
        await message.channel.send(str(minute) + '분이다냥')

    elif message.content.startswith('냥이야 몇초'):
        second = datetime.datetime.today().second
        await message.channel.send(str(second) + '초... ' + str(second+1) + '초.. 지나가버렸다냥')

# 대화

    elif message.content.endswith('냥이야'):
        say = "왜부르냥?/냥?/무슨일이냥?"
        saychoice = say.split("/")
        saynumber = random.randint(1, 3)
        sayresult = saychoice[saynumber - 1]
        await message.channel.send(sayresult)

# 프로필

    elif message.content.endswith('냥이야 프로필'):
        embed=discord.Embed(title="'프로필' 사용법", color=0xABF200)
        embed.add_field(name='사용법', value='`냥이야 프로필 <이름>`', inline=False)
        embed.add_field(name='이름', value='실명으로 써야함', inline=False)
        embed.add_field(name='현재 추가된 사람', value='`차종현`, `김규용`', inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 프로필 '):
        cut = message.content.split(' ')
        name = cut[2]
        if name=='차종현':
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
        elif name=='김규용':
            embed=discord.Embed(title='김규용', description='[관리자] Lv. ∞', color=0x00D8FF)
            embed.set_thumbnail(url='https://photos.google.com/album/AF1QipM0fRSQ62umhTogtcf7Z5VuecHIntIqx0233pJQ/photo/AF1QipOTkyZLRoXDjnrUj2jVSPSUCIZHBeVdS4Gxaf16')
            embed.add_field(name='체력', value=':heart: ∞', inline=True)
            embed.add_field(name='마나', value=':star2: ∞', inline=True)
            embed.add_field(name='물리공격력', value=':dagger: ∞', inline=True)
            embed.add_field(name='마법공격력', value=':dizzy: ∞', inline=True)
            embed.add_field(name='힘', value=':muscle: ∞', inline=True)
            embed.add_field(name='방어력', value=':shield: ∞', inline=True)
            embed.add_field(name='지능', value=':books: ∞', inline=True)
            embed.add_field(name='민첩함', value=':athletic_shoe: ∞', inline=True)
            embed.add_field(name='특성', value=':infinity: 올스텟 무한', inline=False)
            await message.channel.send(embed=embed)       
        else:
            await message.channel.send('아직 만들지 않았거나 없는 이름이다냥')

# 그래프

    elif message.content.startswith('냥이야 그래프 '):
        s = message.content.split(" ")
        f = s[2]
        if f.startswith('y='):
            a = message.content.split('y=')
            a = a[1]
            a = a.replace('+', '%2B')
            a = a.replace(' ', '+')
            await message.channel.send('그래프다냥\nhttps://www.google.com/search?q=y='+str(a))
        elif f.startswith('f(x)='):
            a = message.content.split('f(x)=')
            a = a[1]
            a = a.replace('+', '%2B')
            a = a.replace(' ', '+')
            await message.channel.send('그래프다냥\nhttps://www.google.com/search?q=f(x)='+str(a))
        else:
            await message.channel.send('그래프의 수식은 `y=` 또는 `f(x)=` 으로 시작해야 한다냥')

    elif message.content.endswith('냥이야 그래프'):
        embed=discord.Embed(title="'그래프' 사용법", color=0xABF200)
        embed.add_field(name='사용법', value='`냥이야 그래프 <수식>`', inline=False)
        embed.add_field(name='수식', value='`y=(x에 대한 다항식)` 또는 `f(x)=(x에 대한 다항식)`의 형태로 써야함', inline=False)
        embed.add_field(name='띄어쓰기', value='수식에 들어간 공백은 인식 불가능', inline=False)
        await message.channel.send(embed=embed)

# 계산

    elif message.content.endswith('냥이야 계산'):
        embed=discord.Embed(title="'계산' 사용법", color=0xABF200)
        embed.add_field(name='사용법', value='`냥이야 계산 <식>`', inline=False)
        embed.add_field(name='더하기/빼기', value='`+` 및 `-` 로 사용 가능', inline=False)
        embed.add_field(name='곱하기', value='`×`, `x`, `·` 로 사용 가능', inline=False)
        embed.add_field(name='나누기', value='`÷`, `/` 로 사용 가능', inline=False)
        embed.add_field(name='거듭제곱', value='`^`, `**` 로 사용 가능\n거듭제곱의 지수는 `{ }` 안에 써야함', inline=False)
        embed.add_field(name='절댓값', value='`[ ]` 안에 써야함\n`| |` 필요 없음', inline=False)
        embed.add_field(name='팩토리얼', value='`< >` 안에 써야함\n`!` 필요 없음', inline=False)
        embed.add_field(name='제곱근', value='`$ %` 또는 `√ %` 안에 써야함', inline=False)
        embed.add_field(name='괄호', value='거듭제곱의 지수를 제외한 모든 괄호는 `( )` 로 써야함', inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 계산 '):
        first_cut = message.content.split(' ')
        first_s = first_cut[2:]
        s = str(first_s).replace('^', '**')
        s = s.replace(' ', '')
        s = s.replace("['", '')
        s = s.replace("']", '')
        s = s.replace("'", '')
        s = s.replace(',', '')
        s = s.replace('×', '*')
        s = s.replace('x', '*')
        s = s.replace('·', '*')
        s = s.replace('÷', '/')
        s = s.replace('[', 'abs(')
        s = s.replace(']', ')')
        s = s.replace('<', 'math.factorial(')
        s = s.replace('>', ')')
        s = s.replace('$', 'math.sqrt(')
        s = s.replace('√', 'math.sqrt(')
        s = s.replace('%', ')')
        show = str(first_s).replace('**', '^')
        show = show.replace("['", '')
        show = show.replace("']", '')
        show = show.replace("'", '')
        show = show.replace(',', '')
        show = show.replace('{', '')
        show = show.replace('}', '')
        show = show.replace('*', '·')
        show = show.replace('[', '|')
        show = show.replace(']', '|')
        show = show.replace('<', '')
        show = show.replace('>', '!')
        show = show.replace('$', '√(')
        show = show.replace('%', ')')
        try:
            tmultytest = s.split('**')
            tmultytest = tmultytest[1]
            try:
                multylefttest = s.split('{')
                multylefttest = multylefttest[1]
                try:
                    multyrighttest = s.split('}')
                    multyrighttest = multyrighttest[1]
                    multyleft = int(s.index('{')+1)
                    multyright = int(s.index('}'))
                    try:
                        multyup = float(s[multyleft:multyright])
                        if multyup>10:
                            await message.channel.send('거듭제곱의 지수는 10보다 크면 안된다냥')
                        elif multyup<-10:
                            await message.channel.send('거듭제곱의 지수는 -10보다 작으면 안된다냥')
                        else:
                            s = s.replace('{', '')
                            s = s.replace('}', '')
                            try:
                                v = str(eval(str(s)))
                            except ZeroDivisionError:
                                await message.channel.send('0은 나누는 수가 될 수 없다냥')
                            except NameError:
                                await message.channel.send('계산할 수 없다냥')
                            except SyntaxError:
                                await message.channel.send('계산할 수 없다냥')
                            except ValueError:
                                await message.channel.send('계산할 수 없다냥')
                    except ValueError:
                        await message.channel.send('거듭제곱의 지수로는 실수만 가능하다냥')
                except IndexError:
                    await message.channel.send('거듭제곱의 지수는 `{ }` 안에 써야한다냥')
            except IndexError:
                await message.channel.send('거듭제곱의 지수는 `{ }` 안에 써야한다냥')
        except IndexError:
            try:
                v = str(eval(str(s)))
            except ZeroDivisionError:
                await message.channel.send('0은 나누는 수가 될 수 없다냥')
            except NameError:
                await message.channel.send('계산할 수 없다냥')
            except SyntaxError:
                await message.channel.send('계산할 수 없다냥')
            except ValueError:
                await message.channel.send('계산할 수 없다냥')
        await message.channel.send('**'+show+' = '+v+'** (이)다냥')

    elif message.content.startswith('냥이야 인수분해 '):
        a, b, c, x, y, z = symbols('a b c x y z')
        print(a+b+c+x+y+z)
        cut = message.content.split(' ')
        s = str(cut[2:])
        s = s.replace('[', '')
        s = s.replace(']', '')
        s = s.replace(',', '')
        first_s = s.replace("'", '')
        inp = first_s.replace('**', '^')
        inp = inp.replace('*', '·')
        rs = first_s.replace(' ', '')
        rs = rs.replace('^', '**')
        rs = rs.replace('×', '*')
        rs = rs.replace('·', '*')
        rs = rs.replace('÷', '/')
        try:
            test2 = s.split('=')
            test2 = test2[1]
            await message.channel.send('인수분해할 식에 등호가 포함되어있으면 안된다냥')
        except IndexError:
            cal = factor(rs)
            cal = str(cal)
            try:
                test = cal.split('zoo')
                test = test[1]
                await message.channel.send('0은 나누는 수가 될 수 없다냥')
            except IndexError:
                show = cal.replace('**', '^')
                show = show.replace('*', '·')
                await message.channel.send('**'+str(inp)+' = '+str(show)+'** (이)다냥')

    elif message.content.endswith('냥이야 인수분해'):
        embed=discord.Embed(title="'인수분해' 사용법", color=0xABF200)
        embed.add_field(name='사용법', value='`냥이야 인수분해 <식>`', inline=False)
        embed.add_field(name='수식', value='a, b, c, x, y, z에 대한 다항식 분해 가능함', inline=False)
        embed.add_field(name='곱하기', value='`×`, `·` 로 사용 가능', inline=False)
        embed.add_field(name='나누기', value='`÷`, `/` 로 사용 가능', inline=False)
        embed.add_field(name='거듭제곱', value='`^`, `**` 로 사용 가능', inline=False)
        embed.add_field(name='괄호', value='거듭제곱의 지수를 제외한 모든 괄호는 `( )` 로 써야함', inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 전개 '):
        a, b, c, x, y, z = symbols('a b c x y z')
        cut = message.content.split(' ')
        s = str(cut[2:])
        s = s.replace('[', '')
        s = s.replace(']', '')
        s = s.replace(',', '')
        first_s = s.replace("'", '')
        inp = first_s.replace('**', '^')
        inp = inp.replace('*', '·')
        rs = first_s.replace(' ', '')
        rs = rs.replace('^', '**')
        rs = rs.replace('×', '*')
        rs = rs.replace('·', '*')
        rs = rs.replace('÷', '/')
        try:
            test2 = s.split('=')
            test2 = test2[1]
            await message.channel.send('전개할 식에 등호가 포함되어있으면 안된다냥')
        except IndexError:
            cal = expand(rs)
            cal = str(cal)
            try:
                test = cal.split('zoo')
                test = test[1]
                await message.channel.send('0은 나누는 수가 될 수 없다냥')
            except IndexError:
                show = cal.replace('**', '^')
                show = show.replace('*', '·')
                await message.channel.send('**'+str(inp)+' = '+str(show)+'** (이)다냥')

    elif message.content.endswith('냥이야 전개'):
        embed=discord.Embed(title="'전개' 사용법", color=0xABF200)
        embed.add_field(name='사용법', value='`냥이야 전개 <식>`', inline=False)
        embed.add_field(name='수식', value='a, b, c, x, y, z에 대한 다항식 전개 가능함', inline=False)
        embed.add_field(name='곱하기', value='`×`, `·` 로 사용 가능', inline=False)
        embed.add_field(name='나누기', value='`÷`, `/` 로 사용 가능', inline=False)
        embed.add_field(name='거듭제곱', value='`^`, `**` 로 사용 가능', inline=False)
        embed.add_field(name='괄호', value='거듭제곱의 지수를 제외한 모든 괄호는 `( )` 로 써야함', inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 방정식 '):
        if message.content.endswith('=0'):
            x = symbols('x')
            cut = message.content.split(' ')
            s = str(cut[2:])
            s = s.replace('[', '')
            s = s.replace(']', '')
            s = s.replace(',', '')
            first_s = s.replace("'", '')
            inp = first_s.replace('**', '^')
            inp = inp.replace('*', '·')
            rs = first_s.replace(' ', '')
            rs = rs.replace('^', '**')
            rs = rs.replace('×', '*')
            rs = rs.replace('·', '*')
            rs = rs.replace('÷', '/')
            try:
                a = rs.split('=')
                testest = a[1]
                print(testest)
                try:
                    t = a[2]
                    print(t)
                    await message.channel.send('방정식에 등호는 하나만 존재할 수 있다냥')
                except IndexError:
                    try:
                        show = str(solve(a[0], dict=True))
                        show = show.replace('[', '')
                        show = show.replace(']', '')
                        show = show.replace('{', '')
                        show = show.replace('}', '')
                        show = show.replace(':', ' =')
                        show = show.replace('**', '^')
                        show = show.replace('*', '·')
                        show = show.replace('I', 'i')
                        show = show.replace('sqrt', '√')
                        if show.startswith('x'):
                            await message.channel.send('방정식 '+str(inp)+' 의 해는 **'+str(show)+'** (이)다냥')
                        else:
                            await message.channel.send('계산할 수 없는 방정식이다냥')
                    except:
                        await message.channel.send('계산할 수 없는 방정식이다냥')
            except IndexError:
                await message.channel.send('방정식에는 등호가 포함되어있어야 한다냥')
        elif message.content.endswith('= 0'):
            x = symbols('x')
            cut = message.content.split(' ')
            s = str(cut[2:])
            s = s.replace('[', '')
            s = s.replace(']', '')
            s = s.replace(',', '')
            first_s = s.replace("'", '')
            inp = first_s.replace('**', '^')
            inp = inp.replace('*', '·')
            rs = first_s.replace(' ', '')
            rs = rs.replace('^', '**')
            rs = rs.replace('×', '*')
            rs = rs.replace('·', '*')
            rs = rs.replace('÷', '/')
            try:
                a = rs.split('=')
                testest = a[1]
                try:
                    t = a[2]
                    await message.channel.send('방정식에 등호는 하나만 존재할 수 있다냥')
                except IndexError:
                    try:
                        show = str(solve(a[0], dict=True))
                        show = show.replace('[', '')
                        show = show.replace(']', '')
                        show = show.replace('{', '')
                        show = show.replace('}', '')
                        show = show.replace(':', ' =')
                        show = show.replace('**', '^')
                        show = show.replace('*', '·')
                        show = show.replace('I', 'i')
                        show = show.replace('sqrt', '√')
                        if show.startswith('x'):
                            await message.channel.send('방정식 '+str(inp)+' 의 해는 **'+str(show)+'** (이)다냥')
                        else:
                            await message.channel.send('계산할 수 없는 방정식이다냥')
                    except:
                        await message.channel.send('계산할 수 없는 방정식이다냥')
            except IndexError:
                await message.channel.send('방정식에는 등호가 포함되어있어야 한다냥')
        else:
            await message.channel.send('방정식은 `x에 대한 다항식 = 0` 의 형태여야 한다냥')
    
    elif message.content.endswith('냥이야 방정식'):
        embed=discord.Embed(title="'방정식' 사용법", color=0xABF200)
        embed.add_field(name='사용법', value='`냥이야 방정식 <x에 대한 다항식>=0`', inline=False)
        embed.add_field(name='곱하기', value='`×`, `·` 로 사용 가능', inline=False)
        embed.add_field(name='나누기', value='`÷`, `/` 로 사용 가능', inline=False)
        embed.add_field(name='거듭제곱', value='`^`, `**` 로 사용 가능', inline=False)
        embed.add_field(name='괄호', value='거듭제곱의 지수를 제외한 모든 괄호는 `( )` 로 써야함', inline=False)
        await message.channel.send(embed=embed)

# 가위바위보

    elif message.content.startswith('냥이야 가위바위보 '):
        cut = message.content.split(' ')
        select = cut[2]
        catfull = '가위 바위 보'
        catfull = catfull.split(' ')
        catselect = catfull[random.randint(0, 2)]
        if select == catselect:
            score = 0
        elif select == '가위':
            if catselect == '바위':
                score = 1
            if catselect == '보':
                score = -1
        elif select == '바위':
            if catselect == '보':
                score = 1
            if catselect == '가위':
                score = -1
        elif select == '보':
            if catselect == '가위':
                score = 1
            if catselect == '바위':
                score = -1
        else:
            error = '너 가위바위보 할 줄 모르는거냥?/...냥?/제대로 하라냥'
            error = error.split('/')
            error = error[random.randint(0, 2)]
            await message.channel.send(error)
        if score == 1:
            show = '가소롭다냥!/내가 이겼다냥!/쉽다냥!'
            show = show.split('/')
            show = show[random.randint(0, 2)]
        if score == 0:
            show = '비겼다냥..!'
        if score == -1:
            show = '*(부들부들)*/너 좀 한다냥?/졌다냥...'
            show = show.split('/')
            show = show[random.randint(0, 2)]
        if select == '가위':
            hand = ':v:'
        if select == '바위':
            hand = ':fist:'
        if select == '보':
            hand = ':raised_hand:'
        if catselect == '가위':
            cathand = ':v:'
        if catselect == '바위':
            cathand = ':fist:'
        if catselect == '보':
            cathand = ':raised_hand:'
        await message.channel.send('<@' + str(message.author.id) + '> '+str(hand)+' vs '+str(cathand)+' **냥이**\n'+str(show))
        
    elif message.content.endswith('냥이야 가위바위보'):
        embed=discord.Embed(title="'가위바위보' 사용법", color=0xABF200)
        embed.add_field(name='사용법', value='`냥이야 가위바위보 <가위/바위/보>`', inline=False)
        await message.channel.send(embed=embed)

# 돈/도박

    elif message.content == '냥이야 돈':
        try:
            test = catmoney[message.author.id]
            if test < 500:
                catmoney[message.author.id] = test + 5000
                await message.channel.send('<@'+str(message.author.id)+'> 의 돈이 500원보다 적어서 **5000원**을 지급했다냥\n현재 돈은 **'+str(catmoney[message.author.id])+'원** 이다냥')
            else:
                await message.channel.send('<@'+str(message.author.id)+'> 의 현재 돈은 **'+str(catmoney[message.author.id])+'원** 이다냥')
        except KeyError:
            catmoney[message.author.id] = 5000
            await message.channel.send('돈 시스템을 처음 사용하는 <@'+str(message.author.id)+'> 에게 **5000원**을 지급했다냥')

    elif message.content == '냥이야 도박':
        embed=discord.Embed(title="'도박' 사용법", color=0xABF200)
        embed.add_field(name='사용법', value='`냥이야 도박 <거는 돈>`', inline=False)
        embed.add_field(name='거는 돈', value='보유한 돈보다 많거나 같은 돈은 걸 수 없음', inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 도박 '):
        value = message.content.split(' ')
        value = value[2]
        if value == '확률':
            await message.channel.send('내 도박은 65%로 실패하고, 33%로 성공하고, 2%로 특별한 일이 일어난다냥')
        else:
            try:
                value = int(value)
                if value < 1:
                    await message.channel.send('거는 돈으로는 자연수만 올 수 있다냥')
                else:
                    if value >= int(catmoney[message.author.id]):
                        await message.channel.send('거는 돈이 보유한 돈보다 많거나 같을 수는 없다냥')
                    else:
                        g1 = ['fail'] * 65
                        g2 = ['x2'] * 20
                        g3 = ['x3'] * 9
                        g4 = ['x5'] * 4
                        g5 = ['x100', 'website']
                        gambling = g1+g2+g3+g4+g5
                        final = random.choice(gambling)
                        if final == 'fail':
                            catmoney[message.author.id] = catmoney[message.author.id] - value
                            await message.channel.send('도박에 실패해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원** 이 되었다냥')
                        elif final == 'x2':
                            catmoney[message.author.id] = catmoney[message.author.id] + (value * 2)
                            await message.channel.send('2배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원** 이 되었다냥')
                        elif final == 'x3':
                            catmoney[message.author.id] = catmoney[message.author.id] + (value * 3)
                            await message.channel.send('3배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원** 이 되었다냥')
                        elif final == 'x5':
                            catmoney[message.author.id] = catmoney[message.author.id] + (value * 5)
                            await message.channel.send('5배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원** 이 되었다냥')
                        elif final == 'x100':
                            catmoney[message.author.id] = catmoney[message.author.id] + (value * 100)
                            await message.channel.send('**당첨!**\n100배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원** 이 되었다냥!')
                        elif final == 'website':
                            await message.channel.send('도박은 너무 많이 하면 해롭다냥!\nhttps://www.kcgp.or.kr/pcMain.do')
            except ValueError:   
                await message.channel.send('거는 돈으로는 자연수만 올 수 있다냥')

# 예외처리

    elif message.content.startswith('냥이야 '):
        say = "냥...?/냥?/무슨 말인지 모르겠다냥"
        saychoice = say.split("/")
        saynumber = random.randint(1, 3)
        sayresult = saychoice[saynumber - 1]
        await message.channel.send(sayresult)

# 명령어  

    elif message.content.startswith('/data'):
        if message.author.id == 519751765080408074:
            a = message.content.split(' ')
            try:
                act = a[1]
                # get
                if act == 'get':
                    try:
                        box = a[2]
                        if box == 'catmoney':
                            try:
                                name = a[3]
                                if name == '@a':
                                    await message.channel.send(catmoney)
                                else:
                                    try:
                                        await message.channel.send(str(name)+'의 현재 돈은 **'+str(catmoney[int(name)])+'원** 이다냥')
                                    except KeyError:
                                        await message.channel.send('알 수 없는 유저의 ID이다냥')
                            except IndexError:
                                await message.channel.send('명령어의 실행 대상 유저가 필요하다냥')
                        else:
                            await message.channel.send('명령어의 실행 대상 딕셔너리가 필요하다냥')
                    except IndexError:
                        await message.channel.send('명령어의 실행 대상 딕셔너리가 필요하다냥')
                # set
                elif act == 'set':
                    try:
                        box = a[2]
                        if box == 'catmoney':
                            try:
                                name = a[3]
                                test = catmoney[int(name)]
                                try:
                                    value = a[4]
                                    try:
                                        test = int(value)
                                        catmoney[int(name)] = test
                                        await message.channel.send(str(name)+'의 돈을 **'+str(test)+'원** 으로 설정했다냥')
                                    except ValueError:
                                        await message.channel.send('실행 변수의 자료형은 자연수이다냥')
                                except IndexError:
                                    await message.channel.send('명령어의 대상이 되는 실행 변수가 필요하다냥')
                            except IndexError:
                                await message.channel.send('명령어의 실행 대상 유저가 필요하다냥')
                            except KeyError:
                                await message.channel.send('알 수 없는 유저의 ID이다냥')
                            except ValueError:
                                await message.channel.send('알 수 없는 유저의 ID이다냥')
                        else:
                            await message.channel.send('명령어의 실행 대상 딕셔너리가 필요하다냥')
                    except IndexError:
                        await message.channel.send('명령어의 실행 대상 딕셔너리가 필요하다냥')
                else:
                    await message.channel.send('알 수 없는 추가 데이터다냥')
            except IndexError:
                await message.channel.send('명령어의 추가 데이터가 필요하다냥')
        else:
            await message.channel.send('명령어 접근 권한이 없다냥')

client.run(os.environ["BOT_TOKEN"])

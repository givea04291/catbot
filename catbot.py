import discord
import os
import random
import math
from sympy import factor, expand, symbols, solve
import sys
import json
import urllib.request
import datetime
import pytz
from pytz import common_timezones


catmoney = {519751765080408074: 5000, 645266885495226388: 1, 473827858175754250: 1, 390057085209149440: 100000099000, 633224033667907584: 0, 582832386748973057: 2262000, 485716741289279488: 1, 535758069620277249: 0, 704479706505936978: 0, 554214990001995776: 0}

client = discord.Client()


@client.event
async def on_ready():
    print('후아아암~ 잘잤다냥!')
    game = discord.Game("인간들 놀아주기")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):

# [오류 방지]

    if message.author == client.user:
        return

# [미니게임]/주사위

    elif message.content == '냥이야 주사위':
        embed=discord.Embed(
            title="'주사위' 사용법",
            color=0xABF200
        )
        embed.add_field(
            name='사용법',
            value='`냥이야 주사위 <면의 개수>`',
            inline=False
        )
        embed.add_field(
            name='면의 개수',
            value='주사위 면의 수는 0보다 큰 정수여야 합니다.',
            inline=False
        )
        embed.add_field(
            name='꽝',
            value='5%의 확률로 꽝이 나옴',
            inline=False
        )
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 주사위 '):
        roll = message.content.split(" ")
        rolld = roll[2]
        try:
            inttest = int(rolld)
            print(inttest)
            faildice1 = ['0'] * 95
            faildice2 = ['fail'] * 5
            faildice = faildice1 + faildice2
            diceresult = random.choice(faildice)
            if diceresult == '0':
                dice = random.randint(1, int(rolld))
                await message.channel.send('정' + str(rolld) + '면체 주사위를 굴려서 **' + str(dice) + '**이(가) 나왔다냥!')
            elif diceresult == 'fail':
                await message.channel.send('주사위가 책상 밖으로 떨어져버렸다냥!')
        except ValueError:
            says = ['그런 주사위가 어디있냥!?','어떤 주사위를 굴리라는거냥..?']
            say = random.choice(says)
            await message.channel.send(say)

# [미니게임]/선택

    elif message.content == '냥이야 골라':
        embed=discord.Embed(
            title="'골라' 사용법", 
            color=0xABF200
        )
        embed.add_field(
            name='사용법', 
            value='`냥이야 골라 <옵션1> [옵션2] [옵션3] …`', 
            inline=False
        )
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 골라 '):
        choice = message.content.split(" ")
        choicenumber = random.randint(2, len(choice)-1)
        choiceresult = choice[choicenumber]
        await message.channel.send('내 선택은...\n**'+choiceresult+'**냥!')

# [미니게임]/가위바위보

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
            errorsay = ['...냥?','가위, 바위, 보 3개중에 하나를 내라냥']
            error = random.choice(errorsay)
            await message.channel.send(str(error))
        if score == 1:
            showsay = ['가소롭다냥!','내가 이겼다냥!','너 하나쯤은 내가 이긴다냥!']
            show = random.choice(showsay)
        if score == 0:
            show = '비겼다냥..!'
        if score == -1:
            showsay = ['*(부들부들)*','너 좀 한다냥?','내가 졌다냥... *(쭈글)*']
            show = random.choice(showsay)
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
        
    elif message.content == '냥이야 가위바위보':
        embed=discord.Embed(
            title="'가위바위보' 사용법", 
            color=0xABF200
        )
        embed.add_field(
            name='사용법', 
            value='`냥이야 가위바위보 <가위/바위/보>`', 
            inline=False
        )
        await message.channel.send(embed=embed)

# [시간]

    elif message.content == '냥이야 시간':
        embed=discord.Embed(
            title="'시간' 사용법",
            color=0xABF200
        )
        embed.add_field(
            name='사용법',
            value='`냥이야 시간 <시간대 번호/지역/.>`',
            inline=False
        )
        embed.add_field(
            name='시간대',
            value='`.`을 입력하면 시간대가 KST(한국 표준시)로 지정됩니다\n사이트주소',
            inline=False
        )
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 시간 '):
        timeref = {}
        a = 1
        for zones in common_timezones:
            timeref[a] = zones
            a = a+1
        timenum = message.content.split(' ')
        try:
            timenum = int(timenum[2])
            if timenum > 440 or timenum < 1:
                await message.channel.send('잘못된 시간대이다냥')
            else:
                timez = timeref[timenum]
        except ValueError:
            timenum = str(timenum[2])
            timez = timenum
            if timez == '.':
                timez = 'Asia/Seoul'   
        try:
            time = str(datetime.datetime.now(pytz.timezone(timez)))
            space_split = time.split(' ')
            time_first = space_split[0]
            time_first_split = time_first.split('-')
            time_year = time_first_split[0]
            time_month = time_first_split[1]
            time_day = time_first_split[2]
            time_second = space_split[1]
            time_second_split1 = time_second.split('.')
            time_second_split1 = time_second_split1[0]
            time_second_split2 = time_second_split1.split(':')
            time_hour = time_second_split2[0]
            time_minute = time_second_split2[1]
            time_seconds = time_second_split2[2]
            await message.channel.send(timez+'의 지금 시간은 '+str(time_year)+'년 '+str(time_month)+'월 '+str(time_day)+'일 '+str(time_hour)+'시 '+str(time_minute)+'분 '+str(time_seconds)+'초다냥!')
        except pytz.exceptions.UnknownTimeZoneError:
            await message.channel.send('잘못된 시간대이다냥')

# [번역]

    elif message.content == '냥이야 번역':
        embed=discord.Embed(
            title="'번역' 사용법",
            color=0xABF200
        )
        embed.add_field(
            name='사용법',
            value='`냥이야 번역 <번역할 언어><번역될 언어> <번역할 말>`',
            inline=False
        )
        embed.add_field(
            name='번역 언어',
            value='사이트주소',
            inline=False
        )
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 번역 '):
        try:
            Text = str(message.content[10:])
            client_id = "jsx44lysf3MT2A8yhDdF"
            client_secret = "hCXg7z7NL0"
            url = "https://openapi.naver.com/v1/papago/n2mt"
            encText = urllib.parse.quote(Text)
            if str(message.content[7]) == '한':
                source = 'ko'
                sourceset = '한국어'
            elif str(message.content[7]) == '영':
                source = 'en'
                sourceset = '영어'
            elif str(message.content[7]) == '일':
                source = 'ja'
                sourceset = '일본어'
            elif str(message.content[7]) == '프':
                source = 'fr'
                sourceset = '프랑스어'
            elif str(message.content[7]) == '독':
                source = 'de'
                sourceset = '독일어'
            elif str(message.content[7]) == '러':
                source = 'ru'
                sourceset = '러시아어'
            elif str(message.content[7]) == '스':
                source = 'es'
                sourceset = '스페인어'
            else:
                await message.channel.send('지원되지 않는 언어다냥!')
                return
            if str(message.content[8]) == '한':
                target = 'ko'
                targetset = '한국어'
            elif str(message.content[8]) == '영':
                target = 'en'
                targetset = '영어'
            elif str(message.content[8]) == '일':
                target = 'ja'
                targetset = '일본어'
            elif str(message.content[8]) == '프':
                target = 'fr'
                targetset = '프랑스어'
            elif str(message.content[8]) == '독':
                target = 'de'
                targetset = '독일어'
            elif str(message.content[8]) == '러':
                target = 'ru'
                targetset = '러시아어'
            elif str(message.content[8]) == '스':
                target = 'es'
                targetset = '스페인어'
            else:
                await message.channel.send('지원되지 않는 언어다냥!')
                return
            data = "source="+source+"&target="+target+"&text="+encText
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(request, data=data.encode("utf-8"))
            rescode = response.getcode()
            if rescode == 200:
                response_body = response.read()
                data = response_body.decode('utf-8')
                data = json.loads(data)
                tranText = data['message']['result']['translatedText']
            else:
                await message.channel.send('오류가 발생했다냥: '+rescode)
                return
            embed=discord.Embed(
                title=sourceset+' -> '+targetset+' 번역결과',
                description=tranText,
                color=0xFFE400
            )
            await message.channel.send(embed=embed)
        except urllib.error.HTTPError:
            await message.channel.send('오류가 발생했다냥: 400 Bad Request')

# [계산]

    elif message.content == '냥이야 계산':
        embed=discord.Embed(
            title="'계산' 사용법",
            color=0xABF200
        )
        embed.add_field(
            name='사용법', 
            value='`냥이야 계산 <식>`', 
            inline=False
        )
        embed.add_field(
            name='더하기/빼기', 
            value='`+` 및 `-` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='곱하기', 
            value='`×`, `x`, `·`, `*` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='나누기', 
            value='`÷`, `/` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='거듭제곱', 
            value='`^`, `**` 로 나타냅니다\n거듭제곱의 지수는 `{ }` 안에 써야합니다\n10제곱,-10제곱을 넘는 지수는 계산이 불가능합니다', 
            inline=False
        )
        embed.add_field(
            name='절댓값', 
            value='`[ ]` 안에 수나 식을 써야합니다\n`| |` 는 없어도 됩니다', 
            inline=False
        )
        embed.add_field(
            name='팩토리얼', 
            value='`< >` 안에 수나 식을 써야합니다\n`!` 는 없어도 됩니다', 
            inline=False
        )
        embed.add_field(
            name='제곱근', 
            value='`$ %` 또는 `√ %` 안에 수나 식을 써야합니다', 
            inline=False
        )
        embed.add_field(
            name='괄호', 
            value='거듭제곱의 지수를 제외한 모든 괄호는 `( )` 로 써야합니다', 
            inline=False
        )
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
                            await message.channel.send('거듭제곱을 얼마나 시키려는거냥?! 노조를 세울거다냥! 파업을 할거다냥!')
                        elif multyup<-10:
                            await message.channel.send('거듭제곱을 얼마나 시키려는거냥?! 노조를 세울거다냥! 파업을 할거다냥!')
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
        await message.channel.send('**'+show+' = '+v+'** (이)다냥!')

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
            await message.channel.send('인수분해할 다항식에 등호가 있으면 안된다냥')
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
                await message.channel.send('**'+str(inp)+' = '+str(show)+'** (이)다냥!')

    elif message.content == '냥이야 인수분해':
        embed=discord.Embed(
            title="'인수분해' 사용법", 
            color=0xABF200
        )
        embed.add_field(
            name='사용법', 
            value='`냥이야 인수분해 <식>`', 
            inline=False
        )
        embed.add_field(
            name='수식', 
            value='a, b, c, x, y, z에 대한 다항식을 인수분해할 수 있습니다', 
            inline=False
        )
        embed.add_field(
            name='곱하기', 
            value='`×`, `·`, `*` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='나누기', 
            value='`÷`, `/` 로 나타냅니다',
            inline=False
        )
        embed.add_field(
            name='거듭제곱', 
            value='`^`, `**` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='괄호', 
            value='거듭제곱의 지수를 제외한 모든 괄호는 `( )` 로 써야합니다', 
            inline=False
        )
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
            await message.channel.send('전개할 다항식에 등호가 포함되어있으면 안된다냥')
        except IndexError:
            try:
                cal = expand(rs)
                cal = str(cal)
                try:
                    test = cal.split('zoo')
                    test = test[1]
                    await message.channel.send('0은 나누는 수가 될 수 없다냥')
                except IndexError:
                    show = cal.replace('**', '^')
                    show = show.replace('*', '·')
                    await message.channel.send('**'+str(inp)+' = '+str(show)+'** (이)다냥!')
            except TypeError:
                await message.channel.send('전개할 수 없는 식이다냥')

    elif message.content == '냥이야 전개':
        embed=discord.Embed(
            title="'전개' 사용법", 
            color=0xABF200
        )
        embed.add_field(
            name='사용법', 
            value='`냥이야 전개 <식>`', 
            inline=False
        )
        embed.add_field(
            name='수식', 
            value='a, b, c, x, y, z에 대한 다항식을 전개할 수 있습니다', 
            inline=False
        )
        embed.add_field(
            name='곱하기', 
            value='`×`, `·`, `*` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='나누기', 
            value='`÷`, `/` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='거듭제곱', 
            value='`^`, `**` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='괄호', 
            value='거듭제곱의 지수를 제외한 모든 괄호는 `( )` 로 써야합니다', 
            inline=False
        )
        await message.channel.send(embed=embed)

    elif message.content.startswith('냥이야 방정식 '):
        if message.content.endswith('= 0'):
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
                    await message.channel.send('방정식은 `x에 대한 다항식 = 0` 의 형태여야 한다냥')
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
                            await message.channel.send('방정식 '+str(inp)+' 의 해는 **'+str(show)+'** (이)다냥!')
                        else:
                            await message.channel.send('계산할 수 없는 방정식이다냥')
                    except:
                        await message.channel.send('계산할 수 없는 방정식이다냥')
            except IndexError:
                await message.channel.send('방정식은 `x에 대한 다항식 = 0` 의 형태여야 한다냥')
        elif message.content.endswith('=0'):
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
                    await message.channel.send('방정식은 `x에 대한 다항식 = 0` 의 형태여야 한다냥')
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
                            await message.channel.send('방정식 '+str(inp)+' 의 해는 **'+str(show)+'** (이)다냥!')
                        else:
                            await message.channel.send('계산할 수 없는 방정식이다냥')
                    except:
                        await message.channel.send('계산할 수 없는 방정식이다냥')
            except IndexError:
                await message.channel.send('방정식은 `x에 대한 다항식 = 0` 의 형태여야 한다냥')
        else:
            await message.channel.send('방정식은 `x에 대한 다항식 = 0` 의 형태여야 한다냥')
    
    elif message.content == '냥이야 방정식':
        embed=discord.Embed(
            title="'방정식' 사용법", 
            color=0xABF200
        )
        embed.add_field(
            name='사용법', 
            value='`냥이야 방정식 <x에 대한 다항식>=0`\n3차 이하의 방정식의 해를 정확하게 구할 수 있고, 간단한 4차 이상의 방정식도 풀 수 있습니다', 
            inline=False
        )
        embed.add_field(
            name='곱하기', 
            value='`×`, `·`, `*` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='나누기', 
            value='`÷`, `/` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='거듭제곱', 
            value='`^`, `**` 로 나타냅니다', 
            inline=False
        )
        embed.add_field(
            name='괄호', 
            value='거듭제곱의 지수를 제외한 모든 괄호는 `( )` 로 써야합니다', 
            inline=False
        )
        await message.channel.send(embed=embed)

# [서버관리]/지우기

    elif message.content == '냥이야 지워':
        embed=discord.Embed(
            title="'지워' 사용법", 
            color=0xABF200
        )
        embed.add_field(
            name='사용법', 
            value='`냥이야 지워 <지울 메시지 수>`', 
            inline=False
        )
        embed.add_field(
            name='지울 메시지', 
            value='자신의 메시지는 지울 메시지의 수에 포함되지 않습니다', 
            inline=False
        )
        await message.channel.send(embed=embed)
    
    elif message.content.startswith('냥이야 지워 '):
        delete = message.content.split(' ')
        delete = delete[2]
        try:
            delete = int(delete)
            if delete <= 0:
                await message.channel.send('...도대체 뭘 원하는거냥?')
            elif delete > 100:
                await message.channel.send('지금 장난하는거냥?! 노조를 세울거다냥! 파업을 할거다냥!')
            else:
                await message.channel.purge(limit=delete+1)
                await message.channel.send('최근 메시지 '+str(delete)+'개를 지웠다냥!')
        except ValueError:
            await message.channel.send('...도대체 뭘 원하는거냥?')

# [경제]/돈(프로필 카테고리로 옮길 예정)

    elif message.content == '냥이야 돈':
        try:
            test = catmoney[message.author.id]
            if test < 500:
                catmoney[message.author.id] = test + 5000
                await message.channel.send('<@'+str(message.author.id)+'> 의 돈이 500원보다 적어서 **5000원**을 지급했다냥!\n현재 돈은 **'+str(catmoney[message.author.id])+'원**이다냥')
                await client.get_channel(790406561070972948).send(catmoney)
            else:
                await message.channel.send('<@'+str(message.author.id)+'> 의 현재 돈은 **'+str(catmoney[message.author.id])+'원**이다냥')
        except KeyError:
            catmoney[message.author.id] = 5000
            await message.channel.send('돈 시스템을 처음 사용하는 <@'+str(message.author.id)+'> 에게 **5000원**을 지급했다냥!')
            await client.get_channel(790406561070972948).send(catmoney)

# [경제]/도박

    elif message.content == '냥이야 도박':
        embed=discord.Embed(
            title="'도박' 사용법", 
            color=0xABF200
        )
        embed.add_field(
            name='사용법', 
            value='`냥이야 도박 <거는 돈/올인/절반>`', 
            inline=False
        )
        embed.add_field(
            name='거는 돈', 
            value='보유한 돈보다 더 많은 돈을 걸 수 없습니다', 
            inline=False
        )
        embed.add_field(
            name='확률', 
            value='일반 도박 : `실패 65%`, `2배 20%`, `3배 9%`, `5배 4%`, `특수 2%`\n올인 도박 : `실패 89%`, `4배 5%`, `5배 3%`, `7배 2%`, `특수 1%`', 
            inline=False
        )
        embed.add_field(
            name='올인', 
            value='거는 돈을 보유한 돈 전체로 설정합니다. 이 때, 실패율과 성공배율이 대폭 증가합니다', 
            inline=False
        )
        embed.add_field(
            name='절반', 
            value='거는 돈을 보유한 돈의 절반으로 설정합니다. 이 때, 확률은 일반도박과 동일합니다', 
            inline=False
        )
        embed.add_field(
            name='계산법', 
            value='`돈` = `보유한 돈` - `거는 돈` + (`거는 돈` x `배율`)', 
            inline=False
        )
        await message.channel.send(embed=embed)
    
    elif message.content.startswith('냥이야 도박 '):
        value = message.content.split(' ')
        value = value[2]
        if value == '올인':
            value = int(catmoney[message.author.id])
            if value == 0:
                await message.channel.send('보유한 돈이 없으면 올인을 할 수 없다냥')
            else:
                g1 = ['fail'] * 89
                g2 = ['x4'] * 5
                g3 = ['x5'] * 3
                g4 = ['x7'] * 2
                g5 = ['x150']
                gambling = g1+g2+g3+g4+g5
                final = random.choice(gambling)
                if final == 'fail':
                    catmoney[message.author.id] = 0
                    await message.channel.send('도박에 실패해서 <@'+str(message.author.id)+'> 의 돈은 **0원**이 되었다냥!')
                elif final == 'x4':
                    catmoney[message.author.id] = value * 4
                    await message.channel.send('4배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x5':
                    catmoney[message.author.id] = value * 5
                    await message.channel.send('5배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x7':
                    catmoney[message.author.id] = value * 7
                    await message.channel.send('7배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x150':
                    catmoney[message.author.id] = value * 150
                    await message.channel.send('**당첨!!!**\n150배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                await client.get_channel(790406561070972948).send(catmoney)
        elif value == '절반':
            if int(catmoney[message.author.id]) == 1:
                await message.channel.send('보유한 돈이 1원이면 절반도박을 할 수 없다냥')
            elif int(catmoney[message.author.id]) % 2 == 0:
                value = int(int(catmoney[message.author.id]) / 2)
                g1 = ['fail'] * 65
                g2 = ['x2'] * 20
                g3 = ['x3'] * 9
                g4 = ['x5'] * 4
                g5 = ['x100', 'website']
                gambling = g1+g2+g3+g4+g5
                final = random.choice(gambling)
                if final == 'fail':
                    catmoney[message.author.id] = catmoney[message.author.id] - value
                    await message.channel.send('도박에 실패해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x2':
                    catmoney[message.author.id] = catmoney[message.author.id] + (value * 2) - value
                    await message.channel.send('2배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x3':
                    catmoney[message.author.id] = catmoney[message.author.id] + (value * 3) - value
                    await message.channel.send('3배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x5':
                    catmoney[message.author.id] = catmoney[message.author.id] + (value * 5) - value
                    await message.channel.send('5배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x100':
                    catmoney[message.author.id] = catmoney[message.author.id] + (value * 100) - value
                    await message.channel.send('**당첨!**\n100배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'website':
                    await message.channel.send('도박은 너무 많이 하면 해롭다냥!\nhttps://www.kcgp.or.kr/pcMain.do')
                await client.get_channel(790406561070972948).send(catmoney)
            elif int(catmoney[message.author.id]) % 2 == 1:
                value = int((int(catmoney[message.author.id])-1) / 2)
                g1 = ['fail'] * 65
                g2 = ['x2'] * 20
                g3 = ['x3'] * 9
                g4 = ['x5'] * 4
                g5 = ['x100', 'website']
                gambling = g1+g2+g3+g4+g5
                final = random.choice(gambling)
                if final == 'fail':
                    catmoney[message.author.id] = catmoney[message.author.id] - value
                    await message.channel.send('도박에 실패해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x2':
                    catmoney[message.author.id] = catmoney[message.author.id] + (value * 2) - value
                    await message.channel.send('2배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x3':
                    catmoney[message.author.id] = catmoney[message.author.id] + (value * 3) - value
                    await message.channel.send('3배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x5':
                    catmoney[message.author.id] = catmoney[message.author.id] + (value * 5) - value
                    await message.channel.send('5배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'x100':
                    catmoney[message.author.id] = catmoney[message.author.id] + (value * 100) - value
                    await message.channel.send('**당첨!**\n100배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                elif final == 'website':
                    await message.channel.send('도박은 너무 많이 하면 해롭다냥!\nhttps://www.kcgp.or.kr/pcMain.do')
                await client.get_channel(790406561070972948).send(catmoney)
        else:
            try:
                value = int(value)
                if value < 1:
                    await message.channel.send('거는 돈으로는 자연수만 올 수 있다냥')
                else:
                    if value > int(catmoney[message.author.id]):
                        await message.channel.send('거는 돈이 보유한 돈보다 많을 수는 없다냥')
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
                            await message.channel.send('도박에 실패해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥')
                        elif final == 'x2':
                            catmoney[message.author.id] = catmoney[message.author.id] + (value * 2) - value
                            await message.channel.send('2배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥')
                        elif final == 'x3':
                            catmoney[message.author.id] = catmoney[message.author.id] + (value * 3) - value
                            await message.channel.send('3배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥')
                        elif final == 'x5':
                            catmoney[message.author.id] = catmoney[message.author.id] + (value * 5) - value
                            await message.channel.send('5배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥')
                        elif final == 'x100':
                            catmoney[message.author.id] = catmoney[message.author.id] + (value * 100) - value
                            await message.channel.send('**당첨!**\n100배 도박에 성공해서 <@'+str(message.author.id)+'> 의 돈은 **'+str(catmoney[message.author.id])+'원**이 되었다냥!')
                        elif final == 'website':
                            await message.channel.send('도박은 너무 많이 하면 해롭다냥!\nhttps://www.kcgp.or.kr/pcMain.do')
                        await client.get_channel(790406561070972948).send(catmoney)
            except ValueError:
                saylist = ['도대체 뭘 걸겠다는거냥..?','장난치지 마라냥!']
                say = random.choice(saylist)
                await message.channel.send(str(say))
                
# [기타]/예외처리

    elif message.content.startswith('냥이야 '):
        saylist = ['냥...?','냥?','무슨 말인지 모르겠다냥']
        say = random.choice(saylist)
        await message.channel.send(str(say))

# [기타]/명령어

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
                                        await message.channel.send(str(name)+'의 현재 돈은 **'+str(catmoney[int(name)])+'원**이다냥')
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
                                        await message.channel.send(str(name)+'의 돈을 **'+str(test)+'원**으로 설정했다냥')
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
            await message.channel.send('관리자도 아닌게 어딜 까불고 있냥?')


client.run(os.environ["BOT_TOKEN"])

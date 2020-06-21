import discord
import os

client = discord.Client()
prefix = "냥이야"


@client.event
async def on_ready():
    print("후아아암~ 잘 잤다냥!")
    game = discord.Game("내가 놀아주러 왔다냥!")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    # 수학
    if message.content.endswith(f'{prefix} 가감'):
        await message.channel.send('(1) 더하거나 뺴는 일. 또는 그렇게 하여 알맞게 맞추는 일.')
        await message.channel.send('(2) 덧셈과 뺄셈을 아울러 이르는 말.')

    if message.content.endswith(f'{prefix} 가감법'):
        await message.channel.send('(1) 덧셈과 뺄셈을 하는 방법.')
        await message.channel.send('(2) 두 개 이상의 미지수를 가진 연립 방정식에서 한 미지수의 계수를 곱셈이나 나눗셈을 써서 같게 만든 후, 더하거나 빼어 그 미지수를 없애는 '
                                   '방법.')

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

    if message.content.endswith(f'{prefix} '):
        await message.channel.send('')

    if message.content.endswith(f'{prefix} '):
        await message.channel.send('')


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

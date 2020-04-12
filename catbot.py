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
#인사
    if message.content.startswith("냥이야 안녕"):
        await message.channel.send("다음부턴 고양이말로 인사해라냥")

    if message.content.startswith("냥이야 안냥"):
        await message.channel.send("반갑다냥!")

    if message.content.startswith("냥이야 반가워"):
        await message.channel.send("나도 반갑다냥")
#중1
    if message.content.startswith("냥이야 거듭제곱"):
        embed = (color=0x00D8FF)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/698905428008108073/2e951eacfe5b6cfc.png")
        await message.channel.send("같은 수나 문자를 거듭하여 곱한 것", embed=embed)



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

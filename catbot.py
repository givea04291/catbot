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
    if message.content.startswith(".안녕"):
        await message.channel.send("다음부턴 고양이말로 인사해라냥")

    if message.content.startswith(".안냥"):
        await message.channel.send("반갑다냥!")

    if message.content.startswith(".반가워"):
        await message.channel.send("나도~")

    if message.content.startswith(".테스트"):
        embed = discord.Embed(title="ㅇ", description="ㅇ", color=0xFFD9FA)
        embed.add_field(name="ㅇ", value="ㅇ", inline=True)
        embed.add_field(name="ㅇ", value="ㅇ", inline=True)
        embed.add_field(name="ㅇ", value="ㅇ", inline=True)
        embed.set_image(url="https://media.discordapp.net/attachments/698830342458703912/698830915207430174/827aaf13e2f1acea.png?width=914&height=514")
        embed.set_footer(text="ㅇㅇ")
        await message.channel.send("ㅇㅇㅇㅇㅇ", embed=embed)



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

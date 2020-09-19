from discord.ext import commands
import os
import traceback
import discord
from googletrans import Translator

bot = commands.Bot(command_prefix='/')
token = os.environ['NzU2ODg4MTYwNTkxNDEzMzE5.X2YZBw.nB6NGpQlObRwEt6RtZBMMBReJv8']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzU2ODg4MTYwNTkxNDEzMzE5.X2YZBw.nB6NGpQlObRwEt6RtZBMMBReJv8'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@client.event
async def on_reaction_add(reaction, user):
    print("emoji-id")
    print(reaction.emoji.id)
    if reaction.count == 1:
        # 日本語訳
        if reaction.emoji.id == 687336060556017758:
            translator = Translator()
            trans_en = translator.translate(reaction.message.content, src='en', dest='ja')
            await reaction.message.channel.send(trans_en.text)


        # 英語訳
        if reaction.emoji.id == 687336087408214062:
            translator = Translator()
            trans_en = translator.translate(reaction.message.content, src='ja', dest='en')
            await reaction.message.channel.send(trans_en.text)



# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)


bot.run(token)

from discord.ext import commands
imprt discord
import os
import traceback
import random

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
     if message.content == '!vc':
          userID = []
          userNAME = []

          #ユーザーIDの取得
          user_id = message.author.voice.channel.voice_states.keys()
          for users in user_id:
              print(users)
          userID += user_id
          print("ユーザーIDの取得完了")

          #ユーザーネームの取得
          ID_len = len(userID)
          i = 0
          while i < ID_len:
               ID = str(userID[int(i)])
               user = await client.fetch_user(ID)
               MESSAGE = user.name, user.discriminator, str(user)
               userNAME.insert(0, MESSAGE[0])
               i += 1
               
          #ブキルーレットのチャット
          i = 0
          while i < len(userNAME):
               r = random.randint(1, 129)
               await message.channel.send("**" + str(userNAME[i]) + "**さんは**__" + str(Buki_all[int(r)]) + "__**でし！")
               i += 1
               
     if message.content == '!buki':
          await message.channel.send('でしでし！')

bot.run(token)

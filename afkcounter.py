import discord, random, os, time
from discord.ext import commands

token = input("Enter Token: ")

class counter(discord.Client):
    async def on_ready(self):
        os.system('cls')
        os.system(f'title [COUNTER]')
        os.system(f'mode 30,15')
        print(f""" \u001b[31m
         ╔═╗╔═╗╦╔═
         ╠═╣╠╣ ╠╩╗
         ╩ ╩╚  ╩ ╩ \u001b[35m@9n8
       \u001b[33m---------------
""")
       
        print('\u001b[32m    logged in as {0}'.format(self.user))
    async def on_message(self, message):
        channel = message.channel
        if 'afk' in message.content:
          for i in range(1, 1001):
            await message.channel.send(i)
      

client = counter()


client.run(token, bot=False)

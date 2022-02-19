import discord, os, asyncio, sys, time

from pystyle import Colors, Colorate

from discord.ext import commands


def slow_write(t):
    for f in t: print('' + f, end="");sys.stdout.flush();time.sleep(0.0005)

slow_write("\u001b[38;5;159m-> Insert Token; ")
token = input()

class counter(discord.Client):
    async def on_ready(self):
        os.system('cls')
        os.system(f'title [COUNTER]')
        os.system(f'mode 30,15')
        slow_write(""" \u001b[31m
         ╔═╗╔═╗╦╔═
         ╠═╣╠╣ ╠╩╗
         ╩ ╩╚  ╩ ╩ \u001b[35m@9n8
       \u001b[33m---------------
""")
       
        print('\u001b[32m    logged in as {0}'.format(self.user))
    async def on_message(self, message):
        channel = message.channel
        if 'check' in message.content:
          for i in range(1, 101):
            await message.channel.send(i)
      

client = counter()


client.run(token, bot=False)

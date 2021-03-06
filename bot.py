import discord
import math
import random

TOKEN = 'NTU0ODUxOTY5NDM3NjYzMjMy.D2ip0g.d4ZEPBt5SNyLrPHAObAuIKgGgPo'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('!roll'):
        number = random.randint(1,101)
        msg = '{0.author.mention} rolled:'.format(message) + ' {}'.format(number)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
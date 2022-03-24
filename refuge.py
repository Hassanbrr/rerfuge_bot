import discord
from discord.ext import commands
import asyncio
from asyncio import * 
class CONFIG:
    TOKEN = 'ODk2MzkxMDA5MjQ2NzgxNDcx.YWGbLg.YnVp7XrFBeIgy6N34fuDf3Qyr7E'
    PREFIX = '-'

client = commands.Bot(command_prefix=CONFIG.PREFIX)
voice_object = None

@client.event
async def on_ready():
    print('bot online shod')
  
@client.command()

async def join(ctx):
  global voice_object
  my_channel = ctx.message.author.voice.channel
  #my_channel = client.get_channel(956470964575674383)
  voice_object = await my_channel.connect()
  voice_object.play(discord.FFmpegPCMAudio('https://cdn.discordapp.com/attachments/940539327350472715/956503845301805136/AUD-20220324-WA0000.mp3'))
  await ctx.send('man omadam ro voice ha ha ha :)))')
@client.command()
async def disconnect(ctx):
  global voice_object
  if voice_object != None:
    await voice_object.disconnect()
    voice_object = None
    await ctx.send('man raftm bye')
  else:
    await ctx.send('bot is disconnect')
  my_channel = ctx.message.author.voice.channel
  

@client.command()
async def cmd(ctx):
        await ctx.send('@everyone ki omade??! ')
@client.command()
async def setstatus(ctx, status_type):
  if(status_type == 'idle'):
    await ctx.send('status be idle taghir kard')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Shirin"))

  elif(status_type == 'dnd'):
    await ctx.send('status be dnd taghir kard')
    await client.change_presence(activity=discord.status.dnd )

@client.command()
async def setactivity(ctx, activity_type, *, activit_text):
  if (activity_type == 'listening') :
    await client.change_presnce(activity=discord.Activity(type=discord.activitytype.listdiscord.activitytype.listenig, name="activity_text"))
    
@client.command()
async def clear(ctx, count='10'):
  count = int(count)
  await ctx.channel.purge(limit=count+1)
  await ctx.send(">>> "+str(count)+'message delete shod.')

client.run(CONFIG.TOKEN)

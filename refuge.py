import discord
from discord.ext import commands
import asyncio
from asyncio import * 


class CONFIG:
    TOKEN = 'ODk2MzkxMDA5MjQ2NzgxNDcx.YWGbLg.s8Ef36tBVd1A89afbRzo5uQ-o_s'
    PREFIX = '-'

client = commands.Bot(command_prefix=CONFIG.PREFIX)

@client.event
async def on_ready():
    print('man online shodm')
    

    
voice_object = None



  
@client.command(aliases=['p', 'play'])

async def join(ctx):
  global voice_object
  my_channel = ctx.message.author.voice.channel
  #my_channel = client.get_channel(956470964575674383)
  voice_object = await my_channel.connect()
  voice_object.play(discord.FFmpegPCMAudio('https://cdn.discordapp.com/attachments/943190929672658964/957278306451996793/Koorosh_-_Yebaram_Man_Ft_Arta_Behzad_Leito__Raha_128.mp3'))
  await ctx.send('man omadam ro voice ha ha ha :)))')
@client.command(aliases=['dc'])

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
async def refuge(ctx):
        await ctx.send('@everyone (((i dont belong here!!))) ')


@client.command()
async def setstatus(ctx, status_type):
  if(status_type == 'shirin'):
    await ctx.send('status taghir kard')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Swan"))

  elif(status_type == 'hassan'):
    await ctx.send('status taghir kard')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Beluga whale"))

  elif(status_type == 'alireza'):
    await ctx.send('status taghir kard')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Grizzly bear"))
    


@client.command()
async def setactivity(ctx, activity_type, *, activit_text):
  if (activity_type == 'listening') :
    await client.change_presnce(activity=discord.Activity(type=discord.activitytype.listdiscord.activitytype.listenig, name="activity_text"))
    

@client.command(aliases=['clear', 'clean'])
async def dastor_paksazi(ctx, count='10'):
  count = int(count)
  await ctx.channel.purge(limit=count+1)
  await ctx.send(">>> "+str(count)+'message delete shod.')


client.run(CONFIG.TOKEN)

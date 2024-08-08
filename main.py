#imports required dependicies for discord
import discord
#import the bottoken
import os
from dotenv import load_dotenv
from discord.ext import commands
#queue data structure
from collections import deque 

#importing dependices of playing yt songs
import yt_dlp as yt
load_dotenv()
#these options configure ffmpeg to process audio and youtube-dl to download the best audio format froma single video
FFMEG_OPTIONS = {'options':'-vn'}
YDL_OPTIONS = {'format' : 'bestaudio' , 'noplaylist' : True}

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.voice_states = True

#call the bot when ! is used
client = commands.Bot(command_prefix ='!', intents=intents) 
queue = deque([])

#bot is ready to receive commands
@client.event
async def on_ready(): 
    print("Fanum tax the ohio rizzler")
    print("---------------------------")

#ctx takes the input from the user
@client.command()
async def hello(ctx):
    await ctx.send("Wop wop wop wop wop ima do my stuff")

@client.command()
async def goodbye(ctx):
    await ctx.send("they not like us they not like us")

@client.command()
async def rick(ctx):
    await ctx.send("fuck you")

#when an event function detects something it would something else
@client.event
async def on_member_join(member):
    channel = client.get_channel(1269145446052270174)
    await channel.send(f"Hello, {member.mention}")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1269145446052270174)
    await channel.send(f"Goodbye, {member.mention}")

#if user in a voice chat and uses this command the bot will join
@client.command()
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("get in a voice channel jittleyang")

#makes the bot leave voice chat if it is in one
@client.command() 
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("i need to futtulatugan else where fonem")
    else:
        await ctx.send("i aint even in a voice chat dumbass")
@client.command()
async def __init__(self, client):
        self.client = client
        self.queue = []

trim = False

@client.command(pass_context=True)
async def play(ctx, * , search):
    voice_channel = ctx.author.voice.channel if ctx.author.voice else None
    if not voice_channel:
        return await ctx.send("get in the call dumbass")
    if not ctx.voice_client:
        await voice_channel.connect()
    voice = ctx.guild.voice_client
    async with ctx.typing():
        with yt.YoutubeDL(YDL_OPTIONS) as ydl: 
            info = ydl.extract_info(search, download = False) #grabs the info from yt
            url = info['url']
            title = info['title']
        voice.play(discord.FFmpegPCMAudio(url))
        await ctx.send(f'Now Playing: **{title}**')
    
    while not ctx.voice_client.is_playing():
        # if trim:
        #     print('george')
        #     voice.play(discord.FFmpegPCMAudio(song['url']))
        if queue:
            song = queue.popleft()
            voice.play(discord.FFmpegPCMAudio(song['url']))
            await ctx.send(f'Now Playing: **{song['title']}**')
        else:
            await ctx.send('There are no more songs left to play')

    #add song to queue
    @client.command()
    async def add(ctx, *, search):
        with yt.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(search, download = False)
            title = info['title']
        queue.append(info)
        await ctx.send(f'Added to queue: **{title}**')
        if not ctx.voice_client.is_playing():
            if queue:
                print("fantum")
                song = queue.popleft()
                voice.play(discord.FFmpegPCMAudio(song['url']))
                await ctx.send(f'Now Playing: **{song['title']}**')
            else:
                await ctx.send('There are no more songs left to play')
        
    @client.command()
    async def clear(ctx):
        if ctx.voice_client:
            if queue:
                queue.clear()
                await ctx.send('Queue Cleared')
            else:
                await ctx.send('There is nothing to clear')
                
    def getTitle(index):
            return index['title']
            
    
    @client.command() 
    async def playlist(ctx):
        if queue:
            await ctx.send(f'{index + 1}. {title}' for index, title in enumerate(map(getTitle , queue)))
        
        

    #this th the skip command
    @client.command()
    async def skip(ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("This song is some ass play the next one")
            if queue:
                song = queue.popleft()
                voice.play(discord.FFmpegPCMAudio(song['url']))
                await ctx.send(f'Now Playing: **{song['title']}**')
            else:
                await ctx.send('There are no more songs left to play')


    @client.command()
    async def stop(ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("Music stopped")
        
            
    @client.command()
    async def loop(ctx):
        global trim
        print('fanum')
        if trim:
            trim = False
        else:
            trim = True
            await ctx.send(f'Now looping lee: **{title}**')
            print('hacker')
                
client.run(os.getenv('DISCORD_TOKEN'))



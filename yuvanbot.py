import discord
import tweepy
import io
import os
import imgkit
import chat_exporter
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

ckey = 'jDcuUN7fL9a28tZOQppUlXl8d'
csecret = 'X6Y1M2S9tnvCJmTnuWvKtvcsPlIEYeWEQdpazoIVaWZdlCA8sY'
atoken = '1368016589782544391-K1F02CqppvsgtkN5UDAaBdfk8EfPQI'
asecret = 'NluQ1bCH9ocfuIvgg6oYMG3UZJ6fsefWcEdGW4PetnV9l'


twitter_auth_keys = { 
    "consumer_key"        : ckey,
    "consumer_secret"     : csecret,
    "access_token"        : atoken,
    "access_token_secret" : asecret
}
 
auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
        )
auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
        )
api = tweepy.API(auth)

client = commands.Bot(command_prefix="r ")

@client.event
async def on_ready():
    print("ready")
    chat_exporter.init_exporter(client)
    await client.change_presence(activity=discord.Game(name="with lil kids"))

@client.command()
async def hello(ctx):
    await ctx.send(ctx.author.mention+" vanakam to hackerman")
    await ctx.send("https://data1.ibtimes.co.in/en/full/676141/fake-picture-simbu-oviya.jpg?w=599&h=449&l=50&t=40")
    

@client.command()
async def thala(ctx):
    await ctx.reply("https://tenor.com/view/ajith-maavu-thala-vedalam-viswasam-gif-12088725")

@client.command()
async def sugar(ctx):
    await ctx.reply("https://tenor.com/view/jkledits-ajith-thala-ajithkumar-style-gif-13307846")

@client.command()
async def bobs(ctx):
    li=[]
    li.append(ctx.message)
    transcript = await chat_exporter.raw_export(ctx.channel, li)
    transcript_file = discord.File(io.BytesIO(transcript.encode()), filename=f"transcript-{ctx.channel.name}.html")
    fil = io.BytesIO(transcript.encode())
    config = imgkit.config(wkhtmltoimage='C:/Program Files/wkhtmltopdf/bin/wkhtmltoimage.exe')
    with open('test.html', "wb") as outfile:
        outfile.write(fil.getbuffer())
    with open('test.html', "r") as outfile:
        imgkit.from_file(outfile, 'out.jpg', config = config)
    text = 'What zero pussy does to an mf'
    media = api.media_upload("out.jpg")
    post_result = api.update_status(status=text, media_ids=[media.media_id])
@client.command()
async def breakbharathbot(ctx):
    while True:
        await ctx.send("bestu")

def search(query):
    with YoutubeDL({"format": "bestaudio", "noplaylist": "True"}) as ydl:
        try:
            requests.get(query)
        except:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"][0]
        else:
            info = ydl.extract_info(query, download=False)
    return (info, info["formats"][0]["url"])


@client.command()
async def yt(ctx, *, query=None):
    if query:
        FFMPEG_OPTS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }
        video, source = search(query)
        voice = get(client.voice_clients, guild=ctx.guild)

        channel = ctx.author.voice.channel

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        if not voice.is_playing():
            voice.play(
                discord.FFmpegPCMAudio(source, **FFMPEG_OPTS, executable="C:/Users/Sriram/Desktop/ffmpeg-4.3.2-2021-02-02-essentials_build/bin/ffmpeg"),
                after=lambda e: print("done", e),
            )
            voice.is_playing()
            text = 'Now playing: ' + query
            media = api.media_upload("test.jpg")
            post_result = api.update_status(status=text, media_ids=[media.media_id])
            await ctx.send(text)
        else:
            await ctx.send(f"ethana paatu ley podrathu")
    else:
        await ctx.send("enna paatu podanum nu sollu ley")


client.run("ODA5Njk1MDgwMDU4ODQ3Mjgz.YCY1Tg.9RoULwCNyt4Q9NtuNUmFE6u9etc")


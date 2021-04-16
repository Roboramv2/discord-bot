import tweepy
import io
import os
import imgkit
import chat_exporter
###########Insert your twitter bot credentials here################
ckey = '__'
csecret = '__'
atoken = '__'
asecret = '__'

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

####################discord bot commands for twitter#########################
@client.command()
async def putthisup(ctx): #takes a screenshot of trigger message and posts on twitter
    li=[]
    li.append(ctx.message)
    transcript = await chat_exporter.raw_export(ctx.channel, li)
    transcript_file = discord.File(io.BytesIO(transcript.encode()), filename=f"transcript-{ctx.channel.name}.html")
    fil = io.BytesIO(transcript.encode())
    config = imgkit.config(wkhtmltoimage='__')#insert path of wkhtmltoimage application inside bin of wkhtmltopdf software
    with open('test.html', "wb") as outfile:
        outfile.write(fil.getbuffer())
    with open('test.html', "r") as outfile:
        imgkit.from_file(outfile, 'out.jpg', config = config)
    text = 'Does this work?'
    media = api.media_upload("out.jpg")
    post_result = api.update_status(status=text, media_ids=[media.media_id])


@client.command()
async def post(ctx, *, text):
    post_result = api.update_status(status=text, media_ids=[media.media_id])
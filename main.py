import discord
from discord.ext import commands
from time import sleep
import random
from discord import DMChannel
import glob
import os
import string

TOKEN = 'Your bot token'

client = discord.Bot()

@client.event
async def on_ready():
    print("Ready to start")
   
@client.slash_command()
async def nitrogen(ctx, many):
    for i in range(int(many)):
        a="https://discord.gift/"
        code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        await ctx.channel.send(a +code)
        await ctx.respond("finished")

@client.slash_command()
async def paypayurlgen(ctx, many):
    for i in range(int(many)):
        b="https://pay.paypay.ne.jp/"
        codee = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
        await ctx.channel.send(b +codee)
        await ctx.respond("finished")
        
@client.slash_command()
async def originalgen(ctx):
    user = await client.fetch_user(int(ctx.author.id))
    genpass=r"Write your gen pass. example. C:\\Users\\nagato\\3D Objects\\toilet\\watermelon\\proxy"
    list=glob.glob(genpass+'\\*.txt')
    for i in range(1):
        data=random.choice(list)
        data1=os.path.split(data)[1]
        print(data1)
        await ctx.respond("Check the DM")
        await user.send(file=discord.File(data))
        os.remove(data)
        
client.run(TOKEN) 

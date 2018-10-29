#"Fake Mehmet" Bot By Mehmet

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print ("Activation: Working")
    print ("Bot Name: " + bot.user.name)
    print ("Bot ID: " + bot.user.id)

@bot.command(pass_context=True)
async def Store(ctx):
    await bot.say("https://selly.gg/@UnfairGame")

@bot.command(pass_context=True)
async def Status(ctx):
    await bot.say("""

***Rainbow:*** `Open For Pre-Order - Remaking`
***FN Global:*** `In Stock - Undetected / Remaking on background `
***FN Vengence:*** `In Stock - Undetected`
***FN Desync:*** `In Stock - Updating`
***Dead By Daylight*** `In Stock - Undetected`
***Scum:*** `In Stock - Undetected`
***Pubg:*** `Closed`
    
    """)



@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here your shits.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here server shits.", color=0x00ff00)
    embed.set_author(name="Unfairgame.us")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await bot.say("This cunt is kicked! {}.".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    await bot.say("This cunt is banned! {}.".format(user.name))
    await bot.ban(user)

@bot.command()
async def echo(message: str):
    await bot.say(message)

@bot.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await bot.say('{0} joined at {0.joined_at}'.format(member))

@bot.command(pass_context=True)
async def BotInfo(ctx):
    await bot.say("Im the dumb bot and Mehmet is my Daddy :smile: ")

@bot.command(pass_context=True)
async def FuckYouBot(ctx):
    await bot.say (" Fuck your self kiddo. Im going to ban your toxic ass.")

@client.event
async def on_message(message):
    if message.content.startswith('!delete me'):
        msg = await client.send_message(message.channel, 'Your message deleted daddy')
        await client.delete_message(msg)

@client.event
async def on_message_delete(message):
    fmt = '{0.author.name} has deleted the message:\n{0.content}'
    await client.send_message(message.channel, fmt.format(message))

@bot.command(pass_context=True)
async def verify(ctx):
    server = member.server
    fmt = " -new {0.author} "
    await bot.say(server, fmt.format(member, server))


@bot.command(pass_context=True)
async def Bulk(ctx):
    await bot.say("Global and Rainbow Bulk Prices:")
    await bot.say("http://resimag.com/p1/0d5090a449.png")

@bot.command(pass_context=True)
async def Commands(ctx):
    await bot.say("http://prntscr.com/kxjzvt")



@bot.command(pass_context=True)
async def VerifyChannel(ctx):
    await bot.say(""" ```https://selly.gg/@UnfairGame```
========================================================
` DO YOU NEED HELP?`
Create Support Ticket. When one of the Supports or Admin able for help he will reply your ticket! 

`HOW TO BE VERIFIED?`
Create Support Ticket with your Order ID

`HOW TO CREATE SUPPORT TICKET?`
Send message in channel with ***-new***  command 
example: 
***-new <Your Description>***

`DO YOU WANT TO BECOME A RESELLER?`
Check Bulk prices with ***!Bulk*** command
Than PM ***Mehmet#0001*** for buy

`For See Bot Commands`
Write ***!Commands*** 
========================================================
@everyone
```https://selly.gg/@UnfairGame``` """)


@bot.command(pass_context=True)
async def InformationChannel(ctx):
    await bot.say("""***==========================================================
If you dont have Verified role you cant see channels.
Create ticket with your Order ID for get verified role!


If you need any help or need loader create a ticket.
When one of the Supports or Admin able for help he will reply your ticket! 

How to create Ticket:
Send message in channel with -new command 

example:
-new <Your Description>

Bot Commands for subscription

!Store
!Bulk
==========================================================***
@everyone""")

bot.run("NDg2MjQ0NDM4NTkxNDA2MTAw.DnMkzw.CVH8S9eACB3avj_o5GM7h1un534")

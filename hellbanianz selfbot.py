import discord
from discord.ext import commands
import colorama
from colorama import Fore
import os

colorama.init()
hellprefixallbanianz = input('Prefix: ')
helltokenallbanianz = input('Token: ')

client = commands.Bot(command_prefix=hellprefixallbanianz, self_bot=True)

os.system(f'cls & title [ Hellbanianz ] - Selfbot')
@client.event
async def on_ready():
  print(f'''
{Fore.RED}

 ██░ ██ ▓█████  ██▓     ██▓     ▄▄▄▄    ▄▄▄       ███▄    █  ██▓ ▄▄▄       ███▄    █ ▒███████▒
▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    ▓█████▄ ▒████▄     ██ ▀█   █ ▓██▒▒████▄     ██ ▀█   █ ▒ ▒ ▒ ▄▀░
▒██▀▀██░▒███   ▒██░    ▒██░    ▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒▒██  ▀█▄  ▓██  ▀█ ██▒░ ▒ ▄▀▒░ 
░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    ▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░░██▄▄▄▄██ ▓██▒  ▐▌██▒  ▄▀▒   ░
░▓█▒░██▓░▒████▒░██████▒░██████▒░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░░██░ ▓█   ▓██▒▒██░   ▓██░▒███████▒
 ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒
 ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░  ▒   ▒▒ ░░ ░░   ░ ▒░░░▒ ▒ ░ ▒
 ░  ░░ ░   ░     ░ ░     ░ ░    ░    ░   ░   ▒      ░   ░ ░  ▒ ░  ░   ▒      ░   ░ ░ ░ ░ ░ ░ ░
 ░  ░  ░   ░  ░    ░  ░    ░  ░ ░            ░  ░         ░  ░        ░  ░         ░   ░ ░    
                                     ░                                               ░        



''')

@client.command()
async def test(ctx):
    imageURL = "https://discordapp.com/assets/e4923594e694a21542a489471ecffa50.svg"
    embed = discord.Embed()
    embed.set_image(url=imageURL)
    await ctx.send(embed=embed)

@client.command()
async def channelcr(ctx):
  await ctx.message.delete()
  guild = ctx.message.guild
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')
  await guild.create_text_channel('nuked')

client.run(helltokenallbanianz, bot=False)

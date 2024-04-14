import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
	print('Bot Is Ready')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	embeded = discord.Embed(description=f'I Couldn`t Find That Command!', color=0xe74c3c)
    	await ctx.send(embed=embeded)

@client.command(aliases=['Purge','PURGE'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
	await ctx.channel.purge(limit=amount)
	embeded = discord.Embed(description=f'***Deleted {amount} Messages***', color=0x2ecc71)
	await ctx.send(embed=embeded)

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embeded = discord.Embed(description=f'You Can`t Purge Messages!', color=0xe74c3c)
        await ctx.send(embed=embeded)

@client.command(aliases=['Kick','KICK'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, n=None):
    await member.kick(reason=n)
    embeded = discord.Embed(description=f'***{member} Was Kicked!***', color=0x2ecc71)
    await ctx.send(embed=embeded)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embeded = discord.Embed(description=f'You Can`t Kick Members!', color=0xe74c3c)
        await ctx.send(embed=embeded)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embeded = discord.Embed(description=f'***Kick <member> <reason>***', color=0x2ecc71)
        await ctx.send(embed=embeded)

@client.command(aliases=['Ban','BAN'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embeded = discord.Embed(description=f'***{member} Was Banned!***', color=0x2ecc71)
    await ctx.send(embed=embeded)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
    	embeded = discord.Embed(description=f'You Can`t Ban Members!', color=0xe74c3c)
      await ctx.send(embed=embeded)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embeded = discord.Embed(description=f'***Ban <member> <reason>***', color=0x2ecc71)
        await ctx.send(embed=embeded)

client.run('Bot Token Here')

import discord
from discord.ext import commands

### Configuration ###
bot_token = 'YOUR TOKEN'
bot_prefix = '.'
bot_tag = '[SIMPLE DISCORD BOT] '
bot_name = 'SIMPLE DISCORD BOT'

### Connect/Disconnect bot ###
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")

@client.event
async def on_ready():
    print(bot_tag + 'Bot is ready.\n' +
          bot_tag + 'Prefix: \"' + bot_prefix + '\"\n' +
          bot_tag + 'Created by: GitHub.com/BarthVisuals')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Change this."))

@client.event
async def on_disconnect():
    print(bot_tag + 'Error!.\n' +
          bot_tag + 'Bot stopped.' +
          bot_tag + 'Created by: GitHub.com/BarthVisuals')
    await client.close()

### Commands ###

# Help message
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", color=0x00ff00)
    embed.set_footer(text='GitHub.com/BarthVisuals | 2020')
    embed.add_field(name=bot_prefix + "bot_info", value="Bot informations (ping etc.)", inline=False)
    embed.add_field(name=bot_prefix + "ban", value="Ban user from this server.", inline=False)
    embed.add_field(name=bot_prefix + "kick", value="Kick user from this server.", inline=False)
    embed.add_field(name=bot_prefix + "say", value="Send message as bot.", inline=False)
    await ctx.send(embed = embed)

# Private message | Bot informations
@client.command()
@commands.has_permissions(administrator = True)
async def bot_info(ctx):
    await ctx.message.delete()
    await ctx.author.send(f'Ping: {round(client.latency * 1000)}ms')


# Ban command
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    embed = discord.Embed(title="BANNED", color=0xff0000)
    embed.set_footer(text='GitHub.com/BarthVisuals | 2020')
    embed.add_field(name="Reason:", value=reason, inline=True)
    embed.add_field(name="User: ", value=member.display_name, inline=True)
    await ctx.send(embed = embed)
    await ctx.author.send('You banned user!\ninformations:')
    await ctx.author.send(embed= embed)

# Kick command
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    embed = discord.Embed(title="KICKED", color=0xff0000)
    embed.set_footer(text='GitHub.com/BarthVisuals | 2020')
    embed.add_field(name="Reason:", value=reason, inline=True)
    embed.add_field(name="User: ", value=member.display_name, inline=True)
    await ctx.send(embed = embed)
    await ctx.author.send('You kicked user!\ninformations:')
    await ctx.author.send(embed = embed)

# Say command
@client.command()
@commands.has_permissions(administrator = True)
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

client.run(bot_token)

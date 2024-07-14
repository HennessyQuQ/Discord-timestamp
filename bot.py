import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print("Discord 機械人已连接！")

@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick(reason="被 Discord 機械人踢出")
    await ctx.send(f"{member.name} 已被踢出！")
    
@bot.command(name="commands")
async def commands(ctx):
    commands = bot.commands

    help_message = f"**可用命令：**\n"
    for command in commands:
        help_message += f"- `{command.name}`: {command.help}\n"

    await ctx.send(help_message)
    
@bot.command(name="timestamp")
async def timestamp(ctx):
    dt = datetime.utcnow()
    timestamp = int(dt.timestamp())
    await ctx.send(f"时间戳：{timestamp}")
    
@bot.event
async def on_message(message):
    if message.content.startswith("!timestamp"):
        if bot.is_ready():
            dt = datetime.utcnow()
            timestamp = int(dt.timestamp())
            await message.channel.send(f"时间戳：{timestamp}")
        else:
            await message.channel.send("Discord 機械人尚未连接！")

bot.run("YOUR_BOT_TOKEN")

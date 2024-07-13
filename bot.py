import discord
from datetime import datetime

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("!timestamp"):
        dt = datetime.now()
        timestamp = int(dt.timestamp())
        await message.channel.send(f"時間戳：{timestamp}")

client.run("YOUR_BOT_TOKEN")

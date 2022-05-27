import discord
from discord.ext import commands
import os
os.system("clear")

channel = input("Channel ID: ")

bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
	print(f"{bot.user} On ready[]")
	
@bot.command()
async def send(ctx,member:discord.Member,text):
	if (str(ctx.message.channel.id) == f"{channel}"):
		await member.send(f"{text}")
		await ctx.channel.send("สำเร็จ",delete_after=5)
		await ctx.message.delete()
	
bot.run("โทเคนบอท")

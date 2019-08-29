import discord
import discord.abc
from discord.ext import commands
from redbot.core import commands
import asyncio
import json

Cog = getattr(commands, "Cog", object)

class Moderation(Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def purge(ctx, number):
		"""Mass deletes messages."""
		
		messages = []
		number = int()
		channel = ctx.message.channel
		async for x in channel.logs_from(ctx.message.channel, limit = number):
			messages.append(x)
		
		await Client.delete_messages(messages)





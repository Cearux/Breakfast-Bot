import discord
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
		number = int(number)
		async for x in Client.logs_from(message.channel, limit = number):
			messages.append(x)
		
		await Client.delete_messages(messages)





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
		number = int()
		async for x in client.logs_from(ctx.message.channel, limit = number):
			messages.append(x)
		
		await client.delete_messages(messages)





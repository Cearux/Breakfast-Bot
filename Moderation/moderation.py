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

	@commands.command(pass_context=True)
	async def purge(ctx, number):
		"""Mass deletes messages."""
		
		messages = []
		number = int()
		client = discord.Client()
		
		async for x in ctx.message.channel(limit = number):
			messages.append(x)
		
		await client.delete_messages(messages)





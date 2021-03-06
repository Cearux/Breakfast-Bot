import discord
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


	@commands.command(pass_context=True)
	async def punish(self, ctx, user: discord.Member):
		"""Assigns 'muted' role to user."""
		
		role = discord.Role(role: "Muted")
		await self.bot.add_roles(user, role)
		await self.bot.say("User muted.")
		
	@commands.command(pass_context=True)
	async def unpunish(self, ctx, user: discord.Member):
		"""Removes 'muted' role."""
		
		role = discord.Role(name="Muted")
		await self.bot.remove_roles(user, role)
		await self.bot.say("User unmuted.")

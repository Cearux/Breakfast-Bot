import discord
from discord.ext import commands
import asyncio
import json

class Moderation:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def :


def setup(bot):
	bot.add_cog(Moderation(bot))


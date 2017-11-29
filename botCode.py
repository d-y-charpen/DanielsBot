import random
import secretSauce
import helperFuncs
import discord
from discord.ext import commands

bot = commands.Bot(description = "this is daniel's robot. commands are prefixed with a '!'",
command_prefix = "!")

class Basics:
	@commands.command()
	async def ping(self):
		"""Tests if the bot is active."""
		await bot.say("Pong!")

	@commands.command()
	async def best(self):
		"""Ask who the best champion is."""
		await bot.say("Nautilus, of course.")
		
	@commands.command()
	async def worst(self):
		"""Ask who the worst champion is."""
		await bot.say(random.choice(helperFuncs.champ_list) + ", probably.")
		
		
bot.add_cog(Basics())


bot.run(secretSauce.runID)


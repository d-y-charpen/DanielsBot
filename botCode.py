import random
import secretSauce
import helperFuncs
import discord
from discord.ext import commands

bot = commands.Bot(description = "this is daniel's robot. commands are prefixed with a '!'",
command_prefix = "!")


@bot.command()
async def ping():
	"""Tests if the bot is active."""
	await bot.say("Pong!")

@bot.command()
async def best():
	"""Ask who the best champion is."""
	await bot.say("Nautilus, of course.")
	
@bot.command()
async def worst():
	"""Ask who the worst champion is."""
	await bot.say(random.choice(helperFuncs.champ_list) + ", probably.")

class LeagueOfLegends:
	@commands.command(pass_context=True)
	async def profile(self,ctx,name=""):
		"""Pull up some data on either your nickname or provided name"""
		if(name):
			pass
		else:
			name = ctx.message.author.display_name
		await bot.say("Searching for "+name)
		
		
bot.add_cog(LeagueOfLegends())


bot.run(secretSauce.runID)


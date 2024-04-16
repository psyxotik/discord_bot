import discord
from discord.ext import commands
import random
import config


bot = commands.Bot(command_prefix=config.prefix, intents=config.intents)


@bot.command()
async def clan_id(ctx):
    await ctx.reply('999999')


@bot.command()
async def randomizer(ctx, *arg):
    await ctx.reply(random.randint(0, 100))

# @bot.command()
# async def kick(ctx, user : discord.User(), *arg, reason='Причина не указана'):
#     await bot.kick(user)
#     await ctx.send('Пользователь {user.name} был изгнан по причине "{reason}"')


bot.run(config.Token)
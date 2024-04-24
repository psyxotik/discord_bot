import disnake
from disnake.ext import commands
from data import config
import os

bot = commands.Bot(command_prefix='.', help_command=None, intents=disnake.Intents.all(), test_guilds=[
    471317123616997377, 1215615491729657866])


@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready to work!')

for file in os.listdir("cogs"):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')


@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id=1215625192064421968)

    channel = member.guild.system_channel

    embed = disnake.Embed(
        title='New member!',
        description=f'{member.name}',
        color=0xeba834
    )

    await member.add_roles(role)
    await channel.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author}, У вас недостаточно прав для выполнения данной команды!')
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=disnake.Embed(
            description=f'Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ('
                        f'{ctx.command.brief})\nПример: {ctx.prefix}{ctx.command.usage}'
        ))

bot.run(config.Token)

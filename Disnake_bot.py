import disnake
from disnake.ext import commands
import config
import datetime
import os

bot = commands.Bot(command_prefix='.', help_command=None, intents=disnake.Intents.all(), test_guilds=[
    471317123616997377, 1215615491729657866])
bad_words = ['кф']




@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready to work!')

for file in os.listdir("./cogs"):
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
async def on_message(message):
    await bot.process_commands(message)

    for content in message.content.split():
        for censer in bad_words:
            if content.lower() == censer:
                await message.delete()
                await message.channel.send(f'{message.author.mention} theese words are bad!')


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


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: disnake.Member, *, reason='причина не указана'):
    await member.kick(reason=reason)
    await ctx.send(f'Администратор {ctx.author.mention} исключил пользователя {member.mention}', delete_after=3)
    await ctx.message.delete()


@bot.command(name='бан', aliases=['нах', 'банан'])
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: disnake.Member, *, reason='причина не указана'):
    await member.ban(reason=reason)
    await ctx.send(f'Администратор {ctx.author.mention} забанил пользователя {member.mention}', delete_after=3)
    await ctx.message.delete()


@bot.command(brief='мутит участников на неопределённое время', usage='timeout <@user> <reason=None>')
@commands.has_permissions(kick_members=True)
async def timeout(ctx, member: disnake.Member, *,time= '10', reason='причина не указана'):
    time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
    await member.timeout(reason=reason, until=time)
    await ctx.send(f'Администратор {ctx.author.mention} замутил пользователя {member.mention}', delete_after=3)


@bot.command(brief='размучивает участника', usage='untimeout <@user> <reason=None>')
@commands.has_permissions(kick_members=True)
async def untimeout(ctx, member: disnake.Member, *,time= '10', reason='причина не указана'):
    await member.timeout(reason=reason, until=None)
    await ctx.send(f'Администратор {ctx.author.mention} разамутил пользователя {member.mention}', delete_after=3)

@bot.command(brief='мутит участников на неопределённое время', usage='mute <@user> <reason=None>')
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: disnake.Member, *, reason='причина не указана'):
    role = disnake.utils.get(member.guild.roles, id=1215617267023224842)
    await member.add_roles(role, reason=reason)
    await ctx.send(f'Администратор {ctx.author.mention} замутил пользователя {member.mention}', delete_after=3)


@bot.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: disnake.Member, *, reason='причина не указана'):
    role = disnake.utils.get(member.guild.roles, id=1215617267023224842)
    await member.remove_roles(role, reason=reason)
    await ctx.send(f'Администратор {ctx.author.mention} размутил пользователя {member.mention}', delete_after=3)


@bot.slash_command()
async def calc(inter, a: int, oper: str, b: int):
    if oper == '+':
        result = a + b
    elif oper == '-':
        result = a - b
    else:
        result = f'неверный оператор: {oper}'
    await inter.send(str(result))



# bot.get_channel(484717409702379520)
bot.run(config.Token)

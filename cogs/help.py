import disnake
from disnake.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="help", description="Показать список всех доступных команд")
    async def help(self, ctx):
        embed = disnake.Embed(title="Список команд", description="Список всех доступных команд бота", color=0x7289DA)

        for cog in self.bot.cogs.values():
            command_list = []
            for command in cog.get_commands():
                if command.description:
                    command_list.append(f"**/{command.name}**: {command.description}")
                else:
                    command_list.append(f"**/{command.name}**")

            embed.add_field(name=cog.qualified_name, value="\n".join(command_list), inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
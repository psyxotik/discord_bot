import disnake
from disnake.ext import commands


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="serverinfo", description="Получить информацию о сервере")
    async def server_info(self, ctx):
        guild = ctx.guild

        embed = disnake.Embed(
            title="Информация о сервере",
            color=disnake.Color.blurple()
        )

        embed.add_field(name="Название сервера", value=guild.name, inline=True)
        embed.add_field(name="ID сервера", value=guild.id, inline=True)
        embed.add_field(name="Владелец", value=guild.owner.mention, inline=True)
        embed.add_field(name="Дата создания", value=guild.created_at.strftime("%d %B %Y"), inline=True)
        embed.add_field(name="Регион сервера", value=guild.preferred_locale, inline=True)
        embed.add_field(name="Количество участников", value=guild.member_count, inline=True)
        embed.add_field(name="Количество каналов", value=len(guild.channels), inline=True)
        embed.set_thumbnail(url=guild.icon.url)
        embed.set_footer(text=f"Баннер сервера: {guild.banner}")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ServerInfo(bot))
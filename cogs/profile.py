import disnake
from disnake.ext import commands
from data.database import Database

# Подключение к базе данных
db = Database()

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="profile", description="Показать информацию о пользователе")
    async def profile(self, ctx, user: disnake.Member = None):
        if user is None:
            user = ctx.author

        created_at = user.created_at.strftime("%d %B %Y %H:%M:%S")
        joined_at = user.joined_at.strftime("%d %B %Y %H:%M:%S")
        status = str(user.status).title()
        user_id = user.id

        bio = db.get_bio(user_id) or "Биография отсутствует"

        embed = disnake.Embed(title="Профиль пользователя", color=0x7289DA)
        embed.set_author(name=user.display_name, icon_url=user.avatar.url)
        embed.add_field(name="Дата создания аккаунта", value=created_at, inline=False)
        embed.add_field(name="Дата присоединения", value=joined_at, inline=False)
        embed.add_field(name="Статус", value=status, inline=False)
        embed.add_field(name="ID", value=user_id, inline=False)
        embed.add_field(name="Биография", value=bio, inline=False)

        await ctx.send(embed=embed)

    @commands.slash_command(name="setbio", description="Установить биографию пользователя")
    async def set_bio(self, ctx, *, bio: str):
        user = ctx.author
        user_id = user.id

        db.set_bio(user_id, bio)
        await ctx.send("Биография успешно обновлена.")

def setup(bot):
    bot.add_cog(Profile(bot))
from disnake.ext import commands
from data.database import database


class WordFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="add_word", description="Добавить слово в фильтр")
    async def add_word(self, ctx, word: str):
        server_id = ctx.guild.id
        database.add_word_to_filter(server_id, word)
        await ctx.send(f"Слово '{word}' добавлено в фильтр.")

    @commands.slash_command(name="remove_word", description="Удалить слово из фильтра")
    async def remove_word(self, ctx, word: str):
        server_id = ctx.guild.id
        database.remove_word_from_filter(server_id, word)
        await ctx.send(f"Слово '{word}' удалено из фильтра.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        server_id = message.guild.id
        filtered_words = database.get_filtered_words(server_id)

        for word in filtered_words:
            if word[0] in message.content.lower():
                await message.delete()
                await message.channel.send(
                    f"{message.author.mention}, сообщение содержит запрещенное слово и было удалено.")


def setup(bot):
    bot.add_cog(WordFilter(bot))
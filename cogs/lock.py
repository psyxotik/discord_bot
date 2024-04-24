import disnake
from disnake.ext import commands


class Lockdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.locked_channels = []

    @commands.has_permissions(administrator=True)
    @commands.slash_command(name="lockdown", description="Закрыть/открыть возможность писать в чатах определённой категории")
    async def lockdown(self, ctx, action: str, category: disnake.CategoryChannel = None):
        if action.lower() not in ['lock', 'unlock']:
            await ctx.send("Неверное действие. Используйте 'lock' или 'unlock'.")
            return

        if not category:
            category = ctx.channel.category

        channels = category.text_channels

        for channel in channels:
            if action.lower() == 'lock':
                await channel.set_permissions(ctx.guild.default_role, send_messages=False)
                if channel not in self.locked_channels:
                    self.locked_channels.append(channel)
            else:
                await channel.set_permissions(ctx.guild.default_role, send_messages=True)
                if channel in self.locked_channels:
                    self.locked_channels.remove(channel)

        action_text = "закрыта" if action.lower() == 'lock' else "открыта"
        category_name = category.name
        await ctx.send(f"Возможность писать в каналах категории '{category_name}' для всех участников сервера {action_text}.")


def setup(bot):
    bot.add_cog(Lockdown(bot))
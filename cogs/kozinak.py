from disnake.ext import commands
import disnake
from random import randint


class Cozinak(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(description="Крутануть рулетку")
    async def cozinak(self, interaction):
        sentence_win = [
            "KAVO KAVO KAVO",
            "феноменально!",
            "свекровь гордится вами",
            "забирай ящик морковки"
        ]
        sentence_lose =  [
            "укуси меня пчела, этого казино",
            "нужно отыграть морковку",
            "ну ёлки-иголки",
            "я порву тебя как старую газету",
            "шулер, со мной такие фокусы не проходят",
            "а можно его разобрать и вернуть наши вещи обратно?"
        ]
        emoji = ['🥕', '🍒', '🔔', '❌']
        first_emoji = emoji[randint(0, 3)]
        second_emoji = emoji[randint(0, 3)]
        third_emoji = emoji[randint(0, 3)]
        fourth_emoji = emoji[randint(0, 3)]
        if first_emoji == second_emoji == third_emoji == fourth_emoji:
            if first_emoji == emoji[3]:
                embed = disnake.Embed(title="Козинак", description=f"Вы потянули за рычаг! Вам выпало: {first_emoji} "
                                                                   f"{second_emoji} {third_emoji} {fourth_emoji} \n "
                                                                   f"Вы невероятный неудачник!")
            else:
                embed = disnake.Embed(title="Козинак", description=f"Вы потянули за рычаг! Вам выпало: {first_emoji} "
                                                                   f"{second_emoji} {third_emoji} {fourth_emoji} \n "
                                                                   f"{sentence_win[randint(0, 3)]}")
        else:
            embed = disnake.Embed(title="Козинак", description=f"Вы потянули за рычаг! Вам выпало: {first_emoji} "
                                                               f"{second_emoji} {third_emoji} {fourth_emoji} \n "
                                                               f"{sentence_lose[randint(0, 5)]}")
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Cozinak(bot))
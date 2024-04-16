from disnake.ext import commands
import disnake
from random import randint


class Cazinak(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def cozinak(self, interaction):
        sentence_win = [
            "KAVO KAVO KAVO",
            "феноменально! Actually",
            "свекровь гордится вами catChill",
            "забирай ящик морковки YEPTA"
        ]
        sentence_lose =  [
            "укуси меня пчела, этого казино wtf",
            "нужно отыграть морковку SCAMBA",
            "ну ёлки-иголки Sadge",
            "я порву тебя как старую газету Smadge",
            "шулер, со мной такие фокусы не проходят AAAA",
            "а можно его разобрать и вернуть наши вещи обратно? bubuh"
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
    bot.add_cog(Cazinak(bot))
import discord

from redbot.core.bot import Red
from redbot.core import commands
from redbot.core.i18n import Translator, cog_i18n
from redbot.core.utils.chat_formatting import humanize_timedelta

from typing import Union
from datetime import datetime

import contextlib

_ = Translator("Converters", __file__)


@cog_i18n(_)
class Conversions(commands.Cog):
    """Various conversions"""

    __author__ = "BluDragyn"
    __version__ = "0.1.0"

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    def __init__(self, bot: Red):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthor: {self.__author__}\nCog Version: {self.__version__}"

    @commands.group(aliases=["conversion"])
    async def conv(self, ctx: commands.Context):
    """Various conversion utilities."""

    
    @conv.group(aliases=["ctof"])
    async def celsius(self, ctx: commands.Context):
        """
        Convert degree Celsius to Fahrenheit.
        
        Usage:
        To Fahrenheit: `[p]ctof celsius fahrenheit`
        """

    @celsius.command(name="fahrenheit", aliases=["f"])
    async def celsius_to_fahrenheit(self, ctx: commands.Context, temperature: float):
        fahrenheit = round((temperature * 1.8) + 32, 1)
        msg = _("{temp:,}° Celsius is equal to {f:,}° Fahrenheit.").format(
            temp=temperature, f=fahrenheit
        )
        await ctx.send(msg)

    @conv.group(aliases=["ftoc"])
    async def fahrenheit(self, ctx: commands.Context):
        """
        Convert Fahrenheit degree to Celsius.

        Usage:
        To Celsius: `[p]ftoc fahrenheit celsius`
        """

    @fahrenheit.command(name="celsius", aliases=["c"])
    async def fahrenheit_to_celsius(self, ctx: commands.Context, temperature: float):
        celsius = round((temperature - 32) / 1.8, 1)
        msg = _("{temp:,}° Fahrenheit is equal to {c:,}° Celsius.").format(
            temp=temperature, c=celsius
        )
        await ctx.send(msg)

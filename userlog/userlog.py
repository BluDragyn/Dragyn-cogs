import datetime
import discord

from redbot.core import checks, commands, Config

from redbot.core.bot import Red

__author__ = "saurichable"


class UserLog(commands.Cog):
    """Log when users join/leave into your specified channel."""

    __author__ = "saurichable"
    __version__ = "1.0.3"

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(
            self, identifier=56546565165465456, force_registration=True
        )

        self.config.register_guild(channel=None, join=True, leave=True)

    @commands.group(autohelp=True)
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def userlog(self, ctx):
        """Manage user log settings."""
        pass

    @userlog.command(name="channel")
    async def user_channel_log(self, ctx, channel: discord.TextChannel = None):
        """Set the channel for logs.

        If the channel is not provided, logging will be disabled."""
        if channel:
            await self.config.guild(ctx.guild).channel.set(channel.id)
        else:
            await self.config.guild(ctx.guild).channel.set(None)
        await ctx.tick()

    @userlog.command(name="join")
    async def user_join_log(self, ctx: commands.Context, on_off: bool = None):
        """Toggle logging when users join the current server. 

        If `on_off` is not provided, the state will be flipped."""
        target_state = (
            on_off
            if on_off
            else not (await self.config.guild(ctx.guild).join())
        )
        await self.config.guild(ctx.guild).join.set(target_state)
        if target_state:
            await ctx.send("Logging users joining is now enabled.")
        else:
            await ctx.send("Logging users joining is now disabled.")

    @userlog.command(name="leave")
    async def user_leave_log(self, ctx: commands.Context, on_off: bool = None):
        """Toggle logging when users leave the current server.

        If `on_off` is not provided, the state will be flipped."""
        target_state = (
            on_off
            if on_off
            else not (await self.config.guild(ctx.guild).leave())
        )
        await self.config.guild(ctx.guild).leave.set(target_state)
        if target_state:
            await ctx.send("Logging users leaving is now enabled.")
        else:
            await ctx.send("Logging users leaving is now disabled.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        join = await self.config.guild(member.guild).join()
        if not join:
            return
        channel = member.guild.get_channel(await self.config.guild(member.guild).channel())
        if not channel:
            return
        await channel.send(":green_circle:" + member.mention + " has joined The Kinky Place! Say hi everyone!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        leave = await self.config.guild(member.guild).leave()
        if not leave:
            return
        channel = member.guild.get_channel(await self.config.guild(member.guild).channel())
        if not channel:
            return
        await channel.send(":red_circle:" + member.mention + " said YEET and left. BYE!")

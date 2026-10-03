from .icarus import Icarus


async def setup(bot):
    await bot.add_cog(Icarus(bot))

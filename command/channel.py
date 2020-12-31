import discord, random
from discord import Embed, Colour
from discord.ext import commands
from discord.ext.commands import Cog, command, cooldown, BucketType, has_permissions

c = [15987181, 16763890, 16629176, 765349, 402754, 16711587, 14408959, 10643837]

class Channel(Cog):
  
  def __init__(self, bot):
    
    self.bot = bot
    
  @command(name = 'purge', help = "Purge channel messages or messages from mentioned member", aliases = ['del', 'clear'])
  @has_permissions(manage_messages = True)
  @cooldown(1, 5, BucketType.user)
  async def purge_(self, ctx, limit_or_member):
    
    if len(ctx.message.mentions) == 0:
      
      if not list(limit_or_member)[0].isnumeric():
        
        await ctx.send("<:emoji_8:753337197796786179> | {} Failed convert to prameter limit".format(ctx.author.mention))
        
      else:
        
        if len(list(limit_or_member)[0]) < 0:
          
          await ctx.send("<:emoji_8:753337197796786179> | {} Cannot purge message with that limit".format(ctx.author.mention))
          
        elif len(list(limit_or_member)[0]) > 500:
          
          await ctx.send("<:emoji_8:753337197796786179> | {} Max limit is 500".format(ctx.author.mention))
          
        else:
          
          await ctx.message.delete()
          x = int(limit_or_member)
          await ctx.channel.purge(limit = x)
          
    else:
      
      def check(x):
        
        return x.author.id == ctx.message.mentions[0].id
        
      z = await ctx.channel.purge(check=check, limit = 200)
      
  @command(name = "lock", help = "Lock channel")
  @has_permissions(manage_guild = True, manage_channels = True)
  @cooldown(1, 10, BucketType.user)
  async def lock(self, ctx, *,channel= None):
    
    if channel is None:
      
      channel = ctx.channel
      
      await channel.set_permissions(ctx.guild.default_role, send_messages = False)
      
      embed = Embed()
      embed.description = "{} Locked 🔒".format(channel.mention)
      embed.colour = Colour(random.choice(c))
      embed.timestamp = ctx.message.created_at
      
      await ctx.send(embed=embed)
      
    else:
      
      if len(ctx.message.mentions) > 0:
        
        channel = ctx.message.mentions[0]
        
        await channel.set_permissions(ctx.guild.default_role, send_messages = False)
        embed = Embed()
        embed.description = "{} Locked 🔒".format(channel.mention)
        embed.colour = Colour(random.choice(c))
        embed.timestamp = ctx.message.created_at
        
        await ctx.send(embed=embed)
        
      else:
        
        ch = [w for w in ctx.guild.text_channels if str(channel.lower()) in w.name.lower()][0]
        
        channel = ch
        
        await channel.set_permissions(ctx.guild.default_role, send_messages = False)
        embed = Embed()
        embed.description = "{} Locked 🔒".format(channel.mention)
        embed.colour = Colour(random.choice(c))
        embed.timestamp = ctx.message.created_at
        
        await ctx.send(embed=embed)
        
  @command(name = "hide", help = "Hide channel")
  @has_permissions(manage_guild = True, manage_channels = True)
  @cooldown(1, 10, BucketType.user)
  async def hide(self, ctx, *,channel= None):
    
    if channel is None:
      
      channel = ctx.channel
      
      await channel.set_permissions(ctx.guild.default_role, send_messages = False, read_messages = False)
      
      embed = Embed()
      embed.description = "{} Hided 🔒".format(channel.mention)
      embed.colour = Colour(random.choice(c))
      embed.timestamp = ctx.message.created_at
      
      await ctx.send(embed=embed)
      
    else:
      
      if len(ctx.message.mentions) > 0:
        
        channel = ctx.message.mentions[0]
        
        await channel.set_permissions(ctx.guild.default_role, send_messages = False, read_messages = False)
        embed = Embed()
        embed.description = "{} Hided 🔒".format(channel.mention)
        embed.colour = Colour(random.choice(c))
        embed.timestamp = ctx.message.created_at
        
        await ctx.send(embed=embed)
        
      else:
        
        ch = [w for w in ctx.guild.text_channels if str(channel.lower()) in w.name.lower()][0]
        
        channel = ch
        
        await channel.set_permissions(ctx.guild.default_role, send_messages = False, read_messages = False)
        embed = Embed()
        embed.description = "{} Hided 🔒".format(channel.mention)
        embed.colour = Colour(random.choice(c))
        embed.timestamp = ctx.message.created_at
        
        await ctx.send(embed=embed)
      
  @command(name = "unlock", help = "Unlock channel")
  @has_permissions(manage_guild = True, manage_channels = True)
  @cooldown(1, 10, BucketType.user)
  async def unlock(self, ctx, *,channel = None):
    
    if channel is None:
      
      channel = ctx.channel
      
      await channel.set_permissions(ctx.guild.default_role, send_messages = True)
      
      embed = Embed()
      embed.description = "{} Unlocked 🔓".format(channel.mention)
      embed.colour = Colour(random.choice(c))
      embed.timestamp = ctx.message.created_at
      
      await ctx.send(embed=embed)
      
    else:
      
      if len(ctx.message.mentions) > 0:
        
        channel = ctx.message.mentions[0]
        
        await channel.set_permissions(ctx.guild.default_role, send_messages = True)
        
        embed = Embed()
        embed.description = "{} Unlocked 🔓".format(channel.mention)
        embed.colour = Colour(random.choice(c))
        embed.timestamp = ctx.message.created_at
        
        await ctx.send(embed=embed)
        
      else:
        
        ch = [w for w in ctx.guild.text_channels if str(channel.lower()) in w.name.lower()][0]
        
        channel = ch
        
        await channel.set_permissions(ctx.guild.default_role, send_messages = True)
        
        embed = Embed()
        embed.description = "{} Unlocked 🔓".format(channel.mention)
        embed.colour = Colour(random.choice(c))
        embed.timestamp = ctx.message.created_at
        
        await ctx.send(embed=embed)
      
  @command(name = "slowmode", aliases = ["sm", "smode"], help = "Change slow mode channel")
  @has_permissions(manage_channels = True, manage_guild = True)
  @cooldown(1, 10, BucketType.user)
  async def _mslow(self, ctx, limit):
    
    if int(limit) < 0:
      
      await ctx.send("<:emoji_8:753337197796786179> | {} cannot change slow mode channel with that limit".format(ctx.author.mention))
      
    elif int(limit) == 0:
      
      await ctx.channel.edit(slowmode_delay= 0)
      
      e = Embed(colour = Colour(random.choice(c)))
      e.description = "Successfully disabled channel slow mode"
      e.timestamp = ctx.message.created_at
      await ctx.send(embed=e)
      
    elif int(limit) > 21600:
      
      await ctx.send("<:emoji_8:753337197796786179> | {} cannot change slow mode channel below 21600".format(ctx.author.mention))
      
    else:
      
      limit = int(limit)
      
      await ctx.channel.edit(slowmode_delay = limit)
      
      e = Embed(colour = Colour(random.choice(c)))
      e.description = "Successfully change channel slow mode to {} second(s)".format(limit)
      e.timestamp = ctx.message.created_at
      await ctx.send(embed=e)
      
    
    
def setup(bot):
  
  bot.add_cog(Channel(bot))
import discord, json, asyncio
from discord import Embed, Colour
from discord.ext import commands
from discord.ext.commands import Cog, command, has_permissions, cooldown, BucketType

class Moderation(Cog):
  
  def __init__(self, bot):
    
    self.bot = bot
    
  @Cog.listener()
  async def on_guild_role_delete(self, role):
    
    data = json.load(open("./json/mute.json", "r"))
    
    if not str(role.guild.id) in data:
      
      return
    
    else:
      
      _id = data[str(role.guild.id)]
      
      if int(role.id) == _id:
        
        data.pop(str(role.guild.id))
      
    x = open("./json/mute.json", "w")
    
    json.dump(data, x, indent = 4)
    
  @Cog.listener()
  async def on_guild_channel_create(self, channel):
    
    data = json.load(open("./json/mute.json", "r"))
    
    if not str(channel.guild.id) in data:
      
      return
    
    else:
      
      _id = data[str(channel.guild.id)]
      
      role = discord.utils.get(channel.guild.roles, id = _id)
      
      try:
        
        await channel.set_permissions(role, send_messages = False, connect = False)
        
      except Exception as e:
        
        print(e)
    
  @command(name = "kick", help = "Kick members with optional reason")
  @cooldown(1, 10, BucketType.user)
  async def kicked(self, ctx, member, *, reason = None):
    
    if len(ctx.message.mentions) > 0:
      
      member = ctx.message.mentions[0]
      
      if member.guild_permissions.administrator == True or member.guild_permissions.manage_guild == True:
        
        await ctx.send("<:emoji:753337197796786179> | {} I can\'t kick member with permissions administrator and manage server".format(ctx.author.mention))
        
      else:
        
        await member.kick(reason = str(reason).replace("None", f"No reason provide from {ctx.author.name}"))
        e = Embed()
        e.description = "{} Kicked from {}. Reason : {}".format(member, ctx.guild.name, reason)
        e.timestamp = ctx.message.created_at
        e.colour = Colour.red()
        await ctx.send(embed=e)
        
    else:
      
      member = [w for w in ctx.guild.members if str(member.lower()) in w.display_name.lower()][0]
      
      if member.guild_permissions.administrator == True or member.guild_permissions.manage_guild == True:
        
        await ctx.send("<:emoji:753337197796786179> | {} I can\'t kick member with permissions administrator and manage server".format(ctx.author.mention))
        
      else:
        
        await member.kick(reason = str(reason).replace("None", f"No reason provide from {ctx.author.name}"))
        e = Embed()
        e.description = "{} Kicked from {}. Reason : {}".format(member, ctx.guild.name, reason)
        e.timestamp = ctx.message.created_at
        e.colour = Colour.red()
        await ctx.send(embed=e)
        
  @command(name = "ban", help = "Ban members with optional reason")
  @has_permissions(manage_guild = True, kick_members = True)
  @cooldown(1, 10, BucketType.user)
  async def banned(self, ctx, member, *, reason = None):
    
    if len(ctx.message.mentions) > 0:
      
      member = ctx.message.mentions[0]
      
      if member.guild_permissions.administrator == True or member.guild_permissions.manage_guild == True:
        
        await ctx.send("<:emoji:753337197796786179> | {} I can\'t ban member with permissions administrator and manage server".format(ctx.author.mention))
        
      else:
        
        await member.ban(reason = str(reason).replace("None", f"No reason provide from {ctx.author.name}"))
        e = Embed()
        e.description = "{} Banned from {}. Reason : {}".format(member, ctx.guild.name, reason)
        e.timestamp = ctx.message.created_at
        e.colour = Colour.red()
        await ctx.send(embed=e)
        
    else:
      
      member = [w for w in ctx.guild.members if str(member.lower()) in w.display_name.lower()][0]
      
      if member.guild_permissions.administrator == True or member.guild_permissions.manage_guild == True:
        
        await ctx.send("<:emoji:753337197796786179> | {} I can\'t ban member with permissions administrator and manage server".format(ctx.author.mention))
        
      else:
        
        await member.ban(reason = str(reason).replace("None", f"No reason provide from {ctx.author.name}"))
        e = Embed()
        e.description = "{} Banned from {}. Reason : {}".format(member, ctx.guild.name, reason)
        e.timestamp = ctx.message.created_at
        e.colour = Colour.red()
        await ctx.send(embed=e)
        
  @command(name = "roleadd", help = "Give role to member", aliases = ["ra", "give"])
  @has_permissions(manage_guild = True, manage_roles = True)
  @cooldown(1, 10, BucketType.user)
  async def _role(self, ctx, member:discord.Member, role:discord.Role):
    
    if role in member.roles:
      
      return await ctx.send("{} {} already has {} role".format(ctx.author.mention, member.display_name, role.name))
      
    try:
      
      await member.add_roles(role)
      
      e = Embed(colour = role.colour)
      e.description = "Successfully added {} role to {}".format(role.mention, member.display_name)
      e.timestamp = ctx.message.created_at
      await ctx.send(embed = e)
      
    except Exception as e:
      
      await ctx.send("<:emoji:753337197796786179> | {} Missing permissions. Please check my role position".format(ctx.author.mention))
    
  @command(name = "roleremove", help = "Remove role from member", aliases = ["rr", "take"])
  @has_permissions(manage_roles = True, manage_guild = True)
  @cooldown(1, 10, BucketType.user)
  async def _roles(self, ctx, member:discord.Member, role:discord.Role):
    
    if role not in member.roles:
      
      return await ctx.send("{} {} does not has {} role".format(ctx.author.mention, member.display_name, role.name))
      
    try:
      
      await member.remove_roles(role)
      
      e = Embed(colour = role.colour)
      e.description = "Successfully removed {} role from {}".format(role.mention, member.display_name)
      e.timestamp = ctx.message.created_at
      await ctx.send(embed=e)
      
    except Exception as e:
      
      await ctx.send("<:emoji:753337197796786179> | {} Missing permissions. Please check my role position".format(ctx.author.mention))
      
  @command(name = "mute", help = "Mute member")
  @has_permissions(manage_guild = True, manage_roles = True)
  @cooldown(1, 10, BucketType.user)
  async def _mute(self, ctx, member : discord.Member, duration = None):
    
    file = open("./json/mute.json", "r")
    
    data = json.load(file)
    
    if not str(ctx.guild.id) in data:
      
      await ctx.send("<:emoji:753337197796786179> | {} Please run setupmute first".format(ctx.author.mention))
      
    else:
      
      _id = data[str(ctx.guild.id)]
      
      role = discord.utils.get(ctx.guild.roles, id = _id)
      
      if role in member.roles:
        
        await ctx.send("<:emoji:753337197796786179> | {} {} already muted".format(ctx.author.mention, member.name))
        
      else:
        
        if duration is None:
          
          try:
            
            await member.add_roles(role)
            
            embed = Embed()
            embed.colour = Colour.red()
            embed.description = "{} Muted".format(member)
            embed.timestamp = ctx.message.created_at
            
            await ctx.send(embed=embed)
            
          except Exception as e:
            
            await ctx.send("<:emoji:753337197796786179> | {} Missing permissions. Please check my role position".format(ctx.author.mention))
            
        else:
          
          try:
            
            time = (60 * int(duration))
            
            await member.add_roles(role)
            
            embed = Embed()
            embed.colour = Colour.red()
            embed.description = "{} Muted for {} minute(s)".format(member, duration)
            embed.timestamp = ctx.message.created_at
            
            await ctx.send(embed=embed)
            await asyncio.sleep(time)
            
            await member.remove_roles(role)
            
          except Exception as e:
            
            await ctx.send("<:emoji:753337197796786179> | {} Missing permissions. Please check my role position".format(ctx.author.mention))
            
  @command(name = "unmute", help = "Un mute member")
  @cooldown(1, 10, BucketType.user)
  @has_permissions(manage_roles = True, manage_guild = True)
  async def _unmute(self, ctx, member):
    
    data = json.load(open("./json/mute.json", "r"))
    
    _id = data[str(ctx.guild.id)]
    
    role = discord.utils.get(ctx.guild.roles, id = _id)
    
    if role not in member.roles:
      
      await ctx.send("<:emoji:753337197796786179> | {} Does not muted".format(ctx.author.mention))
      
    else:
      
      try:
        
        if len(ctx.message.mentions) > 0:
          
          member = ctx.message.mentions[0]
          await member.remove_roles(role)
          e = Embed()
          e.colour = discord.Colour.green()
          e.description = "{} Successfully unmuted".format(member)
          e.timestamp = ctx.message.created_at
          await ctx.send(embed=e)
          
        else:
          
          member = [w for w in ctx.guild.members if str(member.lower()) in w.display_name.lower()][0]
          await member.remove_roles(role)
          e = Embed()
          e.colour = discord.Colour.green()
          e.description = "{} Successfully unmuted".format(member)
          e.timestamp = ctx.message.created_at
          await ctx.send(embed=e)
        
      except Exception as e:
        
        print(e)
    
    
def setup(bot):
  
  bot.add_cog(Moderation(bot))
import discord, time, asyncio, json, aiohttp, random, os

from discord.ext.commands import Cog, command, cooldown, BucketType, has_permissions
from discord.ext import commands
from discord import Embed, Colour

from apiclient.discovery import build

def toint(hex):
  return int(hex, 16)

c = [15987181, 16763890, 16629176, 765349, 402754, 16711587, 14408959, 10643837]

yutup = os.environ.get("yt")

youtube = build('youtube', 'v3', developerKey=yutup)

class Meta(Cog):
  
  def __init__(self, bot):
    
    self.bot = bot
    
  @command(name = "setnick", help = "Change member nickname")
  @has_permissions(manage_nicknames = True)
  @cooldown(1, 10, BucketType.user)
  async def _manage_(self, ctx, member : discord.Member, *, new_nickname):
    
    try:
      
      await member.edit(nick = new_nickname)
      
      embed = Embed()
      embed.colour = member.colour
      embed.description = "Successfully change {} nickname to {}".format(member.nick, new_nickname)
      embed.timestamp = ctx.message.created_at
      
      await ctx.send(embed=embed)
      
    except Exception as e:
      
      await ctx.send("<:emoji:753337197796786179> | {} I cannot manage {}. Please check my role position".format(ctx.author.mention, member.name))
      
  @command(name = "resetnick", help = "Reset member nickname")
  @has_permissions(manage_nicknames = True)
  @cooldown(1, 10, BucketType.user)
  async def _manages_(self, ctx, member : discord.Member):
    
    try:
      
      await member.edit(nick = None)
      
      embed = Embed()
      embed.colour = member.colour
      embed.description = "Successfully reset {} nickname".format(member.nick)
      embed.timestamp = ctx.message.created_at
      
      await ctx.send(embed=embed)
      
    except Exception as e:
      
      await ctx.send("<:emoji:753337197796786179> | {} I cannot manage {}. Please check my role position".format(ctx.author.mention, member.name))
    
  @command(name = "ping", help = "Show latency bot and respond time")
  @cooldown(1, 10, BucketType.user)
  async def pong(self, ctx):
    
    ping = self.bot.latency
    _1 = self.bot.get_shard(0).latency
    _2 = self.bot.get_shard(1).latency
    _3 = self.bot.get_shard(2).latency
    start = time.time()
    await asyncio.sleep(0.1)
    end = time.time()
    respon = (end - start)
    embed = discord.Embed(
      title = "Ping Peng Pong 🏓",
      colour = Colour(random.choice(c)),
      timestamp = ctx.message.created_at
      )
    embed.set_footer(text = "Request by : {}".format(ctx.author.display_name), icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = self.bot.user.avatar_url)
    f = [
      ("Bot", f"{ping*1000:,.0f} ms", False),
      ("Heartbeat", f"{respon*1000:,.0f} ms", False),
      #("Shard 1", f"{_1*1000-20:,.0f} ms", False),
      #("Shard 2", f"{_2*1000+60:,.0f} ms", False),
      #("Shard 3", f"{_3*1000+60:,.0f} ms", False)
      ]
    for name, value, inline in f:
      
      embed.add_field(name = name, value=value, inline = inline)
    await ctx.send(embed = embed)
    
  @command(name = "prefix", help = "Change bot prefix")
  @has_permissions(administrator = True)
  @cooldown(1, 20, BucketType.user)
  async def _prefix(self, ctx, prefix):
    
    file = open("./json/prefix.json", "r")
    
    data = json.load(file)
      
    try:
      
      if not str(ctx.guild.id) in data:
        
        data[str(ctx.guild.id)] = prefix
        
        e = Embed()
        e.description = "Prefix successfully change to `{}`".format(prefix)
        e.colour = Colour(random.choice(c))
        e.timestamp = ctx.message.created_at
        await ctx.send(embed=e)
        
      else:
        
        data[str(ctx.guild.id)] = prefix
        
        ee = Embed()
        ee.description = "Prefix successfully change to `{}`".format(prefix)
        ee.colour = Colour(random.choice(c))
        ee.timestamp = ctx.message.created_at
        await ctx.send(embed=ee)
        
    except Exception as error:
      
      print(error)
        
    x = open("./json/prefix.json", "w")
    
    json.dump(data, x, indent = 4)
        
    
  @Cog.listener()
  async def on_command_error(self, ctx, error):
    
    if isinstance(error, commands.CommandNotFound):
      
      return
    
    elif isinstance(error, commands.CommandOnCooldown):
      
      if ctx.author.id != 493768058012172288:
        
        return await ctx.send(f"<:emoji:753337197796786179> | {ctx.author.mention} {ctx.command.name} command on cooldown. Try again after {error.retry_after:,.0f} seconds")
        
      else:
        
        await ctx.reinvoke()
      
    elif isinstance(error, commands.MissingPermissions):
      
      await ctx.send("<:emoji:753337197796786179> | {} {}".format(ctx.author.mention, error))
      
    elif isinstance(error, commands.BotMissingPermissions):
      
      await ctx.send("<:emoji:753337197796786179> | {} {}".format(ctx.author.mention, error))
      
    elif isinstance(error, commands.NotOwner):
      
      await ctx.send("<:emoji:753337197796786179> | {} {}".format(ctx.author.mention, error))
      
    elif isinstance(error, commands.MissingRequiredArgument):
      
      await ctx.send(str("<:emoji:753337197796786179> | {} please provide `{}` as required argument".format(ctx.author.mention, error.param)).replace("_", " ").replace("member: discord.member.Member", "member").replace("role: discord.role.Role", "role"))
      
    elif isinstance(error, commands.NSFWChannelRequired):
      
      await ctx.send("<:emoji:753337197796786179> | {} {} Must be NSFW to run {} command".format(ctx.author.mention, ctx.channel.mention, ctx.command.name))
      
    elif isinstance(error, commands.CommandInvokeError):
      
      print(error)
      await self.bot.get_channel(753916076512903169).send(error)
      
      
  @Cog.listener()
  async def on_guild_remove(self, guild):
    
    file = open('./json/prefix.json', 'r')
    
    data = json.load(file)
    
    if not str(guild.id) in data:
      
      return
    
    else:
      
      data.pop(str(guild.id))
      
    x = open("./json/prefix.json", "w")
    
    json.dump(data, x, indent = 4)
    
  @Cog.listener()
  async def on_command_completion(self, ctx):
    
    file = open("./json/cmd.json", "r")
    
    data = json.load(file)
    
    if not str("run") in data:
      
      data[str("run")] = 0
      
    data[str("run")] += 1
    
    x = open("./json/cmd.json", "w")
    
    json.dump(data, x)
    
  @Cog.listener()
  async def on_message_delete(self, message):
    
    file = open("./json/snipe.json", "r")
    
    data = json.load(file)
    
    if not str(message.guild.id) in data:
      
      data[str(message.guild.id)] = {}
    
    if message.author.bot:
      
      return
    
    data[str(message.guild.id)]["user"] = message.author.id
    
    data[str(message.guild.id)]['content'] = message.content
    
    if len(message.attachments) > 0:
      
      url = str(message.attachments[0].url)
      
      data[str(message.guild.id)]["content"] = url
    
    x = open("./json/snipe.json", "w")
    
    json.dump(data, x, indent = 4)
    
  @command(name = "snipe", aliases = ["s", "sniper"], help = "See lasted deleted message")
  @cooldown(1, 10, BucketType.user)
  async def _snipe(self, ctx):
    
    file = open("./json/snipe.json", "r")
    
    data = json.load(file)
    
    if not str(ctx.guild.id) in data:
      
      return await ctx.send("{} Nothing to snipe".format(ctx.author.mention))
      
    member = discord.utils.get(ctx.guild.members, id=int(data[str(ctx.guild.id)]['user']))
    content = data[str(ctx.guild.id)]["content"]
    
    e = Embed()
    e.set_author(name = member.display_name, icon_url = member.avatar_url)
    e.description = content
    e.colour = Colour(random.choice(c))
    e.timestamp = ctx.message.created_at
    await ctx.send(embed=e)
    
  @command(name = "autorole", aliases = ["ar"], help = "Give role for new member")
  @has_permissions(administrator = True)
  @cooldown(2, 10, BucketType.user)
  async def _join_auto(self, ctx, set_remove_or_now, role: discord.Role = None):
    
    file = open("./json/role.json", "r")
    
    data = json.load(file)
    
    if set_remove_or_now == "set".lower():
      
      if not str(ctx.guild.id) in data:
        
        data[str(ctx.guild.id)] = role.id
        
        e = Embed()
        e.colour = role.colour
        e.description = "Successfully set auto role to {}".format(role.mention)
        e.timestamp = ctx.message.created_at
        await ctx.send(embed=e)
        
      else:
        
        data[str(ctx.guild.id)] = role.id
        
        e = Embed()
        e.colour = role.colour
        e.description = "Successfully set auto role to {}".format(role.mention)
        e.timestamp = ctx.message.created_at
        await ctx.send(embed=e)
        
    elif set_remove_or_now == "remove".lower():
      
      if not str(ctx.guild.id) in data:
        
        return await ctx.send("{} Auto role module does not actived yet".format(ctx.author.mention))
        
      else:
        
        data.pop(str(ctx.guild.id))
        
        e1 = Embed()
        e1.colour = ctx.author.colour
        e1.description = "Successfully removed auto role"
        e1.timestamp = ctx.message.created_at
        await ctx.send(embed=e1)
        
    elif set_remove_or_now == "now".lower():
      
      if not str(ctx.guild.id) in data:
        
        return await ctx.send("{} Auto role module does not actived yet".format(ctx.author.mention))
        
      else:
        
        _id = data[str(ctx.guild.id)]
        
        e1 = Embed()
        e1.colour = ctx.author.colour
        e1.description = f"Auto role currently set in <@&{_id}>"
        e1.timestamp = ctx.message.created_at
        await ctx.send(embed=e1)
        
    x = open("./json/role.json", "w")
    
    json.dump(data, x, indent = 4)
    
  @Cog.listener()
  async def on_member_join(self, member):
    
    data = json.load(open("./json/role.json", "r"))
    
    if not str(member.guild.id) in data:
      
      return
    
    else:
      
      try:
        
        _id = data[str(member.guild.id)]
        role = discord.utils.get(member.guild.roles, id = _id)
        await member.add_roles(role)
        
      except: pass
      
  @Cog.listener()
  async def on_guild_role_delete(self, role):
    
    data = json.load(open("./json/role.json", "r"))
    
    if not str(role.guild.id) in data:
      
      return
    
    else:
      
      _id = data[str(role.guild.id)]
      
      if int(role.id) == _id:
        
        data.pop(str(role.guild.id))
        
    x = open("./json/role.json", "w")
    
    json.dump(data, x, indent = 4)
    
  @command(name = "setupmute", help = "Setup mute role")
  @has_permissions(administrator = True)
  @cooldown(1, 10, BucketType.user)
  async def _upset(self, ctx):
    
    data = json.load(open("./json/mute.json", "r"))
    
    if str(ctx.guild.id) in data:
      
      await ctx.send("<:emoji:753337197796786179> | {} Your guild already has mute role".format(ctx.author.mention))
      
    else:
      
      msg = await ctx.send("Setup...")
      new = await ctx.guild.create_role(name = "Muted", color = discord.Colour(0x000000))
      data[str(ctx.guild.id)] = new.id
      
      for x in ctx.guild.channels:
        
        try:
          
          await x.set_permissions(new, send_messages = False, connect = False)
          
        except:
          
          pass
        
      await msg.edit(content = "Done")
      
    x = open("./json/mute.json", "w")
    
    json.dump(data, x, indent = 4)
    
  @command(name = "rolecolor", aliases = ["rolecolour", "rc"], help = "Change role colour")
  @cooldown(1, 10,BucketType.user)
  @has_permissions(manage_roles = True)
  async def _ngecolor(self, ctx, role:discord.Role, hex):
    
    try:
      
      new = toint(hex.lower().replace("#", ""))
      await role.edit(colour = discord.Colour(new))
      e = Embed()
      e.description = "Successfully change {} role colour".format(role.mention)
      e.colour = discord.Colour(new)
      e.timestamp = ctx.message.created_at
      await ctx.send(embed=e)
 
    except Exception as e:
      
      await ctx.send("<:emoji:753337197796786179> | {} Missing permission. Please check my role position".format(ctx.author.mention))
      
      print(e)
      
  @command(name = 'youtube', aliases = ['yt'], help = 'Youtube Search')
  @cooldown(1, 10, BucketType.user)
  async def ytdl(self, ctx, *, search):
    
    req = youtube.search().list(q = search, part='snippet', type = 'video', maxResults = 1)
    resp = req.execute()
    
    for item in resp['items']:
      
      ids = item['id']['videoId']
      key = "https://www.youtube.com/watch?v="+str(ids)
      
    await ctx.send(key)
      
    
def setup(bot):
  
  bot.add_cog(Meta(bot))
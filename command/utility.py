import discord, psutil, platform, json, random
from discord import Embed, Colour
from discord.ext.commands import command, Cog, cooldown, BucketType

c = [15987181, 16763890, 16629176, 765349, 402754, 16711587, 14408959, 10643837]

class Utility(Cog):
  
  def __init__(self, bot):
    
    self.bot = bot
    
  @Cog.listener()
  async def on_guild_remove(self, guild):
    
    data = json.load(open("./json/snipe.json", "r"))
    
    if not str(guild.id) in data:
      
      return
    
    else:
      
      data.pop(str(guild.id))
      
    x = open("./json/snipe.json", "w")
    
    json.dump(data, x, indent = 4)
    
  @command(name = "help", help = "Help page")
  @cooldown(1, 10, BucketType.user)
  async def guide_page(self, ctx, command = None):
    
    mod = [x.name for x in self.bot.commands if x.cog_name == 'Moderation']
    util = [x.name for x in self.bot.commands if x.cog_name == 'Utility']
    meta = [x.name for x in self.bot.commands if x.cog_name == 'Meta']
    me = [x.name for x in self.bot.commands if x.cog_name == 'Anime']
    fun = [x.name for x in self.bot.commands if x.cog_name == 'Fun']
    gw = [x.name for x in self.bot.commands if x.cog_name == 'Owner']
    nsfw = [x.name for x in self.bot.commands if x.cog_name == 'Nsfw']
    ch = [x.name for x in self.bot.commands if x.cog_name == 'Channel']
    
    embed = Embed()
    embed.title = "{} help command".format(self.bot.user.name)
    embed.colour = Colour(random.choice(c))
    embed.timestamp = ctx.message.created_at
    embed.url = "https://discord.com/oauth2/authorize?client_id={}&permissions=8&scope=bot".format(self.bot.user.id)
    embed.set_thumbnail(url=self.bot.user.avatar_url)
    f = [
      (f"<a:gear_load:740068378768703559> Moderation ({len(mod)})", " - ".join(["`{}`".format(a) for a in mod]), False),
      (f"<:utility:751162110293049404> Utility ({len(meta)})", " - ".join(["`{}`".format(x) for x in meta]), False),
      (f"<:600998736704962560:751161363232981023> Channel ({len(ch)})", " - ".join(["`{}`".format(c) for c in ch]), False),
      (f"<:nuuu:751161811943948338> Anime ({len(me)})", " - ".join(["`{}`".format(w) for w in me]), False),
      (f"📄 Information ({len(util)})", " - ".join(["`{}`".format(z) for z in util]), False),
      (f"<:joystick:751184083966623744> Fun & Roleplay ({len(fun)})", " - ".join(["`{}`".format(y) for y in fun]), False),
      (f"🔞 NSFW ({len(nsfw)})", " - ".join(["`{}`".format(k) for k in nsfw]), False)
      ]
      
    for name, value, inline in f:
      
      embed.add_field(name=name, value=value, inline=inline)
      
    if command is None:
      
      if ctx.author.id != 493768058012172288:
        
        a = [w for w in self.bot.commands if not w.cog_name == 'Owner' and 'Jishaku']
        
        embed.set_footer(text = "{}help [command] for more information | commands show ({})".format(ctx.prefix, len(a)))
        await ctx.send(embed=embed)
        
      else:
        
        embed.add_field(name = f"<a:dancidanciXD:751163223910252605> Owner ({len(gw)})", value = " - ".join(["`{}`".format(j) for j in gw]))
        embed.set_footer(text = "{}help [command] for more information | commands show ({})".format(ctx.prefix, len(self.bot.commands)))
        await ctx.send(embed=embed)
        
    else:
      
      commands = self.bot.get_command(name = command)
      
      aliases = " | ".join([x for x in commands.aliases])
      
      no_ = "None"
      
      embed1 = Embed()
      embed1.timestamp = ctx.message.created_at
      embed1.colour = Colour(random.choice(c))
      embed1.title = "Help for command {}".format(commands.name)
      embed1.set_footer(text = "<> = Require | [] = Optional", icon_url = ctx.author.avatar_url)
      ff = [
        ("Name", commands.name, False),
        ("Aliases", aliases or no_, False),
        ("Description", commands.help, False),
        ("Usage", "{}{} {}".format(ctx.prefix, commands.name, str(commands.signature).replace("_", " ")), False)
        ]
      for name, value, inline in ff:
        
        embed1.add_field(name=name, value=value, inline=inline)
        
      await ctx.send(embed=embed1)
      
  @command(name = 'avatar', help = "Show member avatar", aliases = ["ava", "av"])
  @cooldown(1, 10, BucketType.user)
  async def avatar_(self, ctx, *, member = None):
    
    if member is None:
      
      member = ctx.author
      
      embed = Embed()
      embed.title = "{} Avatar".format(member.display_name)
      embed.set_image(url = member.avatar_url)
      embed.set_footer(text = "Request by : {}".format(ctx.author.name))
      embed.colour = Colour(random.choice(c))
      embed.timestamp = ctx.message.created_at
      await ctx.send(embed=embed)
      
    elif len(ctx.message.mentions) > 0:
      
      member = ctx.message.mentions[0]
      
      embed1 = Embed()
      embed1.title = "{} Avatar".format(member.display_name)
      embed1.set_image(url = member.avatar_url)
      embed1.set_footer(text = "Request by : {}".format(ctx.author.name))
      embed1.colour = Colour(random.choice(c))
      embed1.timestamp = ctx.message.created_at
      await ctx.send(embed=embed1)
      
    else:
      
      member = [w for w in ctx.guild.members if str(member.lower()) in w.display_name.lower()][0]
      
      embed2 = Embed()
      embed2.title = "{} Avatar".format(member.display_name)
      embed2.set_image(url = member.avatar_url)
      embed2.set_footer(text = 'Request by : {}'.format(ctx.author.name))
      embed2.colour = Colour(random.choice(c))
      embed2.timestamp = ctx.message.created_at
      await ctx.send(embed=embed2)
      
  @command(name = "serverinfo", help = "Server information")
  @cooldown(1, 10, BucketType.user)
  async def _server_info(self, ctx):
    
    user = len([w for w in ctx.guild.members if not w.bot])
    _bot = len([w for w in ctx.guild.members if w.bot])
    _role = len([w for w in ctx.guild.roles if w.hoist])
    no_cat = int(len(ctx.guild.text_channels)) + int(len(ctx.guild.voice_channels))
    
    embed = Embed()
    embed.title = "Server created"
    embed.description = str(ctx.guild.created_at.strftime("%A, %#d %B %Y at %I : %M %P")).replace("am", "AM").replace("pm", "PM")
    embed.timestamp = ctx.message.created_at
    embed.colour = Colour(random.choice(c))
    embed.set_footer(text = "Request by : {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = ctx.guild.icon_url)
    f = [
      ("You Joined", str(ctx.author.joined_at.strftime("%A, %#d %B %Y at %I : %M %P").replace("am", "AM").replace("pm", "PM")), False),
      ("Server Name", ctx.guild.name, False),
      ("Server Region", str(ctx.guild.region).upper(), False),
      ("Server ID", ctx.guild.id, False),
      ("Server Owner", "{}#{}".format(ctx.guild.owner.name, ctx.guild.owner.discriminator), False),
      ("Server channel ({})".format(no_cat), "System channel : {}\nAFK channel : {}\nText channel : {}\nVoice channel : {}".format(ctx.guild.system_channel.mention, ctx.guild.afk_channel, len(ctx.guild.text_channels), len(ctx.guild.voice_channels)), False),
      ("Server Member count", "{} Human\n{} Bot".format(user, _bot), False),
      ("Server Role", "{} Role\n{} Hoist".format(len(ctx.guild.roles), _role), False)
      ]
    for name, value, inline in f:
      
      embed.add_field(name=name, value = value, inline = inline)
      
    await ctx.send(embed=embed)
    
  @command(name = "userinfo", help = "Member information", aliases = ["ui", "whois"])
  @cooldown(1, 10, BucketType.user)
  async def _info_member(self, ctx, *,member = None):
    
    if member is None:
      
      member = ctx.author
      
      x = str(member.bot).replace("True", "Bot").replace("False", "Human")
      
      embed = Embed()
      embed.title = "Created"
      embed.description = str(member.created_at.strftime("%A, %#d %B %Y at %I : %M %P")).replace("am", "AM").replace("pm", "PM")
      embed.colour = Colour(random.choice(c))
      embed.timestamp = ctx.message.created_at
      embed.set_thumbnail(url = member.avatar_url)
      embed.set_footer(text = "Request by : {}".format(ctx.author.name))
      f = [
        ("Name", "{}#{}".format(member.name, member.discriminator), False),
        ("Nickname", member.display_name, False),
        ("Member ID", member.id, False),
        ("Status", member.status, False),
        (f"Role [{len(member.roles[1:])}]", " ".join([x.mention for x in member.roles if not x.name == "@everyone"]), False),
        ("Verification", x, False)
        ]
      for name, value, inline in f:
        
        embed.add_field(name=name, value=value, inline = inline)
        
      await ctx.send(embed=embed)
      
    elif len(ctx.message.mentions) > 0:
      
      member = ctx.message.mentions[0]
      
      x = str(member.bot).replace("True", "Bot").replace("False", "Human")
      
      embed = Embed()
      embed.title = "Created"
      embed.description = str(member.created_at.strftime("%A, %#d %B %Y at %I : %M %P")).replace("am", "AM").replace("pm", "PM")
      embed.colour = Colour(random.choice(c))
      embed.timestamp = ctx.message.created_at
      embed.set_thumbnail(url = member.avatar_url)
      embed.set_footer(text = "Request by : {}".format(ctx.author.name))
      f = [
        ("Name", "{}#{}".format(member.name, member.discriminator), False),
        ("Nickname", member.display_name, False),
        ("Member ID", member.id, False),
        ("Status", member.status, False),
        (f"Role [{len(member.roles[1:])}]", " ".join([x.mention for x in member.roles if not x.name == "@everyone"]), False),
        ("Verification", x, False)
        ]
      for name, value, inline in f:
        
        embed.add_field(name=name, value=value, inline = inline)
        
      await ctx.send(embed=embed)
      
    else:
      
      member = [w for w in ctx.guild.members if str(member.lower()) in w.display_name.lower()][0]
      
      x = str(member.bot).replace("True", "Bot").replace("False", "Human")
      
      embed = Embed()
      embed.title = "Created"
      embed.description = str(member.created_at.strftime("%A, %#d %B %Y at %I : %M %P")).replace("am", "AM").replace("pm", "PM")
      embed.colour = Colour(random.choice(c))
      embed.timestamp = ctx.message.created_at
      embed.set_thumbnail(url = member.avatar_url)
      embed.set_footer(text = "Request by : {}".format(ctx.author.name))
      f = [
        ("Name", "{}#{}".format(member.name, member.discriminator), False),
        ("Nickname", member.display_name, False),
        ("Member ID", member.id, False),
        ("Status", member.status, False),
        (f"Role [{len(member.roles[1:])}]", " ".join([x.mention for x in member.roles if not x.name == "@everyone"]), False),
        ("Verification", x, False)
        ]
      for name, value, inline in f:
        
        embed.add_field(name=name, value=value, inline = inline)
        
      await ctx.send(embed=embed)
      
  @command(name = 'stats', help = "Bot stats")
  @cooldown(1, 10, BucketType.user)
  async def __sbot(self, ctx):
    
    file = open("./json/cmd.json", "r")
    
    data = json.load(file)
    
    gw = self.bot.get_user(493768058012172288)
    gw2 = self.bot.get_user(593774699654283265)
    gw3 = self.bot.get_user(271576733168173057)
    gw4 = self.bot.get_user(740075062190669884)
    
    e = Embed()
    e.title = "Created"
    e.description = str(ctx.guild.me.created_at.strftime("%A, %#d %B %Y at %I : %M %P")).replace("am", "AM").replace("pm", "PM")
    e.colour = Colour(random.choice(c))
    e.timestamp = ctx.message.created_at
    e.set_thumbnail(url = self.bot.user.avatar_url)
    e.set_footer(text = "Request by : {}".format(ctx.author.display_name), icon_url = ctx.author.avatar_url)
    f = [
      ("Name", "Bot : {} ({})\nOwner : \n{}\n{}\n{}\n{}".format(self.bot.user, ctx.guild.me.display_name, gw, gw2, gw3, gw4), False),
      ("ID", "Bot : {}\nOwner : {}".format(self.bot.user.id, gw.id), False),
      ("Play for", "{} servers for {} users in {} shards".format(len(self.bot.guilds), len([x for x in self.bot.users if not x.bot]), self.bot.shard_count), False),
      ("Commands", "{} commands\nCommands run {}".format(len([x for x in self.bot.commands if not x.cog_name == "Owner"]), data["run"]), False),
      ("Version", "Bot : {}\nDiscord.py : {}\nPython : {}".format("0.1", discord.__version__, platform.python_version()), False)
      ]
    for name, value, inline in f:
      
      e.add_field(name=name, value=value, inline=inline)
      
    await ctx.send(embed=e)
      
  @command(name = "roleinfo", help = "Role info")
  @cooldown(1, 10, BucketType.user)
  async def _rinfo(self, ctx, *, role):
    
    if len(ctx.message.mentions) > 0:
      
      role = ctx.message.mentions[0]
      e = Embed(colour = role.colour)
      e.title = "Created"
      e.description = str(role.created_at.strftime("%A, %#d %B %Y at %I : %M %P")).replace("am", "AM").replace("pm", "PM")
      e.set_footer(text = "Request by : {}".format(ctx.author.display_name), icon_url=ctx.author.avatar_url)
      e.timestamp = ctx.message.created_at
      f = [
        ("Name", role.name, False),
        ("Color", role.colour, False),
        ("ID", role.id, False),
        ("Hoist", role.hoist, False),
        ("Mentionable", role.mentionable, False),
        ("Position", role.position, False),
        ("Member in {} ({})".format(role.name, len(role.members)), " ".join([w.mention for w in role.members][0:30]), False)
        ]
      for name, value, inline in f:
        e.add_field(name=name, value=value, inline=inline)
      await ctx.send(embed=e)
      
    else:
      
      role = [w for w in ctx.guild.roles if str(role.lower()) in w.name.lower()][0]
      
      e = Embed(colour = role.colour)
      e.title = "Created"
      e.description = str(role.created_at.strftime("%A, %#d %B %Y at %I : %M %P")).replace("am", "AM").replace("pm", "PM")
      e.set_footer(text = "Request by : {}".format(ctx.author.display_name), icon_url=ctx.author.avatar_url)
      e.timestamp = ctx.message.created_at
      f = [
        ("Name", role.name, False),
        ("Color", role.colour, False),
        ("ID", role.id, False),
        ("Hoist", role.hoist, False),
        ("Mentionable", role.mentionable, False),
        ("Position", role.position, False),
        ("Member in {} ({})".format(role.name, len(role.members)), " ".join([w.mention for w in role.members][0:30]) or "None", False)
        ]
      for name, value, inline in f:
        e.add_field(name=name, value=value, inline=inline)
      await ctx.send(embed=e)
    
    
def setup(bot):
  
  bot.add_cog(Utility(bot))
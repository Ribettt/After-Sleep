import discord, os, asyncio, aiohttp, json, datetime
from discord.ext import commands

class Owner(commands.Cog):
  
  def __init__(self, bot):
    
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_member_join(self, member):
    
    if member.guild.id != 754960201215508521:
      
      return
    
    else:
      
      e=discord.Embed(colour=discord.Colour.teal())
      e.title = "Member join"
      e.description = "Name : {}\nBot ? : {}".format(member, member.bot)
      e.timestamp = datetime.datetime.utcnow()
      e.set_thumbnail(url = member.avatar_url)
      await self.bot.get_channel(756197813804859503).send(embed=e)
      
  @commands.Cog.listener()
  async def on_member_remove(self, member):
    
    if member.guild.id != 754960201215508521:
      
      return
    
    else:
      
      e=discord.Embed(colour=discord.Colour.teal())
      e.title = "Member leave"
      e.description = "Name : {}\nBot ? : {}".format(member, member.bot)
      e.timestamp = datetime.datetime.utcnow()
      e.set_thumbnail(url = member.avatar_url)
      await self.bot.get_channel(756197813804859503).send(embed=e)
    
  @commands.command(name = 'load', hidden = True, aliases = ["l"])
  @commands.is_owner()
  async def de_load(self, ctx, name):
    
    try:
      
      self.bot.load_extension(f"command.{name}")
      await ctx.send(f"Loaded command.{name}")
      
    except Exception as e:
      
      await ctx.send("{} {}".format(ctx.author.mention, e))
      print(error)
      
  @commands.command(name = 'unload', aliases = ['un'], hidden = True)
  @commands.is_owner()
  async def de_unload(self, ctx, name):
    
    try:
      
      self.bot.unload_extension(f"command.{name}")
      await ctx.send(f"Unloaded command.{name}")
      
    except Exception as e:
      
      await ctx.send("{} {}".format(ctx.author.mention, e))
      print(error)
      
  @commands.command(name = 'reload', aliases = ["r"], hidden = True)
  @commands.is_owner()
  async def de_reload(self, ctx, name):
    
    try:
      
      if name == "all":
        
        for file in os.listdir('./command'):
          
          if file.endswith('.py'):
            
            self.bot.reload_extension(f'command.{file[:-3]}')
            
        await ctx.send("Reloaded all cog")
            
      else:
        
        self.bot.reload_extension(f"command.{name}")
        await ctx.send(f"Reloaded command.{name}")
        
    except Exception as e:
      
      await ctx.send("{} {}".format(ctx.author.mention, e))
      print(error)
    
  @commands.command(name = "as")
  @commands.is_owner()
  async def _ad(self, ctx, *, pesan):
    
    await ctx.message.delete()
    
    await ctx.channel.trigger_typing()
    await asyncio.sleep(1)
    
    await ctx.send(pesan)
    
  @commands.command(name = "dm")
  @commands.is_owner()
  async def _dmp(self, ctx, user, *, message):
    
    users = [w for w in self.bot.users if w.name.lower().startswith(user.lower())][0]
    mail = self.bot.get_user(users.id)
    await ctx.send("{} Successfully send DM to {}".format(ctx.author.mention, users))
    await mail.send(str(message))
    
  @commands.command(name = "logout")
  @commands.is_owner()
  async def _tee(self, ctx):
    
    await ctx.send("Logout...")
    await self.bot.logout()
    
def setup(bot):
  
  bot.add_cog(Owner(bot))
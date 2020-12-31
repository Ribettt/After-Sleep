import discord, nekos, io, aiohttp, _this, random
from io import BytesIO
from discord.ext import commands

class Nsfw(commands.Cog):
  
  def __init__(self, bot):
    
    self.bot = bot
    
  @commands.command(name = "anal")
  @commands.is_nsfw()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def _anal(self, ctx):
    
    await ctx.send(nekos.img("anal"))
    
  @commands.command(name = "boobs")
  @commands.is_nsfw()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def _nenen(self, ctx):
    
    await ctx.send(nekos.img("boobs"))
    
  @commands.command(name = 'yuri')
  @commands.is_nsfw()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def _yuri(self, ctx):
    
    msg = await ctx.send("<a:loading:753325685505917028> | Please wait..")
    
    url = nekos.img("yuri")
    
    file = discord.File(_this.imgs(url), filename = 'yuri.png')
    
    await msg.delete()
    
    await ctx.send(file = file)
    
  @commands.command(name = 'lewd')
  @commands.is_nsfw()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def _lewat(self, ctx):
    
    msg = await ctx.send("<a:loading:753325685505917028> | Please wait..")
    
    key = random.choice(["lewd", "lewdk", "lewdkemo", "hololewd"])
    
    url = nekos.img(key)
    
    file = discord.File(_this.imgs(url), filename = 'lewd.png')
    
    await msg.delete()
    
    await ctx.send(file = file)
    
  @commands.command(name = "hentai")
  @commands.is_nsfw()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def _classic(self, ctx):
    
    await ctx.send(nekos.img(random.choice(["classic", "random_hentai_gif"])))
    
  @commands.command(name = "solo")
  @commands.is_nsfw()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def _yesolo(self, ctx):
    
    await ctx.send(nekos.img(random.choice(['solog', 'solo'])))
    
def setup(bot):
  
  bot.add_cog(Nsfw(bot))
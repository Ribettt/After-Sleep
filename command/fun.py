import discord, _this, nekos, random, asyncio, os, aiohttp

from discord import Embed, Colour
from discord.ext import commands
from discord.ext.commands import command, Cog, cooldown, BucketType

c = [15987181, 16763890, 16629176, 765349, 402754, 16711587, 14408959, 10643837]

api = os.environ.get("api")

class Fun(Cog):
  
  def __init__(self, bot):
    
    self.bot = bot
    
  @command(name = "reddit", help = "Reddit search")
  @cooldown(1, 10, BucketType.user)
  async def reddit(self, ctx, *, search):
    
    try:
      async with aiohttp.ClientSession() as r:
        async with r.get(f"https://api.ksoft.si/images/rand-reddit/{search}".replace(" ", "%"), headers = {"Authorization": f"Bearer {api}"}) as respond:
          data = await respond.json()
      if str(data['nsfw']).lower() == "true".lower():
        
        if not ctx.channel.nsfw:
          await ctx.send("<:emoji:753337197796786179> | {} NSFW content only on nsfw channel".format(ctx.author.mention))
          
        else:
          embed = Embed()
          embed.title = data["title"]
          embed.set_image(url = data['image_url'])
          embed.set_footer(text = "Request by : {}".format(ctx.author.display_name))
          embed.colour = Colour(random.choice(c))
          embed.timestamp = ctx.message.created_at
          embed.description = "Up votes 👍 : {}\nDown votes 👎 : {}\nComments 💬 : {}\nAuthor 👤 : {}".format(data["upvotes"], data["downvotes"], data["comments"], str(data['author']).replace("/u/", ""))
          await ctx.send(embed = embed)
          
      else:
        
        embed = Embed()
        embed.title = data['title']
        embed.set_image(url = data['image_url'])
        embed.set_footer(text = "Request by : {}".format(ctx.author.display_name))
        embed.colour = Colour(random.choice(c))
        embed.timestamp = ctx.message.created_at
        embed.description = "Up votes 👍 : {}\nDown votes 👎 : {}\nComments 💬 : {}\nAuthor 👤 : {}".format(data["upvotes"], data["downvotes"], data["comments"], str(data['author']).replace("/u/", ""))
        await ctx.send(embed = embed)
        
    except:
      
      await ctx.send("<:emoji:753337197796786179> | {} Cannot get data with query `{}`".format(ctx.author.mention, search))
      
  @command(name = "meme", help = "Meme")
  @cooldown(1, 10, BucketType.user)
  async def __meme(self, ctx):
    
    async with aiohttp.ClientSession() as e:
      
      async with e.get("https://api.ksoft.si/images/random-meme", headers = {"Authorization": f"Bearer {api}"}) as r:
        
        data = await r.json()
        
    embed = Embed()
    embed.title = data["title"]
    embed.set_image(url = data['image_url'])
    embed.set_footer(text = "Request by : {}".format(ctx.author.display_name))
    embed.colour = Colour(random.choice(c))
    embed.timestamp = ctx.message.created_at
    embed.description = "Up votes 👍 : {}\nDown votes 👎 : {}\nComments 💬 : {}\nAuthor 👤 : {}".format(data["upvotes"], data["downvotes"], data["comments"], str(data['author']).replace("/u/", ""))
    await ctx.send(embed = embed)
    
  @command(name = "kiss", help = "Kiss member")
  @cooldown(1,10,BucketType.user)
  async def _kiss(self, ctx, *, member):
    
    key = "kiss"
    
    if len(ctx.message.mentions) > 0:
      
      member = ctx.message.mentions[0]
      
      if ctx.author.id == member.id:
        
        return await ctx.send("<:emoji:753337197796786179> | {} You cannot kiss your self".format(ctx.author.mention))
      
      e = Embed()
      e.description = "{} kissed {}".format(ctx.author.name, member.name)
      e.set_image(url = nekos.img(key))
      e.timestamp = ctx.message.created_at
      e.colour = Colour(random.choice(c))
      await ctx.send(embed=e)
      
    else:
      
      member = [w for w in ctx.guild.members if str(member.lower()) in w.display_name.lower()][0]
      
      if ctx.author.id == member.id:
        
        return await ctx.send("<:emoji:753337197796786179> | {} You cannot kiss your self".format(ctx.author.mention))
      
      e = Embed()
      e.description = "{} kissed {}".format(ctx.author.name, member.name)
      e.set_image(url = nekos.img(key))
      e.colour = Colour(random.choice(c))
      e.timestamp = ctx.message.created_at
      await ctx.send(embed=e)
      
  @command(name = "baka", help = "Baka member? lol..")
  @cooldown(1,10,BucketType.user)
  async def _baka(self, ctx, *, member):
    
    key = "baka"
    
    if len(ctx.message.mentions) > 0:
      
      member = ctx.message.mentions[0]
      
      if ctx.author.id == member.id:
        
        return await ctx.send("<:emoji:753337197796786179> | {} You cannot use to your self".format(ctx.author.mention))
      
      e = Embed()
      e.description = "{} baka".format(member.name)
      e.set_image(url = nekos.img(key))
      e.timestamp = ctx.message.created_at
      e.colour = Colour(random.choice(c))
      await ctx.send(embed=e)
      
    else:
      
      member = [w for w in ctx.guild.members if str(member.lower()) in w.display_name.lower()][0]
      
      if ctx.author.id == member.id:
        
        return await ctx.send("<:emoji:753337197796786179> | {} You cannot use to your self".format(ctx.author.mention))
      
      e = Embed()
      e.description = "{} baka".format(member.name)
      e.set_image(url = nekos.img(key))
      e.colour = Colour(random.choice(c))
      e.timestamp = ctx.message.created_at
      await ctx.send(embed=e)
      
  @command(name = "slap", help = "Slap member")
  @cooldown(1,10,BucketType.user)
  async def _tabok(self, ctx, *, member):
    
    key = "slap"
    
    if len(ctx.message.mentions) > 0:
      
      member = ctx.message.mentions[0]
      
      if ctx.author.id == member.id:
        
        return await ctx.send("<:emoji:753337197796786179> | {} You cannot slap your self".format(ctx.author.mention))
      
      e = Embed()
      e.description = "{} slap {}".format(ctx.author.name, member.name)
      e.set_image(url = nekos.img(key))
      e.colour = Colour(random.choice(c))
      e.timestamp = ctx.message.created_at
      await ctx.send(embed=e)
      
    else:
      
      member = [w for w in ctx.guild.members if str(member.lower()) in w.display_name.lower()][0]
      
      if ctx.author.id == member.id:
        
        return await ctx.send("<:emoji:753337197796786179> | {} You cannot slap your self".format(ctx.author.mention))
      
      e = Embed()
      e.description = "{} slap {}".format(ctx.author.name, member.name)
      e.set_image(url = nekos.img(key))
      e.colour = Colour(random.choice(c))
      e.timestamp = ctx.message.created_at
      await ctx.send(embed=e)
      
  @command(name = "pat", help = "Pat member")
  @cooldown(1,10,BucketType.user)
  async def _pat(self, ctx, *, member):
    
    key = "pat"
    
    if len(ctx.message.mentions) > 0:
      
      member = ctx.message.mentions[0]
      
      if ctx.author.id == member.id:
        
        return await ctx.send("<:emoji:753337197796786179> | {} You cannot pat your self".format(ctx.author.mention))
      
      e = Embed()
      e.description = "{} pat {}".format(ctx.author.name, member.name)
      e.set_image(url = nekos.img(key))
      e.timestamp = ctx.message.created_at
      e.colour = Colour(random.choice(c))
      await ctx.send(embed=e)
      
    else:
      
      member = [w for w in ctx.guild.members if str(member.lower()) in w.display_name.lower()][0]
      
      if ctx.author.id == member.id:
        
        return await ctx.send("<:emoji:753337197796786179> | {} You cannot pat your self".format(ctx.author.mention))
      
      e = Embed()
      e.description = "{} pat {}".format(ctx.author.name, member.name)
      e.set_image(url = nekos.img(key))
      e.timestamp = ctx.message.created_at
      e.colour = Colour(random.choice(c))
      await ctx.send(embed=e)
      
  @command(name = "emoji", help = "Emoji thief")
  @cooldown(1, 10, BucketType.user)
  async def __emmm(self, ctx, *emoji):
    
    try:
      
      e = list(emoji)[0].lower()
      
      if e.startswith("<a:"):
        
        _id, an = e.split(":")[3].split(">")[0], True
        
      else:
        
        _id, an = e.split(":")[2].split(">")[0], False
        
        if an:
          
          ez = Embed()
          ez.set_image(url = "https://cdn.discordapp.com/emojis/{}.gif".format(_id))
          ez.description = "ID : {}\nURL : [Here](https://cdn.discordapp.com/emojis/{}.gif)".format(_id, _id)
          ez.timestamp = ctx.message.created_at
          ez.set_footer(text = "Request by : {}".format(ctx.author.display_name), icon_url = ctx.author.avatar_url)
          ez.colour = Colour(random.choice(c))
          await ctx.send(embed=ez)
          
        else:
          
          ae = Embed()
          ae.set_image(url = "https://cdn.discordapp.com/emojis/{}.png".format(_id))
          ae.description = "ID : {}\nURL : [Here](https://cdn.discordapp.com/emojis/{}.png)".format(_id, _id)
          ae.timestamp = ctx.message.created_at
          ae.set_footer(text = "Request by : {}".format(ctx.author.display_name), icon_url = ctx.author.avatar_url)
          ae.colour = Colour(random.choice(c))
          await ctx.send(embed=ae)
      
    except Exception as e:
      
      await ctx.send("<:emoji:753337197796786179> | {} Invalid emoji".format(ctx.author.mention))
      
  @command(name = "8ball", help = "Ask to bot")
  @cooldown(1, 10, BucketType.user)
  async def __ball(self, ctx, *,question):
    
    if len(question) > 50:
      
      await ctx.send("<:emoji:753337197796786179> | {} Too much question".format(ctx.author.mention))
      
    else:
      
      aa = [w.mention for w in ctx.guild.members if not w.bot]
      
      a = random.choice(["Who is that?", "Sure", "No", "I don\'t know", "Yes", "Maybe", f"Ask with {random.choice(aa)}", "What ?", "No stupid"])
      
      msg = "> {}\n{} {}".format(question, ctx.author.mention, a)
      await ctx.channel.trigger_typing()
      await asyncio.sleep(1)
      await ctx.send(msg)
    
    
def setup(bot):
  
  bot.add_cog(Fun(bot))
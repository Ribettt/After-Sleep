import kitsu, discord, json, aiohttp, _this, nekos, random
from discord import Embed, Colour
from discord.ext.commands import command, Cog, cooldown, BucketType

c = [15987181, 16763890, 16629176, 765349, 402754, 16711587, 14408959, 10643837]

class Anime(Cog):
	
	def __init__(self, bot):
		
		self.bot = bot
		
		self.__headers = {
			
			"Accept": "application/vnd.api+json",
			"Content-Type": "application/vnd.api+json"
			
		}
		
		self.__url = "https://kitsu.io/api/edge"
		
	@command(name = "anime", aliases = ["an"], help = "Anime search")
	@cooldown(1, 10, BucketType.user)
	async def anime(self, ctx, *, anime_name):
	  
		try:
				
				async with aiohttp.ClientSession(headers = self.__headers) as respon:
					async with respon.get(self.__url+"/anime?filter[text]="+str(anime_name).replace(" ", "%")+"&page[limit]=1") as s:
						json = await s.json()
						
						result = json['data'][0]
						data = result['attributes']
						lainnya = "\n".join([w for w in data['abbreviatedTitles']])
						skor = data["averageRating"]
						e = Embed(
							title = data['canonicalTitle'],
							description = data['synopsis'],
							colour = Colour(random.choice(c)),
							url = "https://www.youtube.com/watch?v="+str(data['youtubeVideoId'])
							)
						e.set_thumbnail(url = data['posterImage']['original'])
						file = [
							("Status", str(data['status']).replace("current", "Ongoing").replace("finished", "Complete"), False),
							("Episodes", "{} episodes. {} minute(s)/episode".format(data['episodeCount'], data['episodeLength']), False),
							("Release", "Start : {}\nEnd : {}".format(data['startDate'], data['endDate']), False),
							("Rating", data['ageRatingGuide'], False),
							("Score", skor+"%", False),
							("Type", data['subtype'], False),
							("Abbreviated Title", lainnya or "None", False)
							]
						for name, value, inline in file:
							e.add_field(name = name, value = value, inline = inline)
						await ctx.send(embed=e)
						
		except Exception as e:
			
			await ctx.send("<:emoji:753337197796786179> | {} Cannot get data about {} anime".format(ctx.author.mention, anime_name))
			
			print(e)
	    
	@command(name = "neko", help = "Neko image")
	@cooldown(1, 10, BucketType.user)
	async def _neko(self, ctx):
	  
	  msg = await ctx.send("<a:loading:753325685505917028> | Please wait..")
	  key = nekos.img("neko")
	  
	  file = discord.File(_this.imgs(key), filename = "Neko.png")
	  await msg.delete()
	  await ctx.send(file = file)
	  
	@command(name = "foxgirl", help = "Random fox girl")
	@cooldown(1, 10, BucketType.user)
	async def _fox(self, ctx):
	  
	  msg = await ctx.send("<a:loading:753325685505917028> | Please wait..")
	  key = nekos.img("fox_girl")
	  
	  file = discord.File(_this.imgs(key), filename = "Fox girl.png")
	  await msg.delete()
	  await ctx.send(file = file)
		
def setup(bot):
	
	bot.add_cog(Anime(bot))
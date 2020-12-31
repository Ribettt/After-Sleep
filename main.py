import discord, os, flask, threading, json
from discord.ext import commands
from flask import Flask
from threading import Thread

app = Flask(" ")

async def get_prefix(bot, message):
  
  file = open("./json/prefix.json", "r")
  
  data = json.load(file)
  
  if not str(message.guild.id) in data:
    
    prefix = "!n."
    
    return prefix
    
  else:
    
    prefix = data[str(message.guild.id)]
    
    return prefix

bot = commands.AutoShardedBot(
  command_prefix = get_prefix,
  shard_count = 3,
  owner_ids = [493768058012172288, 593774699654283265, 271576733168173057, 740075062190669884, 754231498495885353]
  )
bot.remove_command('help')

@bot.event
async def on_ready():
  
  print("Ready as {}".format(bot.user.name))
  print("Watching {} server for {} user".format(len(bot.guilds), len([x for x in bot.users if not x.bot])))
  await bot.change_presence(status = discord.Status.dnd, shard_id = None, activity = discord.Activity(name = "piton jelek",type = discord.ActivityType.watching))
  
for file in os.listdir("./command"):
  if file.endswith(".py"):
    bot.load_extension(f"command.{file[:-3]}")

@app.route('/')
def home():
    return "Ready."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

keep_alive()
bot.run(os.environ.get("Token"))
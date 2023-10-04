from Scripts import bot
from Scripts import image_creator
import glob
import os

# Delete cookie
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

# Create image
image_creator.make_post()

# Create post 
bot.create_post()
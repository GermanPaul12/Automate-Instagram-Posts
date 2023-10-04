from instabot import Bot
import Scripts.creds as creds
import os


# Initialize the bot
def create_post():
    bot = Bot()

    # Login to your Instagram account
    bot.login(username=creds.USER, password=creds.PW)

    
    IMAGE_PATH = os.getcwd() + "/output.jpg"
    
    with open("Scripts/post_num.txt", "r") as f:
        num = int(f.read())
        
    HASHTAGS = "#stoics #stoic #wisdom #motivation #MarcusAurelius #Seneca #Epictetus #stoicism #quotes #inspiration #Philosophy #quote #Plato"    
    CAPTION = f"""POST NUMBER: {num}/365
    365 Days of Stoicism Challenge 🧠
    
    What do you think about this quote?
    Comment below 👇
    
    Feel free to share your own quote with us!
    
    {HASHTAGS}
    """
    # Upload a picture
    bot.upload_photo(IMAGE_PATH, caption=CAPTION)

    # Logout from your account
    bot.logout()

if __name__ == '__main__':
    create_post()    
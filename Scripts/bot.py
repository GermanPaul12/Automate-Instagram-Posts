from instabot import Bot
import Scripts.creds as creds
# Initialize the bot
def create_post():
    bot = Bot()

    # Login to your Instagram account
    bot.login(username=creds.USER, password=creds.PW)

    # Upload a picture
    bot.upload_photo('/Users/german/Downloads/test.jpeg', caption='test caption')

    # Logout from your account
    bot.logout()

if __name__ == '__main__':
    create_post()    
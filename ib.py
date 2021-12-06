from instabot import Bot

bot = Bot()

bot.login(username="cohoxe9464",password="KashiJee786143")

followers = bot.get_user_followers("affirmationsandquotes")

for id in followers:
    username=bot.get_username_from_id(id)
    print(username)

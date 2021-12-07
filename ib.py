from instabot import Bot

bot = Bot()

bot.login(username="xeyov61622",password="I have12")

followers = bot.get_user_followers("affirmationsandquotes")

with open("get_followers.txt", "a") as f:
    for i in followers:
        username = bot.get_username_from_user_id(i)
        f.write(str(username) +"\n")
        print(username)

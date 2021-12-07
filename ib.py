from instabot import Bot

bot = Bot()

bot.login(username="xeyov61622",password="I have12")

followers = bot.get_user_followers("poetalia1")

with open("get_followers.txt", "a") as f:
    for i in followers:
        print(i)
        f.write(str(bot.get_username_from_user_id(i)) +"\n")

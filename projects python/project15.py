from instabot import Bot

bot=Bot()
bot.login(username="",password="") #yaha jo id login karni h uska pass or username dalo
bot.follow('') #yaha bot ki madad se kisko follow krna h uski id daalo
bot.upload_photo() #yaha jo photo upload karni h uska location daalo properties me jaake vaha location hoga copy karo and paste,
                   #continue h: location paste karne ke bad sare backword slash(\) inko change to (/) and aage ek or / ye karke us image ka name likho , 
                   # caption bhi likh skte ho COMMA do and caption=..... likh do
bot.unfollow("")
bot.send_message("",["yaha username likhna h"])
followers=bot.get_user_followers("")
for follower in followers:
    print(bot.get_user_followers)
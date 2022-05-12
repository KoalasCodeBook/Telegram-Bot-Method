import telebot,sqlite3

API_KEY = "That's where CTRL + C/V your APIKEY"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['question','ask'])
def hello(message):
    username = message.from_user.first_name
    date = message.date
    question = message.text[7:] 

    con = sqlite3.connect("database.db")
    cursor = con.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS question (username TEXT , question TEXT , date TEXT)")     
    cursor.execute("INSERT INTO question VALUES(?,?,?)",(username,question,date))
    con.commit()

    cursor.execute("SELECT * FROM question")
    data_len = int(len(cursor.fetchall())) 

    text = "#{}. Frage".format(data_len)

    botsMessage = """
    {}. question \From: {}\n**********************\n{}""".format(data_len,username,question)

    bot.send_message(message.chat.id, botsMessage) #botsMessage goes out
    bot.delete_message(message.chat.id,message.id) #deletes the user message





bot.polling()
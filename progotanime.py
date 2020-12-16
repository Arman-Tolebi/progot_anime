import telebot
from telebot import types
# токен-бота
bot = telebot.TeleBot('1383747892:AAF273cwKxhR6KBvPNCtDz8K99mOD1ChhLw')

# если /help, /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! "
                     + message.from_user.first_name
                     + ", в боте можно смотреть аниме тетрадь смерти. «Тетрадь Смерти» обрела невероятную популярность в начале века онлайн, сделав историю противостояния Киры и гениального детектива L классикой детективного жанра и просто культовым аниме!",
                     reply_markup=markup_menu)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_1 = types.KeyboardButton('Тетрадь Смерти 1-13')
btn_2 = types.KeyboardButton('Тетрадь Смерти 14-26')
btn_3 = types.KeyboardButton('Тетрадь Смерти 27-37')
markup_menu.add(btn_1, btn_2, btn_3)

Anime1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a1 = types.KeyboardButton('Тетрадь смерти 1 серия')
btn_a2 = types.KeyboardButton('Тетрадь смерти 2 серия')
btn_a3 = types.KeyboardButton('Тетрадь смерти 3 серия')
btn_a4 = types.KeyboardButton('Тетрадь смерти 4 серия')
btn_a5 = types.KeyboardButton('Тетрадь смерти 5 серия')
btn_a6 = types.KeyboardButton('Тетрадь смерти 6 серия')
btn_a7 = types.KeyboardButton('Тетрадь смерти 7 серия')
btn_a8 = types.KeyboardButton('Тетрадь смерти 8 серия')
btn_a9 = types.KeyboardButton('Тетрадь смерти 9 серия')
btn_a10 = types.KeyboardButton('Тетрадь смерти 10 серия')
btn_a11 = types.KeyboardButton('Тетрадь смерти 11 серия')
btn_a12 = types.KeyboardButton('Тетрадь смерти 12 серия')
btn_a13 = types.KeyboardButton('Тетрадь смерти 13 серия')
btn_a14 = types.KeyboardButton('В меню')
Anime1.add(btn_a1, btn_a2, btn_a3, btn_a4, btn_a5, btn_a6, btn_a7, btn_a8, btn_a9, btn_a10, btn_a11, btn_a12, btn_a13, btn_a14)

Anime2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a15 = types.KeyboardButton('Тетрадь смерти 14 серия')
btn_a16 = types.KeyboardButton('Тетрадь смерти 15 серия')
btn_a17 = types.KeyboardButton('Тетрадь смерти 16 серия')
btn_a18 = types.KeyboardButton('Тетрадь смерти 17 серия')
btn_a19 = types.KeyboardButton('Тетрадь смерти 18 серия')
btn_a20 = types.KeyboardButton('Тетрадь смерти 19 серия')
btn_a21 = types.KeyboardButton('Тетрадь смерти 20 серия')
btn_a22 = types.KeyboardButton('Тетрадь смерти 21 серия')
btn_a23 = types.KeyboardButton('Тетрадь смерти 22 серия')
btn_a24 = types.KeyboardButton('Тетрадь смерти 23 серия')
btn_a25 = types.KeyboardButton('Тетрадь смерти 24 серия')
btn_a26 = types.KeyboardButton('Тетрадь смерти 25 серия')
btn_a27 = types.KeyboardButton('Тетрадь смерти 26 серия')
btn_a28 = types.KeyboardButton('В меню')
Anime2.add(btn_a15, btn_a16, btn_a17, btn_a18, btn_a19, btn_a20, btn_a21, btn_a22, btn_a23, btn_a24, btn_a25, btn_a26, btn_a27, btn_a28)

Anime3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a29 = types.KeyboardButton('Тетрадь смерти 27 серия')
btn_a30 = types.KeyboardButton('Тетрадь смерти 28 серия')
btn_a31 = types.KeyboardButton('Тетрадь смерти 29 серия')
btn_a32 = types.KeyboardButton('Тетрадь смерти 30 серия')
btn_a33 = types.KeyboardButton('Тетрадь смерти 31 серия')
btn_a34 = types.KeyboardButton('Тетрадь смерти 32 серия')
btn_a35 = types.KeyboardButton('Тетрадь смерти 33 серия')
btn_a36 = types.KeyboardButton('Тетрадь смерти 34 серия')
btn_a37 = types.KeyboardButton('Тетрадь смерти 35 серия')
btn_a38 = types.KeyboardButton('Тетрадь смерти 36 серия')
btn_a39 = types.KeyboardButton('Тетрадь смерти 37 серия')
btn_a40 = types.KeyboardButton('В меню')
Anime3.add(btn_a29, btn_a30, btn_a31, btn_a32, btn_a33, btn_a34, btn_a35, btn_a36, btn_a37, btn_a38, btn_a39, btn_a40,)
vmenyu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_naz5 = types.KeyboardButton('В меню')
vmenyu.add(btn_naz5)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "В меню":
        bot.reply_to(message, "Назад", reply_markup=markup_menu)
    if message.text == "Тетрадь Смерти 1-13":
        bot.reply_to(message, "Выберите серию из 1-13", reply_markup=Anime1)
    if message.text == "Тетрадь Смерти 14-26":
        bot.reply_to(message, "Выберите серию из 14-26", reply_markup=Anime2)
    if message.text == "Тетрадь Смерти 27-37":
        bot.reply_to(message, "Выберите серию из 27-37", reply_markup=Anime3)
    if message.text == "Тетрадь смерти 1 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-1.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 2 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-2.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 3 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-3.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 4 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-4.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 5 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-5.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 6 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-6.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 7 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-7.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 8 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-8.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 9 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-9.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 10 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-10.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 11 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-11.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 12 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-12.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 13 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-13.html""",
                     reply_markup=Anime1)
    if message.text == "Тетрадь смерти 14 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-14.html""",
                     reply_markup=Anime2)
    if message.text == "Тетрадь смерти 15 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-15.html""",
                     reply_markup=Anime2)
    if message.text == "Тетрадь смерти 16 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-16.html""",
                     reply_markup=Anime2)
    if message.text == "Тетрадь смерти 17 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-17.html""",
                     reply_markup=Anime2)
    if message.text == "Тетрадь смерти 18 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-18.html""",
                     reply_markup=Anime2)
    if message.text == "Тетрадь смерти 19 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-19.html""",
                     reply_markup=Anime2)
    if message.text == "Тетрадь смерти 20 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-20.html""",
                     reply_markup=Anime2)
    if message.text == "Тетрадь смерти 21 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-21.html""",
                 reply_markup=Anime2)
    if message.text == "Тетрадь смерти 22 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-22.html""",
                 reply_markup=Anime2)
    if message.text == "Тетрадь смерти 23 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-23.html""",
                 reply_markup=Anime2)
    if message.text == "Тетрадь смерти 24 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-24.html""",
                 reply_markup=Anime2)
    if message.text == "Тетрадь смерти 25 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-25.html""",
                 reply_markup=Anime2)
    if message.text == "Тетрадь смерти 26 серия":
        bot.reply_to(message, """https://jut.su/deathnote/episode-26.html""",
                 reply_markup=Anime2)
    if message.text == "Тетрадь смерти 27 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-27.html""",
                 reply_markup=Anime3)
    if message.text == "Тетрадь смерти 28 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-28.html""",
                 reply_markup=Anime3)
    if message.text == "Тетрадь смерти 29 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-29.html""",
                 reply_markup=Anime3)
    if message.text == "Тетрадь смерти 30 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-30.html""",
                 reply_markup=Anime3)
    if message.text == "Тетрадь смерти 31 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-31.html""",
                 reply_markup=Anime3)
    if message.text == "Тетрадь смерти 32 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-32.html""",
                 reply_markup=Anime3)
    if message.text == "Тетрадь смерти 33 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-33.html""",
                 reply_markup=Anime3)
    if message.text == "Тетрадь смерти 34 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-34.html""",
                 reply_markup=Anime3)
    if message.text == "Тетрадь смерти 35 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-35.html""",
                 reply_markup=Anime3)
    if message.text == "Тетрадь смерти 36 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-36.html""",
                 reply_markup=Anime3)
    if message.text == "Тетрадь смерти 37 серия":
        bot.reply_to(message,
                 """https://jut.su/deathnote/episode-37.html""",
                 reply_markup=Anime3)
bot.polling()



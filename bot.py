import telebot
import config
import wikipediaapi


##Бот для мессенджера Telegram, который по запросу будет искать статью в Википедии. Пользователь вводит слово и фразу и бот находит эту статью.
#В случае, если статьи нет, то пользователю приходит соответсвующее оповещение.

bot = telebot.TeleBot(config.TOKEN)
wiki_wiki =  wikipediaapi.Wikipedia('ru')

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('/wiki_search 🔎', '/help 🆘')

@bot.message_handler(commands=['start'])   ##Стартовая команда бота
def start_command(message):
    print(message.from_user.first_name)
    bot.send_message(message.chat.id,'Привет, ' + message.from_user.first_name + '! Я Вики-бот для поиска статей в Википедии!' +
    'Выбери команду /wiki_search и я найду тебе статью или выбери /help чтобы узнать команды', reply_markup=keyboard)



@bot.message_handler(commands=['help'])    ##Команда помощника
def help_command(message):
    bot.send_message(message.chat.id, 'Доступные команды: \n /start - вывод стартового сообщения'+
                                                           '\n /help - вывод вспомогательного сообщения'+
                                                            '\n /wiki_search - поиск статьи по заданному запросу')

@bot.message_handler(commands=['wiki_search'])
def wiki_search_command(message):
    bot.send_message(message.chat.id,'Введите название искомой статьи')


@bot.message_handler(content_types=['text'])
def search(message):
    call = message.text
    page_py =  wiki_wiki.page(call)

    if page_py.exists() == True:
        bot.send_message(message.chat.id, 'Я нашел для тебя эту статью ✔ \n' + page_py.canonicalurl)
    else:
       bot.send_message(message.chat.id, 'Я не нашел для тебя статью 🚫 \n Попробуй написать другое название')


bot.polling()

import telebot
import config
import wikipediaapi

bot = telebot.TeleBot(config.TOKEN)

wiki_wiki =  wikipediaapi.Wikipedia('ru') 



@bot.message_handler(commands=['start'])   ##Стартовая команда бота
def start_command(message):
    bot.send_message(  
        message.chat.id,  
        'Привет! Я Вики-бот для поиска статей в Википедии! Выбери команду /wiki_search и я найду тебе статью.'
    )


@bot.message_handler(commands=['wiki_search'])  
def wiki_search_command(message):    
    bot.send_message(message.chat.id,'Введите название статьи')


@bot.message_handler(content_types=['text'])
def search(message):
    call = message.text
    page_py =  wiki_wiki.page(call)

    if page_py.exists() == True:  # the article exists
        bot.send_message(message.chat.id, 'Я нашел для тебя статью: \n' + page_py.canonicalurl)
    else:
       bot.send_message(message.chat.id, 'Я не нашел для тебя статью :( Попробуй написать другое название')

#-----Работа бота-----#
bot.polling()
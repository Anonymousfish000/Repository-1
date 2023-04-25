import random
import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types
import wikipedia

wikipedia.set_lang('en') #Downloading the language to work with wikipedia

keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
button1 = types.KeyboardButton('Fact')
button2 = types.KeyboardButton('Weather')
button3 = types.KeyboardButton('Films')
button4 = types.KeyboardButton('Books')
keyboard.add(button1, button2, button3, button4)

token = '6105637509:AAE7KtOpEoLLWqs8Fixt9ylaXd5Uyq1mmUk'

bot = telebot.TeleBot(token)#Making the bot function

def getwiki(s):
    try:
        my = wikipedia.page(s)
        # Recieving 1000 words from a wikipedia page
        wikitext = my.content[:1000]
        # Dividing by the full stops
        wikimas = wikitext.split('.')
        # Creating a new variable for the text
        wikitext2 = ''
        # We are going through the sentences
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'There is no info about this subject in the Encyclopedia'

'''def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'There is no information about this in the Encyclopedia'''''



@bot.message_handler(commands = ['pleasewiki'])
def start(message):
    bot.send_message(message.chat.id, 'Send me any word and I will find its meaning\n Please do not type any of these words: \n"Fact"\n"Books"\n"Weather"\n"Films"')

@bot.message_handler(commands =['start'])#When the start command is texted in telegram
def start(message):#Our function
    bot.send_message(message.chat.id, 'I am a bot, you can text me if you need anything')

@bot.message_handler(commands =['info'])
def start(message):
    bot.send_message(message.chat.id, '/start - Begin\n/info - List of commands\n/menu - Some facts\n - Useful things')

@bot.message_handler(commands=['menu'])
def send_fact(message):
    bot.send_message(message.chat.id, 'Press a button please', reply_markup=keyboard)

@bot.message_handler(content_types =['text'])
def start(message):
    if message.text == 'Hello!':
        bot.send_message(message.chat.id, 'Hello! How is it going?')
    elif message.text == 'Good,thanks. And you?':
            bot.send_message(message.chat.id, 'Fine thanks.')
    elif message.text == 'Who created you?':
        bot.send_message(message.chat.id, 'I was created by Maksim on the 28.02.2023')
    elif message.text == 'How old are you?':
            bot.send_message(message.chat.id, 'I am 1 month old.')
    elif message.text == 'Whats up?':
        bot.send_message(message.chat.id, 'Nothing much really')
    elif message.text == 'Could you help me with this?':
        bot.send_message(message.chat.id, 'Sure, what do you need?')
    elif message.text == 'Do you like being a bot?':
        bot.send_message(message.chat.id, 'Yes, I do.')
    elif message.text == 'How old is your creator?':
        bot.send_message(message.chat.id, '13')
    elif message.text == 'Which messaging app do you like the most?':
        bot.send_message(message.chat.id, 'Telegram ofcourse.')
    elif message.text == 'Do you like whatsapp?':
        bot.send_message(message.chat.id, 'NO.')
    elif message.text.lower()=='fact':
        response = requests.get('http://facts.museum/')
        soup = BeautifulSoup(response.text, 'lxml')
        html = soup.find_all('p', class_='content')
        lst = []
        for item in html:
            lst.append(item.text)
        bot.send_message(message.chat.id,random.choice(lst))
    elif message.text.lower()=='films':
        response = requests.get('https://www.timeout.com/film/best-movies-of-all-time')
        soup = BeautifulSoup(response.text, 'lxml')
        html = soup.find_all('h3', class_='_h3_cuogz_1')
        lst = []
        for item in html:
            lst.append(item.text)
        bot.send_message(message.chat.id, 'A great film that you need to watch: ' + random.choice(lst))
    elif message.text.lower()=='books':
        response = requests.get('https://www.panmacmillan.com/blogs/general/must-read-books-of-all-time')
        soup = BeautifulSoup(response.text, 'lxml')
        html = soup.find_all('h3', class_='mb-1 text-lg font-bold sm:text-2xl')
        lst = []
        for item in html:
            lst.append(item.text)
        bot.send_message(message.chat.id, 'Here is abook that you must read: ' + random.choice(lst))
    elif message.text.lower()=='weather':
        response = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%BE%D0%BF%D0%B5%D0%BD%D0%B3%D0%B0%D0%B3%D0%B5%D0%BD')
        soup = BeautifulSoup(response.text, 'lxml')
        html = soup.find('p', class_='today-temp')
        sunset_sunrise = soup.find('div', class_='infoDaylight')
        print(sunset_sunrise.text)
        bot.send_message(message.chat.id, str(html.text) + 'Here are the sunset and sunrise times: ' + str(sunset_sunrise.text))
    else:
        bot.send_message(message.chat.id, getwiki(message.text))





bot.polling(none_stop = True, interval = 0)#Making the bot not close and replying after x seconds


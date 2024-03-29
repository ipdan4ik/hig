# -*- coding: utf-8 -*-

import telebot
from telebot import types
import config


if hasattr(config, 'proxy_server'):
    telebot.apihelper.proxy = config.proxy_server   # настройка прокси сервера

known_users = {}  # TODO: сохранить переменные в файл
bot = telebot.TeleBot(config.access_token)
botname = bot.get_me().username

start_button = types.InlineKeyboardButton(text='Начать', callback_data='start')
start_mark = types.InlineKeyboardMarkup(row_width=1)
start_mark.add(start_button)
next_button = types.InlineKeyboardButton(text='Далее', callback_data='next')
next_mark = types.InlineKeyboardMarkup(row_width=1)
next_mark.add(next_button)


class Player:
    def __init__(self, uid):
        self.uid = uid
        self.state = ['test_label', 0]
        self.gamefile = open('./labels/test_label.rpy', 'r')
        self.save_name = 'Начало'
        self.blank_space = False

    def set_state(self, state):
        self.state[1] = int(state)

    def set_file(self, name):
        self.state[0] = name
        self.gamefile = open('./labels/{0}.rpy'.format(name), 'r')

    def next_line(self):
        for line in self.gamefile:
            self.state[1] += 1
            if line.strip()[0:3] == 'n "' and line.strip() not in ['n ""', 'n "{nw}"']:  # Обычный текст, с новой строки
                normline = format_text(line)
                normline = normline[normline.find('"') + 1: -1]
                normline = "{0}".format(normline)
                if self.blank_space:
                    normline = "\n{}".format(normline)
                self.blank_space = False
                yield [normline, 'new']
            elif line.strip() == 'n ""' or line.strip() == 'n "{nw}"':      # Пустая строка
                self.blank_space = True
            elif line.strip() == 'nvl clear':                               # Очистка поля вывода
                self.blank_space = False
                yield ['', 'clr']
            elif line.strip()[0:8] == 'extend "':
                normline = format_text(line)
                normline = normline[normline.find('"') + 1: -1]
                normline = "{0}".format(normline)
                yield [normline, 'ext']
            elif line.strip()[0:5] == 'jump ':                              # Переход в другой файл
                self.set_file(line.split()[1])
                self.set_state(0)
                normline = '\n{}. Пройдено'.format(self.save_name)
                normline = normline.replace('\\n', '\n')
                self.blank_space = False
                yield [normline, 'cpl']
            elif '$ save_name ' in line:                                    # Запись сохранения
                self.save_name = line.strip()[15:-1]
# TODO: переход по главам, окно подсказок и заметок


def format_text(text):
    import re
    text = text.replace('\\n', '\n')
    text = re.sub('{/?i}', '_', text)
    text = re.sub('{/?b}', '*', text)
    text = re.sub('with .*', '', text)
    text = re.sub('{.*?}', '', text)
    text = text.strip()
    return text


def get_username(user):
    name = user.first_name
    if hasattr(user, 'username'):
        name = user.username
    elif hasattr(user, 'last_name'):
        name = name + user.last_name
    return name


@bot.message_handler(commands=['help'])
def command_help(message):
    cid = message.chat.id
    bot.send_message(cid, open("start.txt", "r").read(), reply_markup=start_mark)


@bot.message_handler(commands=['start'])
def command_start(message):
    global known_users
    uid = message.from_user.id
    if uid not in known_users:
        known_users[uid] = Player(uid)
        print('[NEW] id: {0}, name: {1}'.format(message.from_user.id, message.from_user.username))
    command_help(message)


@bot.message_handler(commands=['restart'])
def command_restart(message):
    global known_users
    cid = message.chat.id
    uid = message.from_user.id
    if uid in known_users:
        known_users[uid].set_state(0)
        known_users[uid].set_file('onikakushi_prologue')
        bot.send_message(cid, 'Прогресс сброшен!', reply_markup=start_mark)
        print('{0}: <progress_restart>'.format(botname), )
    else:
        bot.send_message(cid, 'Вас нет в базе зарегистрированных пользователей, нажмите /start, чтобы начать')
        print('{0}: <reg_error>'.format(botname))


@bot.callback_query_handler(lambda query: query.data == "next")
def callback_next(query):
    global known_users
    cid = query.message.chat.id
    uid = query.from_user.id
    if uid in known_users:
        mid = query.message.message_id
        prev_text = query.message.text
        text, key = next(known_users[uid].next_line())
        if key == 'new':
            print('{0}: "{1}"'.format(botname, text))
            text = "{}\n{}".format(prev_text, text).encode('utf-8')
            bot.edit_message_text(text, chat_id=cid, message_id=mid, parse_mode='Markdown', reply_markup=next_mark)
        elif key == 'blk':
            print('{0}: "{1}"'.format(botname, text))
            text = "{}\n{}".format(prev_text, text).encode('utf-8')
            bot.edit_message_text(text, chat_id=cid, message_id=mid, parse_mode='Markdown', reply_markup=next_mark)
        elif key == 'ext':
            print('{0}: "{1}"'.format(botname, text))
            text = "{} {}".format(prev_text, text).encode('utf-8')
            bot.edit_message_text(text, chat_id=cid, message_id=mid, parse_mode='Markdown', reply_markup=next_mark)
        elif key == 'clr':
            command_play(query)
        elif key == 'cpl':
            print('{0}: "{1}"'.format(botname, text))
            text = "{}\n{}".format(prev_text, text).encode('utf-8')
            bot.edit_message_text(text, chat_id=cid, message_id=mid, parse_mode='Markdown', reply_markup=start_mark)
    else:
        bot.send_message(cid, 'Вас нет в базе зарегистрированных пользователей, нажмите /start, чтобы начать')
        print('{0}: <reg_error>'.format(botname))


@bot.callback_query_handler(lambda query: query.data == "start")
def command_play(query):
    global known_users
    cid = query.message.chat.id
    uid = query.from_user.id
    text, key = next(known_users[uid].next_line())
    if key == 'new':
        bot.send_message(cid, text, parse_mode='Markdown', reply_markup=next_mark)
        print('{0}: "{1}"'.format(botname, text))
    elif key == 'blk':
        command_play(query)
    elif key == 'ext':
        bot.send_message(cid, text, parse_mode='Markdown', reply_markup=next_mark)
        print('{0}: "{1}"'.format(botname, text))
    elif key == 'clr':
        command_play(query)
    elif key == 'cpl':
        bot.send_message(cid, text, parse_mode='Markdown', reply_markup=start_mark)
        print('{0}: "{1}"'.format(botname, text))


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(get_username(m.from_user)) + " [" + str(m.chat.id) + "]: " + m.text)


bot.set_update_listener(listener)
bot.polling()

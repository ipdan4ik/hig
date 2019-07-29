# -*- coding: utf-8 -*-

import telebot
from telebot import types


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.username) + " [" + str(m.chat.id) + "]: " + m.text)


botname = 'vajupa_bot'
known_users = {}  # TODO: save vars to file
bot = telebot.TeleBot("811895373:AAFgMbNGMOjOEb4qaO8IeKtZ0jEG63BpeBk")

next_button = types.InlineKeyboardButton(text='next', callback_data='next')
next_mark = types.InlineKeyboardMarkup(row_width=1)  # keyboard
next_mark.add(next_button)


class Player:
    def __init__(self, uid):
        self.uid = uid
        self.state = ['onikakushi_prologue', 0]
        self.gamefile = open('./labels/onikakushi_prologue.rpy', 'r')

    def set_state(self, state):
        self.state[1] = state

    def set_file(self, name):
        self.state[0] = name
        self.gamefile = open('./labels/{0}.rpy'.format(name), 'r')

    def next_line(self):
        blank_space = False
        for line in self.gamefile:
            self.state[1] += 1
            if line.strip()[0:3] == 'n "' and line.strip() != 'n ""':
                normline = line.strip()[line.strip().find('"') + 1: -1]
                normline = "{0}".format(normline)
                if blank_space:
                    normline = "\n{}".format(normline)
                blank_space = False
                yield [normline, 'new']
            elif line.strip() == 'n ""':
                blank_space = True
            elif line.strip() == 'nvl clear':
                blank_space = False
                yield ['', 'clr']
            elif line.strip()[0:8] == 'extend "':
                normline = line.strip()[line.strip().find('"') + 1: -1]
                normline = "{0}".format(normline)
                yield [normline, 'ext']
            elif line.strip()[0:5] == 'jump ':
                self.set_file(line.split()[1])
                self.set_state(0)
                normline = '{}. Пройдено'.format(line.split()[1])
                blank_space = True
                yield [normline, 'cpl']


@bot.message_handler(commands=['help'])
def command_help(message, run_from='bot'):
    cid = message.chat.id
    bot.send_message(cid, open("start.txt", "r").read(), reply_markup=next_mark)
    if run_from == 'bot':
        print('{0}: <help_text>'.format(botname))


@bot.message_handler(commands=['start'])
def command_start(message):
    global known_users
    uid = message.from_user.id
    if uid not in known_users:
        known_users[uid] = Player(uid)
        print('[NEW] id: {0}, name: {1}'.format(message.from_user.id, message.from_user.username))
    command_help(message, 'command_start')


@bot.message_handler(commands=['restart'])
def command_restart(message):
    global known_users
    cid = message.chat.id
    uid = message.from_user.id
    if uid in known_users:
        known_users[uid].set_state('onikakushi_prologue, 0')
        bot.send_message(cid, 'Прогресс сброшен!')
        print('{0}: <progress_restart>'.format(botname))
        command_play(message)
    else:
        bot.send_message(cid, 'Вас нет в базе зарегистрированных пользователей, нажмите /start, чтобы начать')
        print('{0}: <reg_error>'.format(botname))


# new clr ext
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
            text = "{}\n{}".format(prev_text, text)
            bot.edit_message_text(text, chat_id=cid, message_id=mid, reply_markup=next_mark)
            print('{0}: "{1}"'.format(botname, text))
        elif key == 'blk':
            text = "{}\n{}".format(prev_text, text)
            bot.edit_message_text(text, chat_id=cid, message_id=mid, reply_markup=next_mark)
            print('{0}: "{1}"'.format(botname, text))
        elif key == 'ext':
            text = "{} {}".format(prev_text, text)
            bot.edit_message_text(text, chat_id=cid, message_id=mid, reply_markup=next_mark)
            print('{0}: "{1}"'.format(botname, text))
        elif key == 'clr':
            command_play(query)
        elif key == 'cpl':
            bot.edit_message_text(text, chat_id=cid, message_id=mid, reply_markup=next_mark)
            print('{0}: "{1}"'.format(botname, text))
    else:
        bot.send_message(cid, 'Вас нет в базе зарегистрированных пользователей, нажмите /start, чтобы начать')
        print('{0}: <reg_error>'.format(botname))


def command_play(query):
    global known_users
    cid = query.message.chat.id
    uid = query.from_user.id
    text, key = next(known_users[uid].next_line())
    if key == 'new':
        bot.send_message(cid, text, reply_markup=next_mark)
        print('{0}: "{1}"'.format(botname, text))
    elif key == 'blk':
        command_play(query)
    elif key == 'ext':
        bot.send_message(cid, text, reply_markup=next_mark)
        print('{0}: "{1}"'.format(botname, text))
    elif key == 'clr':
        command_play(query)
    elif key == 'cpl':
        bot.send_message(cid, text, reply_markup=next_mark)
        print('{0}: "{1}"'.format(botname, text))


# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def command_default(message):
#     cid = message.chat.id
#     bot_msg = bot.send_message(cid, 'Привет')
#     bot.edit_message_text("{} ... Edited!".format(bot_msg.text), chat_id=cid, message_id=bot_msg.message_id)


bot.polling()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging
import random
import json
from MonsterSpawn import *
from sql_helper import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Get TOKEN from TOKEN.json
with open('TOKEN.json','r') as f:
    TOKEN = json.load(f)

# Get Monster_dict
with open('Monsters.json', 'r') as f: 
    Monster_dict = json.load(f) 

# Initiate sqlite database
conn = create_connection('db.sqlite')

# create monster table
create_table(conn, """Monsters (
                               ID integer PRIMARY KEY,
                               name text NOT NULL UNIQUE,
                               Monster_id integer NOT NULL,
                               Str integer NOT NULL,
                               Dex integer NOT NULL,
                               Con integer NOT NULL,
                               Int integer NOT NULL,
                               Wis integer NOT NULL,
                               Cha integer NOT NULL,
                               HP integer NOT NULL
                            );""")


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
j = updater.job_queue


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
    text='''Hi! I'm Athena, a DND game bot under development!\n 
            You can use /1D + your_number to roll a dice with range 1 to you_number!\n 
            Use /d to roll multiple dice!\n
            Use /spawn + monster ID, number to spawn monsters!\n
            Use /sudo_info + monster name to get monster info!''')

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def spawn(update, context):
    try:
        text = ' '.join(context.args).upper()
        arg = text.split(",")
        Monster_id = int(arg[0])
        try:
            num = int(arg[1])
        except:
            num = 1
        conn = create_connection('db.sqlite')
        count = monster_count(conn, Monster_id)
        results = Spawn_Monsters(Monster_id, count, num)

        for i in results:
            create_monster(conn, i)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Spawned {0}!".format(i[0]))
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, please try again.")

spawn_handler = CommandHandler('spawn', spawn)
dispatcher.add_handler(spawn_handler)


def rename(update, context):
    try:
        text = ' '.join(context.args)
        arg = text.split(' ')
        monster_name = str(arg[0])
        new_name = str(arg[1])
        conn = create_connection('db.sqlite')
        log = update_monster(conn,monster_name,"name",new_name)
        context.bot.send_message(chat_id=update.effective_chat.id, text=log)

    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, please try again.")

rename_handler = CommandHandler('rename', rename)
dispatcher.add_handler(rename_handler)        

def sudo_info(update, context):
    try:
        conn = create_connection('db.sqlite')
        text = ' '.join(context.args)
        info = monster_info(conn, text)

        context.bot.send_message(chat_id=update.effective_chat.id, text=str(info))
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, please try again.")

sudo_info_handler = CommandHandler('sudo_info', sudo_info)
dispatcher.add_handler(sudo_info_handler)


def D(update, context):
    try:
        num = int(context.args[0])
        context.bot.send_message(chat_id=update.effective_chat.id, text=random.randint(1,num))
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, please try again.")

D_handler = CommandHandler('1D', D)
dispatcher.add_handler(D_handler)


def d(update, context):
    try:
        text = ' '.join(context.args).upper()
        dice = text.split("+")
        s = 0
        n = 0
        eqn = ''
        for i in dice:
            times = int(i.split("D")[0])
            for j in range(times):
                n = random.randint(1,int(i.split("D")[1]))
                s += n
                eqn += str(n) + '+'

        context.bot.send_message(chat_id=update.effective_chat.id, text=eqn[0:-1]+" = "+str(s))
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, please try again.")

d_handler = CommandHandler('d', d)
dispatcher.add_handler(d_handler)


'''
def sudo_KILL(update, context):
    if ' '.join(context.args) == password:
        context.bot.send_message(chat_id=update.message.chat_id, text="Kedith Offline.")
        dont_stop_me_now = 0
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Please put the password after the command.")  

sudo_KILL_handler = CommandHandler('sudo_KILL', sudo_KILL)
dispatcher.add_handler(sudo_KILL_handler)
'''


def unkown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I don't understand that command.")

unkown_handler = MessageHandler(Filters.command, unkown)
dispatcher.add_handler(unkown_handler)


updater.start_polling()

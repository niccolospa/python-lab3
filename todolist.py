from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction

tasks = []

def start():
    file = open("task_list.txt","r")
    list = file.read().split("\n")
    for line in list:
        tasks.append(line)

def insert(bot, update, args):
    tasks.append(args)
    print(tasks)
    update.message.reply_text("The new task %s was successfully added to the list!", args)

def remove(tasks, task):
    tasks.remove(task)

def close_program(tasks):
    file = open(argv[1],"w")
    for task in tasks:
        file.write(task)

def err(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    reply = "I'm sorry, I can't do that."
    update.message.reply_text(reply)

def show(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    if tasks.count() == 0:
        update.message.reply_text("Nothing to do, here!")
        return
    sortedTasks = sorted(tasks)
    reply = str(sortedTasks)
    print(reply)
    update.message.reply_text(reply)

def main():
    '''
    AmITaskListBot
    '''



    updater = Updater("596278031:AAE7CyDuJbFoYIsyKsezaaKBDnzI3lILy98")

    dp = updater.dispatcher

    start()
    dp.add_handler(MessageHandler(Filters.text, err))
    dp.add_handler(CommandHandler("showTasks", show))
    dp.add_handler(CommandHandler("newTask", insert, pass_args=True))
    # dp.add_handler(CommandHandler("removeTask", remove))
    # dp.add_handler(CommandHandler("removeAllTasks", removeall))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__': #equivalente della funzione main
    main()

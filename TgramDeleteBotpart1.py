import telegram.ext
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None

##################################################3
def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('945487978:AAHAsO66Z9xpjHKPIIyjUqaUKTroIAA2XTw')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            delete_msg(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            update.message.reply_text(update.message.text)

def delete_msg(bot, update):
    print(update.message.message_id, type(update.message.message_id))
    for i in range(50):
        bot.deleteMessage(chat_id=update.message.chat_id, message_id= 21+1)
if __name__ == '__main__':
    main()

    
    #########################
telegram_bot = telepot.Bot('945487978:AAHAsO66Z9xpjHKPIIyjUqaUKTroIAA2XTw')
print (telegram_bot.getMe())

response = telegram_bot.getUpdates()
print(response)

print("hello world")

def action(msg):
    chat_id = msg['chat']['id'] 
   
    command = msg['text']  
    print ('Received: %s' % command)
    telegram_bot.sendMessage (820013212, 'Input detected')
    telegram_bot.deleteMessage (820013212 , 2)

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')  


while 1:
    time.sleep(1) 

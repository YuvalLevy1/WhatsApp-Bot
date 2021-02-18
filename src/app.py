from src import whatsapp_bot
import time


def main():
    bot = whatsapp_bot.Bot()
    bot.enter_whatsapp()
    bot.enter_chat("הסתדרות המורים")
    last_mes = ""
    while True:
        time.sleep(0.3)
        message = bot.get_last_message()
        if message != last_mes:
            print(message)
            last_mes = message


if __name__ == '__main__':
    main()

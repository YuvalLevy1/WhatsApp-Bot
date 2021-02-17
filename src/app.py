from src import whatsapp_bot


def main():
    bot = whatsapp_bot.Bot()
    bot.enter_whatsapp()
    bot.enter_chat("שלומי")
    print(bot.get_last_message())


if __name__ == '__main__':
    main()

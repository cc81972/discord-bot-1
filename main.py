# import certifi
import ssl
import bot
# ssl_context = ssl.create_default_context(cafile=certifi.where())
# ssl_context.check_hostname = False
# ssl_context.verify_mode = ssl.CERT_NONE
if __name__ == '__main__':
    bot.run_discord_bot()
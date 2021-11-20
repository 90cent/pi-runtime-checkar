import subprocess
import time
from datetime import datetime
from discord_webhook import DiscordWebhook

# You WILL NEED TO create a private/private.txt file, with your webhook url written in to it

file = open("private/private.txt")
webhook = DiscordWebhook(file.read())
start_time = datetime.now()

webhook.content = "Raspberry script started at " + start_time.strftime("%H: %M: %S: - %d.%b.%Y")
webhook.execute()

def pi_check():
    s = subprocess.run(['uptime'], stdout=subprocess.PIPE)
    webhook.set_content(s.stdout)
    webhook.execute()


while True:
    time.sleep(3)
    pi_check()    



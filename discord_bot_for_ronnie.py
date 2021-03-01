import requests
import random
import time

##This is all POST Request stuff, I didn't do it, stolen from https://www.w3schools.com/PYTHON/ref_requests_post.asp
def send_message(message):
    url = '[YOUR_URL]' ##TODO Change to your URL
    myobj = {'content': message}

    x = requests.post(url, data = myobj)

##This takes an array of strings and picks a random one to assign as the message
def pick_a_message(): 
    options = [] ##TODO Add whatever options you would like
    options_size = len(options)
    return options[random.randint(0, options_size)]

##Main Method
num_of_messages = input("How many messages do you want to send? ")
old_time = time.time() ##Starts the timer for 30 seconds
counter = 0

while counter < int(num_of_messages):
    if time.time() - old_time > 10: ##Reset to 30
        old_time = time.time() ##Resets the timer
        ##I honestly have no idea why send_message() won't accept pick_a_message() so i made an intermediate step
        message = pick_a_message()
        send_message(message)
        counter = counter + 1
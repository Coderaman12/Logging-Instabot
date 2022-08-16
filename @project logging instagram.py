from distutils.command.config import config
from email import message
import logging
from traceback import print_tb
from instabot import Bot
from getpass import getpass
from time import sleep
from os import remove

from requests import delete
logging.basicConfig(filename="logdebug.txt",
                    filemode="a",
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

mybot=Bot()
logging.info("bot initilization.")

sleep(2)
print("connection to http://instagram.com/",end="")
for i in range(3):
    sleep(1)
    print(".",end="")
print()
sleep(2)
print("connection established!")
sleep(1)
logging.info("application initilized.")

## login
username=input("username=")
password=getpass(prompt="Password= ")
mybot.login(username=username,password=password)
print(f"--USER {username} LOGGED IN --")
logging.info("USER LOGGED IN")
while True:
    try:
        print("1. send message to user\n0.exit app")
        n=int(input("choose option"))
        if n==1:
            user=input("enter username to send message: ")
            logging.info(f"choose to send message to {user}.")
            message=input("enter the message : ")
            mybot.send_message(message,user)
            print(f"-- message send to {user} --" )
            logging.info(f"message send to {user}.")
        elif n==0:
            mybot.logout()
            logging.info("user logged out.")
            sleep(2)
            print("logging out in process",end="")
            for i in range(3):
                sleep(1)
                print(".",end="")
            print()
            sleep(2)
            print("connection closed ! ")
            sleep(1)
            print("--logged out succesfully--")
        else:
            print("--wrong input choose again --")
    except Exception as err:
        logging.error(f"found error {err} ")
        print(f"--error {err}.")
remove("comfig")  #delete config folder            
logging.critical("config delected ! ") 

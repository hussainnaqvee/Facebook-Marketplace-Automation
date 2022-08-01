from threading import Thread
import time
from boostListingV2 import main

users = [['boostingAccount1', 'password1'], ['boostingAccount2', 'password2']]

link1 = ['Add your Marketplace profile links, example given below']
#example: ['https://www.facebook.com/marketplace/profile/100002122392064/?ref=permalink']

T1 = Thread(target=main, args=(users, link1))
T1.start()

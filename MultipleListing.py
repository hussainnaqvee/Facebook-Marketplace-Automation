from ast import arg
from main import main
from threading import Thread
import time
from option import details

folder = "M-17"

set1 = [['username1', 'passowrd1'], ['username2', 'password2']]
set2 = [['username1', 'passowrd1'], ['username2', 'password2']]
set3 = [['username1', 'passowrd1'], ['username2', 'password2']]

"""Use Threads according to your system thread Otherwise the script might crash"""
T1 = Thread(target=main, args=(set1, folder))
T2 = Thread(target=main, args=(set2, folder))
T3 = Thread(target=main, args=(set3, folder))

T1.start()
T2.start()
T3.start()

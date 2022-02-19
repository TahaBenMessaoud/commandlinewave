import time
import math 
import random
import os
os.system('color')
a=0
b=0

while(1):
    for i in range(int(math.sin(a/50)*50+50)):
        print("\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(0,b,b//2+128,chr(random.randrange(93)+33)),end="")
    b=int(math.sin(a/2/128)*128+128)
    print("\n")
    time.sleep(0.000000001)
    a=a+math.pi
   
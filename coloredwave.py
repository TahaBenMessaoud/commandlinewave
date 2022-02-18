import time
import math 
import random
import os
os.system('color')
a=0
b=0

while(1):
    for i in range(int(math.sin(a/50)*50+50)):
        print("\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format((20*b%156)+100,((20*b//256)%156)+100,((20*b//(256*2))%156)+100,chr(random.randrange(93)+33)),end="")
        b=b+1
    print("\n")
    time.sleep(0.000000001)
    a=a+math.pi
   

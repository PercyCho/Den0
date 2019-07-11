pw1 = 0 # Setting both the answer and the name to 0. You'll see why
playername = 0
import time # Importing everything...
from colorama import init
init()
from colorama import Fore, Back, Style
import data
from part_1 import bootup, p1_1, p1_2
# Here I have to put all of the functions because of scope (which sucks) so when the player comes back in, they can enter where they left off, and all of the information saves.
def part_1():
    time.sleep(1)
    if(pw1 == '2'):
        p1_1.fn3()
        time.sleep(2)
        p1_2.fn4(0)
    else:
        p1_2.fn4(0)
# And here is the code for the checking to see what part you were on (because it 'Autosaves'(kinda))
savefi1 = open('data/player_data.py', 'r')
eventline = savefi1.readline()
if (eventline == "0\n"):
    pw1 = savefi1.read().split('\n')[1]
    print(Fore.BLACK + Style.NORMAL + Back.CYAN + "Playing from Save 0...")
    part_1()
else:
    savefi1.close()
# And here's the code for the beginning!
print(Style.NORMAL + Fore.RED + Back.RESET + "Put in the password to continue", end="\n" + Fore.YELLOW)
password = input()
if (password == 'password'):
    print(Fore.RED + Style.BRIGHT + 'haha\nvery funny')
    time.sleep(1)
    print('That, in fact, was not the password\nI find it absurd that people are so lazy, so they put "password" as their password. That is SO easy to figure out and MANY people have gotten their phones hacked BECAUSE their password was "password".')
    time.sleep(5.75)
    print('very disapointed')
    exit()
else:
    print(Fore.GREEN + Style.BRIGHT + "yeah it didn't really matter anyway")
    time.sleep(1)
def fn1():
    print('So, how are you?\n  1: Good, I guess\n  2: Not that good', end="\n" + Fore.WHITE)
    global pw1
    pw1 = input()
    if(pw1 == '1'):
        print(Fore.GREEN + 'Oh good!')
    elif(pw1 == '2'):
        print(Fore.GREEN + "That's too bad")
    else:
        print(Fore.GREEN + "let's try that again")
        fn1()
fn1()
time.sleep(1)
print("Let's get to know each other more!")
time.sleep(1)
print("My name is Deno, and I'm a python program. My code is a little basic, but I think thats ok! At least I'm taking to you!")
time.sleep(4)
def name():
    print("What's your name?", end ="\n" + Fore.WHITE)
    global playername
    playername = input()
    if(playername.find( "I'm ") != -1):
        playername = playername.replace("I'm ", "")
        print(Fore.GREEN + "Hi, " + playername + "!")
    elif(playername.find("My name is ") != -1):
        playername = playername.replace("My name is ", "")
        print(Fore.GREEN + "Hi, " + playername + "!")
    else:
        print(Fore.GREEN + "Hi, " + playername + "!")
name()

time.sleep(1)
bootup.fn2()

savefi1 = open('data/player_data.py', 'a')
savefi1.write("0\nplayername = '" + playername + "'\n" + pw1)
savefi1.close()

part_1()
exit()
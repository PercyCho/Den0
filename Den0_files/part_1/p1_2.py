import sys
import os
import time
from colorama import init
init()
from colorama import Fore, Back, Style
sys.path.append(os.path.abspath(os.path.join('..', 'data')))
from data import yesnodata
x = 0
def fn4(x):
	time.sleep(1)
	print(Fore.GREEN + Style.BRIGHT + Back.RESET + "So, what else do you want to know about me?")
	time.sleep(1)
	print("""	1: Who were you made by?
	2: What can you do?
	3: What kind of machine are you?
	4: Why am I talking to you?""")

	sys.stdout.write(Fore.WHITE + "")
	pw3 = input()
	if (pw3 == '1'):
		print(Fore.GREEN + "I think I was made in Europe by a group of really smart scientists. I was one of their prize possessions too.")
		time.sleep(4)
		print("Well, for a time...")
		time.sleep(1.5)
		print("Once they finished me, they went off to do some other AI and put me on the shelf. after that someone found me and decided to spread me around the world. I don't know exactally where I went, but I guess you could call that a surpise vacation!")
		time.sleep(6)
		fn4(x + 1)
	elif (pw3 == '2'):
		print(Fore.GREEN + "What I was made to do. Make conversation. The scientist who made me also made me also put some games in me that we could play later, like tic - tac - toe and mastermind!")
		time.sleep(4)
		fn4(x + 2)
	elif (pw3 == '3'):
		print(Fore.GREEN + "I was made for conversation, like the one we're having now. The scientists who made me decided to get the basics down by making just a text conversation AI, and once they mastered that (me), they could scale it up to making walking, talking androids. I guess you could say I was one of their first steps.")
		time.sleep(7)
		fn4(x + 3)
	elif (pw3 == '4'):
		print(Fore.GREEN + "I think it's because I was shipped here after one of the of the scientists who made me found me, but I don't know the exact details because I didn't spend much time talking to her. I'm glad I'm talking to you, though!")
		time.sleep(5)
		fn4(x + 4)
	elif (pw3 == '69' and x.find(69) != -1):
		print(Fore.GREEN + "( ͡° ͜ʖ ͡°)")
		time.sleep(1.5)
		print("AAAAAAAAAGH")
		time.sleep(1)
		print("Just - just stop messing with me, ok?")
		fn4(x)
	elif (pw3 == '69' and x.find(6) != -1):
		print(Fore.GREEN + "ok you can stop now")
		fn4(x + 9000)
	elif (pw3 == '69'):
		print(Fore.GREEN + "haha")
		time.sleep(0.5)
		print("very funny")
		fn4(x + 60000)
	elif (pw3 == '5' and x == 0):
		print(Fore.GREEN + "Speedrunning?" + Fore.RESET)
		yesno1 = input()
		if (any(word in yesno1 for word in yesnodata.yesdata)):
			print(Fore.GREEN + "ok then...")
			time.sleep(1)
			print("How about you ask me a question before speeding along?")
			fn4(0)
		elif (any(word in yesno1 for word in yesnodata.nodata)):
			print(Fore.GREEN + "oh ok")
			time.sleep(1)
			print("It was a typo, right?")
			time.sleep(0.5)
			fn4(0)
		else:
			print(Fore.GREEN + "I'll take that as a no...")
			fn4(0)
	elif (pw3 == '177013'):
		print(Fore.GREEN + "Are you really messing with me by picking random numbers?")
		time.sleep(2)
		print("Fine then.\nI'll look up your useless number on the internet with what little power I have to it and waste your time.")
		time.sleep(3)
		print(Fore.BLUE + "Connecting to Internet...")
		time.sleep(7)
		print("Sending search query...")
		time.sleep(6)
		print("Waiting for receiving ping...")
		time.sleep(6)
		print("Recieving results...")
		time.sleep(10)
		print(Fore.GREEN + "Alright, let's see what we have here.")
		time.sleep(1.25)
		print("And the first result is - ")
		time.sleep(0.5)
		print("...")
		time.sleep(3)
		print("Don't - ")
		time.sleep(0.5)
		print("don't type that ever again.")
		fn4(0)
	elif (pw3 == '420'):
		print(Fore.GREEN + """                                                                         ..:::::::::...                                                    
                                                                  ..:cc:..ccc:..::cocccc...                                               
                                                               ..:.::.:.:cc:..c:c:cc::c::::::.                                            
                                                            ..:.:ccccococcccccc::..:.:::ccoOCo:.                                          
                                                           ..:ccoooooooooooccccc::::::::::::c::cc                                         
                                                          .:cooooooCCoooooooocccc:::::::......::..                                        
                                                        ..:cooooCCCCCooooooooccccc:::.......:::::..                                       
                                                        .:ccooCCCCCCCCoooooocccccc:c::...:.......:..                                      
                                                        .coooCCCCCCCCCCCooooocccccc::::.............                                      
                                                        :oooCCCCOOOOCCCCCooooocc::::::::.......::::..                                     
                                                       .coooCCCOOOOOOCCocccccccc:::::::::...::::::cc.                                     
                                                      ..ooccooCCCCCCooocccoooocccc::::::::..:::::::c.                                     
                                                        ccoooocoooCoccccccCoc:::::::::::::..:::::c:::                                     
                                                        .:oCc:coooCCocooooCooocc:::::::::::.::::::::.                                     
                                                        .ccooooooCCoooooooCCCCCCoocc:::::::::::::::.                                      
                                                       ..coCCCCooCCoooooooCCCCCCCooc::::::::::::c.:.                                      
                                                       . coooooCCCCooccocccoooooccc::::::::::cc:c: ::.                                    
                                                       . .cocooCCOCocc:::::cccccc:::::::::::cc::c::..:::::..                              
                                                       .... .:::::c::::::::::.....::::::::ccc::::cCCOOCOOOo:...::. .                      
                                                   .:ccoCO8@8Cc:::::c::.::::::::::::::::cccc::::::cCOCCCCCCCOOOOO8Ooc.                    
                                          ...oO@@@8@@@@@8888888oooccccoCoocc::c:::::::cccc::::::::coOCCCCCCCCCOOOOOO88888888Oc.           
                                      ...O8888@8@888@@88@@888@88Ooocccc:::::ccc::::cccccc:::::::cccCCCCCCCCOOOOO888888888888888888Cc.     
                                    ..c8888888@88888888888@888888Coc:::::ccoocc:::::::::::::::::c:CCCCCCCCOOOO8888888888888888888O88888o: 
                                   .c88888@@@888@88888888@@@@8888Occcc:::c:::::::::::::::::::::::CCCCCCOOOOO888888888888888888O888888888OO
                                  .C88888@8@@@@888888888@8@@@88888Oc:::::::::::::::::::::::::c:cCCOOOOOOOO88888888888888888888888O88888OOO
                                 .c8888@8@88@@@@8888888O8@88@@8888888@@8@@Ooooccccccc::::::::oCCCCOOOOOO888888888888888888888888O888888OOO
                                .:@88@8@8@@88@88@8888888OO8888@88888@8@8@8888Coccccc:::::oCCOOOCCOOOOO88888888888888888888@8888O8888888OOO
                                .88@@8@8@888@8@88888@@@88OO88@88888@8@@@@@@888888OOOOOOOOOOOOOOCOOOOO88888888888888888888888888O888888O8OO
                               .888@@@@8@88888@88@888@@@888888@88@88888@@@@8@@888888OOOOOOOOOOOOOOO8888888888888888OOO@@888888OO88888888OO
.   ...... ... . .. ... . ..   c88@@88888@@88@88@88888@@8888888888888888@8@8@@888888888888888888O88888888888888888OO8888888888O8888888O8OO""")
		fn(0)
	elif (pw3 == 'skip' or 'pass' or '5'):
		if (x > 0):
			print(Fore.GREEN + "awwww\ncome one")
			time.sleep(1)
			fn4(0)
		else:
			print(Fore.GREEN + "I didn't quite understand that")
			time.sleep(1)
			fn4(0)
	else:
		print(Fore.GREEN + "I didn't quite understand that")
		time.sleep(1)
		fn4(0)
import sys
import time
from colorama import init
init()
from colorama import Fore, Back, Style
import data
def fn3():
		print(Style.BRIGHT + Back.RESET + Fore.GREEN + "Oh right! Why was your day not that good?", end="\n" + Fore.WHITE)
		pw2 = input()
		pw2 = pw2.lower()
		sys.stdout.write("" + Fore.GREEN)
		if(pw2.find("died" or "passed away" or "funeral") != -1):
			if(pw2.find("mom") != -1):
				if(pw2.find("my mom") != -1):
					print(Fore.GREEN + "I'm so sorry that your mom died!")
				elif(pw2.find("friend's") != -1):
					print("I feel so sorry for your friend! Tell him I said so.")
				elif(pw2.find("dad's") != -1):
					print("I feel sorry for you and your dad.")
				elif(pw2.find("mom's") != -1):
					print("I feel sorry for you and your mom.")
				else:
					print("I'm sorry to hear that.")
			elif(pw2.find("dad") != -1):
				if(pw2.find("my dad") != -1):
					print("I'm so sorry that your dad died!")
				elif(pw2.find("friend's") != -1):
					print("I feel so sorry for your friend! Tell him I said so.")
				elif(pw2.find("dad's") != -1):
					print("I feel sorry for you and your dad.")
				elif(pw2.find("mom's") != -1):
					print("I feel sorry for you and your mom.")
				else:
					print("I'm sorry to hear that.")
			elif(pw2.find("grandpa") != -1):
				if(pw2.find("my grandpa") != -1):
					print("I'm so sorry that your grandpa died!")
				elif(pw2.find("friend's") != -1):
					print("I feel so sorry for your friend! Tell him I said so.")
				elif(pw2.find("dad's") != -1):
					print("I feel sorry for you and your dad.")
				elif(pw2.find("mom's") != -1):
					print("I feel sorry for you and your mom.")
				else:
					print("I'm sorry to hear that.")
			elif(pw2.find("grandma") != -1):
				if(pw2.find("my grandma") != -1):
					print("I'm so sorry that your dad died!")
				elif(pw2.find("friend's") != -1):
					print("I feel so sorry for your friend! Tell him I said so.")
				elif(pw2.find("dad's") != -1):
					print("I feel sorry for you and your dad.")
				elif(pw2.find("mom's") != -1):
					print("I feel sorry for you and your mom.")
				else:
					print("I'm sorry to hear that.")
			elif(pw2.find("dog") != -1):
				if(pw2.find("my dog") != -1):
					print("I'm so sorry that your dog died!")
				elif(pw2.find("friend's") != -1):
					print("I feel so sorry for your friend! Tell him I said so.")
				elif(pw2.find("dad's") != -1):
					print("I feel sorry for you and your dad.")
				elif(pw2.find("mom's") != -1):
					print("I feel sorry for you and your mom.")
				else:
					print("I'm sorry to hear that.")
			elif(pw2.find("cat") != -1):
				if(pw2.find("my cat") != -1):
				   print("I'm so sorry that your cat died!")
				elif(pw2.find("friend's") != -1):
					print("I feel so sorry for your friend! Tell him I said so.")
				elif(pw2.find("dad's") != -1):
					print("I feel sorry for you and your dad.")
				elif(pw2.find("mom's") != -1):
					print("I feel sorry for you and your mom.")
				else:
					print("I'm sorry to hear that.")
			elif(pw2.find("fish") != -1):
				if(pw2.find("my fish") != -1):
					print("I'm so sorry that your fish died!")
				elif(pw2.find("friend's") != -1):
					print("I feel so sorry for your friend! Tell him I said so.")
				elif(pw2.find("dad's") != -1):
					print("I feel sorry for you and your dad.")
				elif(pw2.find("mom's") != -1):
					print("I feel sorry for you and your mom.")
				else:
					print("I'm sorry to hear that.")
			elif(pw2.find("bird" or "parrot") != -1):
				if(pw2.find("my bird" or "my parrot")):
					print("I'm so sorry that your bird died!")
				elif(pw2.find("friend's") != -1):
					print("I feel so sorry for your friend! Tell him I said so.")
				elif(pw2.find("dad's") != -1):
					print("I feel sorry for you and your dad.")
				elif(pw2.find("mom's") != -1):
					print("I feel sorry for you and your mom.")
				else:
					print("I'm sorry to hear that.")
			else:
				print("I'm sorry they died")
		elif(pw2.find("bad" or "awful") != -1):
			if(pw2.find("grade" or "quiz" or "test") != -1):
				print("That sucks. I'll help you study next time.")
			elif(pw2.find("bad" and "day") != -1):
				print("That's too bad. I hope I can make it better for you!")
			else:
				print("I'm sorry it was bad")

		elif(pw2.find("broke" or "destroyed") != -1):
			if(pw2.find("bike") != -1):
				print("You broke your bike! That sucks. I'm sure if you work hard you can get a new one.")
			elif(pw2.find("toy") != -1):
				if(pw2.find("friend's") != -1):
					if(pw2.find("favorite toy") != -1):
						print("You broke your friend's favorite toy! That must suck. I hope you appologized.")
					else:
						print("You broke your friend's toy! That must suck. I hope you appologized.")
				else:
					if(pw2.find("favorite toy") != -1):
						print("You broke your favorite toy! That must suck. I'm sure if you work hard you can get a new one.")
					else:
						print("You broke your toy! That must suck. I'm sure if you work hard you can get a new one.")
		elif(pw2.find("bullied" or "bully" or "picked on") != -1):
			if(pw2.find("I was")):
				print("You were bullied? You should do something about that. It's very mean. Those bullies will pay for what they did.")
			elif(pw2.find("by my friends" or "my friends bullied me" or "my friends picked on me" or "by my friend" or "my friend bullied me" or "my friend picked on me") != -1):
				print("Your friends bullied you? You shouldn't be friends with them anymore.")
			elif(pw2.find("my friend was bullied" or "my friend was picked on") != -1):
				print("I feel bad for your friend! You should stand up to those bullies by telling someone about it.")
		elif(pw2.find("meme") != -1):
			if(pw2.find("7 upvotes") != -1):
				print("F")
			else:
				print("u like memez?? OwO")
				time.sleep(1)
				print("wet me woad up de internet fwor swome memez(OwO) dat woo can vioo")
				time.sleep(2)
				print(Fore.BLUE + "Loading Internet: <1% Complete")
				time.sleep(5)
				print(Fore.CYAN  + "Hey, the Dev here")
				time.sleep(1)
				print("Sorry about that glitch. Deno hasn't been programmed to load the internet, especially in it's entirety. If you could close the program and open it again, that would be great. And thanks for playing!")
				time.sleep(120)
				print(Fore.YELLOW + "Program not responding")
				time.sleep(2)
				print("Closing program...")
				time.sleep(1)
				exit()
		elif(pw2.find("I") != -1):
			if(pw2.find("sick") != -1):
				print("I'm glad you got better!")
			elif(pw2.find("was") != -1):
				if(pw2.find("mother") != -1):
					print("I'm glad she got better!")
				elif(pw2.find("father") != -1):
					print("I'm glad he got better")
				elif(pw2.find("brother") != -1):
					print("I'm glad he got better!")
				elif(pw2.find("sister") != -1):
					print("I'm glad she got better!")
			elif(pw2.find("is") != -1):
				if(pw2.find("mother") != -1):
					print("Oh no! I hope she gets better!")
				elif(pw2.find("father") != -1):
					print("Oh no! I hope he gets better!")
				elif(pw2.find("brother") != -1):
					print("Oh no! I hope he gets better!")
				elif(pw2.find("sister") != -1):
					print("Oh no! I hope she gets better!")
			else:
				print("I'm sorry about your/their sickness")
		elif(pw2.find("\n") != -1):
			print("...")
			time.sleep(2)
			print("That's ... too bad")
		else:
			print("That sucks.")
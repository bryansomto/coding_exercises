def pig_latin(text):
	say = []
	words = text.split()
	for word in words:
		pigtxt = word[1:] + word[0] + 'ay'
		say.append(pigtxt)
	#return say
	return " ".join(say)
	
def self(selfprac):
			return ('\n' + selfprac.upper() + ' — ' + pig_latin(selfprac).upper() + '\n')
			
def selftry():
	selfprac = input("\n\nEnter word or sentence to convert to Pig Latin: ")
	print (self(selfprac))
	more = input("Wanna go again[Yes/No]? ")
	if more.lower() == 'yes':
		return selftry()
	exit()

welcome = "Welcome! Pig Linguist."
username = input(welcome + " Tell us your firstname: ").upper()

print("\nHere's the deal " + username[0].upper() + username[1:].lower() + ", I'm gonna teach you Pig Latin, but I'm definitely telling your buddies you were tryna talk like a Pig?\n" + "\nI guess that's a deal!\n\n" + "Okay, you see " + username[0].upper() + username[1:].lower() + ", Pig Latin is super easy, you simply put the first letter of a word at the end of the word and attach an 'ay'.\n\nExample: Your name, " + username + " in Pig Latin would be " + pig_latin(username).upper() + ". Pretty neat right?\n\nOkay, why dont you try out some words of your own or even a sentence to see how this works below...")


selftry()

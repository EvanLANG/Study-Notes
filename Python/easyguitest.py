import easygui as eg
import sys

while True:
	eg.msgbox("Welcome to the first easygui game!")
	msg = "What do you want to play?"
	title = "Game Interaction"
	choices = ["Coding", "Playing Basketball", "OOXX"]
	choice = eg.choicebox(msg, title, choices)

	eg.msgbox("Your choice is: " + str(choice), "Result")

	msg = "Do you want to play again?"
	title = "Plase, make your choice."

	if eg.ccbox(msg, title):
		pass
	else:
		sys.exit(0)
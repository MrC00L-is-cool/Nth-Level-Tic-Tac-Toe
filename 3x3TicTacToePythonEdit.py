#Thanks to Asher Olsen for help
#Set variables
coordPlayed = []
move = 0
curPlayer = "X"
levels = 2
#Class for 3x3 Grid
#+--------------+
#| A1 | A2 | A3 |
#|--------------|
#| B1 | B2 | B3 |
#|--------------|
#| C1 | C2 | C3 |
#+--------------+
class grid:
	def __init__(self, solved = "no", A1 = "?", A2 = "?", A3= "?", B1 = "?", B2 = "?", B3 = "?", C1 = "?", C2 = "?", C3 = "?"):
		self.solved = solved
		self.A1 = A1
		self.A2 = A2
		self.A3 = A3
		self.B1 = B1
		self.B2 = B2
		self.B3 = B3
		self.C1 = C1
		self.C2 = C2
		self.C3 = C3

	def checkwin(self):
		global curPlayer
		if self.A1 == self.A2 == self.A3 != "?":
			self.solved = curPlayer
		elif self.B1 == self.B2 == self.B3 != "?":
			self.solved = curPlayer
		elif self.C1 == self.C2 == self.C3 != "?":
			self.solved = curPlayer
		elif self.A1 == self.B1 == self.C1 != "?":
			self.solved = curPlayer
		elif self.A2 == self.B2 == self.C2 != "?":
			self.solved = curPlayer
		elif self.A3 == self.B3 == self.C3 != "?":
			self.solved = curPlayer
		elif self.A1 == self.B2 == self.C3 != "?":
			self.solved = curPlayer
		elif self.A3 == self.B2 == self.C1 != "?":
			self.solved = curPlayer
		elif all(s in ("X", "O") for s in [self.A1, self.A2, self.A3, self.B1, self.B2, self.B3, self.C1, self.C2, self.C3]):
			self.solved = "smate"
		else:
			 self.solved = "no"

#End of Program
#Sets terminal back to usable format
def endProg():
	curses.nocbreak()
	screen.keypad(0)
	curses.echo()
	curses.curs_set(1)
	curses.endwin()
	print("Finished")
	exit


def possibleMove(*coords):
	if move == 1:
		coordPlayed.insert(len.coordPlayed - 1, A1)
	elif move == 2:
		coordPlayed.insert(len.coordPlayed - 1, A2)
	elif move == 3:
		coordPlayed.insert(len.coordPlayed - 1, A3)
	elif move == 4:
		coordPlayed.insert(len.coordPlayed - 1, B1)
	elif move == 5:
		coordPlayed.insert(len.coordPlayed - 1, B2)
	elif move == 6:
		coordPlayed.insert(len.coordPlayed - 1, B3)
	elif move == 7:
		coordPlayed.insert(len.coordPlayed - 1, C1)
	elif move == 8:
		coordPlayed.insert(len.coordPlayed - 1, C2)
	elif move == 9:
		coordPlayed.insert(len.coordPlayed - 1, C3)
	else:
		pass

main = grid()

#To check the os
import os
print(os.name)

#For Color
#Attemps to check for curses
try:
	import curses
except:
	if os.name=='nt':
		print("You have been detected running windows, please run this command first")
		print("python -m pip install windows-curses")
		exit
	else:
		print("Something went wrong! Please try to install the Curses module")
		exit
screen = curses.initscr()
curses.start_color()
if curses.has_colors():
	#Basic
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	#1st Player
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
	#2nd Player
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
	#Selected
	curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
else:
	pass

#Test correct size
num_rows, num_cols = screen.getmaxyx()
if num_rows < 9:
	print("Please increase your terminal size")
	exit
if num_cols < 15:
	print("Please increase your terminal size")
	exit


#Set up GUI
win = curses.newwin(0, 0, curses.LINES - 1, curses.COLS - 1)
curses.curs_set(0)
def drawScreen():
	global main, coordPlayed, move, curPlayer, levels
	screen.addstr(0, 0, "╔═══════╦═══════╦═══════╗", curses.color_pair(1))
	screen.addstr(1, 0, "║┏━┳━┳━┓║┏━┳━┳━┓║┏━┳━┳━┓║", curses.color_pair(1))
	screen.addstr(2, 0, "║┃"displayNested(parseCoord(False).A1.A1)"┃"displayNested(parseCoord(False).A1.A2)"┃"displayNested(parseCoord(False).A1.A3)"┃║┃"displayNested(parseCoord(False).A2.A1)"┃"displayNested(parseCoord(False).A2.A2)"┃"displayNested(parseCoord(False).A2.A3)"┃║┃"displayNested(parseCoord(False).A3.A1)"┃"displayNested(parseCoord(False).A3.A2)"┃"displayNested(parseCoord(False).A3.A3)"┃║", curses.color_pair(1))
	screen.addstr(3, 0, "║┣━╋━╋━┫║┣━╋━╋━┫║┣━╋━╋━┫║", curses.color_pair(1))
	screen.addstr(4, 0, "║┃"displayNested(parseCoord(False).A1.B1)"┃"displayNested(parseCoord(False).A1.B2)"┃"displayNested(parseCoord(False).A1.B3)"┃║┃"displayNested(parseCoord(False).A2.B1)"┃"displayNested(parseCoord(False).A2.B2)"┃"displayNested(parseCoord(False).A2.B3)"┃║┃"displayNested(parseCoord(False).A3.B1)"┃"displayNested(parseCoord(False).A3.B2)"┃"displayNested(parseCoord(False).A3.B3)"┃║", curses.color_pair(1))
	screen.addstr(5, 0, "║┣━╋━╋━┫║┣━╋━╋━┫║┣━╋━╋━┫║", curses.color_pair(1))
	screen.addstr(6, 0, "║┃"displayNested(main.A1.C1)"┃"displayNested(main.A1.C2)"┃"displayNested(main.A1.C3)"┃║┃"displayNested(main.A2.C1)"┃"displayNested(main.A2.C2)"┃"displayNested(main.A2.C3)"┃║┃"displayNested(main.A3.C1)"┃"displayNested(main.A3.C2)"┃"displayNested(main.A3.C3)"┃║", curses.color_pair(1))
	screen.addstr(7, 0, "║┗━┻━┻━┛║┗━┻━┻━┛║┗━┻━┻━┛║", curses.color_pair(1))
	screen.addstr(8, 0, "╠═══════╬═══════╬═══════╣", curses.color_pair(1))
	screen.addstr(9, 0, "║┏━┳━┳━┓║┏━┳━┳━┓║┏━┳━┳━┓║", curses.color_pair(1))
	screen.addstr(10, 0, "║┃"displayNested(main.B1.A1)"┃"displayNested(main.B1.A2)"┃"displayNested(main.B1.A3)"┃║┃"displayNested(main.B2.A1)"┃"displayNested(main.B2.A2)"┃"displayNested(main.B2.A3)"┃║┃"displayNested(main.B3.A1)"┃"displayNested(main.B3.A2)"┃"displayNested(main.B3.A3)"┃║", curses.color_pair(1))
	screen.addstr(11, 0, "║┣━╋━╋━┫║┣━╋━╋━┫║┣━╋━╋━┫║", curses.color_pair(1))
	screen.addstr(12, 0, "║┃"displayNested(main.B1.B1)"┃"displayNested(main.B1.B2)"┃"displayNested(main.B1.B3)"┃║┃"displayNested(main.B2.B1)"┃"displayNested(main.B2.B2)"┃"displayNested(main.B2.B3)"┃║┃"displayNested(main.B3.B1)"┃"displayNested(main.B3.B2)"┃"displayNested(main.B3.B3)"┃║", curses.color_pair(1))
	screen.addstr(13, 0, "║┣━╋━╋━┫║┣━╋━╋━┫║┣━╋━╋━┫║", curses.color_pair(1))
	screen.addstr(14, 0, "║┃"displayNested(main.B1.C1)"┃"displayNested(main.B1.C2)"┃"displayNested(main.B1.C3)"┃║┃"displayNested(main.B2.C1)"┃"displayNested(main.B2.C2)"┃"displayNested(main.B2.C3)"┃║┃"displayNested(main.B3.C1)"┃"displayNested(main.B3.C2)"┃"displayNested(main.B3.C3)"┃║", curses.color_pair(1))
	screen.addstr(15, 0, "║┗━┻━┻━┛║┗━┻━┻━┛║┗━┻━┻━┛║", curses.color_pair(1))
	screen.addstr(16, 0, "╠═══════╬═══════╬═══════╣", curses.color_pair(1))
	screen.addstr(17, 0, "║┏━┳━┳━┓║┏━┳━┳━┓║┏━┳━┳━┓║", curses.color_pair(1))
	screen.addstr(18, 0, "║┃"displayNested(main.C1.A1)"┃"displayNested(main.C1.A2)"┃"displayNested(main.C1.A3)"┃║┃"displayNested(main.C2.A1)"┃"displayNested(main.C2.A2)"┃"displayNested(main.C2.A3)"┃║┃"displayNested(main.C3.A1)"┃"displayNested(main.C3.A2)"┃"displayNested(main.C3.A3)"┃║", curses.color_pair(1))
	screen.addstr(19, 0, "║┣━╋━╋━┫║┣━╋━╋━┫║┣━╋━╋━┫║", curses.color_pair(1))
	screen.addstr(20, 0, "║┃"displayNested(main.C1.B1)"┃"displayNested(main.C1.B2)"┃"displayNested(main.C1.B3)"┃║┃"displayNested(main.C2.B1)"┃"displayNested(main.C2.B2)"┃"displayNested(main.C2.B3)"┃║┃"displayNested(main.C3.B1)"┃"displayNested(main.C3.B2)"┃"displayNested(main.C3.B3)"┃║", curses.color_pair(1))
	screen.addstr(21, 0, "║┣━╋━╋━┫║┣━╋━╋━┫║┣━╋━╋━┫║", curses.color_pair(1))
	screen.addstr(22, 0, "║┃"displayNested(main.C1.C1)"┃"displayNested(main.C1.C2)"┃"displayNested(main.C1.C3)"┃║┃"displayNested(main.C2.C1)"┃"displayNested(main.C2.C2)"┃"displayNested(main.C2.C3)"┃║┃"displayNested(main.C3.C1)"┃"displayNested(main.C3.C2)"┃"displayNested(main.C3.C3)"┃║", curses.color_pair(1))
	screen.addstr(23, 0, "║┗━┻━┻━┛║┗━┻━┻━┛║┗━┻━┻━┛║", curses.color_pair(1))
	screen.addstr(24, 0, "╚═══════╩═══════╩═══════╝", curses.color_pair(1))
	screen.addstr(25, 0, "Please enter the place you want to go: ", curses.color_pair(1))
	screen.addstr(26, 0, "It is " + curPlayer + "'s turn", curses.color_pair(1))
	#Apply screen changes
	screen.refresh()
	
def winScreen(winner):
	global main, coordPlayed, move, curPlayer, levels
	screen.erase()
	screen.addstr(0, 0, "             ", curses.color_pair(1))
	screen.addstr(1, 0, "Congradulations   ", curses.color_pair(1))
	screen.addstr(2, 0, "       Player         ", curses.color_pair(1))
	screen.addstr(3, 0, winner + "!", curses.color_pair(1))
	#screen.addstr(4, 0, "┣━━━╋━━━╋━━━┫", curses.color_pair(1))
	#screen.addstr(5, 0, "┃  ?  ┃  ?  ┃  ?  ┃", curses.color_pair(1))
	#screen.addstr(6, 0, "┗━━━┻━━━┻━━━┛", curses.color_pair(1))
	screen.refresh()
	curses.napms(6000)
	endProg()

def resetVars():
	global main, coordPlayed, move, curPlayer, levels
	main = grid()
	coordPlayed = ["roof"]
	move = 0
	curPlayer = "X"
	levels = 1

def parseCoord(all):
	global main, coordPlayed, move, curPlayer, levels
	board = main
	if all == False:
		for i in coordPlayed[:-1]:
			if i == 1:
				board = board.A1
			elif i == 2:
				board = board.A2
			elif i == 3:
				board = board.A3
			elif i == 4:
				board = board.B1
			elif i == 5:
				board = board.B2
			elif i == 6:
				board = board.B3
			elif i == 7:
				board = board.C1
			elif i == 8:
				board = board.C2
			elif i == 9:
				board = board.C3
	else:
		for i in coordPlayed:
			if i == 1:
				board = board.A1
			elif i == 2:
				board = board.A2
			elif i == 3:
				board = board.A3
			elif i == 4:
				board = board.B1
			elif i == 5:
				board = board.B2
			elif i == 6:
				board = board.B3
			elif i == 7:
				board = board.C1
			elif i == 8:
				board = board.C2
			elif i == 9:
				board = board.C3
	return board

def displayNested(coord):
	if isinstance(coord, grid):
		if coord.solved == "X":
			return "~"
		elif coord.solved == "O":
			return "O"
		elif coord.solved == "smate"
			return "!"
		elif coord.solved == "no"
			return "~"
	else:
		return coord

def playerTurn():
	global main, coordPlayed, move, curPlayer, levels
	drawScreen()
	screen.refresh()
	square = screen.getkey(8, 40)
	if square == "1":
		if isinstance(parseCoord(True).A1, grid):
			if parseCoord(True).A1.solved != "no":
				playerTurn()
			else:
				coordPlayed.append(1)
				playerTurn()
		elif parseCoord(True).A1 == "?":
			parseCoord(True).A1 = curPlayer
		else:
			playerTurn()
	elif square == "2":
		if isinstance(parseCoord(True).A2, grid):
			if parseCoord(True).A2.solved != "no":
				playerTurn()
			else:
				coordPlayed.append(2)
				playerTurn()
		elif parseCoord(True).A2 == "?":
			parseCoord(True).A2 = curPlayer
		else:
			playerTurn()
	elif square == "3":
		if isinstance(parseCoord(True).A3, grid):
			if parseCoord(True).A3.solved != "no":
				playerTurn()
			else:
				coordPlayed.append(3)
				playerTurn()
		elif parseCoord(True).A3 == "?":
			parseCoord(True).A3 = curPlayer
		else:
			playerTurn()
	elif square == "4":
		if isinstance(parseCoord(True).B1, grid):
			if parseCoord(True).B1.solved != "no":
				playerTurn()
			else:
				coordPlayed.append(4)
				playerTurn()
		elif parseCoord(True).B1 == "?":
			parseCoord(True).B1 = curPlayer
		else:
			playerTurn()
	elif square == "5":
		if isinstance(parseCoord(True).B2, grid):
			if parseCoord(True).B2.solved != "no":
				playerTurn()
			else:
				coordPlayed.append(5)
				playerTurn()
		elif parseCoord(True).B2 == "?":
			parseCoord(True).B2 = curPlayer
		else:
			playerTurn()
	elif square == "6":
		if isinstance(parseCoord(True).B3, grid):
			if parseCoord(True).B3.solved != "no":
				playerTurn()
			else:
				coordPlayed.append(6)
				playerTurn()
		elif parseCoord(True).B3 == "?":
			parseCoord(True).B3 = curPlayer
		else:
			playerTurn()
	elif square == "7":
		if isinstance(parseCoord(True).C1, grid):
			if parseCoord(True).C1.solved != "no":
				playerTurn()
			else:
				coordPlayed.append(7)
				playerTurn()
		elif parseCoord(True).C1 == "?":
			parseCoord(True).C1 = curPlayer
		else:
			playerTurn()
	elif square == "8":
		if isinstance(parseCoord(True).C2, grid):
			if parseCoord(True).C2.solved != "no":
				playerTurn()
			else:
				coordPlayed.append(8)
				playerTurn()
		elif parseCoord(True).C2 == "?":
			parseCoord(True).C2 = curPlayer
		else:
			playerTurn()
	elif square == "9":
		if isinstance(parseCoord(True).C3, grid):
			if parseCoord(True).C3.solved != "no":
				playerTurn()
			else:
				coordPlayed.append(9)
				playerTurn()
		elif parseCoord(True).C3 == "?":
			parseCoord(True).C3 = curPlayer
		else:
			playerTurn()
	parseCoord(True).checkwin()
	if parseCoord(True).solved != "no":
		coordPlayed = coordPlayed[:-1]
		
	if main.solved == "X":
		winScreen("X")
	elif main.solved == "O":
		winScreen("O")
	elif main.solved == "smate":
		winScreen("None")
	else:
		if curPlayer == "X":
			curPlayer = "O"
			playerTurn()
		else:
			curPlayer = "X"
			playerTurn()

#Play game
try:
	playerTurn()
finally:
	endProg()

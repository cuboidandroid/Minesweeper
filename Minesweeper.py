import random
import os

def GetValidNeighbours(a, b): #this function will return list of neighbours of certain a,b field
	Neighbours=[]
	if a+1<=rows-1 and b+1<=columns-1:
		Neighbours.append((a+1, b+1))
	if a-1>=0 and b-1>=0:
		Neighbours.append((a-1, b-1))
	if a-1>=0 and b+1<=columns-1:
		Neighbours.append((a-1, b+1))
	if a+1<=rows-1 and b-1>=0:
		Neighbours.append((a+1, b-1))
	if b+1<=columns-1:
		Neighbours.append((a, b+1))
	if b-1>=0:
		Neighbours.append((a, b-1))
	if a+1<=rows-1:
		Neighbours.append((a+1, b))
	if a-1>=0:
		Neighbours.append((a-1, b))
	return Neighbours
         		
def zeros(a, b, Neighbours): #if zero is revealed, reveal all the adjacent fields
	for i in Neighbours:
		playergrid[i[0]][i[1]] = grid[i[0]][i[1]]

def tagging(a, b): # every square should have value, that is a number of adjacent bombs
	if (grid[a][b]>8):
		nbgh = GetValidNeighbours(a, b)
		for i in nbgh:
			grid[i[0]][i[1]] += 1

def cls(): #refresh after every action
    os.system('cls' if os.name=='nt' else 'clear')
    
def showplayergrid(rows, columns): # way to print grid in console
	for i in range(rows):
		for j in range(columns):
			print (playergrid[i][j], end='') #or: print (grid[i][j], end=''), or: print (checkedzero[i][j], end='') ... (copy and rename)
		print ('')

# MAKING GRID
rows = 20 #16
columns = 40 #30
bombs = 99 #99
grid = [[0 for x in range(columns)] for y in range(rows)]

# RANDOMLY GENERATING BOMBS
m=0
while m < bombs:
	x1 = random.randint(0,rows-1)
	y1 = random.randint(0,columns-1)
	if grid[x1][y1] < 9:
		grid[x1][y1] = 9
		m = m+1
	else:
		pass	
			
# TAGGING BOMBS' NEIGHBOURHOOD
for a in range(rows):
	for b in range(columns):
		tagging(a, b)
		
# CORRECTING BOMBS' VALUES			
for a in range(rows):
	for b in range(columns):
		if grid[a][b]>8:
			grid[a][b]=9

#MAKING PLAYERGRID
playergrid = [['.' for x in range (columns)] for y in range (rows)]
checkedzero = [[0 for x in range (columns)] for y in range (rows)]

# PLAYING reveal, tag bomb or untag bomb
while True:	
	cls()
	showplayergrid(rows, columns)
	action = input('>>> ')
	action = action.split(' ')
	try:
		action[0]=int(action[0])
		action[1]=int(action[1])
		if len(action)==2 and 0<=action[0]<rows and 0<=action[1]<columns: #if point to reveal belongs to matrix, and action is correctly stated
			if playergrid[action[0]][action[1]] == '.' or 0<playergrid[action[0]][action[1]]<9: #if its unrevealed and not zero or bomb
				playergrid[action[0]][action[1]] = grid[action[0]][action[1]] #assign stuff
			if grid[action[0]][action[1]] == 0: #if we have zero
				ToVisit = [] #make a stack
				ToVisit.append((action[0], action[1])) #add me to stack ;)
				while not ToVisit == []:	#while this stack is not empty start a loop (its not, because line 84)
					CurrentlyChecked = ToVisit.pop() #take last object in stack
					neighbours = GetValidNeighbours(CurrentlyChecked[0], CurrentlyChecked[1]) #take neighbours
					zeros(CurrentlyChecked[0], CurrentlyChecked[1], neighbours) #make zeros
					checkedzero[CurrentlyChecked[0]][CurrentlyChecked[1]] = 1	#remeber that this zero has been checked
					for i in neighbours:
						if grid[i[0]][i[1]] == 0 and checkedzero[i[0]][i[1]] == 0: #if neighbour is 0 add him to stack							
							ToVisit.append(i)
			else:
				pass			
		if len(action)==3:
			if action[2]=='t' and playergrid[action[0]][action[1]] == '.':
				playergrid[action[0]][action[1]] = 'B'
				cls()
				showplayergrid(rows, columns)
			
			
			if action[2]=='u' and playergrid[action[0]][action[1]] == 'B':
				playergrid[action[0]][action[1]] = '.'
				cls()
				showplayergrid(rows, columns)
	except (IndexError, ValueError, TypeError):
		pass
	

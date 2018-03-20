#Draw grid 
# Allow player to move
# Have door for player to move to move 
# Have monster to eat player wen he gets to his room
# Player cannot go past grid walls 
# Tell user if 1. He gets to the door and wins or 
# 2 . He gets to the monster and is eaten

import random
import os

def clear():
	os.system("clear")

grid =[]
for y in range(5):
	for x in range(5):
		grid.append((x,y))


def draw_grid(): # should take args >player pstn
	print(" _"*5)
	for pair in grid:
		if pair[0] != 4:
			if pair == player:
				print("|X", end ='')
			else:
				print("|_", end ='')
		if pair[0]==4:
			if pair ==player:
				print("|X|")
			else:
				print("|_|")

player, monster, door = random.sample(grid, 3)

moves = ["l","r","d","u"]
print ('you are in room {}'.format(player))
print('{} monster room \n{} door'.format(monster, door))
input("Press Enter to play")

while True:
	draw_grid()
	x,y = player
	if x== 0:
		moves.remove("l")
	if x==4:
		moves.remove("r")
	if y== 0:
		moves.remove("u")
	if y== 4:
		moves.remove("d")
	
	print("Available move are : {}".format(" ; ".join(moves)))
	move = input(":>>> ")
	clear()
	if move in moves and move == "l":
		if x -1 < 0:
			player = (x,y)
		else:
			player =(x-1, y)
			
		print ('you are in "L" room {}'.format(player))
		
	elif move in moves and move =="r":
		if x+1 > 4:
			player = (x, y)
			
		else:
			player = (x+1,y)
		
		print ('you are in"R"  room {}'.format(player))

	elif move in moves and move =="d":
		if y+1 > 4:
			player = (x,y)
		else:
			player = (x, y+1)
		print ('you are in "D" room {}'.format(player))
		
	elif move in moves and move =="u":
		if y-1 < 0:
			player (x,y)
		else:
			player = (x, y-1)
		print ('you are in "U"  room {}'.format(player))
		
	elif move in ["l","r","d","u"] and move not in moves:
		print("WALLS ARE HARD \n you just ran into a wall")
	else:
		print("invalid move!!")
		
	moves =["l","r","d","u"]

	if player == monster:
		print("Oh No! the monster got you.......,Better luck next time")
		break
		
	elif player ==door:
		print ("Hurray you have escaped the Prison !!")
		break
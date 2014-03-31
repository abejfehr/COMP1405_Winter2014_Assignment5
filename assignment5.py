#=============================================#
# Assignment 5: Solving a maze with recursion #
# File:   assignment5.py                      #
# Author: Abe Fehr                            #
# Date:   March 25th, 2014                    #
#=============================================#

###
# Function: loadMaze
# Purpose:  Loads a maze from a file parses it
# Input:    filename - the name of the maze file
# Returns:  A 2D list representing a maze
###
def loadMaze(filename):
  try:
    file = open(filename)
    maze = []
    for line in file.readlines():
      line = line.strip()
      maze.append(list(line))
    file.close()
    return maze
  except IOError:
    print "uh oh, something happened!"
    return None
    
    
    
###
# Function: printMaze
# Purpose:  Takes in a 2D list that represents a
#           maze and prints it to the screen
# Input:    maze - the maze to print
###
def printMaze(maze):
  if(maze != None):
    for line in maze:
      print ''.join(line)



###
# Function: findStart
# Purpose:  Finds the starting point S in a maze
# Input:    maze - the maze to get the starting point in
# Returns:  A tuple with its coordinates
###
def findStart(maze):
  for y in range(len(maze)):
    for x in range(len(maze[y])):
      if(maze[y][x] == "S"):
        return (x, y)
  return (-1, -1)



###
# Function: solve
# Purpose:  Solves the maze
# Input:    maze - the maze to be solving
#           y - the y coordinate to start from
#           x - the x coordinate to start from
# Returns:  whether the maze is solvable or not
###
def solve(maze, y, x):
  if(maze[y][x] == "E"):
    return True
  elif(maze[y][x] == "#"):
    return False

  elif(maze[y][x] == " " or maze[y][x] == "S"):
    maze[y][x] = "^" 
    if(solve(maze, y-1, x)):
      return True

    maze[y][x] = ">"
    if(solve(maze, y, x+1)):
      return True

    maze[y][x] = 'v'
    if(solve(maze, y+1, x)):
      return True

    maze[y][x] = "<"
    if(solve(maze, y, x-1)):
      return True

    maze[y][x] = " "
    return False
  return False



#load the maze
myMaze = loadMaze("maze2.maze")

#print it on the screen
print "Before solving:"
printMaze(myMaze)

#find the start coordinates
start = findStart(myMaze)

#makes sure the maze had a start
if(start != (-1, -1)):
  #solve it!
  if(solve(myMaze, start[1], start[0])):
    #put the "S" back in the maze since we changed it
    myMaze[start[1]][start[0]] = "S"
    #print it after it's been solved
    print "After solving:"
    printMaze(myMaze)
  else:
    print "There is no solution"
else:
  print "The maze has no starting position"

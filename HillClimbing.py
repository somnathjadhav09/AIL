import random
from array import array


board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
neighbour = [[0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
queens = [1,0,1,0,0,0,0,0]


def collision_count(column,row):
    coll = 0
   
    for j in range(8):
        if j == row:
            continue
        if board[column][j] == 1 :
            coll += 1
    
    while(column < 7 and row < 7):
        row += 1
        column +=1
        if board[column][row] == 1:
            coll += 1
  
    while(column > 0 and row > 0):
        row -= 1
        column -=1
        if board[column][row] == 1:
            coll += 1
    
    while(column > 0 and row < 7):
        row += 1
        column -=1
        if board[column][row] == 1:
            coll += 1
 
    while(column < 7 and row > 0):
        row -= 1
        column +=1
        if board[column][row] == 1:
            coll += 1
                     
    return coll     

def totalcoll():
    totcoll = 0
    for i in range(8):
       totcoll += collision_count(i,queens[i])
    return totcoll
            
while True:
 
 for i in range(8):
     queens[i] = random.randrange(0,8)
     board[i][queens[i]] = 1



 totalcollision =  totalcoll()
    
 while True:

  for i in range(8):
     
     oldqueen = queens[i]

     
     for j in range(8):
       
         queens[i] = j
       
         neighbour[i][j] = totalcoll()
     
     queens[i] = oldqueen

 
  min = neighbour[0][0]
  minqueencol = 0
  minqueenrow = 0
  for i in range(8):
      for j in range(8):
          if(neighbour[i][j]<min):
              min = neighbour[i][j]
              minqueenrow = j
              minqueencol = i

  if min<totalcollision:
     totalcollision = min
     queens[minqueencol] = minqueenrow
    

  else:
      break

 if totalcollision == 0:
        break

print("a")

for i in range(8):
    for j in range(8):
        print(board[i][j])


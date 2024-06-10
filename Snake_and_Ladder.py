import random

def dice1():
    player1 = random.randint(1,6)
    return( player1 )

def dice2():
    player2 = random.randint(1,6)
    return( player2 )

def game(pos,x):
    ladder_A = [2,8,20,32,41,74,82,85]
    ladder_B = [23,34,77,68,79,88,100,95]
    if pos in ladder_A:
        ladder_C = ladder_B[ladder_A.index(pos)]
        print( f'    PLAYER {x} climbes the LADDER and reaches {ladder_C} ' )
        return( ladder_C )
    
    snake_A = [29,38,47,53,62,86,92,97]
    snake_B = [9,15,5,33,37,54,70,25]
    if pos in snake_A:
        snake_C = snake_B[snake_A.index(pos)]
        print( f'    SNAKE attacks PLAYER {x} and reaches {snake_C} ' )
        return( snake_C )
    else:
        return pos

    

pos1 = 0
pos2 = 0
for k in range(1,101):
    point1 = dice1()
    print( 'player 1 dice : ', point1 )
    pos1 = pos1+point1

    point2 = dice2()
    print( 'player 2 dice : ', point2 )
    pos2 = pos2+point2

    print( f'PLAYER 1 POSITION  : {pos1}' )
    pos1 = game(pos1,1)
    print( f'PLAYER 2 POSITION : {pos2}' )
    pos2 = game(pos2,2)
    print()

    if pos1 >= 100:
        print( '-------PLAYER 1 IS THE WINNER-------' )
        print()
        break
    if pos2 >= 100:
        print( '-------PLAYER 2 IS THE WINNER-------' )
        print()
        break
    else:
        pass


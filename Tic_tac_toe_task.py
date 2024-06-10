def game(xmove , omove , totmoves):
        for i in range(1,6):
            if i%2 != 0:
                for j in range(1,6):
                    if j%2 == 0:
                        print('|' , end = '')
                    else:
                        for x in xmove:
                            if (i,j) == x:
                                print('  x  ' , end= '')
                            else:
                                pass
                        for o in omove:
                            if (i,j) == o:
                                print('  O  ' , end= '')
                            else:
                                pass
                        for y in totmoves:
                            if (i,j) == y:
                                print('     ' , end= '')
                            else:
                                pass
                print()

            else:
                for j in range(1,6):
                    if j%2 == 0:
                        print('|' , end = '')
                    else:
                        print('-----' , end = '')
                print()


def position(xmove,omove):
    xmoves = []
    omoves = []
    pos1 = (1,2,3,4,5,6,7,8,9)
    pos2 = ((1,1),(1,3),(1,5),(3,1),(3,3),(3,5),(5,1),(5,3),(5,5))
    totmoves = [(1,1),(1,3),(1,5),(3,1),(3,3),(3,5),(5,1),(5,3),(5,5)]

    for xmov in xmove:
        for i in range(len(pos1)):
            for j in range(len(pos2)):
                if i == j and pos1[i] == xmov:
                    xmoves.append(pos2[j])
                    totmoves.remove(pos2[j])
                else:
                    pass

    for omov in omove:
        for i in range(len(pos1)):
            for j in range(len(pos2)):
                if i == j and pos1[i] == omov:
                    omoves.append(pos2[j])
                    totmoves.remove(pos2[j])
                else:
                    pass

    game(xmoves , omoves , totmoves)
    print()


def score(j):
    score_pos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for r in score_pos:
        sum1 = 0
        sum2 = 0
        for x in r:
            if x in xmove:
                sum1 = sum1+1
            elif x in omove:
                sum2 = sum2+1

        if j != 5:
            if sum1 == 3:
                print('---------PLAYER 1 IS THE WINNER---------')
                print()
                exit()  
            elif sum2 == 3:
                print('---------PLAYER 2 IS THE WINNER---------') 
                print()
                exit()

        else:
            if sum1 == 3:
                print('---------PLAYER 1 IS THE WINNER---------')
                print()
                exit()  
            elif sum2 == 3:
                print('---------PLAYER 2 IS THE WINNER---------') 
                print()
                exit()
            elif sum1 != 3 and sum2 != 3:
                print('---------IT\'S A DRAW---------')
                print()
                exit()


print(' GAME BEGINS ')
print()
totmoves = [(1,1),(1,3),(1,5),(3,1),(3,3),(3,5),(5,1),(5,3),(5,5)]
game ([],[],totmoves)
print()
pos=[1,2,3,4,5,6,7,8,9]
xmove = []
omove = []

for j in range(1,6):
    if j != 5:
        player1 = (int(input('PLAYER 1 \'X\' enter your position (1 to 9): ')))
        player2 = (int(input('PLAYER 2 \'O\' enter your position (1 to 9): ')))

        while player1 not in pos:
            player1 = (int(input('PLAYER 1 \'X\' enter other position  (1 to 9): ')))
        pos.remove(player1)

        while player2 not in pos:
            player2 = (int(input('PLAYER 2 \'O\' enter other position (1 to 9): ')))
        pos.remove( player2 )
        xmove.append( player1 )
        omove.append( player2 )
        print()
        score(j)

    else:
        player1 = (int(input('PLAYER 1 \'X\' enter your position (1 to 9): ')))
        if player1 not in pos:
            player1 = (int(input('PLAYER 1 \'X\' enter other position  (1 to 9): ')))
        pos.remove(player1)
        xmove.append(player1)
        print()
        score(j)
    
    print()
    position(xmove,omove)
    

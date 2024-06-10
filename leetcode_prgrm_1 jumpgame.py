#...................55. JUMP GAME

class Jump:
    def __init__(self,numbers):
        self.numbers = numbers
    def num(self):
        indx = 0
        for i in range ( 0 , len (self.numbers) ):                           
            self.bound = self.numbers[ indx ]                        
            indx = indx + self.bound
            if indx <= ( len(self.numbers) - 1 ): 
                last_index = indx
            else:
                break
        print( last_index == (len(self.numbers) - 1) )

r1=Jump([2,3,1,1,4])
r1.num()


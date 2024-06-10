#........................139. Word Break (leetcode)

class Split:
    def __init__(self,word,dict):
        self.word = word
        self.dict = dict

    def check(self):
        segmented_str = ''
        for i in self.dict:
            j = 1
            while j >= 1 :
                if i in self.word:
                    segmented_str = segmented_str + ' ' + i
                    new_wrd = self.word.replace( f'{i}' , '' , 1 ) 
                    self.word = new_wrd
                else:
                    break

        print (f'Possible segmented string : {segmented_str}')
        print (new_wrd == '')


s1 = Split('leetcode',['leet','code'])
s1.check()




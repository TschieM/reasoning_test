class Answers():
    def __init__(self):
        self.candidates = ['A', 'B', 'C', 'D']
        self.answer = []
        self.cntA = 0
        self.cntB = 0
        self.cntC = 0
        self.cntD = 0
        self.minCnt = 0
        self.maxCnt = 0

    def fill(self, number):
        if number == 11:
            return
        for ans in self.candidates:
            self.answer = self.answer[:number-1]
            self.answer.extend(ans)
            if number == 10:
                self.cnt_ans()
                if (self.check_ans()):
                    print(self.answer)
            self.fill(number+1)

    def cnt_ans(self):
        self.cntA = 0
        self.cntB = 0
        self.cntC = 0
        self.cntD = 0
        for ans in self.answer:
            if ans == 'A':
                self.cntA += 1
            elif ans == 'B':
                self.cntB += 1
            elif ans == 'C':
                self.cntC += 1
            else:
                self.cntD += 1
        self.minCnt = min(self.cntA, min(self.cntB, min(self.cntC, self.cntD)))
        self.maxCnt = max(self.cntA, max(self.cntB, max(self.cntC, self.cntD)))
    
    def check_ans(self):
        if (self.check2() == False): return False
        if (self.check3() == False): return False
        if (self.check4() == False): return False
        if (self.check5() == False): return False
        if (self.check6() == False): return False
        if (self.check7() == False): return False
        if (self.check8() == False): return False
        if (self.check9() == False): return False
        if (self.check10() == False): return False
        else: return True
    
    def check2(self):
        if self.answer[1]=='A': 
            return self.answer[4]=='C'
        elif self.answer[1]=='B': 
            return self.answer[4]=='D'
        elif self.answer[1]=='C': 
            return self.answer[4]=='A'
        else:
            return self.answer[4]=='B'
    
    def check3(self):
        if self.answer[2] == 'A':
            return (self.answer[5]!=self.answer[2] and self.answer[1]!=self.answer[2])
        elif self.answer[2] == 'B':
            return (self.answer[2]!=self.answer[5] and self.answer[1]!=self.answer[5])
        elif self.answer[2] == 'C':
            return (self.answer[2]!=self.answer[1] and self.answer[1]!=self.answer[5])
        else:
            return (self.answer[2]!=self.answer[3] and self.answer[3]!=self.answer[5])

    def check4(self):
        if self.answer[3]=='A':
            return self.answer[0] == self.answer[4]
        elif self.answer[3]=='B':
            return self.answer[1] == self.answer[6]
        elif self.answer[3]=='C':
            return self.answer[0] == self.answer[8]
        else:
            return self.answer[5] == self.answer[9]

    def check5(self):
        if self.answer[4]=='A':
            return self.answer[7] == 'A'
        elif self.answer[4]=='B':
            return self.answer[3] == 'B'
        elif self.answer[4]=='C':
            return self.answer[8] == 'C'
        else:
            return self.answer[6] == 'D'

    def check6(self):
        ans8 = self.answer[7]
        if self.answer[5]=='A':
            return (self.answer[1]==self.answer[3] and self.answer[3]==ans8)
        elif self.answer[5]=='B':
            return (self.answer[0]==self.answer[5] and self.answer[5]==ans8)
        elif self.answer[5]=='C':
            return (self.answer[2]==self.answer[9] and self.answer[9]==ans8)
        else:
            return (self.answer[4]==self.answer[8] and self.answer[8]==ans8)

    def check7(self):
        if self.answer[6] == 'A':
            return self.cntA == self.minCnt
        elif self.answer[6] == 'B':
            return self.cntB == self.minCnt
        elif self.answer[6] == 'C':
            return self.cntC == self.minCnt
        else: 
            return self.cntD == self.minCnt

    def check8(self):
        if self.answer[7] == 'A':
            return (abs(ord(self.answer[6]) - ord(self.answer[0]))!=1)
        elif self.answer[7] == 'B':
            return (abs(ord(self.answer[4]) - ord(self.answer[0]))!=1)
        elif self.answer[7] == 'C':
            return (abs(ord(self.answer[1]) - ord(self.answer[0]))!=1)
        else:
            return (abs(ord(self.answer[9]) - ord(self.answer[0]))!=1)
    
    def check9(self):
        if self.answer[8] == 'A':
            return ((self.answer[0]==self.answer[5])^(self.answer[5]==self.answer[4]))
        elif self.answer[8] == 'B':
            return ((self.answer[0]==self.answer[5])^(self.answer[9]==self.answer[4]))
        elif self.answer[8] == 'C':
            return ((self.answer[0]==self.answer[5])^(self.answer[1]==self.answer[4]))
        else:
            return ((self.answer[0]==self.answer[5])^(self.answer[8]==self.answer[4]))
    
    def check10(self):
        diff = self.maxCnt - self.minCnt
        if self.answer[9] == 'A':
            return diff == 3
        elif self.answer[9] == 'B':
            return diff == 2
        elif self.answer[9] == 'C':
            return diff == 4
        else:
            return diff == 1

if __name__ == '__main__':
    test = Answers();
    test.fill(1)
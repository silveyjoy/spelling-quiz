import random

spelling = {1:['acceptable','acceptible'], \
2:['accidentally','accidentaly'], \
3:['accommodate','accomodate'], \
4:['acquire','aquire',], \
5:['acquit','aquit'], \
6:['a lot','alot'], \
7:['amateur','amature']}

def playRound():
    def randomSequence(length):
        """
        Takes an int as argument for length of a range of values. 
        Returns a tuple of four randomly assigned and unique ints 
        from within the range.
        """
        def randomNum(length):
            a = random.uniform(1, length+1)
            return int(a)
        
        a = randomNum(length)
        b = randomNum(length)
        while a == b:
            b = randomNum(length)
        c = randomNum(length)
        while a == c or b == c:
            c = randomNum(length)
        d = randomNum(length)
        while a == d or b == d or c == d:
            d = randomNum(length)
        return (a, b, c, d)

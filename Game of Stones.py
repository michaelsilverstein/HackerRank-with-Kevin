##https://www.hackerrank.com/challenges/game-of-stones-1

#Michael so far:
def gos(stones):
    for game in stones:
        if game <= 1:
            return 'Second'
        turn = 0
        while game > 1:
            if game % 5 == 0:
                game -= 5
                turn += 1
            if game % 3 == 0:
                game -= 3
                turn += 1
            if game % 2 == 0:
                game -= 2
                turn += 1
        if turn % 2 == 0:
            return 'First'
        else:
            return 'Second'


#Kevin (works):
a = input()
n = int(a)
c = [input() for _ in range(n)]
b=list(map(int,c))
def gameofstones(b):
    i=0
    for x in b:
        if (x % 7 >=2) and (x % 7 <= 6):
            print('First')
        else: 
            print('Second')
    print(answer)

gameofstones(b)

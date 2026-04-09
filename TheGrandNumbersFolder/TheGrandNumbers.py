'''
allGrandNumbers = range(10000, 100000+1)
allGrandNumbersYeah = [i for i in allGrandNumbers if (i % 5 == 0) and (i % 7 == 0)]
print(allGrandNumbersYeah, end="")

listInt = []
sprinter = int(input("first list length: "))

for i in range(sprinter+1):
    listInt.append(i)
print(listInt)

listIndices = input("Indices of your choice: ")
#print(listIndices)

listIndices = [int(i) for i in listIndices.split()]
sumIndices = sum(listInt[i] for i in listIndices)
print(sumIndices)

#number of heads
C = int(input("No of chicken heads: "))
R = int(input("No of Rabbit heads: "))

totalLegs = lambda C, R: 2*C + 4*R
print(totalLegs(C, R))
'''

def birthdayShare(k):

    probabilityShare = 1
    for i in range(k+1):
        probabilityShare *= ((365-i)/365)
    return (round(1-probabilityShare, 3))

kDot = int(input("The number of birthdays that will be shared is : "))
print(f"Thus, the probability of birthdays that will be shared is : {birthdayShare(kDot)}")
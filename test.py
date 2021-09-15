n = 29
sum = 0
for x in str(n):
    sum += int(x)

print(sum)
    



def largestNumber(n):
    large = (10 ** n) -1
    print(large)

largestNumber(2)

    


def addTwoDigits(n):
    sum = 0
    for x in str(n):
        sum += int(x)
    return sum

print(sum)

import string
s = "abacabad"
x = s.split()
# for x in range(len(s)):

print(x)


def circleOfNumbers(n, firstNumber):
    x = n/2
    if firstNumber == x:
        return(0)
    if firstNumber > x:
        l = firstNumber - x
        return(l)
    else:
        return(firstNumber + x)
        

n = 10
firstNumber = 2
print(circleOfNumbers(n, firstNumber))

def lateRide(n):
    x = int(n/60)
    y = n-(x*60)
    x = str(x)
    y = str(y)
    sum1 = 0
    sum2 = 0
    for i in str(x):
        sum1 += int(i)
    for i in str(y):
        sum2 += int(i)

    final = sum1 + sum2
    return(final)
n = 807
print(lateRide(n))

def phoneCall(min1, min2_10, min11, s):
    if s < min1:
        x = 0
    elif s == min1:
        x = 1
    elif s > min1 and s < 10:
        min1_10 = s - min1
        y = min1_10/min2_10
        x = (int(y) + 1)
    elif s > 11:
        y = 9/min2_10
        a = s - min1
        b = a - (min2_10 * 9)
        c = b/min11
        x = int(c) + int(y) + 1
    
    return x

min1 = 3
min2_10 = 1
min11 = 2
s = 20

print(phoneCall(min1, min2_10, min11, s))


def phoneCall(min1, min2_10, min11, s):
    if s < min1:
        x = 0
    elif s == min1:
        x = 1
    elif s > min1 and s < 10:
        min1_10 = s - min1
        y = min1_10/min2_10
        x = (int(y) + 1)
    elif s > 11:
        a = s - (min1 + (9*min2_10))
        b = a/min11
        x = (1 + 9 + int(b))            
    
    return x

min1 = 3
min2_10 = 1
min11 = 2
s = 20

print(phoneCall(min1, min2_10, min11, s))

def centuryFromYear(year):
    h = int(year/100)
    if year < 100:
        return(1)
    if year%100 == 0:
        return(h)
    else:
        if year > 100:
            return(h+1)

year = 1930
x = centuryFromYear(year)
print(x)


def reachNextLevel(experience, threshold, reward):
    if (experience + reward) > threshold-1:
        return True
    else:
        return False
    
    
experience = 10
threshold = 15
reward = 5
    
print(reachNextLevel(experience, threshold, reward))



def knapsackLight(value1, weight1, value2, weight2, maxW):
    one = value1*weight1
    two = value2*weight2
    if weight1 > maxW:
        return value2
    if weight2 > maxW:
        return value1
    if weight1 > maxW and weight2>maxW:
        return (0)
    if (weight1 + weight2) <= maxW:
        return (value1 + value2)
    if (weight1 + weight2) > maxW:
        if one > two:
            return value1
        else:
            return value2

value1 = 10
weight1 = 5
value2 = 6
weight2 = 4
maxW = 8
x = knapsackLight(value1, weight1, value2, weight2, maxW)
print(x)



def knapsackLight(value1, weight1, value2, weight2, maxW):
    one = value1+weight1
    two = value2+weight2
    if weight1 == maxW and weight1 >= weight2 and weight2 > maxW:
        return value1
    elif weight2 == maxW and weight2 >= weight1 and weight1 > maxW:
        return value2
    elif value1 == value2 and weight1 == weight2:
        return value1
    elif one == two:
        if value1 > value2:
            return value1
        elif value2 > value1:
            return value2
    elif weight1 > maxW and weight2>maxW:
        return (0)
    elif (weight1 + weight2) <= maxW:
        return (value1 + value2)
    elif weight1 > maxW:
        return value2
    elif weight2 > maxW:
        return value1
    elif (weight1 + weight2) > maxW:
        if one > two:
            return value1
        elif two > one:
            return value2
    
    

value1 = 10
weight1 = 5
value2 = 6
weight2 = 4
maxW = 8
x = knapsackLight(value1, weight1, value2, weight2, maxW)
print(x)


def isInfiniteProcess(a, b):
    x = True
    while b > 1:
        if a == b:
            x = False
        a += 1
        b -= 1
    if x is False:
        return False
    else:
        return True 
        
         
a = 2
b = 6

y = isInfiniteProcess(a, b)
print(y)   
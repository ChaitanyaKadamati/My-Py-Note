def mul(a,b=9) :
  return (a**2*b)
print(mul(2))

l = list(range(9))
print(l)
print(range(5,9))
s = iter(l)
print(type(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

print(i**2 for i in l)

zenPython = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
print(zenPython)
words = zenPython.split(' ')
print(words)
words = zenPython.strip().split(' ')
print(words)

for i in range(len(words)):
    words[i] = words[i].strip('.,?* ')
print('stripped words : ', words)

words = zenPython.lower().split(' ')
print(words)

k = [print(i) for i in "maverick" if i not in "aeiou"]

class Person:
    firstname = ''
    lastname = ''
    def tostr(self) :
        self.__openfn()
        return self.firstname + ' - ' + self.lastname
    def __openfn(self):
        print('this is static class')
    firstname = 'John'
    

p1 = Person()
print(p1.tostr())
Person.tostr(p1)
#p1._openfn()

class A:
    x = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x += 1

    def displayCount(self):
        print('Count : %d' % self.x)

    def display(self):
        print('a :', self.a, ' b :', self.b)

a1 = A('George', 25000)
a2 = A('John', 30000)
a1.display()
a2.display()
print(A.x)

class A1:
    def __init__(self, a = 5):
        self.a = a

    def f1(self):
        self.a += 10


class B(A1):
    def __init__(self, b = 0):
        A1.__init__(self, 4)
        self.b = b

    def f1(self):
        self.b += 10

x = B()
x.f1()
print(x.a,'-', x.b)

class class1:
    a = 1

    def f1(self):
        a = 2
        class1.a += 1
        print(class1.a, end=' ')
        print(a, end=' ')

class1().f1()
class1().f1()
print(float())
print(hex(-42))
import itertools
itr = (itertools.dropwhile(lambda x: x<5, [1,4,6,4,1]))
for i in itr :
    print(i, end=' ')
print('')
for i in [i**+1 for i in range(3)] :
    print(i, end=' ')
print('')

import re
# Enter your code here
def functionSearch(a):
    match = re.search('^[aeiouAEIOU].*[aeiouAEIOU]$',a)
    return match
def check_if_word_starts_ends_with_vowels(e):
    if(functionSearch(e)) :
        print(True)
    else:
        print(False)
print('check_if_word_starts_ends_with_vowels')
check_if_word_starts_ends_with_vowels('Africa')
check_if_word_starts_ends_with_vowels('Cdefgh')

def functionMatchStartsWith(a):
    m=re.match('^[e].* [e].*$',a)
    return m
def check_if_2words_starts_char_e(e):
    if(functionMatchStartsWith(e)) :
        print(True)
    else:
        print(False)
print('check_if_2words_starts_char_e')
check_if_2words_starts_char_e('expression expert')
check_if_2words_starts_char_e('eight tricks')

def functionMatchPattern(a):
    result=re.match(r"\b[a-zA-z]",a)
    return result
def check_if_sentense_starts_alphabets(e):
    if(functionMatchPattern(e)) :
        print(True)
    else:
        print(False)
print('check_if_sentense_starts_alphabets')
check_if_sentense_starts_alphabets('India won World Cup in the year 1983')
check_if_sentense_starts_alphabets('22 players will be involved in a cricket match')
check_if_sentense_starts_alphabets('There are 9 planets in the universe')
check_if_sentense_starts_alphabets('51.68% of people add decimal places to make their statistics look more credible')

def functionRECompile(x):
    pattern=re.compile('\d+')
    pattern=re.compile('[A-Z][a-z]* ')
    values= pattern.findall(x)
    return values

print(functionRECompile('''A has 5000 rupees and B has 15000 rupees.C has 85000 rupees and D has 50000 rupees .'''))
print(functionRECompile('Dhoni scored 100 runs and Kohli scored 150 runs.Rohit scored 50 runs and Dhawan scored 250 runs .'))

def main(x):
    pattern=re.compile('\d+')
    values= pattern.findall(x)
    names= re.compile('[A-Z][a-z]*').findall(x)
    dicts={}
    for i in range(len(values)):
        dicts[names[i]] = values[i]
    return dicts
print(main('''A has 5000 rupees and B has 15000 rupees.C has 85000 rupees and D has 50000 rupees .'''))
print(main('Dhoni scored 100 runs and Kohli scored 150 runs.Rohit scored 50 runs and Dhawan scored 250 runs .'))


sample_text=['199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245',
 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',
 '199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085',
 'burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0',
 '199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/sts-73/sts-73-patch-small.gif HTTP/1.0" 200 4179',
 'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0',
 'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0',
 '205.212.115.106 - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/countdown.html HTTP/1.0" 200 3985',
 'd104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',
 '129.94.144.152 - - [01/Jul/1995:00:00:13 -0400] "GET / HTTP/1.0" 200 7074',
 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',
 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786',
 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204',
 'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',
 'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786']
def func1():
    hostspattern = re.compile('\w+.\w+\.\w+\.\w+')
    hosts = []
    for x in sample_text:
        #hosts.append(hostspattern.match(x).group(0))
        hosts.append(re.findall(r'\w+.\w+\.\w+\.\w+',x)[0])
    print(hosts)
    expected = ['199.72.81.55', 'unicomp6.unicomp.net', '199.120.110.21', 'burger.letters.com', '199.120.110.21', 'burger.letters.com', 'burger.letters.com', '205.212.115.106', 'd104.aa.net', '129.94.144.152', 'unicomp6.unicomp.net', 'unicomp6.unicomp.net', 'unicomp6.unicomp.net', 'd104.aa.net', 'd104.aa.net']
    match = True
    if(len(hosts) != len(expected)):
        print('Fail:Length')
        return
    for (i,j) in zip(hosts,expected):
        if(i != j):
            print('Fail: Mismatch at ', i ,i)
            return
    print('Pass: Matched')

def func2():
    timestamp = []
    for x in sample_text:
        timestamp.append(re.findall(r"\[(.*?)\]",x)[0])
    print(timestamp)
    expected = ['01/Jul/1995:00:00:01 -0400', '01/Jul/1995:00:00:06 -0400', '01/Jul/1995:00:00:09 -0400', '01/Jul/1995:00:00:11 -0400', '01/Jul/1995:00:00:11 -0400', '01/Jul/1995:00:00:12 -0400', '01/Jul/1995:00:00:12 -0400', '01/Jul/1995:00:00:12 -0400', '01/Jul/1995:00:00:13 -0400', '01/Jul/1995:00:00:13 -0400', '01/Jul/1995:00:00:14 -0400', '01/Jul/1995:00:00:14 -0400', '01/Jul/1995:00:00:14 -0400', '01/Jul/1995:00:00:15 -0400', '01/Jul/1995:00:00:15 -0400']
    match = True
    if(len(timestamp) != len(expected)):
        print('Fail:Length')
        return
    for (i,j) in zip(timestamp,expected):
        if(i != j):
            print('Fail: Mismatch at ', i ,i)
            return
    print('Pass: Matched')
def func3():
    method_uri_protocol = []
    for x in sample_text:
        y = tuple(re.findall(r'\"(.*?)\"',x)[0].split(' '))
        method_uri_protocol.append(y)
    print(method_uri_protocol)
    expected = [('GET', '/history/apollo/', 'HTTP/1.0'), ('GET', '/shuttle/countdown/', 'HTTP/1.0'), ('GET', '/shuttle/missions/sts-73/mission-sts-73.html', 'HTTP/1.0'), ('GET', '/shuttle/countdown/liftoff.html', 'HTTP/1.0'), ('GET', '/shuttle/missions/sts-73/sts-73-patch-small.gif', 'HTTP/1.0'), ('GET', '/images/NASA-logosmall.gif', 'HTTP/1.0'), ('GET', '/shuttle/countdown/video/livevideo.gif', 'HTTP/1.0'), ('GET', '/shuttle/countdown/countdown.html', 'HTTP/1.0'), ('GET', '/shuttle/countdown/', 'HTTP/1.0'), ('GET', '/', 'HTTP/1.0'), ('GET', '/shuttle/countdown/count.gif', 'HTTP/1.0'), ('GET', '/images/NASA-logosmall.gif', 'HTTP/1.0'), ('GET', '/images/KSC-logosmall.gif', 'HTTP/1.0'), ('GET', '/shuttle/countdown/count.gif', 'HTTP/1.0'), ('GET', '/images/NASA-logosmall.gif', 'HTTP/1.0')]
    match = True
    if(len(method_uri_protocol) != len(expected)):
        print('Fail:Length')
        return
    for (i,j) in zip(method_uri_protocol,expected):
        if(i != j):
            print('Fail: Mismatch at')
            print(i)
            print(j)
            return
    print('Pass: Matched')

def func4():
    status = []
    pat = re.compile('\w+ \w+[.]*$')
    for x in sample_text:
        status.append(pat.search(x).group().split(' ')[0])
    print(status)
    expected = ['200', '200', '200', '304', '200', '304', '200', '200', '200', '200', '200', '200', '200', '200', '200']
    match = True
    if(len(status) != len(expected)):
        print('Fail:Length')
        return
    for (i,j) in zip(status,expected):
        if(i != j):
            print('Fail: Mismatch at ', i ,i)
            return
    print('Pass: Matched')

def func5():
    status = []
    pat = re.compile('\w+ \w+[.]*$')
    for x in sample_text:
        status.append(pat.search(x).group().split(' ')[1])
    print(status)
    expected = ['6245', '3985', '4085', '0', '4179', '0', '0', '3985', '3985', '7074', '40310', '786', '1204', '40310', '786']
    match = True
    if(len(status) != len(expected)):
        print('Fail:Length')
        return
    for (i,j) in zip(status,expected):
        if(i != j):
            print('Fail: Mismatch at ', i ,i)
            return
    print('Pass: Matched')
    '''For testing the code, no input is to be provided'''

func1()
func2()
func3()
func4()
func5()

from itertools import permutations, combinations
import numpy as np
arr = np.array(['A','B','C','D','E'])
p = permutations(arr,2)
print(list(p))
c = combinations(arr,2)
print(list(c))

#In how many ways can 10 balls be picked, from 7 red out of 10, and 3 blue out of 8?
import math
red = math.factorial(10)/(math.factorial(7) * math.factorial(10-7))
blue = math.factorial(8) / (math.factorial(3) * math.factorial(8-3))
print(int(red * blue))

# There are 11 students in a class.
# Number of Boys = 6
# Number of girls = 5
# Scenario
# The teacher wants a group to be formed for the upcoming dance competition. She wants a group of 5 dancers consisting of 3 boys and 2 girls. In how many ways can a group of 5 dancers be formed by selecting 3 boys out of 6 and 2 girls out of 5 ? Help her out!
# Display the number of ways a group of 5 dancers consisting of 3 boys and 2 girls can be formed.
import math
boy = math.factorial(6)/(math.factorial(3) * math.factorial(6-3))
girl = math.factorial(5)/(math.factorial(2) * math.factorial(5-2))
print(int(girl*boy))

def isSequence(arr,i) :
    #return i == len(arr)-1 or (arr[i] == arr[i+1]-1) and isSequence(arr,i+1)
    # if(i == len(arr) -2 ):
    #     return True
    return True if (i == len(arr) -2 ) else ((arr[i] == arr[i+1]-1) and isSequence(arr, i +1))
print(isSequence([1,2,3,4,5,6,7, 8], 0))
print(isSequence([1,2,3,4,6,7,8], 0))

def getSumOfDigits(x) :
    return x if(x<10) else (x %10) + getSumOfDigits(math.floor(x / 10))
print('sum(12345) = ' + str(getSumOfDigits(12345)))
print('sum(10000000091) = ' + str(getSumOfDigits(10000000091)))

def isPalindrome(s,x,y):
    if(x ==y or x>y):
        return True
    if(s[x]==s[y]):
        return True and isPalindrome(s,x+1,y-1)
    else: 
        return False
print(isPalindrome('AlfaBetaGamma',0,len('AlfaBetaGamma')-1))
x = 'AlfaBetaGamma'+ ('AlfaBetaGamma'[::-1])
print(x)
print(isPalindrome(x,0,len(x)-1))
print(isPalindrome('LoaoL',0,len('Loaol')-1))
print(isPalindrome('CoaC',0,len('Coal')-1))
print(isPalindrome('ABCDXYZZYXDCBA',0,len('ABCDXYZZYXDCBA') -1))

class QueensProblem:
    def __init__(self,numOfQueens):
        self.numOfQueens = numOfQueens
        self.chessTable = [[0]*numOfQueens]*numOfQueens

    def solve(self) :
        if(self.setQueens(0)):
            self.printQueens()
        else:
            print('There is no solution!!!')

    def printQueens(self):
        for x in range(self.numOfQueens):
            for y in range(self.numOfQueens):
                if(self.chessTable[x][y] == 1):
                    print(' * ',end='')
                else:
                    print(' - ',end='')
            print()
            
    def setQueens(self,colIndex):
        if(colIndex == self.numOfQueens):
            return True
        for rowIndex in range(self.numOfQueens):
            if(self.isPlaceValid(rowIndex,colIndex)):
                self.chessTable[rowIndex][colIndex] = 1
                if(self.setQueens(colIndex + 1)):
                    return True
                # BackTracking
                self.chessTable[rowIndex][colIndex] = 0 
        return False

    def isPlaceValid(self,rowIndex,colIndex):
        for i in range(colIndex):
            if(self.chessTable[rowIndex][i] == 1):
                print('Lost at 1 value, invalid because of ', self.chessTable[rowIndex], ' ROW ',rowIndex, i)
                return False
        
        a = rowIndex
        b = colIndex
        while (a>=0 and b>=0):
            if(self.chessTable[a][b] == 1):
                print('Lost at 2', a, b)
                return False
            a = a - 1
            b = b - 1

        a = rowIndex
        b = colIndex
        while(a< len(self.chessTable) and b>=0):
            if(self.chessTable[a][b] == 1):
                print('Lost at 3', a, b)
                return False
            a = a + 1
            b = b - 1
            
        print('Pass at ', rowIndex,colIndex)
        return True
            
queensProb = QueensProblem(8)
queensProb.solve()

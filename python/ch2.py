import timeit
from timeit import  Timer
import random


def sumOfN2(n):
    start =time.time()
    theSum=0
    for i in range(1,n+1):
        theSum=i+1
    end=time.time()

    return theSum,end-start

def anagramSolution(s1,s2):
    alist=list(s2)
    pos1=0
    stillOK=True

    while pos1 <len(s1) and stillOK:
        pos2=0
        found=False
        while pos2<len(alist) and not found:
            if s1[pos1]==alist[pos2]:
                found=True
            else:
                pos2=pos2+1
        if found:
            alist[pos2]=None
        else:
            stillOK=False

        pos1=pos1+1
    return stillOK

def anagramSolution4(s1,s2):  #the best
    c1=[0]*26
    c2=[0]*26

    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')
        c1[pos]=c1[pos]+1
    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')
        c2[pos]=c2[pos]+1

    j=0
    stillOK=True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j=j+1
        else:
            stillOK=False
    return stillOK

def test1():
    l=[]
    for i in range(1000):
        l=l+[i]
def test2():
    l=[]
    for i in range(1000):
        l.append(i)

def test3():
    l=[i for i in range(1000)]

def test4():
    l=list(range(1000))


def compare_list_and_dict():
    for i in range(10000,1000001,20000):
        t=Timer("random.randrange(%d) in x "%i,"from __main__ import random,x")
        x=list(range(i))
        lst_time=t.timeit(number=1000)
        x ={j:None for j in range(i)}
        d_time=t.timeit(number=1000)
        print("%d,%10.3f,%10.3f"%(i,lst_time,d_time))


if __name__ == '__main__':
    # print(anagramSolution4('abcd','abdd'))

    # t1=Timer("test1()","from __main__ import test1")
    # print("concat ",t1.timeit(number=1000),"milliseconds")
    # t2=Timer("test2()","from __main__ import test2")
    # print("append",t2.timeit(number=1000),"milliseconds")
    # t3=Timer("test3()","from __main__ import test3")
    # print("comprehension",t3.timeit(number=1000),"milliseconds")
    # t4 = Timer("test4()", "from __main__ import test4")
    # print("list range", t4.timeit(number=1000), "milliseconds")

    # pop_zero=Timer("x.pop(0)","from __main__ import x")
    # pop_end =Timer("x.pop()","from __main__ import x")
    # x=list(range(2000000))
    # print(pop_zero.timeit(number=1000))
    #
    # x=list(range(2000000))
    # print(pop_end.timeit(number=1000))
    compare_list_and_dict()




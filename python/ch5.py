#!/usr/bin/python
#! usr/bin/python #coding=utf-8
def sequentialSearch(alist,item): #在无序顺序查找
    pos=0
    found=False
    while pos<len(alist)and not found:
        if alist[pos]==item:
            found=True
        else:
            pos=pos+1
    return found

def orderedSequentialSearch(alist,item):#在有序中查找
    pos=0
    found=False
    stop=False
    while pos<len(alist)and  not found and not stop:
        if alist[pos]==item:
            found=True
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos=pos+1
    return found

def binarySearch(alist,item):  #二分法,迭代
    first=0
    last=len(alist)-1
    found=False
    while first<=last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True
        else:
            if alist[midpoint]<item:
                first=midpoint+1
            else:
                last=midpoint-1
    return found

def binarySearch_1(alist,item):#二分法,递归
    if len(alist)==0:
        return False
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if alist[midpoint]<item:
                return binarySearch_1(alist[midpoint+1:],item)
            else:
                return binarySearch_1(alist[:midpoint],item)
############################################ 哈希表
class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
    def put(self,key,data):
        hashvalue =self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue] =data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data
            else:
                nextslot =self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot]!=None and self.slots[nextslot]!=key:
                    nextslot=self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot]==None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot]=data

    def hashfunction(self,key,size):
        return key%size
    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
        startslot=self.hashfunction(key,len(self.slots))
        data=None
        stop=False
        found=False
        position=startslot
        while self.slots[position]!=None and not found and not stop:
            if self.slot[position]==key:
                found=True
                data=self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position==startslot :
                    stop=True
        return data

    def __getitem__(self):
        return self.get(key)

    def __setitem__(self,key,data):
        return self.put(key,data)

##############################################################
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp

if __name__=="__main__":
    # testlist=[1,2,3,4,5]
    # print(sequentialSearch(testlist,3))
    # print(orderedSequentialSearch(testlist, 3))
    # print(binarySearch(testlist,3))
    # print(binarySearch_1(testlist, 2))

    # H=HashTable()
    # H[54]="cat"
    # H[26] = "cat"
    # H[93] = "cat1"
    # H[17] = "cat2"
    # H[77] = "cat3"
    # H[31] = "cat4"
    # H[44] = "cat5"
    # H[55] = "cat6"
    # H[20] = "cat7"
    # print(H.slots)
    # print(H.data)
    # H[20]='duck'
    # H[54] = "dog"
    # print(H.data)

    alist=[54,26,93,17,77,32,44,55,20]
    bubbleSort(alist)
    print(alist)
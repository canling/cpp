########################################################
class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
###############################################################
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==[]
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
###########################################################################
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext


class UnorderedList:
    def __init__(self):
        self.head=None
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current=current.getNext()
        return count

    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found

    def remove(self,item):
        current=self.head
        previous=None
        found  =False
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()

        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())


class OrderedList:
    def __init__(self):
        self.head=None

    def size(self):
        current=self.head
        count=0
        while not current:
            count=count+1
            current=current.getNext()
        return count
    def isEmpty(self):
        current=self.head
        if current==None:
            return True
        else:
            return False
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while not found:
            if(current.getData()==item):
                found=Ture;
            else:
                previous=current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self,item):
        current=self.head
        found=False
        stop =False
        while current !=None and not found and not stop:
            if current.get_data()==item:
                found=True
            else:
                if current.get_data()>item:
                    stop=True
                else:
                    current=current.getNext()
        return found

    def add(self,item):
        current=self.head
        previous=None
        stop=False
        while current!=None and not stop:
            if current.getData()>item:
                stop=True
            else:
                previous=current
                current=current.getNext()
        temp=Node(item)
        if previous==None:
            temp.setNext(self.head)
            self.head=temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
######################################################################
def parchecker(symbolString): #ues stack
    s=Stack()
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol== "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index=index+1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def parChecker(symbolString):    #use stack
    s=Stack()
    balenced=True
    index=0
    while index<len(symbolString) and balenced:
        symbol=symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balenced=False
            else:
                top=s.pop()
                if not matches(top,symbol):
                    balenced=False
            index=index+1
        if balenced and s.isEmpty():
            return True
        else:
            return False

def matches(open,close):
    opens="({["
    closers=")}]"
    return opens.index(open)==closers.index(close)



def divideBy2(decNumber): #use stack
    remstack=Stack()
    while decNumber >0:
        rem=decNumber%2
        remstack.push(rem)
        decNumber=decNumber //2
    binString =""
    while not remstack.isEmpty():
        binString =binString+str(remstack.pop())
    return binString

def baseConverter(decNumber,base): #use stack
    digits="0123456789ABCDEF"
    remstack=Stack()
    while decNumber >0:
        rem=decNumber %base
        print(rem,'**')
        remstack.push(rem)
        decNumber=decNumber//base
    newString=''
    while not remstack.isEmpty():
        newString=newString+digits[remstack.pop()]
    return newString



def infixToPostfix(infixexpr):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    opStack =Stack()
    postfixList=[]
    tokenList=infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token=='(':
            opStack.push(token)
        elif token==')':
            topToken=opStack.pop()
            while topToken !='(':
                postfixList.append(topToken)
                topToken=opStack.pop()
        else:
            while(not opStack.isEmpty())and (prec[opStack.peek()]>=prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return "".join(postfixList)

###########################################
def hotPotato(namelist,num):# use Queue
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            #print(simqueue.enqueue(simqueue.dequeue()),'%%%',i,simqueue.size())

        print(simqueue.dequeue())
    return simqueue.dequeue()

def palchecker(aString):    # use Deque
    chardeque=Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual =True
    while chardeque.size()>1 and stillEqual:
        first=chardeque.removeFront()
        last=chardeque.removeRear()
        if first!=last:
            stillEqual=False
    return stillEqual

if __name__ =="__main__":
    # stack=Stack()
    # print(stack.isEmpty())
    # stack.push("dog")
    # stack.push("4")
    # print(stack.peek())
    # stack.push(True)
    # print(stack.size())
    # print(stack.pop())
    # print(stack.size())

    # print(parchecker("(()))"))
    # print(parchecker("(())"))
    # print(parChecker('{}'))

    print(divideBy2(254))
    print(baseConverter(25,2))
    print(baseConverter(28,16))
###########################################
    # q=Queue()
    # q.enqueue(4)
    # q.enqueue("dog")
    # q.enqueue(True)
    # print(q.size())
    # print(q.dequeue())

    # print(hotPotato(["a","b","c","d","e","f"],7))
###############################################
    # d=Deque()
    # print(d.isEmpty())
    # d.addRear(4)
    # d.addRear('dog')
    # d.addFront('cat')
    # d.addFront(True)
    # print(d.size())
    # print(d.isEmpty())
    # print(d.removeFront())
    # print(d.removeRear())

    # print(palchecker("radar"))
    # print(palchecker("linkenpark"))

    # temp=Node(90)
    # print(temp.getData())

    # l=UnorderedList()
    # l.add(1)
    # l.add(2)
    # l.add("a")
    # print(l.remove(1)) #这里还有bug
    # print(l.size())
    # print(l.search(1))
    # print(l.search(2))
    # print(l.search('a'))
    # print(l.remove(2))

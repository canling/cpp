import turtle
from ch3 import *

rStack=Stack()
myTurtle = turtle.Turtle()
myWin = turtle.Screen()
def toStr(n,base):                #转化任意进制，递归方式
    convertString="0123456789ABCDEF"
    if n<base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]


def toStr_1(n,base):             #转化任意进制，栈方式
    convertString ="0123456789ABCDEF"
    while n>0:
        if n<base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n%base])
        n=n//base
    res=""
    while not rStack.isEmpty():
        res=res+rStack.pop()
    return res


def drawSpiral(myTurtle,lineLen): #画螺旋

    if lineLen>0:
        myTurtle.forward(lineLen)
    myTurtle.right(90)
    drawSpiral(myTurtle,lineLen-5)

def tree(branchLen,t):            #画树
    if branchLen >5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)
################################################汉罗塔
def moveTower(height,fromPole,toPole,withPole):   #汉罗塔
    if height>=1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    tp.push(fp.pop())

###############################################迷宫
# def searchFrom(maze,startRow,startColumn):
#     maze.unpdataPosition(startRow,startColumn)
#     if maze[startRow][startColumn]==OBSTACLE:
#         return False
#     if maze[startRow][startColumn]==TRIED:
#         return False
#     if maze.isExit(startRow,startColumn):
#         maze.updatePosition(startRow,startColumn,PART_OF_PATH)
#         return True
#     maze.updatePosition(startRow,startColumn,TRIED)
#     found=searchFrom(maze,startRow-1,startColumn) or \
#           searchFrom(maze,startRow+1, startColumn)or \
#           searchFrom(maze, startRow , startColumn-1) or \
#           searchFrom(maze, startRow , startColumn+1)
#     if found:
#         maze.updatePosition(startRow,startColumn,PART_OF_PATH)
#     else:
#         maze.updataPosition(startRow,startColumn,DEAD_END)
#     return found

def recMC(coinValueList,change):
    minCoins=change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-i)
            if numCoins<minCoins:
                minCoins=numCoins
    return minCoins

# def dpMakeChange(coinValueList,change,minCoins):
#     for cents in range(change+1):
#         coinCount=cents
#         for j in [c for c in coinValueList if c<=cents]:
#             if minCoins[cents-j]+1 <coinCount
if __name__=="__main__":
    # print(toStr(1452,10))   #进制转换
    # print(toStr_1(1452,10))  #进制转换

    # drawSpiral(myTurtle,100)
    # myWin.exitonclick()
    # tree(50,turtle)

    # stack_A =Stack()     #汉罗塔
    # stack_B =Stack()
    # stack_C =Stack()
    # stack_A.push(2)
    # stack_A.push(5)
    # stack_A.push(1)
    # stack_A.push(6)
    # stack_A.push(25)
    # stack_A.push(4)
    # moveTower(6,stack_A,stack_B ,stack_C)
    # for i in range(stack_B.size()):
    #      print(stack_B.pop())
    print("hello world")
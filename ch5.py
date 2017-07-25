

def sequentialSearch(alist,item):
    pos=0
    found=False
    while pos<len(alist)and not found:
        if alist[pos]==item:
            found=True
        else:
            pos=pos+1
    return found

if __name__=="__main__":
    testlist=[1,2,34,45]
    print(sequentialSearch(testlist,34))
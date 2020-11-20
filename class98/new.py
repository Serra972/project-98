def countWords():
    filename=input('enter file name')
    filename1=input('enter file name')
    with open(filename,'r')as a:
        da=a.read()
    with open(filename1,'r')as b:
        db=b.read()
    with open(filename,'w')as a:
        a.write(db)
    with open(filename,'w')as b:
        b.write(da)
    

countWords()
import random
n=int(input("plz Enter the lenght: "))
mylist=[]
while n>len(mylist):
    pc_num=random.randint(0,100) 
    mylist.append(int(pc_num)) 
    print(mylist)   
    if pc_num in mylist:
        mylist=list(dict.fromkeys(mylist)) 
print(mylist)
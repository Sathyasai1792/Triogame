import random
import sys
def prt(a):                                        #printing board for every move
    for i in range(3):
        for j in range(3):
            print(a[i][j],end=' ')
        print()
def win(a,x):                                      #checking if next move is win for computer
    for j in range(3):
        if(a[0][j]==x and a[2][j]==x and a[1][j]==0):
            return j+4
        elif(a[0][j]==x and a[1][j]==x and a[2][j]==0):
            return j+7
        elif(a[2][j]==x and a[1][j]==x and a[0][j]==0):
            return j+1
    for j in range(3):
        if(a[j][0]==x and a[j][2]==x and a[j][1]==0):
            return (j*2+j)+2
        elif(a[j][0]==x and a[j][1]==x and a[j][2]==0):
            return (j*2+j)+3
        elif(a[j][2]==x and a[j][1]==x and a[j][0]==0):
            return (j*2+j)+1
    if(a[0][0]==x and a[2][2]==x and a[1][1]==0):
        return 5
    if(a[0][0]==x and a[1][1]==x and a[2][2]==0):
        return 9
    if(a[1][1]==x and a[2][2]==x and a[0][0]==0):
        return 0
    if(a[0][2]==x and a[2][0]==x and a[1][1]==0 ):
        return 5
    if(a[0][2]==x and a[1][1]==x and a[2][0]==0):
        return 7
    if(a[1][1]==x and a[2][0]==x and a[0][2]==0):
        return 3
    return -1
def play1(t,a):                                        #player input
    a[x(t)][y(t)]=1
def check(a):                                          #checking for win
    c=0
    for i in range(3):
        if(a[i].count(1)==3):
            print("player won")
            sys.exit()
        if(a[i].count(2)==3):
            print("computer won")
            sys.exit()
    for i in range(2):
        for j in range(3):
            if(a[c][j]==i+1):
                if(a[c][j]==a[c+1][j] and a[c][j]==a[c+2][j]):
                    if(i+1==1):
                        print("player won")
                        sys.exit()
                    else:
                        print("computer won")
                        sys.exit()
    for i in range(2):
        if(a[0][0]==i+1):
            if(a[1][1]==a[0][0] and a[0][0]==a[2][2]):
                if(i+1==1):
                    print("player won")
                    sys.exit()
                else:
                    print("computer won")
                    sys.exit()
        if(a[0][2]==i+1):
            if(a[1][1]==a[0][2] and a[0][2]==a[2][0]):
                if(i+1==1):
                    print("player won")
                    sys.exit()
                else:
                    print("computer won")
                    sys.exit()
    for i in range(3):
        if(a[i].count(0)==0):
            c+=1 
            if(c==3):
                print("tie")
                sys.exit()
def x(t):                                           #converting input to x coordinates of list 
    x=int((t-1)/3)
    return x
def y(t):                                               #converting input to y coordinates of list
    y=int((t-1)%3)
    return y
def comp(a,c,s):                                     #computer move
    xx=2
    yy=1
    l=win(a,xx)
    if(l!=-1):
        if(a[x(l)][y(l)]==0):
            a[x(l)][y(l)]=2
            if(l in c):
                c.remove(l)
            if(l in s):
                s.remove(l)
            return 0
    ll=win(a,yy)
    if(ll!=-1):
        
        if(a[x(ll)][y(ll)]==0):
            a[x(ll)][y(ll)]=2
            if(ll in c):
                c.remove(ll)
            elif(ll in s):
                s.remove(ll)
            return 0
    if(a[1][1]==0):
        a[1][1]=2 
        return 0
    if(len(c)!=0):
        while(1):
            t=random.choice(c)
            x2=x(t)
            y2=y(t)
            if(a[x2][y2]==0):
                c.remove(t)
                a[x2][y2]=2
                return 0
            elif(len(c)==0):
                break
    
        
    while(1):
        v=random.choice(s)
        x1=x(v)
        y1=y(v)
        if(a[x1][y1]==0):
            s.remove(v)
            a[x1][y1]=2
            return 0
        elif(len(s)==0):
            break
print("button indications are as follows")
print("1 2 3\n4 5 6\n7 8 9\nenter your move according to this buttons\nGame started !\n")
a=[]
c=[1,3,7,9]
s=[2,4,6,8]
for i in range(3):                                #creating board
    b=[]
    for j in range(3):
        b.append(0)
    a.append(b)
prt(a)                                    #printing board
print()
i=random.randint(0,1)                           #random first chance
while(1):
    if(i%2==0):                                 #player move
        while(1):
            print("Enter your move")
            t=int(input())
            if(a[x(t)][y(t)]==0):
                break
            else:
                print("enter valid option! Enter your move again")
        play1(t,a)
        if( t in c):
            c.remove(t)
        if(t in s):
            s.remove(t)
        prt(a)
        check(a)
        print()
    if(i%2==1):                                  #computer turn
        print("computer turn")
        comp(a,c,s)
        check(a)
        prt(a)
    i+=1

def prt(a):                                   #printing the board for every move
     for i in range(8) :
        for j in range(7):
            print(a[i][j],end=' ')
        print()
def play1(t,a):                               #input of player 1
    i=7;
    while(1):
        if(a[i][t]==chr(32)):
            a[i][t]='R';
            return i
            break
        else:
            i-=1
    
def play2(t,a):                              #input of player 2
    i=7;
    while(1>0):
        if(a[i][t]==chr(32)):
            a[i][t]='Y';
            return i
            break
        else:
            i-=1
def check(ax,t,a):                           #checking for win vertically and horizontally
    
    if(ax<=4):
        if(a[ax][t]==a[ax+1][t] and a[ax][t]==a[ax+2][t] and a[ax][t]==a[ax+3][t]):
            return 1 
    elif(t<3):
        if(a[ax][t]==a[ax][t+1] and a[ax][t]==a[ax][t+2] and a[ax][t]==a[ax][t+3]):
            return 1 
    elif(t>3):
        if(a[ax][t]==a[ax][t-1] and a[ax][t]==a[ax][t-2] and a[ax][t]==a[ax][t-3]):
            return 1 
    elif(t==3):
        if(a[ax][t]==a[ax][t-1] and a[ax][t]==a[ax][t-2] and a[ax][t]==a[ax][t-3]):
            return 1 
        elif(a[ax][t]==a[ax][t+1] and a[ax][t]==a[ax][t+2] and a[ax][t]==a[ax][t+3]):
            return 1 
    else:
        return 0
def check1(ax,t,a):                                      #checking for win diagonally
    if(t>=3):
        if(ax>=4):
            if(a[ax][t]==a[ax-1][t-1] and a[ax][t]==a[ax-2][t-2] and a[ax][t]==a[ax-3][t-3]):
                return 1 
        if(ax<=4):
            if(a[ax][t]==a[ax+1][t-1] and a[ax][t]==a[ax+2][t-2] and a[ax][t]==a[ax+3][t-3]):
                return 1 
    if(t<=3):
        if(ax>=4):
            if(a[ax][t]==a[ax-1][t+1] and a[ax][t]==a[ax-2][t+2] and a[ax][t]==a[ax-3][t+3]):
                return 1
        if(ax<=4):
            if(a[ax][t]==a[ax+1][t+1] and a[ax][t]==a[ax+2][t+2] and a[ax][t]==a[ax+3][t+3]):
                return 1
    else:
        return 0
            
print("player 1 is Red and player 2 is yellow")            
a=[]
b=[]
for p in range(8):                                    #creating board 
    b=[]
    for i in range(7):
        b.append(chr(32))
    a.append(b)
for i in range(7):                                    #indicating column number 
    a[0][i]=i+1
i=0
prt(a)                                                #printing the board
while (1>0):
    if(i%2==0):                                       #player 1
        print("it's Red's turn to play,Enter your column number");
        t= int(input())
        t-=1
        ax=play1(t,a)
        i+=1
        res=check(ax,t,a)
        res1=check1(ax,t,a)
        prt(a)
        if(res==1 or res1==1):
            print("Congratulations Red! You Won")
            break
    if(i%2==1):                                          #player 2
        print("it's Yellow's turn to play,Enter your column number ");
        t= int(input())
        t-=1
        ax= play2(t,a);
        i+=1
        res=check(ax,t,a)
        res1=check1(ax,t,a)
        prt(a)
        if(res==1 or res1==1):
            print("Congratulations Yellow! You Won")
            break

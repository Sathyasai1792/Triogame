print("enter name of the first person")   #taking inputs from user
a=input()
a=a.lower()
print("enter name of the second person")
b=input()
b=b.lower()
x=[]
t=0
c=(a+"bonds"+b)
l=len(c)
for i in range(l):           #counting number of characters repeating in a string
    if (c[i]!="0"):
        t=c.count(c[i])
        c=c.replace(c[i],"0")
        x.append(t)
t=len(x)
i=0
j=t-1
y=[]
p=0
while(len(x)!=2):              #calculating bond as in the question statement
    l=int(t/2)
    s=x[i]+x[j]
    if(s>=10):
        s1=int(s/10)
        y.insert(p,s1)
        s2=int(s%10)
        p+=1
        y.insert(p,s2)
        p+=1
    if(s<10):
        y.insert(p,s)
        p+=1
    i+=1
    j-=1
    if(i==j):
        y.append(x[i])
    if(i>=l):
        x=y
        y=[]
        i=0
        t=len(x)
        j=t-1
        p=0
t=x[0]*10+x[1]        #converting to percentage
print('The bond between ',a,' and ' ,b,' is ',t,'%.')    #output

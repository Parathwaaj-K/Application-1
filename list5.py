
    

#using lambda
li=[(1,2),(3,5),(6,7)]
df=list(map(lambda sub:(sub[1],sub[0]) , li))
print(df)


d=[2,4,6,8]
def swap(d):
    d[1],d[0]= d[0],d[1]
    return d
print(swap(d))

#to check fibonacci
nterms=int(input('Enter the number : '))
a=1
b=0
count=0
if nterms<0:
    print('incorrect input')
elif nterms==1:
        print('sequence number upto',nterms)
else:
    while count<nterms:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
        

    






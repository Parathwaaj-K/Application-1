#intersection using list and filter
from  functools  import reduce


def intersection(arr1,arr2):
    res=list(filter(lambda x:x in arr1,arr2))
    
    print('intersection: ',res)
#drive code
if __name__=='__main__':
      arr1=[1,5,6]
      arr2=[7,8,9]
intersection(arr1,arr2)



#using lambda to find fibonnaci
from functools import reduce

df=lambda n:reduce(lambda x,_: x+[x[-1]+x[-2]],range(n-2),[0,1])
print(df(5))



#ascii
def alphapat(n):
    num=65
    for i in range(0,n):
        for j in range(0,i+1):
            print(end=" ")
            ch=chr(num)
            print(ch,end=' ')
            num+=1
        print('\r')
n=5
alphapat(n)


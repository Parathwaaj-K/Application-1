
from collections import namedtuple

student=namedtuple('student',['color1','color2','color3'])
code=namedtuple('code',['code1','code2','code3'])

s=student('red','blue','orange') 
s1=code('054ufn','09ghf','67bvh')
print({s,s1})

 
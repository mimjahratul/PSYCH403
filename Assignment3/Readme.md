# Level 1 Exercises

## Variable Operations:

1.
```
sub_code = 'sub'
subnr_int = 2
subnr_str = '2'

print(sub_code + subnr_str)
```
Adding subnr_str to sub_code will produce the output 'sub2' because they are both string types and subnr_int is an int typestring and int can not be added

2. Operations to create the outputs: 
```
print(sub_code + " " + subnr_str)
print(sub_code + " " + (subnr_str)*3)
print((sub_code + subnr_str) *3)
print((sub_code)*3 + subnr_str*3)
```

## List Operations
1. 
```
numlist = [1,2,3]
print(numlist*2)
```
2. When you multiply a list by an integer, it prints the values by the multiple (e.g. twice in this case). Whereas for arrays, it prints the multiplication of the numbers in the array by the multiple
```
import numpy as np
numarr = np.array([1,2,3])
print(numarr*2)
```
3. 
```
strlist = ['do','re','mi','fa']
print([strlist[0]*2,strlist[1]*2,strlist[2]*2,strlist[3]*2])
print(strlist*2)
print([strlist[0],strlist[0],strlist[1],strlist[1],strlist[2],strlist[2],strlist[3],strlist[3]])
print([[strlist[0],strlist[0]],[strlist[1],strlist[1]],[strlist[2],strlist[2]],[strlist[3],strlist[3]]])
```

## Zipping 
```
import numpy as np

img1 = []
img2 = []
cues = ['cue1'] * 50 + ['cue2'] * 50

house = ['house1.png'] * 5 + ['house2.png'] * 5 + ['house3.png'] * 5 + ['house4.png'] * 5 + ['house5.png'] * 5
face = ['face1.png'] * 5 + ['face2.png'] * 5 + ['face3.png'] * 5 + ['face4.png'] * 5 + ['face5.png'] * 5

img1.extend(face)
img1.extend(house)
img1.extend(face)
img1.extend(house)

house1 = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png'] * 5
face1 = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png'] * 5

img2.extend(house1)
img2.extend(face1)
img2.extend(house1)
img2.extend(face1)

ziplist = list(zip(img1,img2,cues))
np.random.shuffle(ziplist)
print(ziplist)
```

## Indexing
```
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(colors[4])
print(colors[4][2],colors[4][3])
colors.remove('purple')
colors.append('indigo')
colors.append('violet')
print(colors)
```

## Slicing
```
list100 = list(range(0,101))
print(list100)
print(list100[:10])
print(list100[1:101:2][::-1])
print(list100[97:101][::-1])

print(list100[39:44] == list(range(39,44))) 
```
5. Yes the 40th-44th numbers in the list are equal to integers 39-43. 

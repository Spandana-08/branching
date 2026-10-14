# APPEND METHOD

l1=[10,20,30]
l1.append(40)
print(l1)

#INSERT METHOD

l2=[1,2,3,4,5]
l2.insert(0,0)
print(l2)

l2.insert(10,6)#above index number it add it end of the list
print(l2)
l2.insert(-10,-1)#it add front of the list
print(l2)


#EXTEND METHOD

l3=[21,22,23,24,25]
l4=[26,27,28,29,30]
l3.extend(l4)
print(l3)
l4.extend(l3)
print(l4)

#POP METHOD

l5=[21,22,23,24]
rem_ele=l5.pop()
print(rem_ele)
print(l5)

#POP(INDEX)METHOD

l6=[31,32,33,34]
rem=l6.pop(1)
print(l6)

#REMOVE METHOD

l7=[99,98,97,96]
l7.remove(96)
print(l7)

#CLEAR METHOD

l8=[9,8,7,6]
l8.clear()
print(l8)

#COUNT METHOD

l9=[20,21,22,23,21,21,25,21]
num=l9.count(21)
print(num)

#INDEX METHOD

l10=[23,34,45,54,63]
ind=l10.index(54)
print(ind)

#REVERSE METHOD

l11=[11,22,33,44]
l11.reverse()
print(l11)

#SORT METHOD

l12=[4,3,2,1,5,7,6]
l12.sort()
print(l12)

#QUESTION

# I WANT YOU TO PRINT THE SUM OF SMALLEST NUMBER
#AND LARGEST NUMBER USING METHODS AND INDEXING

l=[59,12,18,14,17]
#l.sort()
#print(l)
#print(l[0]+l[4])

#or

ele1=l.pop(0)
ele2=l.pop(1)
print(ele1+ele2)



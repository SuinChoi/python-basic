# section04-3
# Python Data Type : List & Tuple
# 파이썬 자료형 : 리스트와 튜플

# List : Order(Y), Duplicate(Y), Modify(Y), Delete(Y)
# 리스트 :  순서(O), 중복(O), 수정(O), 삭제(O)

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'pizza', 'pasta', 'hamburger']
e = [10, 100, ['pizza', 'pasta', 'hamburger']]


# 인덱싱
# Indexing
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(d[3]+d[4])
print(e[2][1])
print(e[-1][-2])


# 슬라이싱
# Slicing
print(d[0:2])
print(e[2][1:3])

# 연산
print( c + d )
print( c * 3 )
print(str(c[0])+"hi")


# 수정, 삭제
# Modifying
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a','b','c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)


# 리스트 함수
# Functions for List
y =[5, 2, 3, 1, 4]
print(y)

y.append(6)
print(y)

y.sort()
print(y)

y.reverse()
print(y)

y.insert(2,7) # Insert 7 on index 2
print(y)

y.remove(2)
y.remove(7)
print(y)

y.pop()
print(y) # LIFO

ex = [88, 77]
y.extend(ex)
print(y)
y.append(ex)
print(y)


# --------------------------------------
# 튜플 : 순서(O), 중복(O), 수정(X), 삭제(X)
# Tuple : Order(Y), Duplicate(Y), Modify(N), Delete(N)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# del c[2]   -> Not working
print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)


# 튜플 함수
# Funtions for tuple
z = (5, 2, 1, 3, 4)
print(z)
print(3 in z)
print(z.index(3))
print(z.count(1))
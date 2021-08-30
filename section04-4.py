# Section04-4
# Data Type
# Dictionary & Set
# 딕셔너리와 집합

# 딕셔너리 : 순서x, 중복x, 수정o, 삭제o
# Dictionary : Order(N), Duplicate(N), Modify(Y), Delete(Y)

# Key, Value (Json) -> MongoDB

a = {'name' : 'Choi', 'mobile' : '010-0000-0000', 'birth' : 970630}
b = {0 : 'Hello Python', 1:  ' Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))


# print
print(a.get('name'))
print(a.get('name1'))
print(c['arr'][1:3])


# add
# 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a)



print()
print()
print()
# keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(a.items())
print(1 in b)





print()
print()
print()
print()
print("========================")
#-----------------------------
# Set 집합
# 순서x, 중복x  Order(N), Duplicate(N)

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(c)

t = tuple(b)
print(t)
l=list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

s3 = set([7, 8, 9, 10])
s3.add(18)
print(s3)

s3.remove(10)
print(s3)
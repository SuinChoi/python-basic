# 객체 참조 중요한 특지들
# python object reference

print('Ex1- : ')

# id vs __eq__(==) 증명
x = {'name': 'kim', ' age' : 33, 'city': 'seoul'}
y = x

print('ex2-1 - ', id(x),id(y))
print('ex2-2 - ', x==y)
print('ex2-3 - ', x is y)

x['class'] = 10
print('ex2-4 - ', x, y)


z = {'name': 'kim', ' age' : 33, 'city': 'seoul', 'class' : 10}
print(x is z)
print(x == z) 

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==는 값 비교

print()
print()


# 튜플 불변형의 비교
tuple1 = (10,15, [100, 1000])
tuple2 = (10,15, [100, 1000])

print('ex3-1 - ', id(tuple1),id(tuple2))
print(tuple1 is tuple2)
print(tuple1 == tuple2)
print(tuple1.__eq__(tuple2))

print()
print()


# Copy, Deep copy

# copy
tl1 = [10, [100, 103], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print(tl1 == tl2)
print(tl1 is tl2)
print(tl1 == tl3)
print(tl1 is tl3)

print()
print()

# 증명
print(tl1)
tl1.append(1000)
print(tl1)
tl1[1].remove(103)
print()
print(tl1)
print(tl2)
print(tl3)

print()

print(id(tl1[2]))
tl1[1] +=[110, 120]
tl1[2] += (110, 120) # 튜플 재 할당(객체 새로 생성됨) -> 튜플은 불변이잖니! 추가된거 새로 아이디 생성해줘야지!

print(tl1)
print(tl2)
print(tl3)
print(id(tl1[2]))

print()
print()



# Deep Copy

# 장바구니
class Basket:
    def __init__(self, products=None) -> None:
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)
    
    def del_prod(self, prod_name):
        self._products.remove(prod_name)

import copy 

basket1 = Basket(['Apple', 'Polo RL', 'GUCCI'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print(id(basket1))
print(id(basket2))
print(id(basket3))
        
print()
print(id(basket1._products))
print(id(basket2._products))
print(id(basket3._products))

basket1.put_prod('Orange')
basket1.del_prod('Apple')
print(basket1._products)
print(basket2._products)
print(basket3._products)

print()
print()


# 함수 매개변수 전달 사용
def mul(x, y):
    x += y
    return x

x = 10
y = 5

print('ex6  ', mul(x,y), x, y)
print()

a = [10,100]
b = [5, 10]

# 파이썬 임마는 주소 바로 보내주네 쓸데없게
# C언어 만세다
print(mul(a,b), a, b) # 가변형 매개변수일때 데이터 변경됨


c = (10, 100)
d = (4, 10)
print(mul(c,d), c, d) # 불변형일땐 데이터 안변경됨 하나만해라 진짜 -_-



print()
print()

# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본생성x -> 참조 반환
# 파이썬 이정도면 밀당의 고수임 ㅋ

t11 = (1, 2, 3, 4, 5)
t12 = tuple(t11)
t13 = t11[:]

print(t11 is t12, id(t11), id(t12))
print(t11 is t13, id(t11), id(t13))



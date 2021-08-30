# 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉
# . : 현재 디렉

# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 ", Fibonacci().title)




# 사용2(클래스)
# from pkg.fibonacci import *



# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

print("ex3 ", end="")
fb.fib(500)
print("ex3 ", fb().title)



# 사용4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(1,3))
print("ex4 : ", c.mod(5,3))

# 사용5(함수)
from pkg.calculations import mul as m
print("ex5: ",m(100, 10))

# 사용6 
import pkg.prints as p
p.prt1()
p.prt2()

import builtins
# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('\nMy name is Suin!')

# 변수 선언
myName= 'Suin'

# 조건문
if myName == 'Suin':
    print('Hello, Suin')

# 반복문
print()
for i in range(1, 10):
    for j in range(1, 10):
        print("%d * %d = %2d"%(i, j, i*j))
    print("-----------")


# 함수 선언
def greeting():
    print('Hello!')

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
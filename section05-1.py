# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

if True:
    print("Yes")

if False:
    print("No")
else:
    print("Yes")



# 관계연산자
# >, >=, <. <=. ++, !=
a = 10
b = 0
print(a == b)
print(a != b)
print(a > b)



# 참 거짓 종류(True, False)
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0
city=""

if city:
    print(">>>>True")
else :
    print(">>>>False")



# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용
print('ex1 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1=90
score2 = 'A'

if score1 >=90 and score2 == 'A':
    print('합격')
else:
    print("불합격")



# 다중조건문
num = 90

# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for key in q1:
    if key == "가을":
        print(q1[key])


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "배"}

for v in q2.values():
    if v == "사과":
        print( "사과있네")
else :
    print('사과없음')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 20
if score < 0 or score > 100:
    print('잘못된 입력')
elif score >= 81 and score <=100:
    print('A')
elif score >= 61 and score <=80:
    print('B')
elif score >= 41 and score <=60:
    print('C')
elif score >= 21 and score <=40:
    print('D')
else :
    print('E')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a = 22
b = 60 
c = 18

if a > b : 
    if a > c :
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
human = '990019-599999'
if int(human[7]) == 1 or int(human[7]) == 3 :
    print('male')
elif int(human[7]) == 2 or int(human[7]) == 4:
    print('female')
else:
    print('동물?')

    
# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for v in q3:
    if v == '정':
        continue
    print(v, end=' ')
print()

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for a in range(1, 101, 2):
    print(a, end=' ')
print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for i in q4:
   if(len(i)) >= 5:
       print(i)


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q5:
    if i == i.lower():
        print(i)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
print('--------------------------------')
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q6:
    if i == i.upper():
        print(i.lower(), end=" ")
    else:
        print(i.upper(), end=" ")

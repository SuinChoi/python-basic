# 파일쓰기
# r : 읽기모드
# W : 쓰기모드 ( 기존파일 삭제 )
# a : 추가모드 ( 파일 생성 또는 추가)

# 파일 읽기
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
# 반드시 close 해줄 것
f.close()

print("===============")

# with문 : close 알아서 해줌
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)

print("===============")




with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())


print("===============")




with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(" > ", content)
    content = f.read() # 내용 없음
    print(" > ", content) 

print("===============")




with open('./resource/review.txt', 'r') as f:
    line =f.readline()
    print(line)

    while line:
        print(line, end='******')
        line = f.readline()


print("===============")


with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    
    print('Average : %6.3f '%(sum(score)/len(score)))

print("===============")




with open('./resource/write.txt', 'w') as f:
    f.write('This is test\n')

with open('./resource/write.txt', 'a') as f:
    f.write('This is test')

print("===============")




from random import randint as r
import random
with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(r(0, 50)) +' ')


print("===============")







# writelines  : 리스트 - > 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list=['Kim\n', 'Park\n', 'Choi\n']
    f.writelines(list)



with open('./resource/text4.txt', 'w') as f:
    print("Test Contests1", file=f)
    print("Test Contests1", file=f)







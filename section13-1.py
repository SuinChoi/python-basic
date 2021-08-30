import random
from sqlite3.dbapi2 import Date
import time
import winsound
import sqlite3
import datetime

words = [ ]                 # 영어 단어 리스트(1000개)
n =1                        # 게임 시도 횟수
correct = 0                 # 정답 수
date = datetime.datetime.now()
date = date.strftime('%y-%m-%d %H:%M:%S')

# 파일 열어서 단어 가져와
with open('./resource/word.txt', 'r') as f:
   for c in f:
       words.append(c.strip())
    
# print(words)

# DB 연결한다
conn = sqlite3.connect('C:/Users/suin6/Desktop/python-basic/resource/record.db', isolation_level=None)
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS records(\
    id INTEGER PRIMARY KEY AUTOINCREMENT,\
    correct INTEGER,\
    record text,\
    regidate text\
    )')

print('HELLO')
print()
input('Ready? Press Enter Key To Start!')

start = time.time()


while n <= 5:
    print()
    print()


    temp = words[random.randint(0,1001)]
    print(" Question # %d \n\t" %n, temp)
    user = input("\t ")
    print()

    if temp.strip() == user.strip():
        print("성공")
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        correct+=1              # 맞은 갯수 추가
    else :
        print("야 너 틀림 ㅋ") 
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
    
    n += 1

end = time.time()               # 끝난 시간 
totalTime = end - start         # 끝난 시간 - 처음 시간 = 걸린 시간
totalTime = format(totalTime, ".3f")

cursor.execute('INSERT INTO records (correct, record, regidate) VALUES(?, ?, ?)', (correct, totalTime, date))

print("총 시간 : %f 초" %(float(totalTime)))
print("맞은 갯수 : ", correct)

conn.close()
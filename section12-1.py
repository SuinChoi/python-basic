# DB 써보자
# SQLite

import sqlite3
import datetime

# 삽입 날짜 생성
now= datetime.datetime.now()
print (now)

nowDate = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDate)
print('sql ver: ', sqlite3.version)


# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('C:/Users/suin6/Desktop/python-basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")


# 데이터 삽입
#c.execute("INSERT INTO users VALUES(1, 'Choi', 'suin@googl.com','010-000', 'google.com', ?)", (nowDate,))

# Many 삽입(튜플, 리스트) 
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDate),
    (4, 'Park', 'Park@naver.com', '010-3332-2222', 'Park.com', nowDate),
    (5, 'Jeon', 'Jeon@naver.com', '010-7777-7777', 'Jeon.com', nowDate)
)

c.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)", userList)


# 테이블 데이터 삭제
#conn.excute("DELETE FROM users")
# print('users db deleted : ', conn.execute("DELETE FROM users").rowcount)


# 커밋 : isolation_level = None 일 경우 자동 반영(으로 커밋)

# 롤백
# conn.rollback()


# 접속해제
conn.close()
# DB 테이블 조회



import sqlite3


conn = sqlite3.connect('C:/Users/suin6/Desktop/python-basic/resource/database.db')

c = conn.cursor()

c.execute("SELECT * FROM users")

# 1개 로우 선택
#print("One - > \n", c.fetchone())

# 지정 로우 선택
#print("Three -> \n", c.fetchmany(size=3))

# 전체 로우 선택
#print("ALL ->\n", c.fetchall())

print()


# 순회1
#rows = c.fetchall()
#for row in rows:
#    print('순회 > ', row)

# 순회2
#for row in c.fetchall():
#    print('순회2 > ', row)

# 순회3
#for row in c.execute("SELECT * FROM users ORDER BY id desc"):
#    print('순회 3 > ', row)


# WHERE Retrival
param1 = (3, )
c.execute("SELECT * FROM users WHERE id=?", param1)
print('param1', c.fetchone())




conn.close()
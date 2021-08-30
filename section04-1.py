# section04-1
# 데이터 타입
# Data Type

v_str1 = "Nice"
v_bool = True
v_str2 = "Good"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_list))
print(type(v_tuple))
print(type(v_set))


i1 = 39
i2 = 939
print(i1 * i2)

big_int1 = 9999999999999999999999
big_int2 = 7777777777777777777777
print(big_int1 * big_int2)

f1 = 1.234
f2 = 3.787
print(f1 ** f2) # 제곱

f3 = .5
f4 = 10.
print(f3 + f4)


a = 5.
b = 4
print(type(a), type(b))

result = a + b
print('result = %f' %(result))
print('type of result is : ' ,type(result))

# 형변환 casting
# int, float, complex(복소수)
print(int(result))
print(float(b))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))


# 수치 연산 함수
print(abs(-7))
n, m= divmod(100, 8)
print(n, m)

import math 

print(math.ceil(5.1))
print(math.floor(3.874))
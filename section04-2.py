# section04-2
# Using String
# 문자열, 문자열연산, 슬라이싱

str1="I'm Suin"
str2 = 'Hello'
str3 = ""
str4 = str('aaa')

print(len(str1), len(str2), len(str3), len(str4))

escape_Str = "Do you have a \"bic collection\""
print(escape_Str)
escape_str2 = "Tab\tTab\t"
print(escape_str2)


# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)


# Multi line
# 멀티라인
multi = \
    """String Multi Line Test"""
print(multi)


# Calculating String
#a 문자열연산
str_01 = "*"
str_02 = 'abc'
str_03 = "def"
str_04 = "Hungry"
print(str_01 * 100)
print(str_02 + str_03)
print('a' in str_04)
print('H' in str_04)
print('R' not in str_04)


# Casting 형변환
print(str(77) + 'a')
print(str(10.4))


# 문자열 함수
# String Function
a = 'hangry'
b = "pizza"

print(a.isupper())
print(b.endswith('a'))
print(b.capitalize())
print(a.replace('a', 'u'))
print(list(reversed(b)))


# 슬라이싱 
# Slicing
# a= "Hangry"
# b = "Pizza"
print(a[0:3])
print(a[0:4])
print(a[0:len(a)-1])
print(a[:4])
print(a[:])

print(b[0:4:2])
print(b[1:-1])
print(b[::-1])
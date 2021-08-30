# section02-1
# 파이썬 기초 코딩
# print구문의 이해
# understanding of 'print'

# 기본출력

print('Hello Python!')
print("Hellp Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Seperator 옵션 사용
print('T','E','S','T')
print('T','E','S','T', sep='')
print('2019','02','19',sep='-')
print('niceman','google.com', sep="@")

# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

#format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
print("{0}, {1} and {0}".format('You', 'Me'))
print("{a} and {b}".format(a='You', b='Me'))

print("%s's favourite number is %d" %("Suin", 6))   # %s:문자, %d : 정수, %f:실수

print("Test1: %5d, Price %4.2f" %(776, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123))
print("Test1: {a:5d}, Price: {b: 4.2f}".format(a=776,b=6534.123))

# Escape 코드 
print("'you'")
print('\'\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('\ttest')
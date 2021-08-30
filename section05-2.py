v1 = 1
while v1 < 11:
    print('v1 is : ', v1)
    v1 += 1


for v2 in range(10):
    print('v2 is : ',v2)

for v3 in range(1, 11):
    print('v3 is : ', v3)


# sum 1-100
sum1 = 0
for a in range(1, 10):
    sum1 += a
print(sum1)

print('1+3+5+7+9 =  ', sum(range(1, 10, 2)))



names=['kim', 'choi', 'lee', 'cho']

for v in names:
    print ( 'you are : ', v)

info={
    "name" : 'kim',
    'age' : 33,
    'city' : 'Seoul'
}
for key in info:
    print('info1 ', key)
for key in info.values():
    print('info2 ', key)
for key in info.keys():
    print('info3 ', key)
for k, v in info.items():
    print('info4 ',k, v)
